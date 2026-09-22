# Clara de Oteiza — sitio (site/)

Sitio estático completo de **claradeoteiza.com**. HTML + CSS + JS vanilla,
**sin build**. Mobile-first. Conversión: WhatsApp.

> Brief operativo y reglas: **`../CLAUDE.md`**. Sistema de diseño: **`../DESIGN.md`**.

## Correr localmente

Las páginas internas usan **rutas absolutas**, así que hace falta un servidor:

```bash
cd site
python3 -m http.server 8000
# http://localhost:8000/
```

## Estructura

```
site/
  index.html                         Home (rutas relativas)
  amarres/index.html                 Hub de categoría  ┐
    amarres-de-amor/index.html       Servicio          │ 5 categorías,
    …                                (rutas absolutas)  │ 24 servicios
  tarot-y-videncia/ …                                   │ en total
  limpiezas-y-proteccion/ …                             │
  rituales-y-trabajos/ …                                │
  prosperidad-y-abundancia/ …        ┘
  privacidad/  terminos/  aviso-legal/   Legales
  css/
    styles.css     entry (importa los tokens)
    colors.css     tokens de color (violeta + dorado)   ← ver DESIGN.md
    typography.css escala tipográfica (Manrope + DM Sans)
    layout.css     spacing, radius, sombras, motion, z-index
    base.css       defaults de elementos
    fonts.css      @import de Google Fonts
    home.css       estilos que cargan TODAS las páginas
    internal.css   estilos SÓLO de páginas de servicio y categoría
  js/
    data.js        árbol de páginas, servicios, routing del derivador, testimonios
    background.js  canvas animado de fondo
    app.js         header, menú, reveal, derivador, tracking WhatsApp + línea de cupo semanal
    consent.js     gate de edad (18+) + cookies, Consent Mode v2
  assets/          retratos de marca, fotos de servicios, imágenes, videos, favicon
  robots.txt       permite todo + saluda a bots de LLMs; apunta al sitemap
  sitemap.xml      las 33 URLs
```

## SEO / agéntico

- Cada página: `<title>`, `description`, canonical, Open Graph, favicon `✦`.
- **JSON-LD** en las 33 páginas (ProfessionalService + WebSite; Service + FAQPage +
  BreadcrumbList en servicios).
- `robots.txt` habilita crawlers de buscadores y de LLMs (GPTBot, ClaudeBot,
  PerplexityBot, etc.) y referencia `sitemap.xml`.

## Analytics / consentimiento

- **Consent Mode v2** default `denied` (inline en `<head>`, antes de GTM).
- **GA4** `G-07W3W3044B` + **GTM** `GTM-TLMXCT79`. El GA4 se puede gestionar desde GTM.
- `consent.js`: modal de mayoría de edad + cookies; al aceptar, actualiza el consent.
- Evento de conversión: `whatsapp_click` (dataLayer) con `wa_source`. Es evento
  clave en GA4 y se importa como conversión en Google Ads (`AW-18226437188`).

## Deploy (GitHub Pages, rama `gh-pages`)

Producción: **https://claradeoteiza.com/**. Se publica `site/` **tal cual** en la
raíz de la rama `gh-pages`, que además conserva `CNAME` (claradeoteiza.com) y
`.nojekyll`. Push de `gh-pages` = sitio online en ~1 minuto.

## Config

- WhatsApp `5491136746858` · IG `@ritualesdeamoreterno.ok` · TikTok `@claradeoteiza`.
- Para self-hostear fuentes: reemplazar el `@import` de `css/fonts.css` por `@font-face`.
