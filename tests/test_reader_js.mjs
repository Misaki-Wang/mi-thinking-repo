import test from 'node:test';
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import { readFileSync } from 'node:fs';
import vm from 'node:vm';

const require = createRequire(import.meta.url);
const core = require('../reader/app/reader.js');
const script = readFileSync(new URL('../reader/app/reader.js', import.meta.url), 'utf8');
const html = readFileSync(new URL('../reader/app/index.html', import.meta.url), 'utf8');
const fixture = (id = 'w01-1') => ({
  session_id: id, title: 'Week 1 · Introduction', video_url: 'https://www.youtube.com/watch?v=example',
  blocks: [
    { id: 'b1', start_ms: 0, end_ms: 30000, en: 'Representation learning.', zh: 'Representation learning（表征学习）。', slide_id: 's1', confidence: 'estimated' },
    { id: 'b2', start_ms: 30000, end_ms: 60000, en: 'Another view.', zh: '另一种观点。', slide_id: 's1', confidence: 'estimated' },
    { id: 'b3', start_ms: 60000, end_ms: 90000, en: 'An uncertain passage.', zh: '不确定的段落。', slide_id: null, confidence: 'unmatched', candidates: [{ slide_id: 's2', evidence_terms: ['fusion'] }, { slide_id: 's1' }, { slide_id: 's3' }, { slide_id: 's2' }, { slide_id: 'missing' }] },
    { id: 'b4', start_ms: 90000, end_ms: 120000, en: 'Fusion.', zh: 'Fusion（融合）。', slide_id: 's2', confidence: 'estimated' },
  ],
  slides: [1, 2, 3].map((page) => ({ id: 's' + page, page, deck_id: 'd1', title: 'Slide ' + page, image_url: './slides/' + page + '.webp', source_url: 'https://example.org/slides.pdf', block_ids: [] })),
  decks: [{ id: 'd1', title: 'Lecture slides', source_url: 'https://example.org/slides.pdf' }],
});

test('many-to-one reverse navigation retains the current paragraph, otherwise chooses the first', () => {
  const mapping = core.deriveMappings(fixture(), {});
  assert.deepEqual(mapping.slideToBlocks.get('s1'), ['b1', 'b2']);
  assert.equal(core.chooseBlockForSlide(mapping, 's1', 'b2'), 'b2');
  assert.equal(core.chooseBlockForSlide(mapping, 's1', 'b4'), 'b1');
  assert.equal(core.chooseBlockForSlide(mapping, 's3', 'b4'), null);
});

test('manual reassignment rebuilds inverse mapping without mutating the source', () => {
  const lesson = fixture();
  const before = JSON.stringify(lesson);
  const mapping = core.deriveMappings(lesson, { b2: 's2', b4: null });
  assert.equal(mapping.blockToSlide.get('b2'), 's2');
  assert.deepEqual(mapping.slideToBlocks.get('s1'), ['b1']);
  assert.deepEqual(mapping.slideToBlocks.get('s2'), ['b2']);
  assert.equal(mapping.blockToSlide.get('b4'), null);
  assert.equal(JSON.stringify(lesson), before);
});

test('import is session-scoped and rejects invalid IDs atomically', () => {
  const lesson = fixture();
  const packet = core.exportCorrections(lesson, { b3: 's3', b4: null });
  assert.deepEqual({ ...core.importCorrections(packet, lesson) }, { b3: 's3', b4: null });
  assert.throws(() => core.importCorrections({ ...packet, session_id: 'w02-1' }, lesson));
  assert.throws(() => core.importCorrections({ ...packet, course_id: 'other-course' }, lesson));
  assert.throws(() => core.importCorrections({ ...packet, corrections: { b3: 's3', not_a_block: 's1' } }, lesson));
  assert.throws(() => core.importCorrections({ ...packet, corrections: { b3: 'missing_slide' } }, lesson));
  assert.throws(() => core.importCorrections({ ...packet, corrections: [] }, lesson));
  assert.throws(() => core.importCorrections({ ...packet, corrections: JSON.parse('{"__proto__":"s1"}') }, lesson));
});

test('lesson validation catches dangling mappings, duplicate IDs, and invalid timestamps', () => {
  assert.equal(core.validateLesson(fixture(), 'w01-1').blocks.length, 4);
  assert.throws(() => core.validateLesson(fixture(), 'w02-1'));
  const dangling = fixture(); dangling.blocks[0].slide_id = 'missing';
  assert.throws(() => core.validateLesson(dangling, 'w01-1'));
  const repeated = fixture(); repeated.slides[1].id = 's1';
  assert.throws(() => core.validateLesson(repeated, 'w01-1'));
  const invalid = fixture(); invalid.blocks[1].end_ms = 0;
  assert.throws(() => core.validateLesson(invalid, 'w01-1'));
});

test('empty lessons and unmatched paragraphs remain representable', () => {
  const lesson = fixture(); lesson.blocks = []; lesson.slides = [];
  assert.equal(core.validateLesson(lesson, 'w01-1'), lesson);
  assert.equal(core.deriveMappings(lesson, {}).slideToBlocks.size, 0);
  assert.equal(core.deriveMappings(fixture(), {}).blockToSlide.get('b3'), null);
});

test('asset URLs are local to reader and external source links cannot execute scripts', () => {
  const base = 'https://example.org/repo/reader/course/index.html';
  assert.equal(core.localURL('./slides/page.webp', base), 'https://example.org/repo/reader/course/slides/page.webp');
  assert.throws(() => core.localURL('../../../private.json', base));
  assert.throws(() => core.localURL('https://other.org/image.png', base));
  assert.throws(() => core.localURL('javascript:alert(1)', base));
  assert.equal(core.externalURL('javascript:alert(1)'), null);
  assert.equal(core.externalURL('data:text/html,hello'), null);
  assert.equal(core.externalURL('https://example.org/slides.pdf'), 'https://example.org/slides.pdf');
});

test('request generation rejects stale chapter responses', () => {
  const gate = core.createRequestGate();
  const first = gate.next();
  const second = gate.next();
  assert.equal(gate.current(first), false);
  assert.equal(gate.current(second), true);
});

test('deep links preserve independent block and slide positions and bilingual mode', () => {
  assert.deepEqual(core.readDeepLink('https://example.org/index.html?session=w01-1&lang=both#block=b2&slide=s3'), { session: 'w01-1', language: 'both', block: 'b2', slide: 's3' });
  assert.equal(core.formatTime(3723000), '01:02:03');
  assert.equal(core.formatTime(61000), '01:01');
});

// A small deterministic DOM harness exercises the actual event handlers, without
// a browser dependency or network. It deliberately does not approximate layout QA.
class Node {
  constructor(tag = 'div') {
    this.tagName = tag.toUpperCase(); this.children = []; this.dataset = {}; this.attrs = {}; this.style = {};
    this.events = new Map(); this.className = ''; this.textContent = ''; this.hidden = false;
    this.value = ''; this.checked = true; this.scrollTop = 0; this.scrollLeft = 0;
    this.clientHeight = 500; this.clientWidth = 500; this.offsetWidth = 94;
    this.classList = {
      toggle: (name, on) => { const list = new Set(this.className.split(/\s+/).filter(Boolean)); if (on) list.add(name); else list.delete(name); this.className = [...list].join(' '); },
      add: (name) => this.classList.toggle(name, true), remove: (name) => this.classList.toggle(name, false),
    };
  }
  append(...nodes) { for (const node of nodes) { if (node.fragment) this.append(...node.children); else { node.parent = this; this.children.push(node); } } }
  replaceChildren(...nodes) { this.children = []; this.append(...nodes); }
  setAttribute(name, value) { this.attrs[name] = String(value); }
  removeAttribute(name) { delete this.attrs[name]; }
  addEventListener(type, handler) { const handlers = this.events.get(type) || []; handlers.push(handler); this.events.set(type, handlers); }
  async trigger(type, extras = {}) { for (const handler of this.events.get(type) || []) await handler({ target: this, preventDefault() {}, ...extras }); }
  closest(selector) { if (selector.split(',').some((tag) => tag.toUpperCase() === this.tagName)) return this; return this.parent ? this.parent.closest(selector) : null; }
  querySelector(selector) { for (const node of this.children) { if (selector.startsWith('.') && node.className.split(' ').includes(selector.slice(1))) return node; const nested = node.querySelector(selector); if (nested) return nested; } return null; }
  getBoundingClientRect() { const top = this.dataset.blockId ? (Number(this.dataset.blockId.slice(1)) - 1) * 200 - (this.parent?.scrollTop || 0) : 0; return { top, bottom: top + 180, left: 0 }; }
  scrollTo({ top, left }) { if (top !== undefined) this.scrollTop = top; if (left !== undefined) this.scrollLeft = left; }
  remove() { if (this.parent) this.parent.children = this.parent.children.filter((node) => node !== this); }
  click() { return this.trigger('click'); }
}

async function harness({ href = 'https://example.org/repo/reader/course/index.html', fetchLesson, initialStorage = {} } = {}) {
  const refs = new Map([...html.matchAll(/id="([^"]+)"/g)].map((match) => [match[1], new Node()]));
  const languages = ['zh', 'en', 'both'].map((language) => { const node = new Node('button'); node.dataset.language = language; return node; });
  const store = new Map(Object.entries(initialStorage));
  const fetchedURLs = [];
  const frames = [];
  const windowEvents = new Map();
  const document = new Node('document');
  document.readyState = 'complete'; document.baseURI = href; document.body = new Node('body');
  document.getElementById = (id) => refs.get(id);
  document.createElement = (tag) => new Node(tag);
  document.createDocumentFragment = () => { const node = new Node(); node.fragment = true; return node; };
  document.querySelectorAll = () => languages;
  const location = { href, reload() {} };
  const manifest = { sessions: ['w01-1', 'w02-1', 'w03-1'].map((id) => ({ id, title: id, data_url: './data/' + id + '.json' })), default_session: 'w01-1' };
  let now = 1000;
  const sandbox = {
    document, location, URL, URLSearchParams, AbortController, console, Blob,
    localStorage: { getItem: (key) => store.get(key) || null, setItem: (key, value) => store.set(key, value) },
    history: { replaceState: (_state, _title, url) => { location.href = url; } },
    performance: { now: () => now },
    requestAnimationFrame: (callback) => { frames.push(callback); return frames.length; },
    setTimeout, clearTimeout,
    addEventListener: (type, handler) => { const handlers = windowEvents.get(type) || []; handlers.push(handler); windowEvents.set(type, handlers); },
    getSelection: () => '',
    fetch: async (url) => {
      fetchedURLs.push(url);
      if (url === new URL('./manifest.json', href).href) return { ok: true, json: async () => manifest };
      const entry = manifest.sessions.find((session) => new URL(session.data_url, href).href === url);
      if (!entry) return { ok: false, status: 404 };
      const id = entry.id;
      return { ok: true, json: async () => fetchLesson ? fetchLesson(id) : fixture(id) };
    },
  };
  sandbox.window = sandbox;
  vm.runInNewContext(script, sandbox);
  const flush = async () => { await new Promise((resolve) => setImmediate(resolve)); await new Promise((resolve) => setImmediate(resolve)); };
  await flush();
  return { refs, languages, store, location, document, flush, fetchedURLs,
    block: (id) => refs.get('transcript-pane').children.find((node) => node.dataset.blockId === id),
    scroll: async (top) => { now += 1000; refs.get('transcript-pane').scrollTop = top; await refs.get('transcript-pane').trigger('scroll'); while (frames.length) frames.shift()(); },
    resize: async () => {
      now += 1000;
      // A browser can queue a scroll during reflow before delivering resize.
      await refs.get('transcript-pane').trigger('scroll');
      for (const handler of windowEvents.get('resize') || []) handler();
      while (frames.length) frames.shift()();
    },
  };
}

test('real UI events synchronize in both directions without changing many-to-one paragraph selection', async () => {
  const ui = await harness();
  assert.equal(ui.fetchedURLs[0], 'https://example.org/repo/reader/course/manifest.json');
  assert.equal(ui.refs.get('slide-page').value, 's1');
  await ui.block('b2').querySelector('.block-select').click();
  assert.equal(ui.refs.get('slide-page').value, 's1');
  ui.refs.get('slide-page').value = 's1'; await ui.refs.get('slide-page').trigger('change');
  assert.match(ui.refs.get('block-position').textContent, /2 \/ 4/);
  await ui.refs.get('slide-next').click();
  assert.equal(ui.refs.get('slide-page').value, 's2');
  assert.match(ui.refs.get('block-position').textContent, /4 \/ 4/);
  await ui.scroll(0);
  assert.equal(ui.refs.get('slide-page').value, 's1');
  assert.match(ui.refs.get('block-position').textContent, /1 \/ 4/);
});

test('unmatched paragraph and slide show honest status while retaining the independent reading position', async () => {
  const ui = await harness();
  await ui.block('b3').querySelector('.block-select').click();
  assert.equal(ui.refs.get('slide-page').value, 's1');
  assert.match(ui.refs.get('pair-status').textContent, /本段暂无可靠对应/);
  ui.refs.get('slide-page').value = 's3'; await ui.refs.get('slide-page').trigger('change');
  assert.match(ui.refs.get('pair-status').textContent, /本页暂无对应讲稿/);
  assert.match(ui.refs.get('block-position').textContent, /3 \/ 4/);
});

test('correction mode pins the original paragraph while browsing already-mapped slides, and reset is undoable', async () => {
  const ui = await harness();
  await ui.refs.get('edit-start').click();
  await ui.refs.get('slide-next').click();
  assert.equal(ui.refs.get('slide-page').value, 's2');
  assert.match(ui.refs.get('block-position').textContent, /1 \/ 4/);
  await ui.refs.get('edit-save').click();
  assert.match(ui.refs.get('pair-status').textContent, /已手动对应/);
  assert.equal(JSON.parse([...ui.store.values()][0]).corrections.b1, 's2');
  await ui.refs.get('reset-corrections').click();
  assert.equal(ui.refs.get('slide-page').value, 's1');
  assert.equal(ui.refs.get('undo-reset').hidden, false);
  await ui.refs.get('undo-reset').click();
  assert.equal(ui.refs.get('slide-page').value, 's2');
  assert.equal(JSON.parse([...ui.store.values()][0]).corrections.b1, 's2');
});

test('sync toggle permits independent navigation and Chinese is default', async () => {
  const ui = await harness();
  assert.equal(ui.block('b1').querySelector('.english'), null);
  ui.refs.get('sync-toggle').checked = false; await ui.refs.get('sync-toggle').trigger('change');
  await ui.refs.get('slide-next').click();
  assert.match(ui.refs.get('block-position').textContent, /1 \/ 4/);
  assert.match(ui.refs.get('pair-status').textContent, /双向同步已关闭/);
  await ui.languages[2].click();
  assert.ok(ui.block('b1').querySelector('.english'));
  assert.ok(ui.block('b1').querySelector('.chinese'));
  assert.match(ui.location.href, /lang=both/);
});

test('stale async chapter completion cannot replace the most recently selected chapter', async () => {
  let resolveSecond;
  const second = new Promise((resolve) => { resolveSecond = resolve; });
  const ui = await harness({ fetchLesson: (id) => id === 'w02-1' ? second : fixture(id) });
  const select = ui.refs.get('session-select');
  select.value = 'w02-1'; const pending = select.trigger('change');
  select.value = 'w03-1'; await select.trigger('change');
  resolveSecond(fixture('w02-1')); await pending; await ui.flush();
  assert.equal(select.value, 'w03-1');
  assert.match(ui.location.href, /session=w03-1/);
  assert.equal(ui.refs.get('reader-columns').attrs['aria-busy'], 'false');
});

test('deep-linked independent selections survive initial load', async () => {
  const ui = await harness({ href: 'https://example.org/repo/reader/course/index.html?session=w01-1&lang=both#block=b2&slide=s3' });
  assert.match(ui.refs.get('block-position').textContent, /2 \/ 4/);
  assert.equal(ui.refs.get('slide-page').value, 's3');
  assert.ok(ui.block('b2').querySelector('.english'));
  assert.match(ui.refs.get('pair-status').textContent, /暂未对应/);
});

test('candidate preview pins its paragraph and never silently stores the candidate mapping', async () => {
  const ui = await harness();
  await ui.block('b3').querySelector('.block-select').click();
  const candidates = ui.refs.get('candidate-slides');
  assert.equal(candidates.hidden, false);
  assert.equal(candidates.children.length, 4); // Label and three unique, valid candidates.
  await candidates.children[1].click();
  assert.equal(ui.refs.get('slide-page').value, 's2');
  assert.match(ui.refs.get('block-position').textContent, /3 \/ 4/);
  assert.equal(ui.refs.get('edit-controls').hidden, false);
  assert.equal(ui.store.size, 0);
  assert.match(ui.refs.get('reader-status').textContent, /尚未保存/);
  await ui.refs.get('edit-cancel').click();
  assert.match(ui.refs.get('block-status').textContent, /暂无可靠对应/);
  assert.equal(ui.store.size, 0);
});

test('source-based editorial estimates are distinguished from automated and local manual mappings', async () => {
  const ui = await harness({ fetchLesson: (id) => { const lesson = fixture(id); lesson.blocks[0].match_source = 'editorial_text_review'; return lesson; } });
  assert.match(ui.refs.get('block-status').textContent, /图文校核 · 估计对应/);
  assert.match(ui.refs.get('pair-status').textContent, /图文校核 · 估计对应/);
  await ui.refs.get('edit-start').click();
  await ui.refs.get('edit-save').click();
  assert.match(ui.refs.get('block-status').textContent, /已校对/);
  assert.match(ui.refs.get('pair-status').textContent, /已手动对应/);
});

test('slide image uses its natural aspect ratio and full extracted title remains a tooltip', async () => {
  const ui = await harness();
  const image = ui.refs.get('slide-image');
  image.naturalWidth = 1280; image.naturalHeight = 720;
  image.onload();
  assert.equal(ui.refs.get('slide-stage').style.aspectRatio, '1280 / 720');
  assert.equal(ui.refs.get('slide-title').textContent, 'Lecture slides · 原始第 1 页');
  assert.equal(ui.refs.get('slide-title').title, 'Slide 1');
});

test('changed slides and chapters reveal the slide top; same-page and pinned correction browsing retain position', async () => {
  const ui = await harness();
  const pane = ui.refs.get('slide-scroll');
  pane.scrollTop = 500;
  await ui.block('b2').querySelector('.block-select').click();
  assert.equal(pane.scrollTop, 500, 'same slide keeps the current scroll position');
  await ui.refs.get('slide-next').click();
  assert.equal(pane.scrollTop, 0, 'slide controls reveal a changed slide');
  pane.scrollTop = 500;
  await ui.block('b1').querySelector('.block-select').click();
  assert.equal(pane.scrollTop, 0, 'following a paragraph reveals its changed slide');
  await ui.refs.get('edit-start').click();
  pane.scrollTop = 500;
  await ui.refs.get('slide-next').click();
  assert.equal(pane.scrollTop, 500, 'pinned correction keeps its controls in view');
  ui.refs.get('session-select').value = 'w02-1';
  await ui.refs.get('session-select').trigger('change');
  assert.equal(pane.scrollTop, 0, 'switching chapters clears inherited scroll position');
});

test('viewport reflow re-anchors the active or pinned paragraph without choosing a different block or slide', async () => {
  const ui = await harness();
  const pane = ui.refs.get('transcript-pane');
  await ui.block('b4').querySelector('.block-select').click();
  pane.scrollTop = 90;
  await ui.resize();
  assert.equal(pane.scrollTop, 586, 'active paragraph returns to the top after reflow');
  assert.match(ui.refs.get('block-position').textContent, /4 \/ 4/);
  assert.equal(ui.refs.get('slide-page').value, 's2');
  await ui.block('b1').querySelector('.block-select').click();
  await ui.refs.get('edit-start').click();
  await ui.refs.get('slide-next').click();
  pane.scrollTop = 300;
  await ui.resize();
  assert.equal(pane.scrollTop, 0, 'pinned paragraph remains the reflow anchor');
  assert.match(ui.refs.get('block-position').textContent, /1 \/ 4/);
  assert.equal(ui.refs.get('slide-page').value, 's2', 'reflow does not change the candidate slide');
  assert.equal(ui.refs.get('edit-controls').hidden, false);
});
