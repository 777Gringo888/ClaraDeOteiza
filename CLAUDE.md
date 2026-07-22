# CLAUDE.md — Clara de Oteiza (claradeoteiza.com)

Brief operativo para retomar el trabajo. Para el sistema visual leé **`DESIGN.md`**;
para correr/desplegar, **`site/README.md`**.

## Qué es

Sitio estático de servicios espirituales de **Clara de Oteiza**, Maestra de Alta
Magia. **Sin build** (HTML + CSS + JS vanilla). **Mobile-first** (~80% del
tráfico). **La conversión es siempre WhatsApp.** Marca oscura, mística,
**violeta + dorado** (candlelit). Voz de Clara en **primera persona**, tono
**porteño**, cálido y serio.

Estado: **terminado**. 33 páginas (home + 5 categorías + 24 servicios + 3 legales).
Vive en GitHub Pages (rama `gh-pages`). Pendiente: **DNS** del dominio y marcar la
conversión `whatsapp_click` en GA4.

## Fuente de verdad ⚠️

- **El HTML de `site/` es la fuente de verdad.** Se editó a mano después de
  generarse.
- Los `gen_*.py` / `icon_lib.py` de la raíz fueron **andamiaje de una sola vez**.
  **NO los vuelvas a correr**: pisarían los ajustes hechos a mano.

## Cómo correr / desplegar

```bash
cd site && python3 -m http.server 8000     # http://localhost:8000/
```
Las páginas internas usan **rutas absolutas** → hace falta servidor (no doble-click).

Deploy: se publica la carpeta `site/` en la rama `gh-pages`. Ver `site/README.md`.
Hoy sirve en subpath de preview (`/ClaraDeOteiza/`) vía `scripts/build_ghpages.py`;
al conectar el dominio, se sirve `site/` tal cual en la raíz + archivo `CNAME`.

## Arquitectura

- **Rutas:** la **home** usa rutas relativas (`css/…`, `assets/…`); **todas las
  páginas internas** usan rutas **absolutas** (`/css/…`, `/amarres/…`).
- **CSS** (en `site/css/`): `styles.css` es el entry (importa los tokens
  `colors/typography/layout/base/fonts`). `home.css` lo cargan **todas** las
  páginas. `internal.css` lo cargan **sólo** las páginas de servicio y categoría.
- **JS** (en `site/js/`): `data.js` (datos + derivador), `background.js` (canvas de
  fondo), `app.js` (interacciones + derivador + tracking de WhatsApp),
  `consent.js` (gate de edad + cookies, Consent Mode v2).

## Reglas que NO se rompen

1. **En cada página nueva** deben ir, en el `<head>`: Consent Mode v2 + GA4
   (`G-07W3W3044B`) + GTM (`GTM-TLMXCT79`), el `<noscript>` de GTM tras `<body>`,
   el favicon, el JSON-LD, y `<link>` a `styles.css` + `home.css` (+ `internal.css`
   si es servicio/categoría). Cargá al final del body: `data.js`, `background.js`,
   `app.js`, `consent.js`.
2. **Deploy al preview:** `scripts/build_ghpages.py` reescribe rutas con el prefijo
   `/ClaraDeOteiza`. Por eso **evitá literales `"/"` sueltos en JS** (los mangla).
   En `app.js`, el prefijo de categoría se busca con `path.indexOf(k)` sin `/` inicial.
3. **Un solo código** en el mensaje de WhatsApp. Lo arma `app.js` (IIFE de reserva):
   `Mi código de reserva de consulta gratis es #<CAT>-<rnd>. Envío este mensaje para
   entrar en el cupo de consultas de esta semana.` El evento `whatsapp_click`
   (dataLayer, para GTM/GA4) **lee ese mismo código** — no inyectar un segundo.
4. **Urgencia:** el mensaje es **"las consultas gratis tienen cupos limitados por
   semana"** (lo escaso es el beneficio gratis). No poner urgencia de "semana" en el
   hero de la home (va limpio); la urgencia vive en el derivador, la barra de
   beneficios, la píldora de servicios/categoría, el CTA final y la burbuja flotante.

## Copy / voz

- Primera persona (Clara), porteño, cálido y honesto. Nunca prometer resultados.
- **Prohibido:** "garantizado", "100% efectivo", plazos fijos ("48 horas"),
  "doblegar", "dominar", "paga al ver resultados", "irrompible".
- **Magia blanca** siempre (no causa daño). Números reales: TikTok +25.000.

## Datos

- WhatsApp `5491136746858` · TikTok `@claradeoteiza`.
- Dominio: **claradeoteiza.com** (registrado en Squarespace).

## Pendientes

1. **DNS** → apuntar claradeoteiza.com a GitHub Pages (registros A + CNAME `www`) y
   dar vuelta el deploy a la raíz + `CNAME`.
2. **GA4** → marcar `whatsapp_click` como evento clave (conversión) desde GTM/GA4.
