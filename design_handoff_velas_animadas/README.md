# Handoff: Velas Animadas — Clara de Oteiza

## Overview
An **animated candle-glow overlay** on a fixed brand photograph of Clara de Oteiza at her
tarot altar. The photo is static; warm, flickering light glows are layered on top of each
lit candle so the scene appears alive (candlelight breathing). Intended as a hero/ambient
visual for the web (e.g. header, landing hero, or embedded loop).

## About the Design Files
The file in this bundle (`Velas Animadas.dc.html`) is a **design reference created in
HTML** — a prototype showing the intended look and motion, not production code to ship
as-is. The task is to **recreate this effect in the target codebase's environment**
(React/Vue/Svelte/plain component, etc.) using its established patterns. The technique is
framework-agnostic: an `<img>` with absolutely-positioned glow `<div>`s over it, animated
with CSS keyframes.

> Note: the prototype was authored as a "Design Component" (`.dc.html`) which pulls in a
> small runtime (`support.js`). That runtime is **not** needed for the effect — it's just
> the prototyping harness. Reimplement with a plain image + overlay divs (see below).

## Fidelity
**High-fidelity (hifi).** Final motion, colors, blend modes and glow placement. Recreate
faithfully. All glow positions are expressed as **percentages of the image box** so they
scale with any image width.

## Screens / Views

### Single view — Animated altar image
- **Purpose**: Ambient brand visual; candles appear lit and flickering.
- **Layout**:
  - Outer wrapper: full-viewport flex, centered, dark radial background
    `radial-gradient(120% 120% at 50% 30%, #17101f 0%, #0b0710 70%)`, padding 24px.
  - Image container: `position: relative`, `width: min(720px, 92vw)`, `container-type:
    inline-size` (so `cqw` units resolve against it), `line-height: 0`, `border-radius:
    14px`, `overflow: hidden`, shadow `0 30px 90px rgba(0,0,0,.7), 0 0 0 1px
    rgba(207,162,74,.22)`.
  - `<img>`: `display:block; width:100%; height:auto`. Source photo is 1122×1402.
  - Glow layers: absolutely-positioned children of the image container. Each is a radial
    gradient with `mix-blend-mode: screen` and `pointer-events: none`, animated by the
    shared `glowFlick` keyframe. Positions in `%` (of container), sizes in `cqw`
    (% of container width).

- **Glow components** (left / top are the CENTER of the glow; the flick keyframe transforms
  with `translate(-50%,-50%)` so the element is centered on that point). Warm palette,
  cream-gold core → orange mid → transparent:

  | Candle | left% | top% | size (cqw) | shape | flick dur | delay |
  |---|---|---|---|---|---|---|
  | Vela pareja — llama izq | 48.7 | 53.9 | 2.4×4.4 (oval) | teardrop | 1.5s | 0 |
  | Vela pareja — llama der | 52.8 | 55.0 | 2.4×4.4 (oval) | teardrop | 1.35s | -0.4s |
  | Candelabro alto (arriba izq) | 5.5 | 7 | 4 | circle | 3.1s | -1.1s |
  | Farolillo marroquí izq | 10.5 | 44 | 8 | circle | 2.7s | -0.6s |
  | Vela roja pilar izq | 6 | 66 | 8 | circle | 2.2s | -1.9s |
  | Vela rosa pilar izq | 13.5 | 79 | 6 | circle | 3.3s | -2.3s |
  | Farolillo dorado izq | 14.5 | 82 | 4 | circle | 2.9s | -0.9s |
  | Votiva rosa frontal izq | 20 | 89.5 | 6 | circle | 2.5s | -1.4s |
  | Votiva roja der (media) | 89 | 44 | 6 | circle | 2.8s | -0.4s |
  | Vela roja pilar der | 85 | 79 | 8 | circle | 2.1s | -1.6s |
  | Votiva roja frontal der | 74 | 90.5 | 6 | circle | 3.0s | -2.1s |

  - **Circle glows**: `border-radius:50%; aspect-ratio:1;`
    `background: radial-gradient(circle, rgba(255,206,130,.65) 0%, rgba(255,150,60,.36) 32%, rgba(255,90,30,0) 70%)`
    (warm candles). Lantern/candelabra variants use a slightly softer gold
    `rgba(255,214,140,.6) → rgba(255,160,70,.3) → transparent`; pink votives use
    `rgba(255,190,140,.55) → rgba(255,120,90,.3) → transparent`.
  - **Oval (couple) glows** — flame-shaped, taller than wide:
    `width:2.4cqw; height:4.4cqw; border-radius:50% 50% 50% 50% / 62% 62% 40% 40%;`
    `background: radial-gradient(ellipse 58% 70% at 50% 62%, rgba(255,244,210,.92) 0%, rgba(255,190,90,.5) 42%, rgba(255,120,40,0) 78%)`.

## Interactions & Behavior
- **No user interaction** — purely ambient, infinite loop.
- **Animation** — one shared keyframe `glowFlick` drives every glow; per-candle `duration`
  and negative `animation-delay` desync them so nothing pulses in lockstep:

  ```css
  @keyframes glowFlick {
    0%   { opacity:.50; transform:translate(-50%,-50%) scale(1.00); }
    18%  { opacity:.92; transform:translate(-50%,-50%) scale(1.07); }
    33%  { opacity:.64; transform:translate(-50%,-50%) scale(0.97); }
    50%  { opacity:1.0; transform:translate(-50%,-50%) scale(1.06); }
    66%  { opacity:.70; transform:translate(-50%,-50%) scale(1.01); }
    82%  { opacity:.95; transform:translate(-50%,-50%) scale(1.04); }
    100% { opacity:.50; transform:translate(-50%,-50%) scale(1.00); }
  }
  ```

  Timing `ease-in-out`, `infinite`.
- **Accessibility** — all animation gated behind
  `@media (prefers-reduced-motion: reduce) { animation: none !important; }`.
- **Blend** — every glow uses `mix-blend-mode: screen` so it only adds light (never darkens
  the photo). Keep this; without it the glows look like opaque dots.

## State Management
None. Static image + CSS animation only. No JS state, no data fetching.

## Design Tokens
- **Dark bg**: `#17101f` → `#0b0710` (radial), gold hairline `rgba(207,162,74,.22)`.
- **Flame core**: `rgba(255,244,210,.9)` / cream-gold `#fff4d0`.
- **Warm mid**: `rgba(255,190,90,.5)`, `rgba(255,150,60,.36)`.
- **Warm falloff**: `rgba(255,120,40,0)` / `rgba(255,90,30,0)` (transparent).
- **Radii**: container 14px; oval flame `50% 50% 50% 50% / 62% 62% 40% 40%`.
- **Shadow**: `0 30px 90px rgba(0,0,0,.7)`.
- **Motion**: durations 1.35s–3.3s, `ease-in-out`, `infinite`; blend `screen`.

## Assets
- `assets/clara.png` — brand photograph, 1122×1402 PNG (Clara holding a pink couple candle
  at her altar). Included in this bundle. All glow coordinates are calibrated to THIS image;
  if the photo is swapped, recalibrate the `%` positions.

## Files
- `Velas Animadas.dc.html` — the working prototype (open in a browser to see the effect).
- `assets/clara.png` — the source photograph.

## Implementation note
Simplest production form: a container `<figure>` with the `<img>` and one `<span>` per
candle. Drive positions/sizes from a small data array (`{left, top, w, h, dur, delay,
shape}`) and render the glows in a loop. Keep `container-type: inline-size` on the figure so
`cqw` sizing stays proportional, or convert `cqw` sizes to `%` of width.
