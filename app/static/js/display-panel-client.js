function showLayout(id) {
        if (!id || !layouts.includes(id)) return;
        document.querySelectorAll(".layout").forEach(sec => sec.classList.remove("active"));
        document.getElementById(id)?.classList.add("active");
        if (pill) pill.textContent = "Current: " + id;
        // update URL hash without reloading
        if (history.pushState) history.replaceState(null, "", location.pathname + "?id=" + encodeURIComponent(id));
}
const layouts = ["bible-search", "hymn-search", "display-announcement"];
const pill = document.getElementById("current-pill");
const socket = io();
socket.on("layout_changed", (data) => {
    showLayout(data.layout);
});

socket.on("bible_search_results", (data) => {
  const results = data.bible_search_results || [];

  // Which div gets which translation
  const containers = {
    KOUGO: "kougo-search-results",
    CUNP:  "cunp-search-results",
    NIV:   "niv-search-results",
  };

  // (optional) simple HTML escape
  const esc = (s) => String(s)
    .replace(/&/g,"&amp;").replace(/</g,"&lt;")
    .replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#39;");

  // make one verse HTML block
  const verseHTML = (v) =>
    `<div class="verse"><sup class="verse-number">${v.verse}</sup>${esc(v.text)}</div>`;

  // group results by translation
  const byTrans = results.reduce((acc, r) => {
    (acc[r.translation] ||= []).push(r);
    return acc;
  }, {});

  // render into each container
  for (const [t, elId] of Object.entries(containers)) {
    const el = document.getElementById(elId);
    const items = byTrans[t] || [];
    el.innerHTML = items.length ? items.map(verseHTML).join("") : `<div class="muted">No results</div>`;
  }
});