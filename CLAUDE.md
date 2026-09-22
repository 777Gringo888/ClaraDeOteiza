# CLAUDE.md — Clara de Oteiza (claradeoteiza.com)

Brief operativo para retomar el trabajo. Para el sistema visual leé **`DESIGN.md`**;
para correr/desplegar, **`site/README.md`**.

## Qué es

Sitio estático de servicios espirituales de **Clara de Oteiza**, Maestra de Alta
Magia. **Sin build** (HTML + CSS + JS vanilla). **Mobile-first** (~80% del
tráfico). **La conversión es siempre WhatsApp.** Marca oscura, mística,
**violeta + dorado** (candlelit). Voz de Clara en **primera persona**, tono
**porteño**, cálido y serio.

Estado: **terminado y online** en https://claradeoteiza.com/. 33 páginas (home +
5 categorías + 24 servicios + 3 legales). GitHub Pages, rama `gh-pages`.
Versión vigente: **v2.0 "consulta personalizada"** (22/09/2026). La consulta con
Clara **se cobra**: el sitio no menciona nada gratis.

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

Deploy: el contenido de `site/` se copia **tal cual** a la raíz de la rama
`gh-pages`, conservando `CNAME` (claradeoteiza.com) y `.nojekyll`. Commit + push de
`gh-pages` = producción. `scripts/build_ghpages.py` era para el preview en subpath
y **ya no se usa**.

Versiones: antes de cada paquete de cambios se crea un tag por versión
(`vX.Y-nombre` sobre `gh-pages` y `vX.Y-nombre-fuente` sobre `main`) para poder
restaurar.

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
2. **Nada gratis.** La consulta se cobra: no usar "gratis", "gratuita" ni "sin
   costo" en ningún texto, mensaje, meta o schema. "Sin compromiso" solo en las FAQs.
3. **Mensaje de WhatsApp:** `Hola Clara, quiero reservar una consulta sobre <tema>.`
   (en `data-wa-msg` y en el `href`). `app.js` le agrega una sola vez la línea
   `Te escribo para entrar en el cupo de consultas de esta semana.` Sin códigos de
   reserva. El evento `whatsapp_click` (dataLayer) se dispara igual en cada click.
4. **Urgencia = cupos:** Clara atiende pocas consultas por semana ("Pocos cupos por
   semana", "Atiendo pocas consultas por semana"). El hero de la home va limpio; la
   urgencia vive en el derivador, la barra de beneficios, la píldora de
   servicios/categoría, el CTA final y la burbuja flotante.

## Copy / voz

- Primera persona (Clara), porteño, cálido y honesto. Nunca prometer resultados.
- **Prohibido:** "garantizado", "100% efectivo", plazos fijos ("48 horas"),
  "doblegar", "dominar", "paga al ver resultados", "irrompible".
- **Magia blanca** siempre (no causa daño). Números reales: TikTok +25.000.

## Datos

- WhatsApp `5491136746858` · TikTok `@claradeoteiza`.
- Dominio: **claradeoteiza.com** (registrado en Squarespace).

## Pendientes

Ninguno. DNS conectado y `whatsapp_click` marcado como evento clave en GA4.
