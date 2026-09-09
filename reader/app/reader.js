/* Standalone course reader. Base alignment data is never mutated by corrections. */
(function (global) {
  "use strict";

  const COURSE_ID = "mit-mmai-2026";
  const STORAGE_PREFIX = "mi-thinking:reader:" + COURSE_ID + ":v1:";
  const own = (object, key) => Object.prototype.hasOwnProperty.call(object, key);
  const record = (value) => value !== null && typeof value === "object" && !Array.isArray(value);
  const validId = (value) => typeof value === "string" && /^[a-zA-Z0-9][a-zA-Z0-9_.:-]{0,120}$/.test(value);

  function validateLesson(input, expectedSession) {
    if (!record(input) || input.session_id !== expectedSession || !validId(input.session_id) || !Array.isArray(input.blocks) || !Array.isArray(input.slides)) {
      throw new Error("章节数据格式不正确，或章节 ID 不一致。");
    }
    const slideIds = new Set();
    for (const slide of input.slides) {
      if (!record(slide) || !validId(slide.id) || slideIds.has(slide.id) || !Number.isInteger(slide.page) || slide.page < 1 || typeof slide.image_url !== "string") {
        throw new Error("Slide 数据不完整或含重复 ID。");
      }
      slideIds.add(slide.id);
    }
    const blockIds = new Set();
    for (const block of input.blocks) {
      if (!record(block) || !validId(block.id) || blockIds.has(block.id) || !Number.isFinite(block.start_ms) || !Number.isFinite(block.end_ms) || block.start_ms < 0 || block.end_ms < block.start_ms || typeof block.en !== "string" || typeof block.zh !== "string") {
        throw new Error("讲稿数据不完整或含重复 ID。");
      }
      if (block.slide_id !== null && block.slide_id !== undefined && !slideIds.has(block.slide_id)) {
        throw new Error("讲稿对应到了不存在的 slide。");
      }
      blockIds.add(block.id);
    }
    return input;
  }

  function validateCorrections(input, lesson) {
    if (!record(input)) throw new Error("校对内容必须是一个 JSON 对象。");
    const blocks = new Set(lesson.blocks.map((block) => block.id));
    const slides = new Set(lesson.slides.map((slide) => slide.id));
    const result = Object.create(null);
    for (const [blockId, slideId] of Object.entries(input)) {
      if (!blocks.has(blockId) || (slideId !== null && !slides.has(slideId))) {
        throw new Error("校对文件含有当前章节中不存在的段落或 slide ID。");
      }
      result[blockId] = slideId;
    }
    return result;
  }

  function importCorrections(input, lesson) {
    if (!record(input) || input.schema_version !== 1 || input.course_id !== COURSE_ID || input.session_id !== lesson.session_id) {
      throw new Error("请选择当前课程、当前章节的校对文件。");
    }
    return validateCorrections(input.corrections, lesson);
  }

  function exportCorrections(lesson, corrections) {
    return { schema_version: 1, course_id: COURSE_ID, session_id: lesson.session_id, corrections: validateCorrections(corrections, lesson) };
  }

  function deriveMappings(lesson, corrections) {
    const checked = validateCorrections(corrections, lesson);
    const blockToSlide = new Map();
    const slideToBlocks = new Map(lesson.slides.map((slide) => [slide.id, []]));
    for (const block of lesson.blocks) {
      const slideId = own(checked, block.id) ? checked[block.id] : (block.slide_id || null);
      blockToSlide.set(block.id, slideId);
      if (slideId && slideToBlocks.has(slideId)) slideToBlocks.get(slideId).push(block.id);
    }
    return { blockToSlide, slideToBlocks };
  }

  function chooseBlockForSlide(mappings, slideId, currentBlockId) {
    const ids = mappings.slideToBlocks.get(slideId) || [];
    return ids.includes(currentBlockId) ? currentBlockId : (ids[0] || null);
  }

  function formatTime(milliseconds) {
    const seconds = Math.max(0, Math.floor(milliseconds / 1000));
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const remainder = seconds % 60;
    return (hours ? String(hours).padStart(2, "0") + ":" : "") + String(minutes).padStart(2, "0") + ":" + String(remainder).padStart(2, "0");
  }

  function localURL(value, base) {
    const root = new URL("./", base);
    const url = new URL(value, root);
    if (url.origin !== root.origin || !url.pathname.startsWith(root.pathname) || !["http:", "https:"].includes(url.protocol)) {
      throw new Error("阅读器资源地址不在当前页面目录内。");
    }
    return url.href;
  }

  function externalURL(value) {
    try {
      const url = new URL(value);
      return url.protocol === "https:" ? url.href : null;
    } catch (_) { return null; }
  }

  function createRequestGate() {
    let generation = 0;
    return { next: () => ++generation, current: (token) => token === generation };
  }

  function readDeepLink(href) {
    const url = new URL(href);
    const hash = new URLSearchParams(url.hash.replace(/^#/, ""));
    return { session: url.searchParams.get("session"), language: url.searchParams.get("lang"), block: hash.get("block"), slide: hash.get("slide") };
  }

  const core = { COURSE_ID, validateLesson, validateCorrections, importCorrections, exportCorrections, deriveMappings, chooseBlockForSlide, formatTime, localURL, externalURL, createRequestGate, readDeepLink };
  if (typeof module !== "undefined" && module.exports) module.exports = core;
  global.MIReaderCore = core;
  if (typeof document === "undefined") return;

  async function boot() {
    const element = (id) => document.getElementById(id);
    const refs = {};
    ["session-select", "sync-toggle", "reader-help", "help-toggle", "lesson-title", "lesson-counts", "reader-columns", "load-error", "load-error-text", "reload-button", "transcript-pane", "block-position", "block-status", "video-link", "slide-prev", "slide-next", "slide-page", "slide-scroll", "slide-title", "original-link", "slide-stage", "slide-placeholder", "slide-image", "image-error", "image-retry", "pair-status", "related-blocks", "candidate-slides", "slide-thumbnails", "edit-start", "edit-controls", "edit-label", "edit-save", "edit-unmatch", "edit-cancel", "correction-summary", "export-corrections", "import-corrections", "reset-corrections", "undo-reset", "import-file", "reader-status"].forEach((id) => { refs[id] = element(id); });
    const state = {
      manifest: null, lesson: null, sessionId: null, language: "zh", sync: true,
      activeBlockId: null, activeSlideId: null, editBlockId: null,
      corrections: Object.create(null), mappings: null, undoCorrections: null,
      blockNodes: new Map(), thumbNodes: new Map(), blocks: new Map(), slides: new Map(),
      requestGate: createRequestGate(), controller: null, ignoreScrollUntil: 0, scrollFrame: null, resizeFrame: null,
      imageGeneration: 0, origin: "block"
    };
    const announce = (message) => { refs["reader-status"].textContent = message; };
    const make = (tag, className, text) => {
      const node = document.createElement(tag);
      if (className) node.className = className;
      if (text !== undefined) node.textContent = text;
      return node;
    };
    const setLink = (node, value) => {
      const url = externalURL(value);
      node.hidden = !url;
      if (url) node.href = url;
      else node.removeAttribute("href");
    };
    const storageKey = () => STORAGE_PREFIX + state.sessionId;

    function persistCorrections() {
      try {
        localStorage.setItem(storageKey(), JSON.stringify(exportCorrections(state.lesson, state.corrections)));
        return true;
      } catch (_) {
        announce("此浏览器无法保存校对；本次校对仍可使用，请导出 JSON 备份。");
        return false;
      }
    }

    function loadCorrections() {
      try {
        const raw = localStorage.getItem(storageKey());
        return raw ? importCorrections(JSON.parse(raw), state.lesson) : Object.create(null);
      } catch (_) {
        announce("已忽略不兼容的本地校对数据，使用自动对应。可重新导入有效备份。");
        return Object.create(null);
      }
    }

    function updateURL() {
      if (!state.sessionId) return;
      const url = new URL(location.href);
      url.searchParams.set("session", state.sessionId);
      url.searchParams.set("lang", state.language);
      const hash = new URLSearchParams();
      if (state.activeBlockId) hash.set("block", state.activeBlockId);
      if (state.activeSlideId) hash.set("slide", state.activeSlideId);
      url.hash = hash.toString();
      history.replaceState(null, "", url.href);
    }

    function badgeForBlock(block) {
      if (own(state.corrections, block.id)) return state.corrections[block.id] ? ["已校对", "manual"] : ["手动标为未对应", "weak"];
      if (!state.mappings.blockToSlide.get(block.id)) return ["暂无可靠对应", "weak"];
      if (block.match_source === "editorial_text_review") return ["图文校核 · 估计对应", ""];
      return block.confidence === "weak" ? ["候选对应 · 待校对", "weak"] : ["自动对应 · 待校对", ""];
    }

    function renderTranscript() {
      state.blockNodes.clear();
      const fragment = document.createDocumentFragment();
      state.lesson.blocks.forEach((block, index) => {
        const article = make("article", "transcript-block" + (state.language === "both" ? " bilingual" : ""));
        article.id = "block-" + block.id;
        article.dataset.blockId = block.id;
        const top = make("div", "block-top");
        const select = make("button", "block-select", String(index + 1).padStart(2, "0") + "  ·  " + formatTime(block.start_ms) + "–" + formatTime(block.end_ms));
        select.type = "button";
        select.setAttribute("aria-label", "阅读第 " + (index + 1) + " 段，" + formatTime(block.start_ms));
        select.addEventListener("click", () => selectBlock(block.id, { origin: "block", scroll: false }));
        const badge = badgeForBlock(block);
        top.append(select, make("span", "block-match " + badge[1], badge[0]));
        article.append(top);
        if (state.language !== "en") article.append(make("p", "block-text chinese", block.zh || "本段暂无中文译文。"));
        if (state.language !== "zh") article.append(make("p", "block-text english", block.en || "English transcript unavailable."));
        article.addEventListener("click", (event) => {
          if (event.target.closest("button,a") || (global.getSelection && String(global.getSelection()).length)) return;
          selectBlock(block.id, { origin: "block", scroll: false });
        });
        fragment.append(article);
        state.blockNodes.set(block.id, article);
      });
      if (!state.lesson.blocks.length) fragment.append(make("p", "empty-state", "本章节暂无视频讲稿。你可以在右侧独立浏览已有 slides，或返回课程查看预览与 Readings guidance。"));
      refs["transcript-pane"].replaceChildren(fragment);
      updateBlockAppearance();
    }

    function renderSlideNavigation() {
      const options = document.createDocumentFragment();
      const thumbnails = document.createDocumentFragment();
      state.thumbNodes.clear();
      state.lesson.slides.forEach((slide, index) => {
        const option = make("option", "", (index + 1) + " / " + state.lesson.slides.length);
        option.value = slide.id;
        options.append(option);
        const button = make("button", "thumbnail");
        button.type = "button";
        button.setAttribute("aria-label", (slide.deck_id || "Slides") + "，第 " + slide.page + " 页" + (slide.title ? "，" + slide.title : ""));
        button.title = (slide.title || "Slide") + " · " + (slide.deck_id || "") + " p." + slide.page;
        const image = make("img");
        image.loading = "lazy";
        image.decoding = "async";
        image.alt = "";
        image.width = 86;
        image.height = 61;
        try { image.src = localURL(slide.image_url, document.baseURI); } catch (_) { /* Main viewer reports invalid images. */ }
        button.append(image, make("span", "", (index + 1) + " · p." + slide.page));
        button.addEventListener("click", () => selectSlide(slide.id, { origin: "slide" }));
        thumbnails.append(button);
        state.thumbNodes.set(slide.id, button);
      });
      refs["slide-page"].replaceChildren(options);
      refs["slide-thumbnails"].replaceChildren(thumbnails);
      refs["slide-page"].disabled = !state.lesson.slides.length;
      refs["slide-thumbnails"].hidden = !state.lesson.slides.length;
    }

    function updateBlockAppearance() {
      state.blockNodes.forEach((node, id) => {
        const active = id === state.activeBlockId;
        node.classList.toggle("active", active);
        const button = node.querySelector(".block-select");
        if (active) button.setAttribute("aria-current", "true");
        else button.removeAttribute("aria-current");
      });
      const block = state.blocks.get(state.activeBlockId);
      const index = block ? state.lesson.blocks.findIndex((entry) => entry.id === block.id) : -1;
      refs["block-position"].textContent = index >= 0 ? "段落 " + (index + 1) + " / " + state.lesson.blocks.length : "暂无讲稿";
      refs["block-status"].textContent = block ? badgeForBlock(block)[0] + " · " + formatTime(block.start_ms) : "本章节暂无视频讲稿";
      if (block && externalURL(state.lesson.video_url)) {
        const url = new URL(state.lesson.video_url);
        url.searchParams.set("t", String(Math.floor(block.start_ms / 1000)));
        setLink(refs["video-link"], url.href);
      } else setLink(refs["video-link"], null);
      refs["edit-start"].disabled = !block || Boolean(state.editBlockId);
    }

    function scrollToBlock(id) {
      const node = state.blockNodes.get(id);
      if (!node) return;
      const pane = refs["transcript-pane"];
      state.ignoreScrollUntil = performance.now() + 350;
      const top = node.getBoundingClientRect().top - pane.getBoundingClientRect().top + pane.scrollTop - 14;
      pane.scrollTo({ top: Math.max(0, top), behavior: "auto" });
    }

    function selectBlock(id, options = {}) {
      if (!state.lesson || !state.blocks.has(id)) return;
      if (state.editBlockId && state.editBlockId !== id) {
        if (options.origin !== "scroll") announce("正在校对已固定的段落；请先保存或取消，再选择其他段落。");
        return;
      }
      state.activeBlockId = id;
      state.origin = options.origin || "block";
      updateBlockAppearance();
      if (options.scroll) scrollToBlock(id);
      if (state.sync && !state.editBlockId && state.origin !== "slide") {
        const slideId = state.mappings.blockToSlide.get(id);
        if (slideId) selectSlide(slideId, { origin: "block", skipURL: true });
      }
      updatePairStatus();
      updateURL();
    }

    function selectSlide(id, options = {}) {
      if (!state.lesson) return;
      const slide = state.slides.get(id);
      if (!slide) return;
      const changed = state.activeSlideId !== id;
      state.activeSlideId = id;
      state.origin = options.origin || "slide";
      if (changed) {
        renderCurrentSlide();
        if (!state.editBlockId) refs["slide-scroll"].scrollTo({ top: 0, behavior: "auto" });
      }
      if (state.sync && !state.editBlockId && state.origin === "slide") {
        const blockId = chooseBlockForSlide(state.mappings, id, state.activeBlockId);
        if (blockId) {
          state.activeBlockId = blockId;
          updateBlockAppearance();
          scrollToBlock(blockId);
        }
      }
      updatePairStatus();
      updateEditControls();
      if (!options.skipURL) updateURL();
    }

    function renderCurrentSlide(retry = false) {
      const slide = state.slides.get(state.activeSlideId);
      const generation = ++state.imageGeneration;
      refs["image-error"].hidden = true;
      refs["slide-image"].hidden = !slide;
      refs["slide-placeholder"].hidden = Boolean(slide);
      if (!slide) {
        refs["slide-stage"].classList.remove("loading");
        refs["slide-image"].removeAttribute("src");
        refs["slide-title"].textContent = "暂无 slides";
        refs["slide-placeholder"].textContent = "本章节尚无可用 slides。已有讲稿仍可独立阅读。";
        refs["slide-prev"].disabled = true;
        refs["slide-next"].disabled = true;
        setLink(refs["original-link"], null);
        return;
      }
      const index = state.lesson.slides.findIndex((item) => item.id === slide.id);
      const deck = (state.lesson.decks || []).find((item) => item.id === slide.deck_id);
      refs["slide-title"].textContent = (deck ? deck.title : (slide.deck_id || "Slides")) + " · 原始第 " + slide.page + " 页";
      refs["slide-title"].title = slide.title || refs["slide-title"].textContent;
      const source = externalURL(slide.source_url || (deck && deck.source_url));
      if (source) {
        const url = new URL(source);
        url.hash = "page=" + slide.page;
        setLink(refs["original-link"], url.href);
      } else setLink(refs["original-link"], null);
      refs["slide-prev"].disabled = index <= 0;
      refs["slide-next"].disabled = index >= state.lesson.slides.length - 1;
      refs["slide-page"].value = slide.id;
      state.thumbNodes.forEach((node, id) => node.setAttribute("aria-current", id === slide.id ? "true" : "false"));
      const thumb = state.thumbNodes.get(slide.id);
      if (thumb) {
        const strip = refs["slide-thumbnails"];
        const left = thumb.getBoundingClientRect().left - strip.getBoundingClientRect().left + strip.scrollLeft;
        if (left < strip.scrollLeft || left + thumb.offsetWidth > strip.scrollLeft + strip.clientWidth) strip.scrollTo({ left: Math.max(0, left - strip.clientWidth / 2 + thumb.offsetWidth / 2), behavior: "auto" });
      }
      const image = refs["slide-image"];
      image.alt = (slide.title || "课程 slide") + "，" + (deck ? deck.title : "") + "，第 " + slide.page + " 页";
      refs["slide-stage"].classList.add("loading");
      image.onload = () => {
        if (generation !== state.imageGeneration) return;
        if (image.naturalWidth > 0 && image.naturalHeight > 0) refs["slide-stage"].style.aspectRatio = image.naturalWidth + " / " + image.naturalHeight;
        refs["slide-stage"].classList.remove("loading");
        refs["image-error"].hidden = true;
      };
      image.onerror = () => {
        if (generation !== state.imageGeneration) return;
        refs["slide-stage"].classList.remove("loading");
        refs["image-error"].hidden = false;
      };
      try {
        const url = new URL(localURL(slide.image_url, document.baseURI));
        if (retry) url.searchParams.set("retry", String(Date.now()));
        image.src = url.href;
      } catch (_) { image.onerror(); }
    }

    function updatePairStatus() {
      const block = state.blocks.get(state.activeBlockId);
      const slide = state.slides.get(state.activeSlideId);
      const mapped = block ? state.mappings.blockToSlide.get(block.id) : null;
      const ids = slide ? state.mappings.slideToBlocks.get(slide.id) || [] : [];
      let message = "";
      let warning = false;
      if (state.editBlockId) message = "已固定当前段落。自由切换右侧 slide，选好后保存对应关系。";
      else if (!slide) { message = "本章节暂无可用 slides，可继续阅读讲稿。"; warning = true; }
      else if (state.origin === "slide" && !ids.length) { message = "本页暂无对应讲稿；左侧保留之前的阅读位置。"; warning = true; }
      else if (block && !mapped) { message = "本段暂无可靠对应；右侧保留当前 slide，可手动校对。"; warning = true; }
      else if (!block) { message = "本章节暂无视频讲稿，当前为 slides 独立阅读。"; warning = true; }
      else if (mapped !== slide.id) { message = "讲稿与当前 slide 暂未对应。" + (!state.sync ? "双向同步已关闭。" : "可点击段落恢复对应位置。"); warning = true; }
      else if (own(state.corrections, block.id)) message = "当前段落与此页已手动对应。";
      else if (block.match_source === "editorial_text_review") message = "图文校核 · 估计对应。已结合讲稿与 slide 内容检查，仍可继续校对。";
      else message = "当前段落自动对应到此页，建议结合内容校对。";
      refs["pair-status"].textContent = message;
      refs["pair-status"].classList.toggle("warning", warning);
      const fragment = document.createDocumentFragment();
      if (ids.length) {
        fragment.append(make("span", "", "本页讲稿"));
        ids.forEach((id) => {
          const related = state.blocks.get(id);
          const button = make("button", "", formatTime(related.start_ms));
          button.type = "button";
          button.setAttribute("aria-label", "跳到本页讲稿 " + formatTime(related.start_ms));
          button.setAttribute("aria-pressed", id === state.activeBlockId ? "true" : "false");
          button.addEventListener("click", () => selectBlock(id, { origin: "block", scroll: true }));
          fragment.append(button);
        });
      }
      refs["related-blocks"].replaceChildren(fragment);
      renderCandidates(block);
    }

    function renderCandidates(block) {
      const fragment = document.createDocumentFragment();
      const seen = new Set();
      const candidates = block && Array.isArray(block.candidates) ? block.candidates.filter((candidate) => {
        if (!record(candidate) || !state.slides.has(candidate.slide_id) || seen.has(candidate.slide_id)) return false;
        seen.add(candidate.slide_id);
        return true;
      }).slice(0, 3) : [];
      if (candidates.length) {
        fragment.append(make("span", "", "参考候选 · 点击校对"));
        candidates.forEach((candidate) => {
          const slide = state.slides.get(candidate.slide_id);
          const deck = (state.lesson.decks || []).find((item) => item.id === slide.deck_id);
          const multiDeck = (state.lesson.decks || []).length > 1;
          const label = (multiDeck ? (slide.deck_id || "Slides") + " · " : "") + "p." + slide.page;
          const button = make("button", "", label);
          button.type = "button";
          button.setAttribute("aria-label", "固定当前段落并预览候选 slide：" + (deck ? deck.title + "，" : "") + "第 " + slide.page + " 页；不会自动保存");
          const terms = Array.isArray(candidate.evidence_terms) ? candidate.evidence_terms.filter((term) => typeof term === "string").slice(0, 5) : [];
          button.title = (slide.title || "候选 slide") + (terms.length ? " · 相关词：" + terms.join(", ") : "") + " · 仅预览，需手动保存";
          button.addEventListener("click", () => {
            if (!state.lesson || !state.blocks.has(block.id)) return;
            state.activeBlockId = block.id;
            state.editBlockId = block.id;
            updateBlockAppearance();
            selectSlide(slide.id, { origin: "candidate" });
            announce("已固定当前段落并打开候选 slide；尚未保存。确认内容后点击「将本段对应到当前页」。");
          });
          fragment.append(button);
        });
      }
      refs["candidate-slides"].replaceChildren(fragment);
      refs["candidate-slides"].hidden = !candidates.length;
    }

    function updateEditControls() {
      const editing = Boolean(state.editBlockId);
      refs["edit-controls"].hidden = !editing;
      refs["edit-start"].disabled = editing || !state.activeBlockId;
      refs["edit-save"].disabled = !state.activeSlideId;
      refs["correction-summary"].textContent = Object.keys(state.corrections).length + " 段手动校对 · 仅保存在此浏览器";
      refs["reset-corrections"].disabled = !Object.keys(state.corrections).length;
      refs["export-corrections"].disabled = !state.lesson;
      refs["import-corrections"].disabled = !state.lesson;
      refs["undo-reset"].hidden = !state.undoCorrections;
      if (editing) {
        const block = state.blocks.get(state.editBlockId);
        const slide = state.slides.get(state.activeSlideId);
        refs["edit-label"].textContent = "固定段落 " + formatTime(block.start_ms) + "。" + (slide ? "待保存：" + (slide.deck_id || "Slides") + " 第 " + slide.page + " 页。" : "请选择一张 slide。") + "校对期间暂停自动跳转。";
      }
    }

    function applyCorrections(message) {
      state.mappings = deriveMappings(state.lesson, state.corrections);
      state.editBlockId = null;
      renderTranscript();
      if (state.activeBlockId) selectBlock(state.activeBlockId, { origin: "block", scroll: true });
      else updatePairStatus();
      updateEditControls();
      const saved = persistCorrections();
      if (saved) announce(message);
    }

    async function fetchJSON(url, signal) {
      const response = await fetch(localURL(url, document.baseURI), { signal });
      if (!response.ok) throw new Error("资源加载失败（HTTP " + response.status + "）。");
      return response.json();
    }

    async function loadSession(id, deepLink) {
      const entry = state.manifest.sessions.find((session) => session.id === id);
      if (!entry) return;
      const token = state.requestGate.next();
      if (state.controller) state.controller.abort();
      state.controller = new AbortController();
      state.sessionId = id;
      state.lesson = null;
      state.editBlockId = null;
      state.undoCorrections = null;
      state.activeBlockId = null;
      state.activeSlideId = null;
      refs["slide-scroll"].scrollTo({ top: 0, behavior: "auto" });
      refs["session-select"].value = id;
      refs["reader-columns"].setAttribute("aria-busy", "true");
      refs["load-error"].hidden = true;
      refs["lesson-title"].textContent = entry.title;
      announce("正在载入章节…");
      try {
        const lesson = validateLesson(await fetchJSON(entry.data_url, state.controller.signal), id);
        if (!state.requestGate.current(token)) return;
        state.lesson = lesson;
        state.blocks = new Map(lesson.blocks.map((block) => [block.id, block]));
        state.slides = new Map(lesson.slides.map((slide) => [slide.id, slide]));
        state.corrections = loadCorrections();
        state.mappings = deriveMappings(lesson, state.corrections);
        refs["lesson-title"].textContent = lesson.title || entry.title;
        refs["lesson-counts"].textContent = lesson.blocks.length + " 段讲稿 · " + lesson.slides.length + " 页 slides";
        document.title = (lesson.title || entry.title) + " · 讲稿 × Slides";
        renderTranscript();
        renderSlideNavigation();
        const firstBlock = deepLink && state.blocks.has(deepLink.block) ? deepLink.block : (lesson.blocks[0] && lesson.blocks[0].id);
        const desiredSlide = deepLink && state.slides.has(deepLink.slide) ? deepLink.slide : null;
        if (firstBlock) selectBlock(firstBlock, { origin: "block", scroll: true });
        if (desiredSlide) selectSlide(desiredSlide, { origin: "deeplink" });
        else if (!state.activeSlideId && lesson.slides.length) selectSlide(lesson.slides[0].id, { origin: "initial" });
        else if (!lesson.slides.length) renderCurrentSlide();
        updatePairStatus();
        updateEditControls();
        refs["reader-columns"].setAttribute("aria-busy", "false");
        updateURL();
        announce("已载入 " + (lesson.title || entry.title) + "。点击或滚动讲稿、切换 slide，即可双向阅读。对应关系为自动估计。");
      } catch (error) {
        if (!state.requestGate.current(token) || error.name === "AbortError") return;
        refs["load-error-text"].textContent = error.message || "章节加载失败。";
        refs["load-error"].hidden = false;
        refs["lesson-counts"].textContent = "加载失败";
        announce("章节尚未载入，请重新加载或选择其他章节。");
      }
    }

    function nextSlide(delta) {
      if (!state.lesson) return;
      const index = state.lesson.slides.findIndex((slide) => slide.id === state.activeSlideId);
      const slide = state.lesson.slides[index + delta];
      if (slide) selectSlide(slide.id, { origin: "slide" });
    }

    function setLanguage(language) {
      if (!["zh", "en", "both"].includes(language)) return;
      state.language = language;
      document.querySelectorAll("[data-language]").forEach((button) => button.setAttribute("aria-pressed", button.dataset.language === language ? "true" : "false"));
      if (state.lesson) {
        renderTranscript();
        if (state.activeBlockId) scrollToBlock(state.activeBlockId);
        updateURL();
      }
    }

    refs["session-select"].addEventListener("change", () => loadSession(refs["session-select"].value));
    document.querySelectorAll("[data-language]").forEach((button) => button.addEventListener("click", () => setLanguage(button.dataset.language)));
    refs["sync-toggle"].addEventListener("change", () => {
      state.sync = refs["sync-toggle"].checked;
      if (state.sync && state.activeBlockId && !state.editBlockId) selectBlock(state.activeBlockId, { origin: "block", scroll: false });
      updatePairStatus();
      announce(state.sync ? "双向同步已开启。" : "双向同步已关闭，可分别浏览讲稿与 slides。");
    });
    refs["help-toggle"].addEventListener("click", () => {
      refs["reader-help"].hidden = !refs["reader-help"].hidden;
      refs["help-toggle"].setAttribute("aria-expanded", refs["reader-help"].hidden ? "false" : "true");
    });
    refs["slide-prev"].addEventListener("click", () => nextSlide(-1));
    refs["slide-next"].addEventListener("click", () => nextSlide(1));
    refs["slide-page"].addEventListener("change", () => selectSlide(refs["slide-page"].value, { origin: "slide" }));
    refs["image-retry"].addEventListener("click", () => renderCurrentSlide(true));
    refs["reload-button"].addEventListener("click", () => state.manifest ? loadSession(state.sessionId) : location.reload());
    document.addEventListener("keydown", (event) => {
      if (event.defaultPrevented || event.altKey || event.ctrlKey || event.metaKey || event.shiftKey || event.target.closest("input,select,textarea,[contenteditable=true]") || !state.lesson) return;
      if (event.key === "ArrowLeft" || event.key === "ArrowRight") { event.preventDefault(); nextSlide(event.key === "ArrowLeft" ? -1 : 1); }
      if (event.key === "Escape" && state.editBlockId) { state.editBlockId = null; updateEditControls(); updatePairStatus(); announce("已取消校对，对应关系未更改。"); }
    });
    refs["transcript-pane"].addEventListener("scroll", () => {
      if (state.scrollFrame !== null) return;
      state.scrollFrame = requestAnimationFrame(() => {
        state.scrollFrame = null;
        if (!state.lesson || !state.sync || state.editBlockId || performance.now() < state.ignoreScrollUntil) return;
        const pane = refs["transcript-pane"];
        const target = pane.getBoundingClientRect().top + Math.min(90, pane.clientHeight * .2);
        let candidate = null;
        let distance = Infinity;
        state.blockNodes.forEach((node, id) => {
          const rect = node.getBoundingClientRect();
          const current = rect.top <= target && rect.bottom > target ? 0 : Math.abs(rect.top - target);
          if (current < distance) { distance = current; candidate = id; }
        });
        if (candidate && candidate !== state.activeBlockId) selectBlock(candidate, { origin: "scroll", scroll: false });
      });
    }, { passive: true });
    global.addEventListener("resize", () => {
      // Reflow may emit a scroll event before the active paragraph is re-anchored.
      state.ignoreScrollUntil = performance.now() + 350;
      if (state.resizeFrame !== null) return;
      state.resizeFrame = requestAnimationFrame(() => {
        state.resizeFrame = null;
        if (state.lesson) scrollToBlock(state.editBlockId || state.activeBlockId);
      });
    }, { passive: true });
    refs["edit-start"].addEventListener("click", () => {
      if (!state.activeBlockId) return;
      state.editBlockId = state.activeBlockId;
      updateEditControls();
      updatePairStatus();
      announce("已固定当前段落。请浏览右侧 slides，选好对应页后保存。");
    });
    refs["edit-cancel"].addEventListener("click", () => { state.editBlockId = null; updateEditControls(); updatePairStatus(); announce("已取消校对，对应关系未更改。"); });
    refs["edit-save"].addEventListener("click", () => {
      if (!state.editBlockId || !state.activeSlideId) return;
      state.corrections[state.editBlockId] = state.activeSlideId;
      state.activeBlockId = state.editBlockId;
      state.undoCorrections = null;
      applyCorrections("已保存当前段落与 slide 的对应关系。");
    });
    refs["edit-unmatch"].addEventListener("click", () => {
      if (!state.editBlockId) return;
      state.corrections[state.editBlockId] = null;
      state.activeBlockId = state.editBlockId;
      state.undoCorrections = null;
      applyCorrections("已将当前段落标为未对应。");
    });
    refs["export-corrections"].addEventListener("click", () => {
      if (!state.lesson) return;
      const blob = new Blob([JSON.stringify(exportCorrections(state.lesson, state.corrections), null, 2) + "\n"], { type: "application/json" });
      const url = URL.createObjectURL(blob);
      const link = make("a");
      link.href = url;
      link.download = COURSE_ID + "-" + state.sessionId + "-corrections.json";
      document.body.append(link);
      link.click();
      link.remove();
      setTimeout(() => URL.revokeObjectURL(url), 1000);
      announce("已导出当前章节的校对 JSON。");
    });
    refs["import-corrections"].addEventListener("click", () => refs["import-file"].click());
    refs["import-file"].addEventListener("change", async () => {
      const file = refs["import-file"].files[0];
      refs["import-file"].value = "";
      if (!file || !state.lesson) return;
      const session = state.sessionId;
      const lesson = state.lesson;
      try {
        if (file.size > 1024 * 1024) throw new Error("校对文件超过 1 MB，已停止导入。");
        const imported = importCorrections(JSON.parse(await file.text()), lesson);
        if (state.sessionId !== session || state.lesson !== lesson) throw new Error("章节已切换，请在当前章节重新导入。");
        state.undoCorrections = { ...state.corrections };
        state.corrections = Object.assign(Object.create(null), state.corrections, imported);
        applyCorrections("已合并导入当前章节的校对。可使用「撤销恢复」回到导入前。");
      } catch (error) { announce("导入未完成：" + (error.message || "JSON 格式不正确。")); }
    });
    refs["reset-corrections"].addEventListener("click", () => {
      if (!state.lesson || !Object.keys(state.corrections).length) return;
      state.undoCorrections = { ...state.corrections };
      state.corrections = Object.create(null);
      applyCorrections("当前章节已恢复自动对应。可点击「撤销恢复」找回之前的校对。");
    });
    refs["undo-reset"].addEventListener("click", () => {
      if (!state.lesson || !state.undoCorrections) return;
      state.corrections = Object.assign(Object.create(null), state.undoCorrections);
      state.undoCorrections = null;
      applyCorrections("已恢复上一步之前的校对。");
    });

    const navigateFromURL = () => {
      if (!state.manifest) return;
      const deep = readDeepLink(location.href);
      if (deep.language) setLanguage(deep.language);
      if (deep.session && deep.session !== state.sessionId) { loadSession(deep.session, deep); return; }
      if (!state.lesson) return;
      state.editBlockId = null;
      if (deep.block && state.blocks.has(deep.block)) selectBlock(deep.block, { origin: "deeplink", scroll: true });
      if (deep.slide && state.slides.has(deep.slide)) selectSlide(deep.slide, { origin: "deeplink" });
      updateEditControls();
    };
    global.addEventListener("hashchange", navigateFromURL);
    global.addEventListener("popstate", navigateFromURL);

    try {
      const manifest = await fetchJSON("./manifest.json");
      if (!record(manifest) || !Array.isArray(manifest.sessions) || !manifest.sessions.length) throw new Error("课程目录为空或格式不正确。");
      const ids = new Set();
      manifest.sessions.forEach((session) => {
        if (!record(session) || !validId(session.id) || ids.has(session.id) || typeof session.title !== "string" || typeof session.data_url !== "string") throw new Error("课程目录含有无效或重复章节。");
        localURL(session.data_url, document.baseURI);
        ids.add(session.id);
      });
      state.manifest = manifest;
      refs["session-select"].replaceChildren(...manifest.sessions.map((session) => {
        const option = make("option", "", session.title);
        option.value = session.id;
        return option;
      }));
      refs["session-select"].disabled = false;
      const deep = readDeepLink(location.href);
      if (deep.language) setLanguage(deep.language);
      const requested = ids.has(deep.session) ? deep.session : (ids.has(manifest.default_session) ? manifest.default_session : manifest.sessions[0].id);
      await loadSession(requested, deep);
    } catch (error) {
      refs["load-error-text"].textContent = error.message || "无法加载课程目录。";
      refs["load-error"].hidden = false;
      announce("阅读器尚未载入。请重新加载，或返回现有课程页面继续阅读。");
    }
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot, { once: true });
  else boot();
})(typeof window !== "undefined" ? window : globalThis);
