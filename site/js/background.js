/* background.js — signature ambient backdrop: floating gold particles on a
   canvas. Ported from AnimatedBackground.jsx. Honors prefers-reduced-motion
   (the drifting gradient + static layers remain; particles are skipped). */
(function () {
  "use strict";

  var PARTICLES = 42;
  var canvas = document.querySelector(".cdo-bg__canvas");
  if (!canvas) return;

  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce) return;

  var ctx = canvas.getContext("2d");
  var raf, w, h, dpr;
  var dots = [];

  function resize() {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    w = canvas.clientWidth; h = canvas.clientHeight;
    canvas.width = w * dpr; canvas.height = h * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }
  resize();
  window.addEventListener("resize", resize);

  for (var i = 0; i < PARTICLES; i++) {
    dots.push({
      x: Math.random() * w,
      y: Math.random() * h,
      r: Math.random() * 1.8 + 0.4,
      vy: -(Math.random() * 0.28 + 0.06),
      vx: (Math.random() - 0.5) * 0.14,
      a: Math.random() * 0.5 + 0.2,
      tw: Math.random() * Math.PI * 2
    });
  }

  function draw() {
    ctx.clearRect(0, 0, w, h);
    for (var i = 0; i < dots.length; i++) {
      var d = dots[i];
      d.x += d.vx; d.y += d.vy; d.tw += 0.02;
      if (d.y < -6) { d.y = h + 6; d.x = Math.random() * w; }
      if (d.x < -6) d.x = w + 6;
      if (d.x > w + 6) d.x = -6;
      var alpha = d.a * (0.6 + 0.4 * Math.sin(d.tw));
      var grd = ctx.createRadialGradient(d.x, d.y, 0, d.x, d.y, d.r * 4);
      grd.addColorStop(0, "rgba(241, 216, 150, " + alpha + ")");
      grd.addColorStop(1, "rgba(241, 216, 150, 0)");
      ctx.fillStyle = grd;
      ctx.beginPath();
      ctx.arc(d.x, d.y, d.r * 4, 0, Math.PI * 2);
      ctx.fill();
    }
    raf = requestAnimationFrame(draw);
  }
  draw();

  window.addEventListener("pagehide", function () {
    if (raf) cancelAnimationFrame(raf);
  });
})();
