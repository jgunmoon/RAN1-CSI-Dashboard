"""CSI 결정 HTML 대시보드(reports/index.html).

외부 스크립트 없이 한 파일로 동작합니다(글꼴만 Google Fonts, 없으면 시스템 글꼴). 같은 DB와 설정이면 같은 HTML이 나옵니다.
결정 전체를 JSON으로 넣고, 구분·범위 체크박스에 맞춰 직전 회의 대비 카드, 회의별 주제 차트, 표, 결정 목록을 브라우저에서 다시 그립니다.
기본 표시는 확정 범위의 Agreement입니다.
"""
import json
from html import escape

from scripts.model import TYPES, provisional, short

TITLE = "RAN1 CSI 결정 대시보드"
CHECKED_AT = '<span class="checked" hidden>__CHECKED_AT__</span>'
# 주제 색: dataviz 기본 범주 팔레트 1~5번(순서 고정, 인접 쌍 색각이상 검증됨). 마지막(기타)은 회색.
SERIES_LIGHT = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4"]
SERIES_DARK = ["#3987e5", "#d95926", "#199e70", "#c98500", "#d55181"]
OTHER = ("#9aa1ab", "#6b7380")

CSS = """
:root {
  --bg: #f6f7f9; --panel: #ffffff; --ink: #14181f; --ink-2: #4a5260; --ink-3: #737b88;
  --rule: #dfe3e9; --accent: #2a78d6; --new: #0d6b3c; --new-bg: #dcf3e6; --cand: #8a5a00; --cand-bg: #fff3d6;
  --mark: #ffe08a;
  --font-body: "IBM Plex Sans KR", "Apple SD Gothic Neo", "Malgun Gothic", system-ui, sans-serif;
  --font-data: "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace;
  color-scheme: light; __LIGHT_SERIES__
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg: #11141a; --panel: #181c24; --ink: #eef1f5; --ink-2: #b8c0cc; --ink-3: #8b94a3;
  --rule: #2a313d; --accent: #3987e5; --new: #7fd9a6; --new-bg: #173526; --cand: #f2c46b; --cand-bg: #3a2f14;
  --mark: #6b5208; color-scheme: dark; __DARK_SERIES__ } }
:root[data-theme="dark"] {
  --bg: #11141a; --panel: #181c24; --ink: #eef1f5; --ink-2: #b8c0cc; --ink-3: #8b94a3;
  --rule: #2a313d; --accent: #3987e5; --new: #7fd9a6; --new-bg: #173526; --cand: #f2c46b; --cand-bg: #3a2f14;
  --mark: #6b5208; color-scheme: dark; __DARK_SERIES__ }
body { background: var(--bg); color: var(--ink); font-family: var(--font-body); font-size: 15px; line-height: 1.55; margin: 0; }
.wrap { max-width: 1160px; margin: 0 auto; padding-block: 28px 56px;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px));
  display: grid; gap: 36px; }
h1, h2, h3 { text-wrap: balance; margin: 0; line-height: 1.25; }
h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.01em; }
h2 { font-size: 19px; font-weight: 600; }
a { color: var(--accent); text-underline-offset: 2px; }
:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.eyebrow { font-family: var(--font-data); font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: var(--ink-3); }
.mono, .num { font-family: var(--font-data); font-variant-numeric: tabular-nums; }
.muted { color: var(--ink-2); }
.small { font-size: 13px; }
header { display: grid; gap: 10px; }
.topline { display: flex; justify-content: space-between; gap: 12px; align-items: baseline; flex-wrap: wrap; }
.updated { margin: 0; font-size: 13px; color: var(--ink-2); }
.updated b { font-family: var(--font-data); font-weight: 500; color: var(--ink); white-space: nowrap; }
.theme { font: inherit; font-size: 13px; padding: 3px 10px; border: 1px solid var(--rule); border-radius: 999px;
  background: var(--panel); color: var(--ink-2); cursor: pointer; }
.facts { display: flex; flex-wrap: wrap; gap: 8px 28px; margin: 4px 0 0; }
.facts div { display: grid; gap: 2px; }
.facts dt { font-size: 12px; color: var(--ink-3); }
.facts dd { margin: 0; font-family: var(--font-data); font-size: 18px; font-variant-numeric: tabular-nums; }
.lede { margin: 0; max-width: 72ch; color: var(--ink-2); font-size: 14px; }
.notice { border-left: 3px solid var(--cand); background: var(--cand-bg); padding: 10px 14px; border-radius: 6px; margin: 6px 0 0; font-size: 13px; }
section { display: grid; gap: 14px; min-width: 0; }
.sticky { position: sticky; top: 0; z-index: 5; display: grid; gap: 6px; background: var(--bg); padding: 6px 0 4px; margin: -6px 0 -4px; }
.tabs { display: flex; gap: 4px; overflow-x: auto; border-bottom: 1px solid var(--rule); scrollbar-width: thin; }
.tabs button { font: inherit; font-size: 14px; padding: 8px 14px; border: 0; border-bottom: 2px solid transparent; background: none;
  color: var(--ink-2); cursor: pointer; white-space: nowrap; }
.tabs button[aria-selected="true"] { color: var(--ink); font-weight: 600; border-bottom-color: var(--accent); }
.tabs button:hover { color: var(--ink); }
.tabs .count { font-family: var(--font-data); font-size: 12px; color: var(--ink-3); font-weight: 400; }
.tab-panel { display: grid; gap: 28px; min-width: 0; }
.tab-panel[hidden] { display: none; }
.title-row { display: flex; flex-wrap: wrap; gap: 8px 32px; align-items: baseline; justify-content: space-between; }
.lede-row { display: flex; flex-wrap: wrap; gap: 4px 12px; align-items: baseline; }
.section-head { display: flex; flex-wrap: wrap; gap: 4px 12px; align-items: baseline; }
details.help { font-size: 13px; color: var(--ink-2); max-width: 80ch; }
details.help > summary { cursor: pointer; color: var(--accent); font-size: 12px; list-style: none; display: inline; }
details.help > summary::before { content: "ⓘ "; }
details.help[open] { flex-basis: 100%; }
details.help > div { margin-top: 6px; padding: 8px 12px; border-left: 3px solid var(--accent-soft, var(--rule)); background: var(--panel); border-radius: 4px; }
.brief { font-size: 13px; color: var(--ink-2); background: var(--panel); border: 1px solid var(--rule); border-radius: 8px; padding: 8px 12px;
  display: flex; flex-wrap: wrap; gap: 6px; align-items: center; }
.batches { display: grid; gap: 8px; }
details.batch { background: var(--panel); border: 1px solid var(--rule); border-radius: 8px; }
details.batch > summary { cursor: pointer; padding: 10px 14px; font-size: 13px; }
details.batch[open] > summary { border-bottom: 1px solid var(--rule); }
.batch-body { padding: 10px 14px; display: grid; gap: 8px; }
details.more-filters > summary { cursor: pointer; font-size: 13px; color: var(--accent); }
details.more-filters[open] { display: grid; gap: 10px; }
.warns { display: flex; flex-wrap: wrap; gap: 6px; }
.chip.warn-chip { color: var(--cand); background: var(--cand-bg); border-color: transparent; cursor: help; }
.filterbar { background: var(--panel); border: 1px solid var(--rule); border-radius: 8px;
  padding: 10px 14px; display: flex; flex-wrap: wrap; gap: 8px 22px; align-items: center; font-size: 13px; color: var(--ink-2); }
.filterbar fieldset { display: flex; flex-wrap: wrap; gap: 6px 14px; align-items: center; border: 0; padding: 0; margin: 0; }
.filterbar legend { float: left; padding: 0; margin-right: 2px; font-weight: 600; color: var(--ink); }
.filterbar label { display: inline-flex; gap: 6px; align-items: center; }
.filterbar .sep { padding-left: 12px; border-left: 1px solid var(--rule); }
.filterbar .state { margin-left: auto; color: var(--ink-3); }
.filterbar[hidden] { display: none; }
.cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 140px), 1fr)); gap: 10px; }
.card { background: var(--panel); border: 1px solid var(--rule); border-radius: 8px; padding: 12px 14px; display: grid; gap: 4px; }
.card .name { display: flex; gap: 8px; align-items: center; font-size: 13px; color: var(--ink-2); }
.card .big { font-family: var(--font-data); font-size: 26px; font-variant-numeric: tabular-nums; line-height: 1.1; }
.card .diff { font-family: var(--font-data); font-size: 12px; color: var(--ink-3); }
.card .diff b { color: var(--ink); font-weight: 500; }
.swatch { width: 10px; height: 10px; border-radius: 3px; flex: none; display: inline-block; }
.panel { background: var(--panel); border: 1px solid var(--rule); border-radius: 8px; padding: 16px; min-width: 0; display: grid;
  grid-template-columns: minmax(0, 1fr); gap: 12px; }
.legend { display: flex; flex-wrap: wrap; gap: 6px 16px; font-size: 13px; color: var(--ink-2); }
.legend span { display: inline-flex; gap: 6px; align-items: center; }
svg.chart { width: 100%; height: auto; display: block; overflow: visible; }
svg.chart text { fill: var(--ink-3); font-family: var(--font-data); font-size: 11px; }
svg.chart text.val { fill: var(--ink); }
svg.chart text.latest { fill: var(--ink); font-weight: 600; }
svg.chart .grid { stroke: var(--rule); stroke-width: 1; }
svg.chart .seg { stroke: var(--panel); stroke-width: 2; cursor: pointer; }
svg.chart .seg:hover, svg.chart .seg:focus-visible { opacity: .8; outline: none; }
.table-scroll { overflow-x: auto; border: 1px solid var(--rule); border-radius: 8px; background: var(--panel); }
table { border-collapse: collapse; width: 100%; font-size: 14px; }
th, td { text-align: left; padding: 8px 12px; border-bottom: 1px solid var(--rule); vertical-align: top; }
th { font-size: 12px; font-weight: 600; color: var(--ink-3); white-space: nowrap; }
th.latest { color: var(--ink); }
tr:last-child td { border-bottom: 0; }
td.num, th.num { text-align: right; white-space: nowrap; }
tr.total td { font-weight: 600; background: var(--bg); }
tr.group td { background: var(--bg); font-size: 12px; font-weight: 600; color: var(--ink-3); }
td .sub { display: block; font-size: 12px; color: var(--ink-3); }
td.label { min-width: 26ch; }
td.latest-col { background: color-mix(in srgb, var(--accent) 7%, transparent); }
button.cell { font: inherit; font-family: var(--font-data); font-variant-numeric: tabular-nums; color: var(--accent);
  background: none; border: 0; border-radius: 4px; padding: 1px 6px; margin: -1px -6px; cursor: pointer;
  text-decoration: underline dotted; text-underline-offset: 3px; }
button.cell:hover { background: var(--bg); }
button.cell:disabled { color: var(--ink-3); text-decoration: none; cursor: default; background: none; }
.search { display: grid; gap: 10px; }
.search input[type=search], #fg-q { width: 100%; box-sizing: border-box; font: inherit; font-size: 16px; padding: 10px 12px;
  border: 1px solid var(--rule); border-radius: 6px; background: var(--bg); color: var(--ink); }
.filters { display: flex; flex-wrap: wrap; gap: 8px 16px; align-items: center; font-size: 13px; color: var(--ink-2); }
.filters label { display: inline-flex; gap: 6px; align-items: center; max-width: 100%; min-width: 0; }
.filters select { font: inherit; font-size: 13px; padding: 4px 6px; border: 1px solid var(--rule); border-radius: 6px;
  background: var(--bg); color: var(--ink); max-width: 100%; min-width: 0; flex: 0 1 auto; }
#list { scroll-margin-top: 140px; }
.presets { display: flex; flex-wrap: wrap; gap: 6px; align-items: center; font-size: 13px; color: var(--ink-3); }
.presets button, .more, .reset { font: inherit; font-size: 13px; padding: 3px 10px; border: 1px solid var(--rule); border-radius: 999px;
  background: var(--bg); color: var(--accent); cursor: pointer; }
.summary-line { font-size: 13px; color: var(--ink-2); }
.summary-line .num { color: var(--ink); }
.results { display: grid; gap: 12px; min-width: 0; }
.result { border-top: 1px solid var(--rule); padding-top: 12px; display: grid; gap: 6px; min-width: 0; }
.result.is-new { border-left: 3px solid var(--new); padding-left: 10px; }
.result-head { display: flex; flex-wrap: wrap; gap: 4px 10px; align-items: center; font-size: 13px; }
.chip { display: inline-flex; gap: 5px; align-items: center; font-size: 12px; font-weight: 600; padding: 1px 8px; border-radius: 999px;
  white-space: nowrap; border: 1px solid var(--rule); color: var(--ink-2); }
.chip.new { color: var(--new); background: var(--new-bg); border-color: transparent; }
.chip.cand { color: var(--cand); background: var(--cand-bg); border-color: transparent; }
.label-orig { font-size: 11px; letter-spacing: .06em; color: var(--ink-3); font-family: var(--font-data); }
.orig { margin: 0; padding: 10px 12px; border: 1px solid var(--rule); border-radius: 6px; background: var(--bg);
  font-size: 13px; overflow-wrap: anywhere; max-height: 15em; overflow-y: auto; display: grid; gap: 6px; min-width: 0; }
.orig-text { white-space: pre-line; }
.orig-table { overflow-x: auto; }
.orig-table table { font-size: 12px; width: auto; min-width: 100%; background: var(--panel); }
.orig-table td { border: 1px solid var(--rule); padding: 4px 6px; min-width: 6ch; max-width: 60ch; white-space: pre-line; }
.meta { font-size: 12px; color: var(--ink-2); }
.meta b { font-weight: 600; color: var(--ink-3); }
.warn { font-size: 12px; color: var(--cand); background: var(--cand-bg); border-radius: 6px; padding: 4px 8px; }
.chip.stage { border-style: dashed; }
.ffs-item { border-top: 1px solid var(--rule); padding: 10px 0; display: grid; gap: 6px; }
.ffs-line { font-size: 13px; padding: 6px 10px; border-left: 3px solid var(--accent); background: var(--bg); border-radius: 4px; overflow-wrap: anywhere; }
.ffs-follow { font-size: 12px; color: var(--ink-2); display: flex; flex-wrap: wrap; gap: 6px; align-items: center; }
.link-btn { font: inherit; font-size: 12px; padding: 0 8px; border: 1px solid var(--rule); border-radius: 999px; background: var(--panel);
  color: var(--accent); cursor: pointer; }
td.fg-row { font-size: 12px; color: var(--ink-2); max-width: 70ch; }
td.fg-row summary { cursor: pointer; color: var(--accent); }
.src { font-size: 12px; color: var(--ink-3); overflow-wrap: anywhere; }
.kw { font-size: 12px; color: var(--cand); }
.related-tags { font-size: 12px; color: var(--ink-3); }
.chip.changed { color: var(--cand); background: var(--cand-bg); border-color: var(--cand); }
.hidden-btn { font: inherit; font-size: 12px; padding: 0 8px; border: 1px solid var(--cand); border-radius: 999px;
  background: var(--cand-bg); color: var(--cand); cursor: pointer; }
.notice.alert { border-left-color: #d23c3c; }
.notice ul { margin: 6px 0 0; padding-left: 18px; }
.changes td.line { min-width: 30ch; }
td.related, th.related { border-left: 1px solid var(--rule); }
mark { background: var(--mark); color: inherit; border-radius: 2px; padding: 0 1px; }
.empty { color: var(--ink-3); font-size: 13px; padding: 20px 0; text-align: center; border: 1px dashed var(--rule); border-radius: 6px; }
footer { font-size: 13px; color: var(--ink-3); border-top: 1px solid var(--rule); padding-top: 16px; }
#tip { position: fixed; pointer-events: none; z-index: 20; background: var(--ink); color: var(--bg);
  font-family: var(--font-data); font-size: 12px; padding: 6px 8px; border-radius: 4px; white-space: pre; }
@media (max-width: 640px) { h1 { font-size: 23px; } .sticky { position: static; } .filterbar .state { margin-left: 0; } #list { scroll-margin-top: 8px; } }
"""

SCRIPT = r"""
(() => {
  const D = JSON.parse(document.getElementById('csi-data').textContent);
  const $ = id => document.getElementById(id);
  const el = (tag, cls, text) => { const n = document.createElement(tag); if (cls) n.className = cls; if (text != null) n.textContent = text; return n; };
  const link = (url, label) => { if (!/^https:\/\//.test(url || '')) return el('span', null, label);
    const a = el('a', null, label); a.href = url; a.target = '_blank'; a.rel = 'noopener'; return a; };
  const short = m => m.replace('RAN1#', '#');
  const TOPIC = Object.fromEntries(D.topics.map((t, i) => [t.id, { ...t, i }]));
  const SHORT = { 'Agreement': 'Agreement', 'Working Assumption': 'WA', 'Conclusion': 'Conclusion' };
  const latest = D.meetings[D.meetings.length - 1], prev = D.meetings[D.meetings.length - 2];
  const swatch = id => { const s = el('span', 'swatch'); s.style.background = `var(--t-${id})`; return s; };

  // ── 테마 (자동 → 라이트 → 다크). 저장은 이 브라우저에만, 실패해도 동작합니다.
  const root = document.documentElement, themeBtn = $('theme');
  const THEMES = ['auto', 'light', 'dark'], THEME_LABEL = { auto: '테마: 자동', light: '테마: 라이트', dark: '테마: 다크' };
  const setTheme = t => { if (t === 'auto') root.removeAttribute('data-theme'); else root.dataset.theme = t;
    themeBtn.textContent = THEME_LABEL[t]; themeBtn.dataset.t = t; try { localStorage.setItem('csi-theme', t); } catch (e) {} };
  let saved = 'auto'; try { saved = localStorage.getItem('csi-theme') || 'auto'; } catch (e) {}
  setTheme(THEMES.includes(saved) ? saved : 'auto');
  themeBtn.addEventListener('click', () => setTheme(THEMES[(THEMES.indexOf(themeBtn.dataset.t) + 1) % 3]));

  // ── 전역 필터: 구분(종류 + FFS) · 범위(확정/후보)
  const bar = $('filters');
  function pred() {
    const types = [...bar.querySelectorAll('input[data-type]:checked')].map(i => i.value);
    const scopes = [...bar.querySelectorAll('input[data-scope]:checked')].map(i => i.value);
    const ffs = $('g-ffs').checked;
    return e => types.includes(e.type) && scopes.includes(e.scope === 'candidate' ? 'candidate' : 'confirmed') && (!ffs || e.ffs > 0);
  }
  function stateText() {
    const types = [...bar.querySelectorAll('input[data-type]:checked')].map(i => SHORT[i.value]);
    const scopes = [...bar.querySelectorAll('input[data-scope]:checked')].map(i => i.value === 'candidate' ? '후보' : '확정');
    return `${scopes.join('+') || '범위 없음'} · ${types.join('·') || '구분 없음'}${$('g-ffs').checked ? ' · FFS 있는 것만' : ''}`;
  }
  const countBy = (list, key) => { const o = {}; list.forEach(e => { const k = key(e); o[k] = (o[k] || 0) + 1; }); return o; };
  // 지금 체크 때문에 보이지 않는 결정 수 (구분별, 후보). 놓치지 않도록 상태 줄에 항상 보여주고, 누르면 그 체크를 켭니다.
  function hiddenCounts() {
    const types = [...bar.querySelectorAll('input[data-type]:checked')].map(i => i.value);
    const confOn = bar.querySelector('input[value="confirmed"]').checked, candBox = $('g-cand');
    const ffsOk = e => !$('g-ffs').checked || e.ffs > 0;
    const scopeOk = e => e.scope === 'candidate' ? candBox.checked : confOn;
    const out = [];
    bar.querySelectorAll('input[data-type]:not(:checked)').forEach(box => {
      const n = D.entries.filter(e => e.type === box.value && scopeOk(e) && ffsOk(e)).length;
      if (n) out.push([SHORT[box.value], n, box]);
    });
    if (!candBox.checked) {
      const n = D.entries.filter(e => e.scope === 'candidate' && types.includes(e.type) && ffsOk(e)).length;
      if (n) out.push(['후보', n, candBox]);
    }
    return out;
  }
  function renderState(base) {
    const st = $('state');
    st.replaceChildren(`표시 중: ${stateText()} · ${base.length.toLocaleString()}건`);
    const hidden = hiddenCounts();
    if (!hidden.length) return;
    st.append(' · 숨김: ');
    hidden.forEach(([label, n, box], i) => {
      const b = el('button', 'hidden-btn', `${label} ${n}`); b.type = 'button'; b.title = '체크를 켜서 함께 보기';
      b.addEventListener('click', () => { box.checked = true; update(); });
      if (i) st.append(' · ');
      st.append(b);
    });
  }

  // ── 직전 회의 대비 카드
  function cards(list) {
    const box = $('delta'); box.replaceChildren();
    const now = countBy(list.filter(e => e.meeting === latest), e => e.topic);
    const before = prev ? countBy(list.filter(e => e.meeting === prev), e => e.topic) : {};
    const all = [{ id: '__all', label: '전체' }, ...D.topics];
    all.forEach(t => {
      const n = t.id === '__all' ? Object.values(now).reduce((a, b) => a + b, 0) : (now[t.id] || 0);
      const p = t.id === '__all' ? Object.values(before).reduce((a, b) => a + b, 0) : (before[t.id] || 0);
      const c = el('button', 'card'); c.type = 'button'; c.style.font = 'inherit'; c.style.textAlign = 'left'; c.style.cursor = 'pointer';
      c.style.color = 'inherit';
      const name = el('span', 'name'); if (t.id !== '__all') name.append(swatch(t.id)); name.append(t.label);
      const d = el('span', 'diff'); const diff = n - p;
      d.append(prev ? `${short(prev)} ${p} → ` : '', el('b', null, `${diff >= 0 ? '+' : ''}${diff}`));
      c.append(name, el('span', 'big', String(n)), d);
      c.title = `${latest} 신규 결정 보기`;
      c.addEventListener('click', () => focusList({ topic: t.id === '__all' ? '' : 'p:' + t.id, meeting: latest }));
      box.append(c);
    });
  }

  // ── 회의별 주제 누적 막대
  const tip = $('tip');
  const showTip = (text, x, y) => { tip.textContent = text; tip.hidden = false;
    const w = tip.offsetWidth, h = tip.offsetHeight;
    tip.style.left = Math.max(8, Math.min(x + 12, innerWidth - w - 8)) + 'px'; tip.style.top = Math.max(8, y - h - 12) + 'px'; };
  function chart(list) {
    const NS = 'http://www.w3.org/2000/svg', svg = $('chart'); svg.replaceChildren();
    const per = D.meetings.map(m => countBy(list.filter(e => e.meeting === m), e => e.topic));
    const totals = per.map(o => Object.values(o).reduce((a, b) => a + b, 0));
    const top = Math.max(1, ...totals), step = top > 100 ? 50 : top > 40 ? 20 : top > 15 ? 10 : 5;
    const ymax = Math.ceil(top / step) * step;
    const W = Math.max(320, Math.round(svg.clientWidth || 720)), H = W < 500 ? 220 : 260, L = 34, B = 24, T = 18, slot = (W - L) / D.meetings.length, bw = Math.min(46, slot * 0.58);
    svg.setAttribute('viewBox', `0 0 ${W} ${H}`);
    const mk = (tag, attrs, text) => { const n = document.createElementNS(NS, tag);
      Object.entries(attrs).forEach(([k, v]) => n.setAttribute(k, v)); if (text != null) n.textContent = text; svg.append(n); return n; };
    for (let v = 0; v <= ymax; v += step) {
      const y = H - B - (H - B - T) * v / ymax;
      mk('line', { class: 'grid', x1: L, x2: W, y1: y, y2: y });
      mk('text', { x: L - 6, y: y + 4, 'text-anchor': 'end' }, v);
    }
    D.meetings.forEach((m, i) => {
      const x = L + slot * i + (slot - bw) / 2; let y = H - B;
      const order = D.topics.filter(t => per[i][t.id]);
      order.forEach((t, k) => {
        const n = per[i][t.id], h = (H - B - T) * n / ymax, isTop = k === order.length - 1, r = isTop ? Math.min(4, h / 2) : 0;
        const y0 = y - h;
        const d = r ? `M${x},${y} V${y0 + r} Q${x},${y0} ${x + r},${y0} H${x + bw - r} Q${x + bw},${y0} ${x + bw},${y0 + r} V${y} Z`
                    : `M${x},${y} V${y0} H${x + bw} V${y} Z`;
        const p = mk('path', { class: 'seg', d, fill: `var(--t-${t.id})`, tabindex: 0, role: 'button',
          'aria-label': `${m} ${t.label} ${n}건` });
        const text = `${m} · ${t.label}\n${n}건 (회의 합계 ${totals[i]}건)\n누르면 결정 목록`;
        p.addEventListener('pointermove', ev => showTip(text, ev.clientX, ev.clientY));
        p.addEventListener('pointerleave', () => { tip.hidden = true; });
        p.addEventListener('focus', () => { const b = p.getBoundingClientRect(); showTip(text, b.left, b.top); });
        p.addEventListener('blur', () => { tip.hidden = true; });
        p.addEventListener('click', () => focusList({ topic: 'p:' + t.id, meeting: m }));
        p.addEventListener('keydown', ev => { if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); focusList({ topic: 'p:' + t.id, meeting: m }); } });
        y = y0;
      });
      if (totals[i]) mk('text', { class: 'val', x: x + bw / 2, y: y - 5, 'text-anchor': 'middle' }, totals[i]);
      mk('text', { class: m === latest ? 'latest' : '', x: x + bw / 2, y: H - 6, 'text-anchor': 'middle' }, short(m));
    });
    svg.setAttribute('aria-label', `회의별 주제별 결정 수 (${stateText()}), 최대 ${top}건`);
  }

  // ── 표 (주제 × 회의, Agenda × 회의). 숫자를 누르면 아래 목록이 그 조건으로 바뀝니다.
  // r.related가 있으면 맨 끝에 '관련 포함' 열(관련 주제 태그로 센 전체 회의 합계)을 붙입니다.
  function matrix(tbody, rows, list, colTotals) {
    tbody.replaceChildren();
    const sums = Object.fromEntries(D.meetings.map(m => [m, 0]));
    const extra = rows.some(r => r.related) ? 1 : 0;
    rows.forEach(r => {
      if (r.group) { const tr = el('tr', 'group'); const td = el('td', null, r.group); td.colSpan = D.meetings.length + 2 + extra; tr.append(td); tbody.append(tr); return; }
      const mine = list.filter(r.match), per = countBy(mine, e => e.meeting);
      if (r.hideEmpty && !mine.length) return;
      const tr = el('tr'); const lab = el('td', 'label');
      if (r.topic) lab.append(swatch(r.topic), ' ');
      lab.append(r.label); if (r.sub) lab.append(el('span', 'sub', r.sub)); tr.append(lab);
      D.meetings.forEach(m => {
        const n = per[m] || 0; sums[m] += n;
        const td = el('td', 'num' + (m === latest ? ' latest-col' : '')); const b = el('button', 'cell', String(n));
        b.type = 'button'; b.disabled = !n; b.addEventListener('click', () => focusList({ ...r.focus, meeting: m }));
        td.append(b); tr.append(td);
      });
      const tot = el('td', 'num'); const b = el('button', 'cell', String(mine.length)); b.type = 'button'; b.disabled = !mine.length;
      b.addEventListener('click', () => focusList({ ...r.focus, meeting: '' })); tot.append(b); tr.append(tot);
      if (r.related) {
        const n = list.filter(r.related.match).length, td = el('td', 'num related'), rb = el('button', 'cell', String(n));
        rb.type = 'button'; rb.disabled = !n; rb.title = `${r.label}이(가) 관련 주제로 붙은 결정 (주된 주제가 다른 결정 포함)`;
        rb.addEventListener('click', () => focusList(r.related.focus)); td.append(rb); tr.append(td);
      }
      tbody.append(tr);
    });
    if (colTotals) {
      const tr = el('tr', 'total'); tr.append(el('td', null, '합계'));
      D.meetings.forEach(m => tr.append(el('td', 'num' + (m === latest ? ' latest-col' : ''), String(sums[m]))));
      tr.append(el('td', 'num', String(Object.values(sums).reduce((a, b) => a + b, 0))));
      if (extra) tr.append(el('td', 'num related', '—'));
      tbody.append(tr);
    }
  }
  const topicRows = D.topics.map(t => ({ label: t.label, topic: t.id, match: e => e.topic === t.id, focus: { topic: 'p:' + t.id },
    related: { match: e => e.tags.includes(t.id), focus: { topic: 't:' + t.id } } }));
  function agendaRows() {
    const rows = []; let sec = null;
    D.agendas.forEach(a => {
      if (a.section !== sec) { sec = a.section; rows.push({ group: sec }); }
      rows.push({ label: a.label, sub: a.number_note, match: e => e.rule === a.index, focus: { agenda: 'r' + a.index } });
    });
    if (D.entries.some(e => e.scope === 'manual'))
      rows.push({ group: '수동 포함' }, { label: 'include_ids', match: e => e.scope === 'manual', focus: { agenda: 'manual' } });
    if ($('g-cand').checked) {
      rows.push({ group: '후보 (포함 Agenda 밖 · 키워드 일치 · 확인 필요)' });
      D.cand_agendas.forEach(c => rows.push({ label: c.title, sub: `${c.section} · ${c.numbers}`, hideEmpty: true,
        match: e => e.scope === 'candidate' && e.cand_key === c.key, focus: { agenda: 'c' + c.key } }));
    }
    return rows;
  }

  // ── 결정 목록 (검색 + 주제 + 회의 + Agenda)
  const q = $('q'), fTopic = $('f-topic'), fMeeting = $('f-meeting'), fAgenda = $('f-agenda'), fWord = $('f-word');
  const out = $('results'), summary = $('summary'), PAGE = 20;
  const opt = (sel, value, label) => { const o = el('option', null, label); o.value = value; sel.append(o); };
  const gPrimary = el('optgroup'), gTag = el('optgroup');
  gPrimary.label = '주된 주제'; gTag.label = '관련 주제 포함';
  D.topics.forEach(t => { opt(gPrimary, 'p:' + t.id, t.label); opt(gTag, 't:' + t.id, `${t.label} (관련 포함)`); });
  fTopic.append(gPrimary, gTag);
  [...D.meetings].reverse().forEach(m => opt(fMeeting, m, m + (m === latest ? ' (최신)' : '')));
  D.agendas.forEach(a => opt(fAgenda, 'r' + a.index, a.label));
  opt(fAgenda, 'manual', '수동 포함 (include_ids)');
  opt(fAgenda, 'cand', '[후보 전체]');
  D.cand_agendas.forEach(c => opt(fAgenda, 'c' + c.key, `[후보] ${c.title}`));
  const fStage = $('f-stage'), fImpact = $('f-impact'), fClause = $('f-clause'), fWarn = $('f-warn');
  D.stages.forEach(s => opt(fStage, s.id, s.label));
  D.impacts.forEach(t => opt(fImpact, t.id, t.label));
  // 규격 조항: 사양 + 조항 앞 두 단계로 묶음 (예: TS 38.214 5.2). 많이 나온 순이 아니라 사양·조항 번호 순.
  (() => {
    const groups = {};
    D.entries.forEach(e => new Set(e.clauses.map(c => { const [ts, spec, num] = c.split(' '); return `${ts} ${spec} ${num.split('.').slice(0, 2).join('.')}`; }))
      .forEach(g => { groups[g] = (groups[g] || 0) + 1; }));
    const key = g => g.split(/[ .]/).slice(1).map(x => x.padStart(4, '0')).join('.');
    Object.keys(groups).sort((a, b) => key(a) < key(b) ? -1 : 1).forEach(g => opt(fClause, g, `${g} (${groups[g]})`));
  })();
  const extraOk = e => (!fStage.value || e.stage === fStage.value) && (!fImpact.value || e.impact.includes(fImpact.value))
    && (!fClause.value || e.clauses.some(c => c === fClause.value || c.startsWith(fClause.value + '.')))
    && (!fWarn.checked || e.warn.length > 0);
  const esc = t => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const pattern = (t, word) => word ? `(?<![A-Za-z0-9])${esc(t)}(?![A-Za-z0-9])` : esc(t);
  function highlight(node, text, re) {
    if (!re) { node.append(text); return; }
    let last = 0;
    for (const m of text.matchAll(re)) { if (!m[0]) continue; node.append(text.slice(last, m.index), el('mark', null, m[0])); last = m.index + m[0].length; }
    node.append(text.slice(last));
  }
  // 원문의 R1- 번호는 3GPP FTP 링크로 (회의 폴더는 원본 근거 TDoc 번호 범위로 추정, 드물게 403이면 근거 TDoc·Chair notes 링크 사용)
  function inline(node, text, re, tdocs) {
    let last = 0;
    for (const m of text.matchAll(/\bR1-\d{7}\b/g)) {
      if (!tdocs[m[0]]) continue;
      highlight(node, text.slice(last, m.index), re);
      const a = link(tdocs[m[0]], m[0]); a.title = 'TDoc 열기 (3GPP FTP)'; node.append(a);
      last = m.index + m[0].length;
    }
    highlight(node, text.slice(last), re);
  }
  // '|'로 시작하는 줄은 표 한 행으로 그립니다 (FG 표, TP 표 등). 원문 글자는 바꾸지 않습니다.
  function richText(e, re) {
    const box = el('div', 'orig'); let buf = [], rows = [];
    const flushText = () => { if (buf.length) { const d = el('div', 'orig-text'); inline(d, buf.join('\n'), re, e.tdocs); box.append(d); buf = []; } };
    const flushTable = () => {
      if (!rows.length) return;
      const wrap = el('div', 'orig-table'), t = el('table');
      rows.forEach(r => { const tr = el('tr'); r.forEach(c => { const td = el('td'); inline(td, c, re, e.tdocs); tr.append(td); }); t.append(tr); });
      wrap.append(t); box.append(wrap); rows = [];
    };
    e.text.split('\n').forEach(l => {
      const s = l.trim();
      if (s.length > 1 && s[0] === '|') { flushText(); rows.push(s.replace(/^\||\|$/g, '').split('|').map(c => c.trim())); }
      else { flushTable(); buf.push(l); }
    });
    flushText(); flushTable();
    return box;
  }
  const STAGE = Object.fromEntries(D.stages.map(s => [s.id, s.label]));
  const IMPACT = Object.fromEntries(D.impacts.map(t => [t.id, t.label]));
  const WARN_SHORT = { math: '수식 누락 의심', color: '색 표시 손실 — TDoc 확인', tdoc: '변경은 TDoc에' };
  const WARN = {
    math: '수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. 숫자·기호는 Chair notes 원문으로 확인하세요.',
    color: '색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없어 무엇이 바뀌었는지 알 수 없습니다. TDoc에서 확인하세요.',
    tdoc: '실제 변경 내용은 TDoc에 있습니다 — 본문·출처의 TDoc 링크를 여세요.',
  };
  function render(e, re) {
    const box = el('article', 'result' + (e.meeting === latest ? ' is-new' : ''));
    const head = el('div', 'result-head');
    head.append(el('span', 'mono', e.meeting));
    if (e.meeting === latest) head.append(el('span', 'chip new', '신규'));
    if (D.provisional.includes(e.meeting)) head.append(el('span', 'chip cand', '잠정'));
    if (RECENT[e.id]) { const c = el('span', 'chip changed', RECENT[e.id]); c.title = `${D.recent.at.slice(0, 10)} 실행에서 과거 회의 결정이 바뀜`; head.append(c); }
    const tc = el('span', 'chip'); tc.append(swatch(e.topic), TOPIC[e.topic].label); tc.title = '주된 주제'; head.append(tc);
    const rel = e.tags.filter(t => t !== e.topic);
    if (rel.length) head.append(el('span', 'related-tags', '관련: ' + rel.map(t => TOPIC[t].label).join(' · ')));
    head.append(el('span', 'chip', SHORT[e.type]));
    const sc = el('span', 'chip stage', STAGE[e.stage]); sc.title = '진행 단계'; head.append(sc);
    if (e.scope === 'candidate') head.append(el('span', 'chip cand', '후보'));
    if (e.scope === 'manual') head.append(el('span', 'chip', '수동 포함'));
    head.append(el('span', 'mono', e.item), el('span', 'muted', e.title));
    box.append(head);
    if (e.scope === 'candidate') box.append(el('div', 'kw', '일치: ' + e.kw.join(', ')));
    if (e.impact.length || e.clauses.length) {
      const meta = el('div', 'meta');
      if (e.impact.length) meta.append(el('b', null, '구현 영향 '), e.impact.map(i => IMPACT[i]).join(' · '));
      if (e.clauses.length) {
        if (e.impact.length) meta.append('  ');
        meta.append(el('b', null, '규격 '), e.clauses.slice(0, 5).join(', ') + (e.clauses.length > 5 ? ` 외 ${e.clauses.length - 5}` : ''));
      }
      box.append(meta);
    }
    if (e.warn.length) {  // 짧은 표시만, 설명은 마우스를 올리면 (탭·포커스로도)
      const w = el('div', 'warns');
      e.warn.forEach(k => { const c = el('span', 'chip warn-chip', '⚠ ' + WARN_SHORT[k]); c.title = WARN[k]; c.tabIndex = 0; w.append(c); });
      box.append(w);
    }
    box.append(el('span', 'label-orig', 'Chair notes 원문'));
    box.append(richText(e, re));
    const src = el('div', 'src'); const s = e.source;
    src.append(link(s.url, s.doc));
    if (s.tdoc) src.append(' · ', link(s.tdoc_url, s.tdoc));
    if (s.discussion) src.append(' · ', el('span', 'mono', `[${s.discussion}]`));
    src.append(' · ', el('span', 'mono', e.id));
    if (e.ffs) src.append(` · FFS ${e.ffs}줄`);
    box.append(src);
    return box;
  }
  let hits = [], shown = 0, curRe = null, timer, idFilter = null, idLabel = '';
  // 최근 변경 이력: 변경 묶음이 30일 안이면 해당 결정에 '과거 회의 추가/변경' 표시
  const RECENT = {};
  if (D.recent && Date.now() - Date.parse(D.recent.at) < 30 * 864e5)
    Object.entries(D.recent.items).forEach(([id, w]) => { RECENT[id] = w === 'added' ? '과거 회의에 추가' : '원문·범위 변경'; });
  function showMore() {
    out.querySelector('.more')?.remove();
    hits.slice(shown, shown + PAGE).forEach(e => out.append(render(e, curRe)));
    shown = Math.min(shown + PAGE, hits.length);
    if (shown < hits.length) { const b = el('button', 'more', `더 보기 (남은 ${hits.length - shown}건)`); b.type = 'button'; b.addEventListener('click', showMore); out.append(b); }
  }
  // 'p:srs'는 주된 주제가 SRS인 결정, 't:srs'는 SRS가 관련 주제로 붙은 결정(주된 주제가 다른 결정 포함)
  function topicOk(e) {
    const v = fTopic.value; if (!v) return true;
    return v[0] === 'p' ? e.topic === v.slice(2) : e.tags.includes(v.slice(2));
  }
  function agendaOk(e) {
    const v = fAgenda.value; if (!v) return true;
    if (v === 'manual') return e.scope === 'manual';
    if (v === 'cand') return e.scope === 'candidate';
    if (v[0] === 'r') return e.rule === +v.slice(1);
    return e.scope === 'candidate' && e.cand_key === v.slice(1);
  }
  function list(base) {
    const nExtra = [fStage.value, fImpact.value, fClause.value, fWarn.checked].filter(Boolean).length;
    $('more-state').textContent = nExtra ? `· ${nExtra}개 적용 중` : '';
    if (idFilter) {  // '최근 변경' 버튼: 구분·범위 체크와 다른 조건을 무시하고 그 결정만 보여줌
      hits = D.entries.filter(e => idFilter.has(e.id)).reverse(); curRe = null; out.replaceChildren(); shown = 0;
      summary.replaceChildren(el('span', 'num', `${hits.length}건`), ` · ${idLabel} (구분·범위 체크와 관계없이 모두 표시 · '조건 지우기'로 해제)`);
      showMore(); return;
    }
    const groups = q.value.trim().split(/\s+OR\s+|\s*\|\s*/).map(g => g.split(/\s+/).filter(Boolean)).filter(g => g.length);
    const terms = groups.flat();
    const groupRes = groups.map(g => g.map(t => new RegExp(pattern(t, fWord.checked), 'i')));
    curRe = terms.length ? new RegExp(terms.map(t => pattern(t, fWord.checked)).join('|'), 'gi') : null;
    hits = base.filter(e => topicOk(e) && (!fMeeting.value || e.meeting === fMeeting.value) && agendaOk(e) && extraOk(e) &&
      (!groupRes.length || groupRes.some(g => g.every(r => r.test(e.text) || r.test(e.title))))).reverse();
    out.replaceChildren(); shown = 0;
    const per = countBy(hits, e => e.meeting);
    summary.replaceChildren(el('span', 'num', `${hits.length.toLocaleString()}건`),
      hits.length ? ' · 회의별 ' + D.meetings.filter(m => per[m]).map(m => `${short(m)} ${per[m]}`).join(' · ') + ` · 최신 회의부터 · ${stateText()}`
                  : ` · 조건에 맞는 결정이 없습니다 (${stateText()}). 위 체크박스나 검색어를 확인하세요.`);
    showMore();
  }
  // 카드·차트·표의 숫자를 누르면 이전 검색어와 조건을 모두 지우고 누른 조건만 적용합니다 (남아 있으면 0건처럼 보임).
  function focusList(f) {
    q.value = ''; fTopic.value = f.topic || ''; fMeeting.value = f.meeting || ''; fAgenda.value = f.agenda || '';
    fStage.value = fImpact.value = fClause.value = ''; fWarn.checked = false;
    idFilter = f.ids ? new Set(f.ids) : null; idLabel = f.label || '';
    if (fAgenda.value[0] === 'c' && !$('g-cand').checked) { $('g-cand').checked = true; }
    update(); showTab('list'); $('list').scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
  function update() {
    const ok = pred(), base = D.entries.filter(ok);
    renderState(base);
    cards(base); chart(base);
    matrix($('topic-body'), topicRows, base, true);
    matrix($('agenda-body'), agendaRows(), base, false);
    list(base);
  }
  // ── 탭: 요약 · 결정 목록 · Agenda별 · FFS 추적 · FG 목록 · 변경 이력. 주소의 #탭이름으로 바로 열 수 있습니다(예: …/#ffs).
  const TABS = [...document.querySelectorAll('[data-tab]')].map(b => b.dataset.tab);
  const FILTERED = ['summary', 'list', 'agenda'];  // 위 필터 줄(구분·범위)이 적용되는 탭
  function showTab(t, record = true) {
    if (!TABS.includes(t)) t = 'summary';
    document.querySelectorAll('[data-tab]').forEach(b => b.setAttribute('aria-selected', String(b.dataset.tab === t)));
    document.querySelectorAll('.tab-panel').forEach(p => { p.hidden = p.dataset.panel !== t; });
    bar.hidden = !FILTERED.includes(t);
    if (t === 'summary') chart(D.entries.filter(pred()));  // 숨겨져 있던 동안 폭을 몰라 다시 그림
    if (record && location.hash !== '#' + t) history.replaceState(null, '', '#' + t);
  }
  const header = document.querySelector('main > header');
  document.querySelectorAll('[data-tab]').forEach(b => b.addEventListener('click', () => {
    showTab(b.dataset.tab);
    const top = header.offsetTop + header.offsetHeight;  // 아래로 내려가 있었으면 탭 바로 아래부터 보이게
    if (scrollY > top) scrollTo({ top });
  }));
  document.querySelectorAll('[data-goto]').forEach(b => b.addEventListener('click', () => { showTab(b.dataset.goto); scrollTo({ top: header.offsetTop + header.offsetHeight }); }));
  addEventListener('hashchange', () => showTab(location.hash.slice(1), false));
  bar.addEventListener('change', update);
  let rw; addEventListener('resize', () => { clearTimeout(rw); rw = setTimeout(() => chart(D.entries.filter(pred())), 200); });
  q.addEventListener('input', () => { idFilter = null; clearTimeout(timer); timer = setTimeout(() => list(D.entries.filter(pred())), 150); });
  [fTopic, fMeeting, fAgenda, fWord, fStage, fImpact, fClause, fWarn].forEach(n => n.addEventListener('change', () => { idFilter = null; list(D.entries.filter(pred())); }));
  $('reset').addEventListener('click', () => {
    idFilter = null; q.value = ''; fTopic.value = fMeeting.value = fAgenda.value = fStage.value = fImpact.value = fClause.value = ''; fWarn.checked = false;
    list(D.entries.filter(pred())); });
  const BYID = Object.fromEntries(D.entries.map(e => [e.id, e]));
  const idButton = (label, ids, title) => { const b = el('button', 'link-btn', label); b.type = 'button';
    b.addEventListener('click', () => focusList({ ids, label: title })); return b; };
  // ── FFS 추적: 확정 결정의 FFS 줄마다, 같은 Agenda의 이후 회의 결정 중 단어가 많이 겹치는 '후속 결정 후보'
  (() => {
    const fT = $('ffs-topic'), fM = $('ffs-meeting'), fOpen = $('ffs-open'), outF = $('ffs-list'), sumF = $('ffs-summary');
    D.topics.forEach(t => opt(fT, t.id, t.label));
    [...D.meetings].reverse().forEach(m => opt(fM, m, m));
    let rows = [], shownF = 0;
    function item(f) {
      const e = BYID[f.id], box = el('div', 'ffs-item'), head = el('div', 'result-head');
      head.append(el('span', 'mono', f.meeting));
      if (f.meeting === latest) head.append(el('span', 'chip new', '신규 FFS'));
      const tc = el('span', 'chip'); tc.append(swatch(e.topic), TOPIC[e.topic].label); head.append(tc);
      head.append(el('span', 'mono', e.item), el('span', 'muted', e.title), idButton('원 결정 보기', [f.id], `${f.meeting} FFS의 원 결정`));
      const line = el('div', 'ffs-line'); line.textContent = f.line;
      const fol = el('div', 'ffs-follow');
      if (f.followups.length) {
        fol.append('후속 결정 후보 (단어 겹침, 해소 판정 아님):');
        f.followups.forEach(id => fol.append(idButton(BYID[id].meeting, [id], `${f.meeting} FFS "${f.line.slice(0, 40)}…"의 후속 결정 후보`)));
      } else if (f.meeting === latest) fol.append('최신 회의의 FFS — 다음 회의 결과를 기다리는 중입니다.');
      else fol.append('후속 결정 후보 없음 — 이후 회의에서 같은 Agenda에 겹치는 결정이 아직 없습니다. 미결이거나 다른 표현으로 다뤄졌을 수 있습니다.');
      box.append(head, line, fol);
      return box;
    }
    function more() {
      outF.querySelector('.more')?.remove();
      rows.slice(shownF, shownF + 30).forEach(f => outF.append(item(f)));
      shownF = Math.min(shownF + 30, rows.length);
      if (shownF < rows.length) { const b = el('button', 'more', `더 보기 (남은 ${rows.length - shownF}줄)`); b.type = 'button'; b.addEventListener('click', more); outF.append(b); }
    }
    function draw() {
      rows = D.ffs.filter(f => (!fT.value || BYID[f.id].topic === fT.value) && (!fM.value || f.meeting === fM.value) && (!fOpen.checked || !f.followups.length)).reverse();
      outF.replaceChildren(); shownF = 0;
      const open = rows.filter(f => !f.followups.length).length;
      sumF.replaceChildren(el('span', 'num', `${rows.length}줄`), ` · 후속 결정 후보 있음 ${rows.length - open} · 없음 ${open} · 최신 회의부터`);
      more();
    }
    [fT, fM, fOpen].forEach(n => n.addEventListener('change', draw));
    draw();
  })();
  // ── UE feature(FG) 목록
  (() => {
    const body = $('fg-body'), fq = $('fg-q');
    function draw() {
      const words = fq.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
      body.replaceChildren();
      D.fgs.filter(f => words.every(w => (f.id + ' ' + f.name).toLowerCase().includes(w))).forEach(f => {
        const tr = el('tr');
        tr.append(el('td', 'mono', f.id));
        const name = el('td'); name.append(f.name); if (f.item) name.append(el('span', 'sub', f.item)); tr.append(name);
        tr.append(el('td', 'mono small', [...new Set(f.meetings)].map(short).join(', ')));
        const det = el('td', 'fg-row'), d = el('details'), sm = el('summary', null, '표 내용');
        d.append(sm, el('div', null, f.row.slice(3).join(' | ') || '—')); det.append(d); tr.append(det);
        const b = el('td'); b.append(idButton(`결정 ${f.ids.length}건`, f.ids, `FG ${f.id} 정의·수정 결정`)); tr.append(b);
        body.append(tr);
      });
    }
    fq.addEventListener('input', draw); draw();
  })();
  document.querySelectorAll('[data-ids]').forEach(b => b.addEventListener('click', () =>
    focusList({ ids: JSON.parse(b.dataset.ids), label: b.dataset.label })));
  // 최신 회의에서 기본 화면(확정 Agreement) 밖에 있는 결정 수. 체크 상태와 관계없이 고정 표시합니다.
  (() => {
    const box = $('latest-hidden'), now = D.entries.filter(e => e.meeting === latest);
    const parts = [
      ['Working Assumption', now.filter(e => e.scope !== 'candidate' && e.type === 'Working Assumption').length,
        () => { bar.querySelector('input[value="Working Assumption"]').checked = true; focusList({ meeting: latest }); }],
      ['Conclusion', now.filter(e => e.scope !== 'candidate' && e.type === 'Conclusion').length,
        () => { bar.querySelector('input[value="Conclusion"]').checked = true; focusList({ meeting: latest }); }],
      ['후보', now.filter(e => e.scope === 'candidate').length,
        () => { bar.querySelectorAll('input[data-type]').forEach(i => { i.checked = true; }); focusList({ meeting: latest, agenda: 'cand' }); }],
    ].filter(([, n]) => n);
    if (!parts.length) { box.hidden = true; return; }
    box.append(`${latest}에서 기본 화면(확정 Agreement) 밖에 있는 결정: `);
    parts.forEach(([label, n, fn], i) => {
      const b = el('button', 'hidden-btn', `${label} ${n}건`); b.type = 'button'; b.addEventListener('click', fn);
      if (i) box.append(' · ');
      box.append(b);
    });
    box.append(' — 지원하지 않기로 한 결론(Conclusion)이나 다른 Agenda의 CSI 결정(후보)도 구현 범위에 영향을 줄 수 있습니다.');
  })();
  document.querySelectorAll('[data-preset]').forEach(b => b.addEventListener('click', () => { q.value = b.dataset.preset; list(D.entries.filter(pred())); q.focus(); }));
  update();
  showTab(location.hash.slice(1) || 'summary', false);
})();
"""


def _e(text):
    return escape(str(text), quote=True)


def _json_for_script(data):
    # 본문에 '</script>'나 '<!--'가 있어도 스크립트 태그가 끝나지 않도록 막습니다.
    return json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/").replace("<!--", "<\\!--")


def _series_css(topics, colors, other):
    vals = [f"--t-{t['id']}: {colors[i] if i < len(colors) else other};" for i, t in enumerate(topics[:-1])]
    vals.append(f"--t-{topics[-1]['id']}: {other};")
    return " ".join(vals)


def css(topics):
    return (CSS.replace("__LIGHT_SERIES__", _series_css(topics, SERIES_LIGHT, OTHER[0]))
               .replace("__DARK_SERIES__", _series_css(topics, SERIES_DARK, OTHER[1])))


def _numbers_note(a, meetings):
    runs = []
    for m in meetings:
        n = a["numbers"].get(m)
        if n and (not runs or runs[-1][1] != n):
            runs.append((m, n))
    if not runs:
        return "아직 결정 없음"
    if len(runs) == 1:
        return f"Agenda {runs[0][1]}"
    return "번호 변경 " + " → ".join(f"{short(m)}: {n}" for m, n in runs)


def data(m):
    cand_keys = {}
    entries = []
    for e in m["entries"]:
        p = e["agenda_path"]
        ck = ""
        if e["scope"] == "candidate":
            k = (p[0]["title"], p[-1]["title"])
            ck = cand_keys.setdefault(k, str(len(cand_keys)))
        entries.append({"id": e["id"], "meeting": e["meeting"], "item": e["agenda_item"], "title": e["agenda_title"],
                        "type": e["type"], "text": e["text"], "ffs": len(e.get("ffs") or []), "topic": e["topic"], "tags": e["tags"],
                        "scope": e["scope"], "rule": e["agenda_rule"], "kw": e["keywords"], "cand_key": ck,
                        "stage": e["stage"], "impact": e["impact"], "clauses": e["clauses"], "warn": e["warn"], "tdocs": e["tdocs"],
                        "source": {k: e["source"].get(k) for k in ("doc", "url", "tdoc", "tdoc_url", "discussion") if e["source"].get(k)}})
    counts = {}
    for e in entries:
        if e["cand_key"]:
            counts[e["cand_key"]] = counts.get(e["cand_key"], 0) + 1
    numbers = {}
    for e in m["entries"]:
        if e["scope"] == "candidate":
            p = e["agenda_path"]
            numbers.setdefault((p[0]["title"], p[-1]["title"]), set()).add(p[-1]["number"])
    cands = [{"key": key, "section": s, "title": t, "count": counts[key], "numbers": ", ".join(sorted(numbers[(s, t)]))}
             for (s, t), key in cand_keys.items()]
    cands.sort(key=lambda c: (-c["count"], c["section"], c["title"]))
    return {"meetings": m["meetings"], "topics": m["topics"], "provisional": m["provisional"],
            "agendas": [{"index": a["index"], "label": a["label"], "section": a["section"],
                         "number_note": _numbers_note(a, m["meetings"])} for a in m["agendas"]],
            "cand_agendas": cands, "entries": entries,
            "recent": _recent(m), "stages": m["stages"], "impacts": m["impacts"],
            "fgs": [{"id": f["id"], "item": f["item"], "name": f["name"], "ids": f["ids"], "meetings": f["meetings"], "row": f["row"]}
                    for f in m["fgs"]],
            "ffs": m["ffs"]}


def _recent(m):
    """가장 최근 변경 묶음에서 아직 남아 있는 결정(추가·변경)의 id → 종류."""
    hist = m.get("changes") or []
    if not hist:
        return None
    return {"at": hist[0]["at"], "items": {x["id"]: x["what"] for x in hist[0]["items"] if x["what"] != "removed"}}


WHAT = {"added": "추가", "changed": "변경", "removed": "삭제"}
FIELD_KO = {"meeting": "회의", "type": "구분", "text": "원문", "scope": "범위"}


def _alerts_html(m):
    a = m["alerts"]
    if not (a["dropped"] or a["new"]):
        return ""
    rows = [f'<li>포함 Agenda <b>{_e(d["label"])}</b> ({_e(d["section"])}): {_e(m["prev"])}에 {d["prev_count"]}건 → '
            f'{_e(m["latest"])}에 없음. 제목·섹션이 바뀌었으면 config/csi_scope.yaml의 agendas를 고칩니다.</li>' for d in a["dropped"]]
    rows += [f'<li>새 Agenda <b>{_e(r["number"])} {_e(r["title"])}</b> ({_e(r["section"])}{" · 새 섹션" if r["new_section"] else ""}): '
             f'확정 {r["confirmed"]} · 후보 {r["candidate"]} / 전체 {r["total"]}건. CSI Agenda면 agendas에 넣습니다.</li>' for r in a["new"]]
    return (f'<div class="notice alert"><b>Agenda 확인 필요 ({_e(m["prev"])} → {_e(m["latest"])})</b> — '
            f'결정이 범위에서 조용히 빠지지 않도록 확인하세요.<ul>{"".join(rows)}</ul></div>')


def _help(text):
    """제목 옆 '설명' 펼침. 긴 설명은 기본으로 접어 화면을 짧게 둡니다."""
    return f'<details class="help"><summary>설명</summary><div>{text}</div></details>'


def _batch_ids(m, c):
    live = {e["id"] for e in m["entries"]}
    return [x["id"] for x in c["items"] if x["what"] != "removed" and x["id"] in live]


def _change_brief(m):
    """요약 탭의 최근 변경 한 줄."""
    hist = m.get("changes") or []
    if not hist:
        return ""
    c, k = hist[0], hist[0]["counts"]
    nm = ", ".join(f'{x["meeting"]} {x["count"]}건' for x in c["new_meetings"])
    parts = ([f"새 회의 {nm}"] if nm else []) + [f"과거 회의 추가 {k['added']} · 변경 {k['changed']} · 삭제 {k['removed']}"]
    ids = _batch_ids(m, c)
    view = (f'<button type="button" class="link-btn" data-ids="{_e(json.dumps(ids))}" data-label="{_e(c["at"][:10])} 과거 회의 추가·변경 결정">'
            f'목록에서 보기 ({len(ids)})</button>') if ids else ""
    return (f'<div class="brief"><b>최근 변경</b> <span class="mono">{_e(c["at"][:10])}</span> · {_e(c["reason"])} · {" · ".join(_e(x) for x in parts)} '
            f'{view} <button type="button" class="link-btn" data-goto="changes">변경 이력 탭</button></div>')


def _changes_html(m):
    hist = m.get("changes") or []
    help_ = _help("실행마다 직전 결과와 비교한 기록입니다. 새 회의 결정은 <span class=\"chip new\">신규</span>로 보이지만, "
                  "원본이 <b>과거 회의</b>를 다시 처리해 생긴 추가·변경·삭제(파서 개선, 잠정 → 종료본 교체, 범위 설정 변경)는 여기서만 알 수 있습니다. "
                  "최근 30일 안의 변경은 결정 목록에도 '과거 회의에 추가'·'원문·범위 변경'으로 표시됩니다. 최근 10번까지 보여줍니다.")
    head = f'<div class="section-head"><h2>변경 이력</h2>{help_}</div>'
    if not hist:
        return (f'<section id="changes" class="tab-panel" data-panel="changes" hidden>{head}'
                '<p class="empty">아직 기록된 변경이 없습니다. 결과가 처음 달라진 실행부터 남습니다.</p></section>')
    batches = []
    for c in hist[:10]:
        k = c["counts"]
        nm = ", ".join(f'{x["meeting"]} {x["count"]}건' for x in c["new_meetings"]) or "새 회의 없음"
        summary = (f'<span class="mono">{_e(c["at"].replace("T", " ")[:16])} UTC</span> · {_e(c["reason"])} · {_e(nm)} · '
                   f'과거 회의 추가 {k["added"]} · 변경 {k["changed"]} · 삭제 {k["removed"]}')
        body = '<p class="small muted">과거 회의 변경 없음</p>'
        if c["items"]:
            ids = _batch_ids(m, c)
            trs = "".join(
                f'<tr><td>{WHAT[x["what"]]}{(" (" + ", ".join(FIELD_KO.get(f, f) for f in x["fields"]) + ")") if x["fields"] else ""}</td>'
                f'<td class="mono">{_e(x["meeting"])}</td><td>{_e(x["type"])}</td><td>{_e({"agenda": "확정", "manual": "확정(수동)", "candidate": "후보"}[x["scope"]])}</td>'
                f'<td>{_e(x["agenda"])}</td><td class="line">{_e(x["line"])}</td>'
                f'<td class="mono small"><a href="{_e(x["url"])}" target="_blank" rel="noopener">{_e(x["id"])}</a></td></tr>'
                for x in c["items"][:100])
            button = (f'<button type="button" class="link-btn" data-ids="{_e(json.dumps(ids))}" data-label="{_e(c["at"][:10])} 과거 회의 추가·변경 결정">'
                      f'결정 목록에서 원문 보기 ({len(ids)}건)</button>') if ids else ""
            body = (f'{button}<div class="table-scroll"><table class="changes"><thead><tr><th>변경</th><th>회의</th><th>구분</th><th>범위</th>'
                    f'<th>Agenda</th><th>원문 첫 줄</th><th>id</th></tr></thead><tbody>{trs}</tbody></table></div>')
        batches.append(f'<details class="batch"><summary>{summary}</summary><div class="batch-body">{body}</div></details>')
    return f"""<section id="changes" class="tab-panel" data-panel="changes" hidden>
  {head}
  <p class="lede">묶음을 펼치면 바뀐 결정과 원문 첫 줄이 나옵니다.</p>
  <div class="batches">{"".join(batches)}</div>
</section>"""


def _check(attr, value, label, checked):
    return f'<label><input type="checkbox" {attr} value="{_e(value)}"{" checked" if checked else ""}> {_e(label)}</label>'


def render_body(m):
    cfg, db, meetings = m["config"], m["db"], m["meetings"]
    latest, prev = m["latest"], m["prev"]
    conf = sum(1 for e in m["entries"] if e["scope"] != "candidate")
    cand = len(m["entries"]) - conf
    notices = "".join(
        f'<p class="notice"><b>{_e(p)}</b>는 회의 종료본이 아닌 <span class="mono">{_e(provisional(db, p)["doc"])}</span> 기준 '
        "<b>잠정</b> 결과입니다. 결정이 바뀌거나 빠질 수 있으며, 원본 DB가 종료본으로 바뀌면 다음 실행에서 자동으로 교체됩니다.</p>"
        for p in m["provisional"])
    if m["unknown_manual_ids"]:
        notices += ('<p class="notice">원본 DB에 없는 수동 목록 id가 있습니다: <span class="mono">'
                    + _e(", ".join(m["unknown_manual_ids"])) + "</span> (config/csi_scope.yaml 확인)</p>")
    types = "".join(_check("data-type", t, t, t == "Agreement") for t in TYPES)
    heads = "".join(f'<th class="num{" latest" if mt == latest else ""}">{_e(short(mt))}</th>' for mt in meetings)
    base = cfg.get("report_base_url", "")
    topic_links = " · ".join(f'<a href="{_e(base)}by_topic/{_e(t["id"])}.md">{_e(t["label"])}</a>' for t in m["topics"])
    presets = "".join(f'<button type="button" data-preset="{_e(p)}">{_e(p)}</button>' for p in cfg.get("search_presets") or [])
    src = cfg["source"]
    counts = {"ffs": len(m["ffs"]), "fg": len(m["fgs"]), "changes": len(m.get("changes") or [])}
    tabs = [("summary", "요약", None), ("list", "결정 목록", None), ("agenda", "Agenda별", None),
            ("ffs", "FFS 추적", counts["ffs"]), ("fg", "FG 목록", counts["fg"]), ("changes", "변경 이력", counts["changes"])]
    tab_buttons = "".join(
        f'<button type="button" role="tab" id="tab-{t}" data-tab="{t}" aria-controls="panel-{t}" aria-selected="false">{_e(label)}'
        + (f' <span class="count">{n}</span>' if n is not None else "") + "</button>" for t, label, n in tabs)
    return f"""<main class="wrap">
<header>
  <div class="topline">
    <p class="updated">원본 DB 마지막 업데이트 <b>{_e(m["updated_kst"] or "기록 없음")}</b>{CHECKED_AT}</p>
    <button type="button" class="theme" id="theme">테마: 자동</button>
  </div>
  <div class="title-row">
    <h1>{TITLE}</h1>
    <dl class="facts">
      <div><dt>최신 회의</dt><dd>{_e(latest)}{' <span class="chip cand">잠정</span>' if latest in m["provisional"] else ""}</dd></div>
      <div><dt>추적 범위</dt><dd>{_e(short(meetings[0]))} – {_e(short(latest))} ({len(meetings)}회)</dd></div>
      <div><dt>확정</dt><dd>{conf:,}</dd></div>
      <div><dt>후보</dt><dd>{cand:,}</dd></div>
    </dl>
  </div>
  <div class="lede-row"><p class="lede">CSI 획득·보고, CSI-RS, codebook, beam management, SRS, AI/ML CSI에 관한 RAN1 결정을 Chair notes 원문 그대로 모았습니다.</p>
    {_help("<b>확정</b>은 CSI Agenda(설정 파일의 포함 목록)에 기록된 결정, <b>후보</b>는 다른 Agenda에서 CSI 키워드가 나온 결정이라 CSI가 아닐 수 있습니다. "
           "기본 화면은 확정 Agreement만 보여주며, 숨긴 결정 수는 필터 줄 오른쪽 '숨김'에 항상 나옵니다. "
           "결정 본문은 요약하지 않은 원문이고, 주제·진행 단계·구현 영향·⚠ 표시는 이 대시보드가 원문 단어로 붙인 것입니다.")}</div>
  {_alerts_html(m)}
  {notices}
</header>

<div class="sticky">
  <nav class="tabs" role="tablist" aria-label="화면 고르기">{tab_buttons}</nav>
  <form class="filterbar" id="filters" onsubmit="return false" aria-label="표시할 결정 고르기">
    <fieldset><legend>구분</legend>{types}<label class="sep" title="FFS 줄이 들어 있는 결정. 이후 회의에서 해소됐는지는 'FFS 추적' 탭에서 후보로 확인합니다."><input type="checkbox" id="g-ffs"> FFS 있는 결정만</label></fieldset>
    <fieldset><legend>범위</legend>{_check("data-scope", "confirmed", "확정", True)}{_check('data-scope id="g-cand"', "candidate", "후보 (키워드 일치)", False)}</fieldset>
    <span class="state small" id="state" aria-live="polite"></span>
  </form>
</div>

<div class="tab-panel" id="panel-summary" data-panel="summary" role="tabpanel" aria-labelledby="tab-summary">
<section>
  <div class="section-head"><h2>직전 회의 대비 <span class="mono muted">{_e(short(prev) if prev else "-")} → {_e(short(latest))}</span></h2>
    {_help(f"{_e(latest)}의 주제별 결정 수와 직전 회의 대비 증감입니다. {_e(latest)} 결정은 모두 이번 회의의 신규 결정이며 목록에서 <span class='chip new'>신규</span>로 표시합니다. 카드를 누르면 그 신규 결정을 결정 목록 탭에서 보여줍니다.")}</div>
  <div class="cards" id="delta"></div>
  <p class="small muted" id="latest-hidden"></p>
  {_change_brief(m)}
</section>

<section>
  <div class="section-head"><h2>회의별 · 주제별 결정 수</h2>
    {_help("막대 조각에 올리면 건수, 누르면 그 회의·주제의 결정을 결정 목록 탭에서 보여줍니다. 차트와 표의 회의별 숫자는 결정마다 하나인 <b>주된 주제</b>로 셉니다. "
           "한 결정이 여러 주제에 걸치면(예: CSI-RS와 CSI 보고) 나머지는 <b>관련 주제</b>로 붙습니다. 표 맨 끝 '관련 포함' 열은 관련 주제까지 센 수라 합계가 전체보다 큽니다.")}</div>
  <div class="panel">
    <div class="legend">{"".join(f'<span><i class="swatch" style="background: var(--t-{_e(t["id"])})"></i>{_e(t["label"])}</span>' for t in m["topics"])}</div>
    <svg class="chart" id="chart" role="img"></svg>
  </div>
  <div class="table-scroll"><table>
    <thead><tr><th>주된 주제</th>{heads}<th class="num">합계</th><th class="num related" title="그 주제가 관련 주제로 붙은 결정 수 (전체 회의)">관련 포함</th></tr></thead><tbody id="topic-body"></tbody>
  </table></div>
</section>
</div>

<section id="list" class="tab-panel" data-panel="list" role="tabpanel" aria-labelledby="tab-list" hidden>
  <div class="section-head"><h2>결정 목록</h2>
    {_help("결정 본문은 Chair notes <b>원문 그대로</b>이며 요약하지 않았습니다(표는 표로, R1- 번호는 TDoc 링크로만 바꿔 보여줍니다). "
           "띄어 쓰면 모두 포함(AND), <span class='mono'>|</span> 또는 대문자 <span class='mono'>OR</span>로 나누면 하나라도 포함(OR)된 결정을 찾습니다. "
           "⚠ 표시: <b>수식 누락 의심</b>은 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있다는 뜻, <b>색 표시 손실</b>은 색으로 표시된 추가·삭제를 알 수 없다는 뜻, "
           "<b>변경은 TDoc에</b>는 실제 변경 내용이 TDoc에만 있다는 뜻입니다. 표시에 마우스를 올리면 설명이 나옵니다.")}</div>
  <div class="panel search" role="search">
    <input type="search" id="q" placeholder="예: CSI-RS | NZP, codebook OR PMI, beam failure" autocomplete="off" aria-label="결정 원문과 Agenda 제목에서 찾을 키워드">
    <div class="filters">
      <label>주제 <select id="f-topic"><option value="">전체</option></select></label>
      <label>회의 <select id="f-meeting"><option value="">전체</option></select></label>
      <label>Agenda <select id="f-agenda"><option value="">전체</option></select></label>
      <button type="button" class="reset" id="reset">조건 지우기</button>
    </div>
    <details class="more-filters" id="more-filters"><summary>상세 필터 <span class="small muted" id="more-state"></span></summary>
      <div class="filters">
        <label>진행 단계 <select id="f-stage"><option value="">전체</option></select></label>
        <label>구현 영향 <select id="f-impact"><option value="">전체</option></select></label>
        <label>규격 조항 <select id="f-clause"><option value="">전체</option></select></label>
        <label title="수식 누락 의심, 색 표시 변경 손실, 실제 변경이 TDoc에만 있는 결정"><input type="checkbox" id="f-warn"> 원문·TDoc 확인 필요만</label>
        <label><input type="checkbox" id="f-word" checked> 단어 단위로만 찾기</label>
      </div>
      {f'<div class="presets">추천 검색어 {presets}</div>' if presets else ""}
    </details>
    <div class="summary-line" id="summary" aria-live="polite"></div>
    <div class="results" id="results"></div>
  </div>
</section>

<section class="tab-panel" data-panel="agenda" id="panel-agenda" role="tabpanel" aria-labelledby="tab-agenda" hidden>
  <div class="section-head"><h2>Agenda별 결정 수</h2>
    {_help("포함 Agenda는 번호가 아니라 '섹션 + Agenda 제목'으로 회의 간에 이어 붙였습니다. 번호가 바뀐 Agenda는 바뀐 과정을 함께 적었습니다. "
           "필터 줄에서 '후보'를 켜면 키워드로 잡힌 결정이 많은 Agenda도 나옵니다. 숫자를 누르면 결정 목록 탭에서 그 결정을 보여줍니다.")}</div>
  <div class="table-scroll"><table>
    <thead><tr><th>Agenda</th>{heads}<th class="num">합계</th></tr></thead><tbody id="agenda-body"></tbody>
  </table></div>
</section>

<section id="ffs" class="tab-panel" data-panel="ffs" role="tabpanel" aria-labelledby="tab-ffs" hidden>
  <div class="section-head"><h2>FFS 추적</h2>
    {_help("확정 결정에 남은 FFS(For Further Study) 줄입니다. 같은 포함 Agenda의 <b>이후 회의</b> 결정 중 단어가 많이 겹치는 것을 '후속 결정 후보'로 붙였습니다. "
           "단어 겹침으로 고른 후보일 뿐 FFS가 해소됐다는 판정이 아니니 원문으로 확인하세요. "
           "'후속 결정 후보가 없는 FFS만'을 켜면 아직 아무 후속 논의도 보이지 않는 미결 항목만 남습니다. 위 필터 줄(구분·범위)은 이 탭에 적용되지 않습니다.")}</div>
  <div class="panel">
    <div class="filters">
      <label>주된 주제 <select id="ffs-topic"><option value="">전체</option></select></label>
      <label>회의 <select id="ffs-meeting"><option value="">전체</option></select></label>
      <label><input type="checkbox" id="ffs-open"> 후속 결정 후보가 없는 FFS만</label>
    </div>
    <div class="summary-line" id="ffs-summary" aria-live="polite"></div>
    <div id="ffs-list"></div>
  </div>
</section>

<section id="fg" class="tab-panel" data-panel="fg" role="tabpanel" aria-labelledby="tab-fg" hidden>
  <div class="section-head"><h2>UE feature (FG) 목록</h2>
    {_help("확정 범위의 UE feature 결정 표에서 FG 번호·이름과, 그 FG를 정의·수정한 결정을 모았습니다(HW 사양 체크리스트용). "
           "원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없어 '표 내용'에는 지운 글자도 섞여 있을 수 있습니다. 최종 정의는 TDoc(FG 시트)으로 확인하세요.")}</div>
  <div class="panel">
    <input type="search" id="fg-q" placeholder="FG 번호·이름으로 찾기 (예: 58-1, CSI prediction, 128 ports)" autocomplete="off" aria-label="FG 찾기">
    <div class="table-scroll"><table>
      <thead><tr><th>FG</th><th>이름</th><th>수정한 회의</th><th>표 내용</th><th></th></tr></thead><tbody id="fg-body"></tbody>
    </table></div>
  </div>
</section>

{_changes_html(m)}

<footer>원본: <a href="https://github.com/{_e(src["repo"])}">{_e(src["repo"])}</a> (브랜치 <span class="mono">{_e(src["branch"])}</span>)의 DB를 읽기만 합니다.
  주제별 마크다운 리포트: {topic_links}. 범위·주제 규칙은 config/csi_scope.yaml에 있으며, 이 페이지는 scripts/build.py가 자동으로 생성합니다.</footer>
</main>
<div id="tip" hidden></div>
<script type="application/json" id="csi-data">{_json_for_script(data(m))}</script>"""


def render_html(m):
    fonts = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
             '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500'
             '&family=IBM+Plex+Sans+KR:wght@400;600;700&display=swap">')
    return ('<!doctype html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            f"<title>{TITLE}</title>\n{fonts}\n<style>{css(m['topics'])}</style>\n</head>\n<body>\n"
            f"{render_body(m)}\n<script>{SCRIPT}</script>\n</body>\n</html>\n")

