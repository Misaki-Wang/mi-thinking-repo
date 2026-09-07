#!/usr/bin/env python3
"""Verify course reading identities against primary metadata; cache evidence locally.

Uses the arXiv Atom API in one batch and publisher/author pages otherwise.
The public JSON intentionally contains no abstracts or article bodies. Evidence
under .work/readings is private working material and must never be published.
"""

from __future__ import annotations

import argparse
import datetime as dt
import difflib
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import tempfile
import time
import unicodedata
from urllib.parse import quote, urlencode, urlparse
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "course/mit-mmai-2026/catalog.json"
OUTPUT = ROOT / "course/mit-mmai-2026/reading-sources.json"
WORK = ROOT / ".work/readings"
MAX_BYTES = 8 * 1024 * 1024
LAST_REQUEST: dict[str, float] = {}
ARXIV = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5}(?:v\d+)?)")
CORRECTIONS = {
    "Scaling Instruction-Finetuned Language Models": "https://arxiv.org/abs/2210.11416",
    "LLaVA-Med: Training a Large Language-and-Vision Assistant for Biomedicine in One Day": "https://arxiv.org/abs/2306.00890",
    "Unraveling the Connections Between Flow Matching and Diffusion Probabilistic Models": "https://arxiv.org/abs/2411.07625v1",
}
PII_DOIS = {"S0167865513002584": "10.1016/j.patrec.2013.07.003"}
PRIMARY_SUPPLEMENTS = {
    "https://dl.acm.org/doi/pdf/10.1145/319382.319398": ("https://hci.stanford.edu/courses/cs547/abstracts/98-99/990226-oviatt.html", "Our ability", "Dr. Sharon Oviatt", "Author's 1999 Stanford talk abstract on the same topic; not the paper full text."),
    "https://dl.acm.org/doi/abs/10.1145/3411764.3445300": ("https://lab.plopes.org/", "Stereo-Smell via Electrical Trigeminal Stimulation", "Preserving Agency", "Author lab's description of the linked CHI 2021 project."),
    "https://dl.acm.org/doi/abs/10.1145/3290605.3300233": ("https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/", "Advances in artificial intelligence", "Opens in a new tab", "Author institution's publication abstract."),
}


def clean(value):
    return re.sub(r"\s+", " ", html.unescape(value or "")).strip()


def normalized_title(value):
    return " ".join(re.findall(r"\w+", unicodedata.normalize("NFKD", value).casefold()))


def fetch(url):
    host = urlparse(url).netloc
    delay = max(0, LAST_REQUEST.get(host, 0) + (3.1 if "export.arxiv" in host else 1.1) - time.monotonic())
    if delay:
        time.sleep(delay)
    LAST_REQUEST[host] = time.monotonic()
    request = Request(quote(url, safe=":/?=&%+#@,"), headers={"User-Agent": "Personal-Course-Reading-Verifier/1.0 (metadata-only; public academic sources)"})
    with urlopen(request, timeout=40) as response:
        raw = response.read(MAX_BYTES + 1)
        if len(raw) > MAX_BYTES:
            raise ValueError("Response exceeds metadata size limit")
        return raw, response.headers.get_content_type(), response.url


class MetadataParser(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.metadata = {}
        self.title = []
        self.headings = []
        self.parts = []
        self.ignored = 0
        self.in_title = False
        self.in_h1 = False
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in {"script", "style", "noscript"}:
            self.ignored += 1
        if tag == "meta":
            key = attrs.get("name", attrs.get("property", "")).casefold()
            self.metadata.setdefault(key, []).append(attrs.get("content", ""))
        if tag == "title":
            self.in_title = True
        if tag == "h1":
            self.in_h1 = True

    def handle_endtag(self, tag):
        if tag in {"script", "style", "noscript"} and self.ignored:
            self.ignored -= 1
        if tag == "title":
            self.in_title = False
        if tag == "h1":
            self.in_h1 = False

    def handle_data(self, value):
        if self.ignored:
            return
        if self.in_title:
            self.title.append(value)
        if self.in_h1:
            self.headings.append(value)
        self.parts.append(value)

    def first(self, *keys):
        for key in keys:
            values = self.metadata.get(key)
            if values and clean(values[0]):
                return clean(values[0])
        return ""


def arxiv_batch(urls):
    ids = sorted({ARXIV.search(url)[1] for url in urls})
    if not ids:
        return {}
    url = "https://export.arxiv.org/api/query?" + urlencode({"id_list": ",".join(ids), "max_results": len(ids)})
    raw, _, resolved = fetch(url)
    tree = ET.fromstring(raw)
    ns = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    results = {}
    for entry in tree.findall("a:entry", ns):
        eid = entry.findtext("a:id", "", ns)
        match = ARXIV.search(eid)
        if not match:
            continue
        ident = re.sub(r"v\d+$", "", match[1])
        results[ident] = {
            "resolved_title": clean(entry.findtext("a:title", "", ns)),
            "abstract": clean(entry.findtext("a:summary", "", ns)),
            "authors": [clean(a.findtext("a:name", "", ns)) for a in entry.findall("a:author", ns)],
            "published": entry.findtext("a:published", "", ns),
            "updated": entry.findtext("a:updated", "", ns),
            "resolved_url": eid.replace("http://", "https://"),
            "metadata_url": resolved,
            "evidence_level": "primary_abstract",
            "retrieval_method": "arxiv_atom_api",
            "retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            "errors": [],
        }
    return results


def crossref(doi):
    url = "https://api.crossref.org/works/" + quote(doi, safe="/")
    raw, _, resolved = fetch(url)
    item = json.loads(raw)["message"]
    description = clean(re.sub(r"<[^>]+>", " ", item.get("abstract", "")))
    return {
        "resolved_title": clean(" ".join(item.get("title", []))),
        "authors": [clean(a.get("given", "") + " " + a.get("family", "")) for a in item.get("author", [])],
        "abstract": description,
        "resolved_url": "https://doi.org/" + doi,
        "metadata_url": resolved,
        "evidence_level": "publisher_registered_abstract" if description else "publisher_registered_metadata_only",
        "retrieval_method": "crossref_doi_registry",
        "retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "errors": [],
    }


def web_metadata(url):
    errors = []
    try:
        raw, mime, resolved = fetch(url)
        if "html" not in mime:
            raise ValueError(f"Expected metadata HTML, received {mime}")
        doc = MetadataParser(raw.decode("utf-8", errors="replace"))
        title = doc.first("citation_title", "dc.title", "og:title", "twitter:title") or clean(" ".join(doc.headings)) or clean(" ".join(doc.title))
        if "colab.research.google.com" in url:
            raise ValueError("Colab returned an application/sign-in shell; notebook content and title are not verified")
        if not title or re.search(r"^(access denied|just a moment|forbidden|robot|error|sign in)", title, re.I):
            raise ValueError(f"No usable source title: {title!r}")
        abstract = doc.first("citation_abstract", "dc.description", "description", "og:description")
        return {
            "resolved_title": title,
            "authors": [clean(a) for a in doc.metadata.get("citation_author", [])],
            "abstract": abstract,
            "text_snippet": clean(" ".join(doc.parts))[:22000],
            "resolved_url": resolved,
            "metadata_url": resolved,
            "evidence_level": "primary_page_excerpt",
            "retrieval_method": "publisher_or_author_html",
            "retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            "errors": [],
        }
    except Exception as error:
        errors.append(f"{type(error).__name__}: {error}")
    doi_match = re.search(r"(?:doi/(?:abs/|pdf/)?|chapter/|article/)(10\.[^?#]+)", url)
    doi = doi_match[1] if doi_match else PII_DOIS.get(url.rstrip("/").split("/")[-1])
    if doi:
        try:
            result = crossref(doi)
            result["errors"] = errors
            return result
        except Exception as error:
            errors.append(f"Crossref fallback {type(error).__name__}: {error}")
    return {"resolved_title": None, "abstract": "", "evidence_level": "unavailable", "retrieval_method": "failed", "errors": errors, "retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat()}


def records(catalog):
    by_url = {}
    for session in catalog["sessions"]:
        for reading in session["readings"]:
            original_url = reading["url"]
            url = original_url.strip()
            if url not in by_url:
                by_url[url] = {"id": "reading-" + hashlib.sha256(url.encode()).hexdigest()[:12], "url": url, "url_variants": [], "title": reading["title"], "schedule_titles": [], "sessions": [], "occurrences": []}
            record = by_url[url]
            if original_url not in record["url_variants"]:
                record["url_variants"].append(original_url)
            if reading["title"] not in record["schedule_titles"]:
                record["schedule_titles"].append(reading["title"])
            if session["id"] not in record["sessions"]:
                record["sessions"].append(session["id"])
            record["occurrences"].append({"session": session["id"], "title": reading["title"], "url": original_url})
    return list(by_url.values())


def compare_titles(source):
    comparisons = []
    resolved = source.get("resolved_title")
    for title in source["schedule_titles"]:
        expected, actual = normalized_title(title), normalized_title(resolved or "")
        equal = expected == actual
        score = difflib.SequenceMatcher(None, expected, actual).ratio() if resolved else 0
        if not resolved:
            category = "unverified"
        elif equal:
            category = "match"
        elif expected == actual + " " + actual:
            category = "duplicated_schedule_title"
        elif title == "Blog Post on Self-Evolving AI" and source["url"] == "https://quao627.github.io/blog/self-evolving-agents/":
            category = "descriptive_schedule_label"
        else:
            category = "title_variant" if score >= 0.86 else "title_mismatch"
        comparisons.append({"schedule_title": title, "resolved_title": resolved, "comparison": category, "similarity": round(score, 3)})
    return comparisons


def atomic_json(path, value):
    with tempfile.NamedTemporaryFile("w", dir=path.parent, encoding="utf-8", delete=False) as temporary:
        json.dump(value, temporary, ensure_ascii=False, indent=2)
        temporary.write("\n")
        temp_path = Path(temporary.name)
    temp_path.replace(path)


def write_outputs(sources, evidence):
    WORK.mkdir(parents=True, exist_ok=True)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now(dt.timezone.utc).isoformat()
    metadata = {
        "course": "mit-mmai-2026",
        "verified_at": stamp,
        "scope": "Source identity and primary metadata/abstract availability only; this is not full-paper content or claim verification. Raw abstracts and page excerpts remain in ignored .work/readings.",
        "sources": sources,
        "counts": {"unique_normalized_urls": len(sources), "verified_titles": sum(bool(s.get("resolved_title")) for s in sources), "substantive_title_mismatches": sum(s.get("title_mismatch") is True for s in sources), "unavailable": sum(s.get("status") == "unavailable" for s in sources)},
    }
    atomic_json(OUTPUT, metadata)
    atomic_json(WORK / "evidence.json", {"verified_at": stamp, "sources": evidence})
    for source in evidence:
        (WORK / (source["id"] + ".txt")).write_text("\n\n".join(["Source URL: " + source["url"], "Schedule title: " + source["title"], "Resolved title: " + str(source.get("resolved_title")), "Evidence level: " + source.get("evidence_level", ""), "Abstract or description:\n" + source.get("abstract", ""), "Page excerpt:\n" + source.get("text_snippet", "")]) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true", help="Fetch sources again instead of reusing local evidence")
    args = parser.parse_args()
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    sources = records(catalog)
    prior = {}
    cache = WORK / "evidence.json"
    if cache.exists() and not args.refresh:
        prior = {s["url"]: s for s in json.loads(cache.read_text())["sources"]}
    manual_file = WORK / "manual-evidence.json"
    manual = json.loads(manual_file.read_text()) if manual_file.exists() else {}
    notebooks_file = ROOT / ".work/sources/reading-notebooks.json"
    notebooks = {n["url"].strip(): n for n in json.loads(notebooks_file.read_text())} if notebooks_file.exists() else {}
    arxiv_urls = [s["url"] for s in sources if ARXIV.search(s["url"]) and s["url"] not in prior]
    arxiv_urls.extend(CORRECTIONS.values())
    try:
        arxiv = arxiv_batch(arxiv_urls)
        print(f"arXiv batch returned {len(arxiv)} primary records", flush=True)
    except Exception as error:
        arxiv = {}
        print(f"arXiv batch unavailable: {type(error).__name__}: {error}; trying individual primary pages", flush=True)
    evidence = []
    public = []
    for index, base in enumerate(sources, 1):
        url = base["url"]
        match = ARXIV.search(url)
        if url in notebooks and notebooks[url].get("status") == "acquired":
            notebook = notebooks[url]
            notebook_path = ROOT / notebook["local_path"]
            raw = (notebook_path / "notebook.ipynb").read_bytes()
            if hashlib.sha256(raw).hexdigest() != notebook["sha256"]:
                raise ValueError(f"Cached notebook hash differs for {url}")
            result = {"resolved_title": re.sub(r"^#+\s*", "", notebook["markdown_headings"][0]), "abstract": "", "text_snippet": (notebook_path / "notebook.txt").read_text()[:22000], "evidence_level": "primary_notebook", "retrieval_method": "public_google_drive_notebook", "resolved_url": notebook["resolved_url"], "metadata_url": notebook["resolved_url"], "sha256": notebook["sha256"], "errors": [], "retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat()}
        elif url in manual:
            result = manual[url]
        elif url in prior and prior[url].get("status") != "unavailable":
            result = {k: v for k, v in prior[url].items() if k not in base}
        elif match and re.sub(r"v\d+$", "", match[1]) in arxiv:
            result = arxiv[re.sub(r"v\d+$", "", match[1])].copy()
        else:
            result = web_metadata("https://arxiv.org/abs/" + match[1] if match else url)
        if url in PRIMARY_SUPPLEMENTS and not result.get("supplementary_source_note"):
            alternate, anchor, end_anchor, note = PRIMARY_SUPPLEMENTS[url]
            try:
                raw, _, resolved = fetch(alternate)
                doc = MetadataParser(raw.decode("utf-8", errors="replace"))
                text = clean(" ".join(doc.parts))
                offset = text.find(anchor)
                if offset < 0:
                    raise ValueError(f"Expected author-source evidence anchor not found: {anchor}")
                end = text.find(end_anchor, offset)
                result["text_snippet"] = text[offset:end if end > offset else offset + 6500]
                result["supplementary_source_urls"] = [resolved]
                result["supplementary_source_note"] = note
                result["evidence_level"] = "primary_author_page_excerpt"
            except Exception as error:
                result.setdefault("errors", []).append(f"Author supplement {type(error).__name__}: {error}")
        full = {**base, **result}
        comparisons = compare_titles(full)
        full["title_comparisons"] = comparisons
        full["title_mismatch"] = any(c["comparison"] == "title_mismatch" for c in comparisons) if full.get("resolved_title") else None
        full["status"] = "unavailable" if not full.get("resolved_title") else "verified_title_mismatch" if full["title_mismatch"] else "verified_metadata"
        full["candidate_corrections"] = []
        full["candidate_evidence"] = []
        for title in base["schedule_titles"]:
            if title not in CORRECTIONS:
                continue
            correction_url = CORRECTIONS[title]
            ident = re.sub(r"v\d+$", "", ARXIV.search(correction_url)[1])
            correction = arxiv.get(ident, {})
            expected = normalized_title(title)
            actual = normalized_title(correction.get("resolved_title", ""))
            status = "verified_title_match_candidate" if expected == actual else "verified_title_prefix_candidate" if actual.startswith(expected + " ") else "unverified_candidate"
            full["candidate_corrections"].append({"schedule_title": title, "url": correction_url, "resolved_title": correction.get("resolved_title"), "status": status, "note": "Editorial candidate matching the schedule label; original course URL remains unchanged. Instructor intent is not independently confirmed."})
            if correction:
                full.setdefault("candidate_evidence", []).append({"url": correction_url, **correction})
        evidence.append(full)
        public.append({k: v for k, v in full.items() if k not in {"abstract", "text_snippet", "candidate_evidence"}})
        # Checkpoint allows content writers to begin while slower publishers resolve.
        write_outputs(public, evidence)
        print(f"{index}/{len(sources)} {full['status']}: {base['title']}", flush=True)
    print(json.dumps(json.loads(OUTPUT.read_text())["counts"], ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
