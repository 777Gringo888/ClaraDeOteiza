# Clara de Oteiza — claradeoteiza.com

Sitio de servicios espirituales de **Clara de Oteiza**, Maestra de Alta Magia
(amarres, tarot y videncia, limpiezas y protección, rituales y anti-brujería,
prosperidad y abundancia). **Conversión principal: WhatsApp.**

Sitio estático (HTML + CSS + JS vanilla, **sin build**), optimizado mobile-first
(≈80% del tráfico) y con un fuerte trabajo de **CRO** (conversion rate
optimization).

## Estado: ✅ terminado y online en https://claradeoteiza.com/

- **33 páginas**: home + 5 hubs de categoría + 24 páginas de servicio + 3 legales
  (privacidad, términos, aviso legal).
- Versión vigente: **v2.0 "consulta personalizada"** (tags `v2.0-consulta-personalizada*`).
- Versión anterior restaurable: **v1.0 "consulta gratis"** (tags `v1.0-consulta-gratis*`).

## Estructura del repo

```
site/                     ← EL SITIO (fuente de verdad). Empezá por site/README.md
  index.html              Home
  amarres/ …              5 hubs de categoría, cada uno con sus servicios
  tarot-y-videncia/ …
  limpiezas-y-proteccion/ …
  rituales-y-trabajos/ …
  prosperidad-y-abundancia/ …
  privacidad/ terminos/ aviso-legal/   Legales
  css/  js/  assets/       Estilos, comportamiento y multimedia
  robots.txt  sitemap.xml  favicon → SEO / crawl
  README.md                Cómo correr, editar y desplegar
  css/  js/  assets/       (detallado en site/README.md)
CLAUDE.md                 Brief operativo (Claude Code lo lee solo) — leer para retomar
DESIGN.md                 Sistema de diseño + patrones CRO (leer antes de tocar UI)
scripts/build_ghpages.py  Deploy viejo al preview en subpath (ya no se usa)

gen_*.py, icon_lib.py     ⚠️ Andamiaje de UNA sola vez (ver nota abajo)
design_handoff_velas_animadas/   Referencia de diseño (efecto de velas), ya implementado
```

## Cómo ver el sitio localmente

Las páginas internas usan rutas absolutas (`/css/…`, `/amarres/…`), así que
**necesitás un servidor** (no alcanza el doble-click):

```bash
cd site
python3 -m http.server 8000
# abrí http://localhost:8000/
```

## Deploy

El sitio se publica en la rama **`gh-pages`** (GitHub Pages), en la raíz de
claradeoteiza.com.
Detalle del flujo de deploy en `site/README.md`.

## ⚠️ Sobre los generadores (`gen_*.py`, `icon_lib.py`)

Fueron **andamiaje de una sola vez** para crear las 24 páginas de servicio a
partir de un molde. **Desde entonces el HTML se editó a mano** (CRO, copys,
urgencia, etc.), así que **el HTML de `site/` es la fuente de verdad** y
**los generadores NO deben volver a correrse** (pisarían los ajustes hechos a
mano). Se conservan sólo como referencia histórica.

## Datos del proyecto

- **WhatsApp:** `5491136746858` (en todos los CTAs).
- **TikTok:** `@claradeoteiza` (+25.000).
- **Analytics:** GTM `GTM-TLMXCT79` + GA4 `G-07W3W3044B` (Consent Mode v2).
- **Copy prohibido:** "garantizado", "100% efectivo", plazos fijos ("48 horas"),
  "doblegar", "dominar", "paga al ver resultados", "irrompible".
