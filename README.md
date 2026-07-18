# Clara de Oteiza — Home page (static)

Production static build of the **claradeoteiza.com** home page, a framework-free
recreation of the `project/home/` design prototype. Pure HTML + CSS + vanilla JS,
no build step.

## Run locally

Any static file server works — the page uses no bundler:

```bash
cd site
python3 -m http.server 8000
# open http://localhost:8000/
```

Deploy by uploading the `site/` folder as-is to any static host (Netlify,
Vercel, S3/CloudFront, Nginx, GitHub Pages, …).

## Structure

```
site/
  index.html          Full home page (semantic, works without JS)
  css/
    styles.css        Design-system entry (imports the token files)
    fonts.css         Manrope + DM Sans (Google Fonts)
    colors.css        Warm-black / wine / gold color tokens
    typography.css    Type scale + weights
    layout.css        Spacing, radius, shadow, motion, z-index
    base.css          Element defaults
    home.css          Page styles (translated 1:1 from the prototype)
  js/
    data.js           Sitemap subset, services, derivador routing, testimonios
    background.js      Animated gold-particle canvas backdrop
    app.js            Header, mobile menu, scroll-reveal, derivador, scroller
  assets/             Brand portraits, service photos, imagery, testimonio shots
```

## Sections (top → bottom)

Header (sticky, blur-on-scroll) · Hero (gold-ringed portrait) · **Derivador**
(interactive triage: chips + free-text keyword classification → routed internal
links + WhatsApp CTA) · Sobre Clara (+ magia-blanca trust badge) · 6 Servicios
cards · central CTA · Testimonios (horizontal WhatsApp-screenshot gallery) ·
Instagram / TikTok social proof · legal disclaimer · Footer · floating WhatsApp
button.

## Behavior notes

- **Progressive enhancement:** all copy and links render without JavaScript. JS
  adds the interactive Derivador, mobile menu, scroll-reveal, header blur, and
  personalized WhatsApp messages (`data-wa-msg`).
- **Accessibility / motion:** WCAG-AA contrast throughout; the animated
  background, scroll reveals, and smooth scrolling all honor
  `prefers-reduced-motion`.
- **Testimonios rotation:** the prototype rotates a deterministic 6–8 subset per
  page slug (for the 162 planned internal pages). This home page renders the
  fixed `home`-slug subset (screenshots 16–20, 01–03). The rotation function
  lives in `js/data.js` (`CDO.pickTestimonios`) for reuse on internal pages.
- **Internal links** (service cards, derivador results) point at their planned
  relative URLs (`/amarres/…`, `/tarot-y-videncia/…`); wire routing when the
  internal pages are built.

## Config

- **WhatsApp number:** `5491136746858` (from the brief), used in every CTA.
- **Instagram:** `@ritualesdeamoreterno.ok` · **TikTok:** `@claradeoteiza`.
- **Fonts:** Manrope + DM Sans via Google Fonts. To self-host, swap the `@import`
  in `css/fonts.css` for local `@font-face` rules.
