"use strict";

(() => {
  const base = document.body.dataset.base || "/";
  const cards = Array.from(document.querySelectorAll(".lesson-card"));
  const input = document.querySelector("#lesson-filter");
  const filters = Array.from(document.querySelectorAll("[data-filter]"));
  let selected = "all";
  function filterLessons() {
    const terms = (input?.value || "").trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    let count = 0;
    cards.forEach(card => {
      const show = (selected === "all" || card.dataset.kind === selected) && terms.every(term => card.dataset.search.includes(term));
      card.hidden = !show;
      if (show) count += 1;
    });
    const countLabel = document.querySelector("#lesson-count");
    if (countLabel) countLabel.textContent = `${count} 个章节`;
    const empty = document.querySelector("#filter-empty");
    if (empty) empty.hidden = count !== 0;
  }
  input?.addEventListener("input", filterLessons);
  filters.forEach(button => button.addEventListener("click", () => {
    selected = button.dataset.filter;
    filters.forEach(item => {
      item.classList.toggle("selected", item === button);
      item.setAttribute("aria-pressed", String(item === button));
    });
    filterLessons();
  }));

  const menu = document.querySelector(".lesson-menu");
  const narrow = window.matchMedia("(max-width: 680px)");
  const resizeMenu = () => { if (menu) menu.open = !narrow.matches; };
  resizeMenu();
  narrow.addEventListener("change", resizeMenu);

  const dialog = document.querySelector("#search-dialog");
  const search = document.querySelector("#site-search");
  const status = document.querySelector("#search-status");
  const results = document.querySelector("#search-results");
  let index = null;
  let loading = null;
  let searchTimer;

  async function loadIndex() {
    if (index) return index;
    if (!loading) {
      loading = fetch(`${base}search-index.json`, {credentials: "same-origin"})
        .then(response => {
          if (!response.ok) throw new Error("Search index unavailable");
          return response.json();
        })
        .then(data => {
          if (!Array.isArray(data)) throw new Error("Invalid search index");
          index = data.map(item => ({...item, haystack: `${item.title} ${item.headings} ${item.text}`.toLocaleLowerCase()}));
          return index;
        }).catch(error => { loading = null; throw error; });
    }
    return loading;
  }

  function highlight(element, text, terms) {
    if (!terms.length) { element.textContent = text; return; }
    const pattern = new RegExp(terms.map(term => term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")).join("|"), "gi");
    let start = 0;
    for (const match of text.matchAll(pattern)) {
      element.append(document.createTextNode(text.slice(start, match.index)));
      const mark = document.createElement("mark");
      mark.textContent = match[0];
      element.append(mark);
      start = match.index + match[0].length;
    }
    element.append(document.createTextNode(text.slice(start)));
  }

  async function runSearch() {
    const query = search.value.trim().toLocaleLowerCase();
    results.replaceChildren();
    if (!query) { status.textContent = "输入关键词，搜索全部课程与笔记。"; return; }
    status.textContent = "正在搜索…";
    try {
      const data = await loadIndex();
      if (query !== search.value.trim().toLocaleLowerCase()) return;
      const terms = query.split(/\s+/).filter(Boolean);
      const matches = data.filter(item => terms.every(term => item.haystack.includes(term))).map(item => ({
        ...item,
        score: terms.reduce((sum, term) => sum + (item.title.toLocaleLowerCase().includes(term) ? 12 : 0) + (item.headings.toLocaleLowerCase().includes(term) ? 3 : 0), 0) + (item.kind === "课程预览" ? 2 : 0)
      })).sort((a, b) => b.score - a.score);
      status.textContent = matches.length ? `找到 ${matches.length} 份笔记${matches.length > 30 ? "，显示最相关的 30 份" : ""}` : "没有找到匹配内容，试试英文术语或更短的关键词。";
      matches.slice(0, 30).forEach(item => {
        const url = new URL(item.url, window.location.origin);
        if (url.origin !== window.location.origin || !url.pathname.startsWith(base)) return;
        const link = document.createElement("a");
        link.className = "search-result";
        link.href = url.href;
        const kind = document.createElement("small");
        kind.textContent = item.kind;
        const title = document.createElement("h3");
        highlight(title, item.title, terms);
        const snippet = document.createElement("p");
        const first = Math.min(...terms.map(term => item.text.toLocaleLowerCase().indexOf(term)).filter(position => position >= 0));
        const begin = Number.isFinite(first) ? Math.max(0, first - 55) : 0;
        const excerpt = (begin ? "…" : "") + item.text.slice(begin, begin + 200) + (item.text.length > begin + 200 ? "…" : "");
        highlight(snippet, excerpt, terms);
        link.append(kind, title, snippet);
        results.append(link);
      });
    } catch (_) {
      status.textContent = "搜索暂时不可用。请刷新页面后重试，或从课程导航继续阅读。";
    }
  }

  function openSearch() {
    if (!dialog.open) dialog.showModal();
    search.focus();
  }
  document.querySelector(".search-open")?.addEventListener("click", openSearch);
  document.querySelector("#search-close")?.addEventListener("click", () => dialog.close());
  dialog?.addEventListener("click", event => { if (event.target === dialog) dialog.close(); });
  search?.addEventListener("input", () => { clearTimeout(searchTimer); searchTimer = setTimeout(runSearch, 120); });
  document.addEventListener("keydown", event => {
    const editing = /INPUT|TEXTAREA|SELECT/.test(document.activeElement?.tagName || "") || document.activeElement?.isContentEditable;
    if (event.key === "/" && !editing && !event.metaKey && !event.ctrlKey && !event.altKey) {
      event.preventDefault();
      openSearch();
    }
  });

  const tocLinks = Array.from(document.querySelectorAll(".toc a"));
  if (tocLinks.length && "IntersectionObserver" in window) {
    const observer = new IntersectionObserver(entries => {
      for (const entry of entries) {
        if (entry.isIntersecting) tocLinks.forEach(link => link.classList.toggle("is-current", decodeURIComponent(link.hash.slice(1)) === entry.target.id));
      }
    }, {rootMargin: "-110px 0px -65% 0px"});
    document.querySelectorAll(".prose h2,.prose h3").forEach(heading => observer.observe(heading));
  }
})();
