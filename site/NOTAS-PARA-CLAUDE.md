# Clara de Oteiza — Notas del proyecto (para retomar)

> Resumen de qué es esto, qué se hizo y **qué falta**. Pensado para que un
> Claude local (o cualquiera) retome el trabajo sin contexto previo.

## Qué es
Home page de **claradeoteiza.com** — sitio de servicios espirituales (amarres,
tarot, videncia, limpiezas, prosperidad, rituales). Conversión principal:
WhatsApp. Marca: oscura, mística, **violeta + dorado** (candlelit), voz de Clara
en **primera persona**.

## Cómo correr
- Ver: doble click en `site/index.html` (no necesita servidor).
- Editar: es HTML/CSS/JS plano, sin build. Archivos en `site/`:
  - `index.html` — la home
  - `css/` — `styles.css` (entry), tokens (`colors/typography/layout/base/fonts`), `home.css`
  - `js/` — `data.js` (derivador + datos), `background.js`, `app.js` (interacciones)
  - `assets/` — imágenes + videos (`motion-bg.mp4`, `cta-candles.mp4`)

## Qué está hecho ✅
- Home completa: header, hero, derivador, sobre, rituales, CTA, testimonios, instagram, footer, WhatsApp flotante.
- **Paleta azul-violácea** (se movió desde el vino/rojo original para matchear los videos).
- **Videos de fondo**: Hero+Derivador comparten uno (motion-bg) con separador; CTA central usa cta-candles. Loop con crossfade. Pausan fuera de pantalla. Respetan reduce-motion.
- **Derivador inteligente**: chips + texto libre que puntúa contra ~40 páginas del árbol y deriva a la más específica. Incluye infidelidad ("me engaña").
- **Rituales**: filas foto+texto alternadas; la foto es clickeable con **confirmación de 2 clicks** (toca → oscurece + "Conocer más" → segundo toque navega).
- **Sobre Clara** y derivador en **primera persona**.
- Mobile pulido: textos grandes, hero centrado, menú sólido, botones WhatsApp adaptados.
- Imágenes de marca optimizadas.

## Qué FALTA ⛔ (pendientes)
1. **Las 162 páginas internas** — el sitio es SOLO la home. Los links (`/amarres/`, `/tarot-y-videncia/`, `/privacidad/`, `/terminos/`, etc.) todavía no existen. Hay que crear las landings (el sitemap completo está en `chats/chat1.md`).
3. **Publicar online** — subir `site/` a un hosting (Netlify/Vercel/etc.) y conectar el dominio claradeoteiza.com.
4. **SEO por página** — la home tiene title/description/OG. Las 162 páginas necesitan su metadata propia.
5. **Legales** — redactar y crear /privacidad/, /terminos/, /aviso-legal/.
6. **Derivador — ampliar** — cubre las intenciones más comunes; se pueden sumar más palabras clave / páginas para casos puntuales (ver `PAGES` en `js/data.js`).
7. **Videos loop seamless** — el crossfade oculta el salto, pero lo ideal es reexportar los videos como loops perfectos.
8. **Fuentes** — hoy Manrope + DM Sans desde Google Fonts. Si quieren self-host, sumar los `@font-face` en `css/fonts.css`.
9. **Analytics / pixel** (Meta/Google) — si quieren medir conversiones, falta.

## Analytics / tags
- **Google Tag Manager** instalado como gestor central: contenedor **`GTM-TLMXCT79`**.
  - Script en `<head>` (arriba de todo) + `<noscript>` justo después de `<body>`.
  - GA4, píxel de Meta, conversiones, etc. se cargan DESDE GTM (no en el código).
  - ⚠️ **Cada página interna nueva debe incluir los mismos 2 snippets de GTM** (ver `index.html`, comentarios "Google Tag Manager").

## Datos del proyecto
- WhatsApp: `5491136746858` (en todos los CTAs).
- Instagram: `@ritualesdeamoreterno.ok` · TikTok: `@claradeoteiza`.
- Copy prohibido (NO usar): "garantizado", "100% efectivo", plazos fijos ("48 horas"), "doblegar", "dominar", "paga al ver resultados", "irrompible".
