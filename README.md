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
    app.js         header, menú, reveal, derivador, tracking WhatsApp + código de reserva
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
- Evento de conversión: `whatsapp_click` (dataLayer) con `wa_source` + `wa_code`.
  **Pendiente:** marcarlo como evento clave en GA4 (desde GTM/GA4).

## Deploy (GitHub Pages, rama `gh-pages`)

**Preview (subpath, hoy):** las rutas absolutas necesitan el prefijo del subpath.

```bash
python3 scripts/build_ghpages.py        # genera /tmp/ghpages-build con rutas /ClaraDeOteiza
# publicar esa carpeta en la rama gh-pages (worktree o gh-pages deploy)
```

**Dominio propio (claradeoteiza.com, al conectar DNS):** ya no hace falta reescribir
rutas — se publica `site/` **tal cual** en la rama `gh-pages` + un archivo **`CNAME`**
con `claradeoteiza.com`. Ver pendientes de DNS en `../CLAUDE.md`.

## Config

- WhatsApp `5491136746858` · TikTok `@claradeoteiza`.
- Para self-hostear fuentes: reemplazar el `@import` de `css/fonts.css` por `@font-face`.
