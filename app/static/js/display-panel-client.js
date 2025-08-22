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
    console.log(`data: ${data.layout}`)
    showLayout(data.layout);
});