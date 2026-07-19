/* consent.js — Puerta de mayoría de edad + consentimiento de cookies (Consent Mode v2).
   Se apoya en el gtag('consent','default', denied) que ya está en el <head>.
   Al aceptar: gtag('consent','update', granted) + recuerda la decisión. */
(function () {
  "use strict";
  var KEY = "cdo_consent_v1";
  function saved() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function store(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }
  function gtagSafe() { window.dataLayer = window.dataLayer || []; window.gtag = window.gtag || function () { dataLayer.push(arguments); }; }

  function grant() {
    gtagSafe();
    window.gtag("consent", "update", {
      ad_storage: "granted", analytics_storage: "granted",
      ad_user_data: "granted", ad_personalization: "granted"
    });
    window.dataLayer.push({ event: "consent_granted" });
  }

  var decision = saved();
  if (decision === "granted") { grant(); return; }   // ya aceptó
  if (decision === "essential") { return; }            // ya eligió solo esencial (queda denied)

  // ---- Construir el modal ----
  function build() {
    var wrap = document.createElement("div");
    wrap.className = "cdo-consent";
    wrap.setAttribute("role", "dialog");
    wrap.setAttribute("aria-modal", "true");
    wrap.setAttribute("aria-label", "Aviso de edad y cookies");
    wrap.innerHTML =
      '<div class="cdo-consent__card">' +
        '<div class="cdo-consent__star" aria-hidden="true">✦</div>' +
        '<h2 class="cdo-consent__title">Entrás al mundo de la <span>Alta Magia</span></h2>' +
        '<p class="cdo-consent__text">Rituales poderosos y magia blanca real, con más de 20 años de experiencia. Para continuar, confirmá que sos <strong>mayor de 18 años</strong> y elegí tus cookies.</p>' +
        '<div class="cdo-consent__actions">' +
          '<button class="cdo-consent__btn cdo-consent__btn--primary" data-consent="grant">Soy mayor de 18 · Aceptar y entrar</button>' +
          '<button class="cdo-consent__btn cdo-consent__btn--ghost" data-consent="essential">Solo lo esencial</button>' +
        '</div>' +
        '<button class="cdo-consent__minor" data-consent="minor">Soy menor de 18</button>' +
        '<p class="cdo-consent__legal">Al entrar aceptás nuestra <a href="/privacidad/">Política de Privacidad</a> y los <a href="/terminos/">Términos</a>. Usamos cookies para analítica y publicidad.</p>' +
      '</div>';
    document.body.appendChild(wrap);
    document.documentElement.style.overflow = "hidden";
    requestAnimationFrame(function () { wrap.classList.add("is-open"); });

    function close() { wrap.classList.remove("is-open"); document.documentElement.style.overflow = ""; setTimeout(function () { wrap.remove(); }, 300); }

    wrap.addEventListener("click", function (e) {
      var act = e.target.getAttribute && e.target.getAttribute("data-consent");
      if (!act) return;
      if (act === "grant") { grant(); store("granted"); close(); }
      else if (act === "essential") { store("essential"); close(); }
      else if (act === "minor") {
        wrap.querySelector(".cdo-consent__card").innerHTML =
          '<div class="cdo-consent__star" aria-hidden="true">🕯️</div>' +
          '<h2 class="cdo-consent__title">Gracias por tu visita</h2>' +
          '<p class="cdo-consent__text">Este sitio y sus servicios son solo para personas mayores de 18 años. Te esperamos cuando cumplas la edad.</p>';
      }
    });
  }

  if (document.body) build();
  else document.addEventListener("DOMContentLoaded", build);
})();
