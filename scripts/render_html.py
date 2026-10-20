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
.filterbar { position: sticky; top: 0; z-index: 5; background: var(--panel); border: 1px solid var(--rule); border-radius: 8px;
  padding: 10px 14px; display: flex; flex-wrap: wrap; gap: 8px 22px; align-items: center; font-size: 13px; color: var(--ink-2); }
.filterbar fieldset { display: flex; flex-wrap: wrap; gap: 6px 14px; align-items: center; border: 0; padding: 0; margin: 0; }
.filterbar legend { float: left; padding: 0; margin-right: 2px; font-weight: 600; color: var(--ink); }
.filterbar label { display: inline-flex; gap: 6px; align-items: center; }
.filterbar .sep { padding-left: 12px; border-left: 1px solid var(--rule); }
.filterbar .state { margin-left: auto; color: var(--ink-3); }
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
.search input[type=search] { width: 100%; box-sizing: border-box; font: inherit; font-size: 16px; padding: 10px 12px;
  border: 1px solid var(--rule); border-radius: 6px; background: var(--bg); color: var(--ink); }
.filters { display: flex; flex-wrap: wrap; gap: 8px 16px; align-items: center; font-size: 13px; color: var(--ink-2); }
.filters label { display: inline-flex; gap: 6px; align-items: center; max-width: 100%; min-width: 0; }
.filters select { font: inherit; font-size: 13px; padding: 4px 6px; border: 1px solid var(--rule); border-radius: 6px;
  background: var(--bg); color: var(--ink); max-width: 100%; min-width: 0; flex: 0 1 auto; }
#list { scroll-margin-top: 64px; }
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
  font-size: 13px; white-space: pre-line; overflow-wrap: anywhere; max-height: 16em; overflow-y: auto; }
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
@media (max-width: 640px) { h1 { font-size: 23px; } .filterbar { position: static; } .filterbar .state { margin-left: 0; } }
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
    return `${scopes.join('+') || '범위 없음'} · ${types.join('·') || '구분 없음'}${$('g-ffs').checked ? ' · FFS 남은 것만' : ''}`;
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
  const out = $('results'), summary = $('summary'), PAGE = 40;
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
  const esc = t => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const pattern = (t, word) => word ? `(?<![A-Za-z0-9])${esc(t)}(?![A-Za-z0-9])` : esc(t);
  function highlight(node, text, re) {
    if (!re) { node.textContent = text; return; }
    let last = 0;
    for (const m of text.matchAll(re)) { if (!m[0]) continue; node.append(text.slice(last, m.index), el('mark', null, m[0])); last = m.index + m[0].length; }
    node.append(text.slice(last));
  }
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
    if (e.scope === 'candidate') head.append(el('span', 'chip cand', '후보'));
    if (e.scope === 'manual') head.append(el('span', 'chip', '수동 포함'));
    head.append(el('span', 'mono', e.item), el('span', 'muted', e.title));
    box.append(head);
    if (e.scope === 'candidate') box.append(el('div', 'kw', '일치: ' + e.kw.join(', ')));
    box.append(el('span', 'label-orig', 'Chair notes 원문'));
    const text = el('p', 'orig'); highlight(text, e.text, re); box.append(text);
    const src = el('div', 'src'); const s = e.source;
    src.append(link(s.url, s.doc));
    if (s.tdoc) src.append(' · ', link(s.tdoc_url, s.tdoc));
    if (s.discussion) src.append(' · ', el('span', 'mono', `[${s.discussion}]`));
    src.append(' · ', el('span', 'mono', e.id));
    if (e.ffs) src.append(` · 남은 FFS ${e.ffs}건`);
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
    if (idFilter) {  // '최근 변경' 버튼: 구분·범위 체크와 다른 조건을 무시하고 그 결정만 보여줌
      hits = D.entries.filter(e => idFilter.has(e.id)).reverse(); curRe = null; out.replaceChildren(); shown = 0;
      summary.replaceChildren(el('span', 'num', `${hits.length}건`), ` · ${idLabel} (구분·범위 체크와 관계없이 모두 표시 · '조건 지우기'로 해제)`);
      showMore(); return;
    }
    const groups = q.value.trim().split(/\s+OR\s+|\s*\|\s*/).map(g => g.split(/\s+/).filter(Boolean)).filter(g => g.length);
    const terms = groups.flat();
    const groupRes = groups.map(g => g.map(t => new RegExp(pattern(t, fWord.checked), 'i')));
    curRe = terms.length ? new RegExp(terms.map(t => pattern(t, fWord.checked)).join('|'), 'gi') : null;
    hits = base.filter(e => topicOk(e) && (!fMeeting.value || e.meeting === fMeeting.value) && agendaOk(e) &&
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
    idFilter = f.ids ? new Set(f.ids) : null; idLabel = f.label || '';
    if (fAgenda.value[0] === 'c' && !$('g-cand').checked) { $('g-cand').checked = true; }
    update(); $('list').scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
  function update() {
    const ok = pred(), base = D.entries.filter(ok);
    renderState(base);
    cards(base); chart(base);
    matrix($('topic-body'), topicRows, base, true);
    matrix($('agenda-body'), agendaRows(), base, false);
    list(base);
  }
  bar.addEventListener('change', update);
  let rw; addEventListener('resize', () => { clearTimeout(rw); rw = setTimeout(() => chart(D.entries.filter(pred())), 200); });
  q.addEventListener('input', () => { idFilter = null; clearTimeout(timer); timer = setTimeout(() => list(D.entries.filter(pred())), 150); });
  [fTopic, fMeeting, fAgenda, fWord].forEach(n => n.addEventListener('change', () => { idFilter = null; list(D.entries.filter(pred())); }));
  $('reset').addEventListener('click', () => { idFilter = null; q.value = ''; fTopic.value = fMeeting.value = fAgenda.value = ''; list(D.entries.filter(pred())); });
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
            "recent": _recent(m)}


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


def _changes_html(m):
    hist = m.get("changes") or []
    lede = ("실행마다 직전 결과와 비교한 기록입니다. 새 회의 결정은 위에서 <span class=\"chip new\">신규</span>로 보이지만, "
            "원본이 <b>과거 회의</b>를 다시 처리해 생긴 추가·변경·삭제(파서 개선, 잠정 → 종료본 교체, 범위 설정 변경)는 여기서만 알 수 있습니다. "
            "최근 30일 안의 변경은 결정 목록에도 표시됩니다.")
    if not hist:
        return (f'<section id="changes"><h2>최근 변경 이력</h2><p class="lede">{lede}</p>'
                '<p class="empty">아직 기록된 변경이 없습니다. 이 기능을 켠 뒤 결과가 처음 달라진 실행부터 남습니다.</p></section>')
    rows = []
    for c in hist[:5]:
        nm = ", ".join(f'{x["meeting"]} {x["count"]}건' for x in c["new_meetings"]) or "—"
        k = c["counts"]
        rows.append(f'<tr><td class="mono">{_e(c["at"].replace("T", " ")[:16])} UTC</td><td>{_e(c["reason"])}</td><td>{_e(nm)}</td>'
                    f'<td class="num">{k["added"]}</td><td class="num">{k["changed"]}</td><td class="num">{k["removed"]}</td></tr>')
    items = hist[0]["items"]
    detail = ""
    if items:
        live = {e["id"] for e in m["entries"]}
        ids = [x["id"] for x in items if x["what"] != "removed" and x["id"] in live]
        trs = "".join(
            f'<tr><td>{WHAT[x["what"]]}{(" (" + ", ".join(FIELD_KO.get(f, f) for f in x["fields"]) + ")") if x["fields"] else ""}</td>'
            f'<td class="mono">{_e(x["meeting"])}</td><td>{_e(x["type"])}</td><td>{_e({"agenda": "확정", "manual": "확정(수동)", "candidate": "후보"}[x["scope"]])}</td>'
            f'<td>{_e(x["agenda"])}</td><td class="line">{_e(x["line"])}</td>'
            f'<td class="mono small"><a href="{_e(x["url"])}" target="_blank" rel="noopener">{_e(x["id"])}</a></td></tr>'
            for x in items[:100])
        button = (f'<button type="button" class="reset" data-ids="{_e(json.dumps(ids))}" data-label="{_e(hist[0]["at"][:10])} 과거 회의 추가·변경 결정">'
                  f'결정 목록에서 원문 보기 ({len(ids)}건)</button>') if ids else ""
        detail = (f'<h3>가장 최근 묶음({_e(hist[0]["at"][:10])})의 과거 회의 변경 {len(items)}건</h3>{button}'
                  f'<div class="table-scroll"><table class="changes"><thead><tr><th>변경</th><th>회의</th><th>구분</th><th>범위</th>'
                  f'<th>Agenda</th><th>원문 첫 줄</th><th>id</th></tr></thead><tbody>{trs}</tbody></table></div>')
    return f"""<section id="changes">
  <h2>최근 변경 이력</h2>
  <p class="lede">{lede}</p>
  <div class="table-scroll"><table>
    <thead><tr><th>실행 시각</th><th>이유</th><th>새 회의</th><th class="num">과거 회의 추가</th><th class="num">변경</th><th class="num">삭제</th></tr></thead>
    <tbody>{"".join(rows)}</tbody>
  </table></div>
  {detail}
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
    return f"""<main class="wrap">
<header>
  <div class="topline">
    <p class="updated">원본 DB 마지막 업데이트 <b>{_e(m["updated_kst"] or "기록 없음")}</b>{CHECKED_AT}</p>
    <button type="button" class="theme" id="theme">테마: 자동</button>
  </div>
  <span class="eyebrow">3GPP TSG RAN WG1 · Chair notes 기준 · CSI 관련 결정</span>
  <h1>{TITLE}</h1>
  <p class="lede">CSI 획득·보고, CSI-RS, codebook(PMI/CQI/RI), beam management(TCI, beam failure 등), SRS, AI/ML CSI(압축·예측)에 관한 RAN1 결정을 모았습니다.
    <b>확정</b>은 CSI Agenda(설정 파일의 포함 목록)에 기록된 결정, <b>후보</b>는 다른 Agenda에서 CSI 키워드가 나온 결정이라 CSI가 아닐 수 있습니다.</p>
  <dl class="facts">
    <div><dt>최신 회의</dt><dd>{_e(latest)}{' <span class="chip cand">잠정</span>' if latest in m["provisional"] else ""}</dd></div>
    <div><dt>추적 범위</dt><dd>{_e(meetings[0])} – {_e(short(latest))} ({len(meetings)}회)</dd></div>
    <div><dt>확정 결정</dt><dd>{conf:,}</dd></div>
    <div><dt>후보 결정</dt><dd>{cand:,}</dd></div>
  </dl>
  {_alerts_html(m)}
  {notices}
</header>

<form class="filterbar" id="filters" onsubmit="return false" aria-label="표시할 결정 고르기">
  <fieldset><legend>구분</legend>{types}<label class="sep"><input type="checkbox" id="g-ffs"> FFS 남은 결정만</label></fieldset>
  <fieldset><legend>범위</legend>{_check("data-scope", "confirmed", "확정", True)}{_check('data-scope id="g-cand"', "candidate", "후보 (키워드 일치)", False)}</fieldset>
  <span class="state small" id="state" aria-live="polite"></span>
</form>

<section>
  <h2>직전 회의 대비 <span class="mono muted">{_e(short(prev) if prev else "-")} → {_e(short(latest))}</span></h2>
  <p class="lede">{_e(latest)}의 결정 수와 직전 회의 대비 증감입니다. {_e(latest)} 결정은 모두 이번 회의의 신규 결정이며, 목록에서 <span class="chip new">신규</span>로 표시합니다. 카드를 누르면 해당 신규 결정을 보여줍니다.</p>
  <div class="cards" id="delta"></div>
  <p class="small muted" id="latest-hidden"></p>
</section>

{_changes_html(m)}

<section>
  <h2>회의별 · 주제별 결정 수</h2>
  <div class="panel">
    <div class="legend">{"".join(f'<span><i class="swatch" style="background: var(--t-{_e(t["id"])})"></i>{_e(t["label"])}</span>' for t in m["topics"])}</div>
    <svg class="chart" id="chart" role="img"></svg>
    <span class="small muted">막대 조각에 올리면 건수, 누르면 그 회의·주제의 결정 목록을 보여줍니다. 차트와 표의 회의별 숫자는 결정마다 하나인 <b>주된 주제</b>로 셉니다.
      한 결정이 여러 주제에 걸치면(예: CSI-RS와 CSI 보고) 나머지는 <b>관련 주제</b>로 붙습니다. 표 맨 끝 '관련 포함' 열은 관련 주제까지 센 수라 합계가 전체보다 큽니다.</span>
  </div>
  <div class="table-scroll"><table>
    <thead><tr><th>주된 주제</th>{heads}<th class="num">합계</th><th class="num related" title="그 주제가 관련 주제로 붙은 결정 수 (전체 회의)">관련 포함</th></tr></thead><tbody id="topic-body"></tbody>
  </table></div>
</section>

<section>
  <h2>Agenda별 결정 수</h2>
  <p class="lede">포함 Agenda는 번호가 아니라 '섹션 + Agenda 제목'으로 회의 간에 이어 붙였습니다. 번호가 바뀐 Agenda는 바뀐 과정을 함께 적었습니다.
    위에서 '후보'를 켜면 키워드로 잡힌 결정이 많은 Agenda도 나옵니다.</p>
  <div class="table-scroll"><table>
    <thead><tr><th>Agenda</th>{heads}<th class="num">합계</th></tr></thead><tbody id="agenda-body"></tbody>
  </table></div>
</section>

<section id="list">
  <h2>결정 목록</h2>
  <div class="panel search" role="search">
    <input type="search" id="q" placeholder="예: CSI-RS | NZP, codebook OR PMI, beam failure" autocomplete="off" aria-label="결정 원문과 Agenda 제목에서 찾을 키워드">
    <div class="filters">
      <label>주제 <select id="f-topic"><option value="">전체</option></select></label>
      <label>회의 <select id="f-meeting"><option value="">전체</option></select></label>
      <label>Agenda <select id="f-agenda"><option value="">전체</option></select></label>
      <label><input type="checkbox" id="f-word" checked> 단어 단위로만 찾기</label>
      <button type="button" class="reset" id="reset">조건 지우기</button>
    </div>
    {f'<div class="presets">추천 검색어 {presets}</div>' if presets else ""}
    <div class="summary-line" id="summary" aria-live="polite"></div>
    <div class="results" id="results"></div>
  </div>
  <p class="lede">결정 본문은 Chair notes <b>원문 그대로</b>이며 요약하지 않았습니다. 주제·신규·후보 표시만 이 대시보드가 붙인 것입니다.
    띄어 쓰면 모두 포함(AND), <span class="mono">|</span> 또는 대문자 <span class="mono">OR</span>로 나누면 하나라도 포함(OR)된 결정을 찾습니다.</p>
</section>

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

