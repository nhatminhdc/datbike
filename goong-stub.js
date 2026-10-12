/* Stand-in for the domain-locked Goong map. Keeps the store list script
   from throwing, and never clears the Google Maps embed inside #map. */
(function () {
  function noop() {}
  function chain() { return this; }

  function Map() {
    this.getZoom = function () { return 12; };
    this.flyTo = noop;
    this.fitBounds = noop;
    this.zoomTo = noop;
    this.on = chain;
    this.once = chain;
    this.off = chain;
    this.remove = noop;
    this.resize = noop;
  }

  function Marker(o) {
    var el = document.createElement("div");
    if (o && o.nodeType === 1) el = o;
    else if (o && o.element && o.element.nodeType === 1) el = o.element;
    var popup = {
      isOpen: function () { return false; },
      remove: noop,
      addTo: function () { return this; }
    };
    return {
      setLngLat: function () { return this; },
      addTo: function () { return this; },
      setPopup: function (p) { popup = p || popup; return this; },
      getPopup: function () { return popup; },
      remove: noop,
      getElement: function () { return el; }
    };
  }

  function Popup() {
    return {
      setHTML: function () { return this; },
      setLngLat: function () { return this; },
      remove: noop,
      addTo: function () { return this; },
      isOpen: function () { return false; }
    };
  }

  function LngLatBounds() {
    return { extend: function () { return this; } };
  }

  window.goongjs = {
    accessToken: "",
    Map: Map,
    Marker: Marker,
    Popup: Popup,
    LngLatBounds: LngLatBounds
  };

  function wireBranches() {
    var nav = document.querySelector(".st-branch-nav");
    var frame = document.querySelector("#map.st-map iframe");
    if (!nav || !frame) return;
    nav.addEventListener("click", function (e) {
      var btn = e.target.closest && e.target.closest(".st-branch");
      if (!btn) return;
      var src = btn.getAttribute("data-src");
      if (src) frame.src = src;
      nav.querySelectorAll(".st-branch").forEach(function (b) {
        b.classList.toggle("is-on", b === btn);
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", wireBranches);
  } else {
    wireBranches();
  }
})();
