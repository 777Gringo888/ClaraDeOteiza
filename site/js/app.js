/* app.js — behavior for the Clara de Oteiza home page.
   Header scroll state, mobile menu, scroll-reveal, WhatsApp message
   personalization, the interactive Derivador, and the testimonios scroller. */
(function () {
  "use strict";

  var CDO = window.CDO || {};

  // Official WhatsApp glyph markup (brand mark, not a UI icon).
  function waGlyph(size) {
    return '<svg width="' + size + '" height="' + size + '" viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16.04 4C9.9 4 4.9 9 4.9 15.14c0 2.15.6 4.16 1.66 5.88L4.6 28l7.15-1.88a11.1 11.1 0 0 0 4.29.86h.01c6.14 0 11.14-5 11.14-11.14C27.19 9 22.19 4 16.04 4Zm0 20.4h-.01c-1.36 0-2.7-.37-3.86-1.06l-.28-.16-4.25 1.11 1.13-4.14-.18-.29a9.2 9.2 0 0 1-1.41-4.91c0-5.09 4.15-9.24 9.25-9.24 2.47 0 4.79.96 6.53 2.71a9.18 9.18 0 0 1 2.71 6.54c0 5.1-4.15 9.24-9.24 9.24Zm5.07-6.92c-.28-.14-1.64-.81-1.9-.9-.25-.09-.44-.14-.62.14-.18.28-.71.9-.87 1.08-.16.18-.32.2-.6.07-.28-.14-1.17-.43-2.23-1.38-.82-.74-1.38-1.65-1.54-1.93-.16-.28-.02-.43.12-.57.12-.12.28-.32.42-.48.14-.16.18-.28.28-.46.09-.18.05-.35-.02-.48-.07-.14-.62-1.5-.85-2.05-.22-.54-.45-.46-.62-.47l-.53-.01c-.18 0-.48.07-.73.35-.25.28-.96.94-.96 2.3 0 1.36.98 2.67 1.12 2.85.14.18 1.93 2.95 4.67 4.14.65.28 1.16.45 1.56.58.65.21 1.25.18 1.72.11.53-.08 1.64-.67 1.87-1.32.23-.65.23-1.2.16-1.32-.07-.12-.25-.18-.53-.32Z"/></svg>';
  }

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  // ---- Footer year ----
  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());

  // ---- Header scroll state ----
  var header = document.getElementById("header");
  if (header) {
    var onScroll = function () {
      if (window.scrollY > 20) header.classList.add("is-scrolled");
      else header.classList.remove("is-scrolled");
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  // ---- Mobile menu ----
  var burger = document.getElementById("burger");
  var menu = document.getElementById("mobile-menu");
  if (burger && menu) {
    var toggleMenu = function (open) {
      burger.classList.toggle("is-open", open);
      menu.classList.toggle("is-open", open);
      if (header) header.classList.toggle("is-menu-open", open);
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    };
    burger.addEventListener("click", function () {
      toggleMenu(!menu.classList.contains("is-open"));
    });
    menu.addEventListener("click", function (e) {
      if (e.target.closest("a")) toggleMenu(false);
    });
  }

  // ---- Scroll reveal ----
  (function () {
    var els = document.querySelectorAll(".cdo-reveal");
    var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (reduce || !("IntersectionObserver" in window)) {
      for (var i = 0; i < els.length; i++) els[i].classList.add("in");
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
    els.forEach(function (el) { io.observe(el); });
  })();

  // ---- Personalize WhatsApp links that carry a specific message ----
  if (CDO.wa) {
    var waLinks = document.querySelectorAll("[data-wa-msg]");
    for (var w = 0; w < waLinks.length; w++) {
      waLinks[w].setAttribute("href", CDO.wa(waLinks[w].getAttribute("data-wa-msg")));
    }
  }

  // ---- Derivador ----
  (function () {
    var chipsWrap = document.getElementById("chips");
    var form = document.getElementById("derivador-form");
    var input = document.getElementById("derivador-input");
    var resultEl = document.getElementById("derivador-result");
    if (!chipsWrap || !form || !resultEl || !CDO.CHIPS) return;

    var chipButtons = chipsWrap.querySelectorAll(".chip");

    function setActive(id) {
      for (var i = 0; i < chipButtons.length; i++) {
        chipButtons[i].classList.toggle("is-active", chipButtons[i].getAttribute("data-chip") === id);
      }
    }

    function waFor(data) {
      var tema = data.label ? "mi tema es: " + data.label.toLowerCase() + ". " : "";
      return CDO.wa("Hola Clara, " + tema + "me gustaría una consulta gratuita.");
    }

    function renderResult(data) {
      if (!data) { resultEl.hidden = true; resultEl.innerHTML = ""; return; }

      var html;
      if (data.clarify) {
        html =
          '<p class="cdo-result__clarify-q">Quiero orientarte bien. ¿Tu tema es de <strong>pareja</strong>, de <strong>protección y energía</strong>, o de <strong>otro tipo</strong>?</p>' +
          '<div class="cdo-result__clarify-chips">' +
            '<button class="chip" data-refine="alejo">Es de pareja</button>' +
            '<button class="chip" data-refine="bloqueos">Es de protección / energía</button>' +
            '<button class="chip" data-refine="dinero">Es de dinero o trabajo</button>' +
            '<button class="chip" data-refine="claridad">Quiero claridad / tarot</button>' +
          '</div>';
      } else {
        var pages = data.pages.map(function (pg) {
          return '<a class="cdo-result__page" href="' + esc(pg.href) + '">' + esc(pg.label) +
            '<span class="arrow" aria-hidden="true">→</span></a>';
        }).join("");
        html =
          '<p class="cdo-result__intro">' + esc(data.intro) + '</p>' +
          '<p class="cdo-result__kicker">Te puede servir</p>' +
          '<div class="cdo-result__pages">' + pages + '</div>' +
          '<a class="wa-btn wa-btn--sm cdo-result__wa" href="' + esc(waFor(data)) + '" target="_blank" rel="noopener noreferrer">' +
            waGlyph(18) + 'Reservá tu consulta gratis de la semana</a>';
      }
      resultEl.innerHTML = html;
      resultEl.hidden = false;

      if (data.clarify) {
        var refineBtns = resultEl.querySelectorAll("[data-refine]");
        for (var i = 0; i < refineBtns.length; i++) {
          refineBtns[i].addEventListener("click", function (e) {
            var id = e.currentTarget.getAttribute("data-refine");
            var c = CDO.chipById(id);
            if (c) { setActive(id); renderResult(c); }
          });
        }
      }
    }

    for (var b = 0; b < chipButtons.length; b++) {
      chipButtons[b].addEventListener("click", function (e) {
        var id = e.currentTarget.getAttribute("data-chip");
        var c = CDO.chipById(id);
        if (c) { setActive(id); renderResult(c); }
      });
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var r = CDO.classify(input ? input.value : "");
      if (!r) return;
      setActive(null);
      renderResult(r);
    });
  })();

  // ---- Seamless video loop (crossfade two copies to hide the seam) ----
  (function () {
    var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (reduce) return;
    var wraps = document.querySelectorAll("[data-vloop]");
    Array.prototype.forEach.call(wraps, function (wrap) {
      var vids = wrap.querySelectorAll("video");
      if (vids.length < 2) return;
      var XF = 0.8; // crossfade seconds
      var active = vids[0], idle = vids[1];
      idle.style.opacity = "0"; active.style.opacity = "1";
      var swapping = false;
      var start = function (v) { var pr = v.play(); if (pr && pr.catch) pr.catch(function () {}); };
      var onScreen = true;
      if ("IntersectionObserver" in window) {
        new IntersectionObserver(function (es) {
          onScreen = es[0].isIntersecting;
          if (!onScreen) { active.pause(); idle.pause(); }
        }, { threshold: 0.02 }).observe(wrap);
      }
      var tick = function () {
        if (onScreen && active.paused && active.readyState >= 2) start(active);
        var d = active.duration;
        if (d && !swapping && active.currentTime >= d - XF) {
          swapping = true;
          idle.currentTime = 0;
          start(idle);
          idle.style.opacity = "1";
          active.style.opacity = "0";
          var prev = active;
          active = idle; idle = prev;
          setTimeout(function () { swapping = false; }, XF * 1000);
        }
        requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    });
  })();

  // ---- Two-tap confirm on service photos (tap once → darken + confirm, tap again → go) ----
  (function () {
    var medias = document.querySelectorAll("[data-confirm]");
    if (!medias.length) return;
    var disarmAll = function (except) {
      Array.prototype.forEach.call(medias, function (m) {
        if (m !== except) m.classList.remove("is-armed");
      });
    };
    Array.prototype.forEach.call(medias, function (m) {
      m.addEventListener("click", function (e) {
        if (!m.classList.contains("is-armed")) {
          e.preventDefault();          // first tap only arms it
          disarmAll(m);
          m.classList.add("is-armed");
        }
        // second tap: let the default link navigation happen
      });
    });
    document.addEventListener("click", function (e) {
      if (!e.target.closest("[data-confirm]")) disarmAll(null);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") disarmAll(null);
    });
  })();

  // ---- WhatsApp lead tracking: unique code per click + source + GTM event ----
  (function () {
    var CHARS = "ABCDEFGHJKMNPQRSTUVWXYZ23456789"; // sin caracteres ambiguos
    function rnd(n) {
      var s = "";
      for (var i = 0; i < n; i++) s += CHARS.charAt(Math.floor(Math.random() * CHARS.length));
      return s;
    }
    function sourceOf(a) {
      if (a.getAttribute("data-wa-source")) return a.getAttribute("data-wa-source");
      if (a.classList.contains("wa-btn--floating")) return "flotante";
      if (a.closest(".cdo-mobile-menu")) return "menu";
      if (a.closest(".cdo-header")) return "header";
      if (a.closest(".cdo-derivador")) return "derivador";
      var row = a.closest(".service-row");
      if (row) {
        var t = row.querySelector(".service-row__title");
        var name = t ? t.textContent.trim().toLowerCase()
          .replace(/[áàä]/g, "a").replace(/[éèë]/g, "e").replace(/[íìï]/g, "i")
          .replace(/[óòö]/g, "o").replace(/[úùü]/g, "u")
          .replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "") : "x";
        return "servicio-" + name;
      }
      if (a.closest(".cdo-hero-section")) return "hero";
      if (a.closest(".cdo-cta-central")) return "cta";
      if (a.closest(".cdo-footer")) return "footer";
      var s = a.closest("section");
      return (s && s.id) ? s.id : "web";
    }
    document.addEventListener("click", function (e) {
      var a = e.target.closest ? e.target.closest('a[href*="wa.me"]') : null;
      if (!a) return;
      var src = sourceOf(a);
      var code = "CDO-" + src.toUpperCase().replace(/[^A-Z0-9-]/g, "").slice(0, 20) + "-" + rnd(4);
      try {
        var u = new URL(a.href);
        var text = (u.searchParams.get("text") || "").replace(/\n*\(Ref:[^)]*\)\s*$/i, "");
        u.searchParams.set("text", text + "\n\n(Ref: " + code + ")");
        a.href = u.toString();
      } catch (err) { /* si no se puede parsear, se abre igual */ }
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({ event: "whatsapp_click", wa_source: src, wa_code: code });
    }, true); // fase de captura → corre antes de navegar
  })();

  // ---- Testimonios scroller arrows ----
  (function () {
    var scroller = document.getElementById("testimonios-scroller");
    if (!scroller) return;
    var arrows = document.querySelectorAll(".cdo-arrow");
    for (var i = 0; i < arrows.length; i++) {
      arrows[i].addEventListener("click", function (e) {
        var dir = parseInt(e.currentTarget.getAttribute("data-dir"), 10) || 1;
        scroller.scrollBy({ left: dir * Math.min(scroller.clientWidth * 0.8, 640), behavior: "smooth" });
      });
    }
  })();

})();

/* ============================================================
   CRO — Código de reserva + urgencia (cupos)
   Corre en todas las páginas (script al final del body).
   ============================================================ */
(function () {
  "use strict";

  // ---- Código de reserva único = ref (prefijo de categoría + aleatorio) ----
  function genRand() {
    var s = "ABCDEFGHJKMNPQRSTUVWXYZ23456789", c = "";
    for (var i = 0; i < 4; i++) c += s.charAt(Math.floor(Math.random() * s.length));
    return c;
  }
  function catPrefix() {
    var p = location.pathname.toLowerCase();
    var map = {
      "amarres": "AMR", "tarot-y-videncia": "TAR", "limpiezas-y-proteccion": "LIM",
      "prosperidad-y-abundancia": "PRO", "rituales-y-trabajos": "RIT"
    };
    // busca la categoría en cualquier parte del path (robusto a subcarpeta de preview)
    for (var k in map) { if (p.indexOf(k) !== -1) return map[k]; }
    return "CDO";
  }
  var CODE = catPrefix() + "-" + genRand();

  // Anexar el código + instrucción a cada link de WhatsApp
  var extra = encodeURIComponent(
    "\n\nMi código de reserva es #" + CODE +
    ". Envío este mensaje para asegurar mi cupo de esta semana."
  );
  var links = document.querySelectorAll('a[href*="wa.me"]');
  for (var i = 0; i < links.length; i++) {
    var h = links[i].getAttribute("href");
    if (h && h.indexOf("text=") !== -1 && h.indexOf("c%C3%B3digo%20de%20reserva") === -1 && h.indexOf("digo%20de%20reserva") === -1) {
      links[i].setAttribute("href", h + extra);
    }
  }

  // ---- Burbuja de cupos sobre el floater (urgencia honesta) ----
  (function () {
    var floater = document.querySelector(".wa-btn--floating");
    if (!floater) return;
    try { if (sessionStorage.getItem("cdo_cupos_closed")) return; } catch (e) {}
    var bubble = document.createElement("div");
    bubble.className = "cdo-cupos-bubble";
    bubble.innerHTML =
      '<button class="cdo-cupos-bubble__x" aria-label="Cerrar">&times;</button>' +
      'Esta semana quedan <strong>pocos cupos</strong> para consulta gratuita. Aseguremos el tuyo 🕯️';
    document.body.appendChild(bubble);
    // aparece con la INTERACCIÓN: cuando la persona scrollea y ya se enganchó
    var shown = false;
    function reveal() {
      if (shown) return;
      if (window.scrollY > 700 || window.scrollY > document.documentElement.scrollHeight * 0.25) {
        shown = true;
        bubble.classList.add("is-show");
        window.removeEventListener("scroll", reveal);
      }
    }
    window.addEventListener("scroll", reveal, { passive: true });
    bubble.querySelector(".cdo-cupos-bubble__x").addEventListener("click", function (ev) {
      ev.stopPropagation();
      bubble.classList.remove("is-show");
      try { sessionStorage.setItem("cdo_cupos_closed", "1"); } catch (e) {}
    });
    bubble.addEventListener("click", function () { floater.click(); });
  })();
})();
