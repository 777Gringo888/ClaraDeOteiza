# DESIGN.md — Sistema de diseño de Clara de Oteiza

Guía del sistema visual y de los patrones de conversión (CRO). Leé esto **antes de
tocar la UI** para mantener todo coherente. Los tokens viven en `site/css/`.

---

## 1. Identidad

Marca **oscura, mística, candlelit**: fondo violeta-negro, acento **azul-violeta**
(matchea los videos de velas) y **dorado** cálido para detalle y jerarquía. El dark
mode **es** la identidad (no hay light mode). Texto siempre en **crema cálida** para
contraste WCAG-AA.

Sensación: seria, íntima, confiable. Nada estridente. El dorado se usa con criterio
(destaques, acentos), no en bloques grandes.

---

## 2. Color (`site/css/colors.css`)

### Fondos (violeta-negro)
`--ink-950 #080610` · `--ink-900 #100B1C` · `--ink-850 #170F28` ·
`--ink-800 #1E1434` · `--ink-750 #261942` · `--ink-700 #33245A`
Base semántica: `--bg-base #0A0714`.

### Acento primario — azul-violeta
> ⚠️ Nombres legacy: los tokens `--wine-*` y `--red-*` **contienen violeta** (la
> paleta se movió del vino original al azul-violeta). No los renombres a ciegas.

`--red-500 #6E34CE` (violeta firma) · `--red-400 #8A54E0` · `--red-600 #5A2AB0` ·
`--ember-500 #A06BF0` (highlight) · `--wine-900 #241046` · `--wine-700 #44208A`.

### Acento secundario — dorado
`--gold-500 #CFA24A` (firma) · `--gold-400 #E1BE6C` · `--gold-300 #F1D896`
(texto dorado sobre oscuro) · `--gold-200 #F8E9BE` · `--gold-600 #B08838`.

**Uso del dorado (importante para contraste):** destaques fuertes con `--gold-500`
(rico/oscuro, contrasta mejor sobre fondo claro de video); texto dorado sobre oscuro
`--gold-300`; respuestas de FAQ `--gold-200`. El "beige" claro **no** se usa para
texto porque no contrasta.

### Texto (crema)
`--text-heading` (cream-50) · `--text-body` (cream-100) · `--text-muted` (cream-200) ·
`--text-faint` (cream-300) · `--text-on-gold` (ink-950, para botones dorados).

### Bordes y utilitarios
`--border-hairline` (dorado tenue) · `--border-gold` · `--whatsapp #25D366` ·
`--focus-ring #E1BE6C`.

---

## 3. Tipografía (`site/css/typography.css`)

- **Display / títulos:** Manrope (700–800). **Cuerpo / UI:** DM Sans.
  (Vía Google Fonts en `fonts.css`; se pueden self-hostear con `@font-face`.)
- Escala fluida (clamp): `--fs-display` (3–5rem) · `--fs-h1` (2.5–3.5) ·
  `--fs-h2` (2–2.6) · `--fs-h3` (1.55–1.85) · `--fs-lead` (1.2–1.375) ·
  `--fs-body 1.0625rem` · `--fs-eyebrow .8125rem`.
- **`.gold-accent`** dorada dentro de títulos para resaltar la palabra clave.
- **Eyebrow**: `.sec-head__eyebrow` con `✦` dorado + mayúsculas espaciadas.

---

## 4. Layout

- `.container` centrado con max-width. Secciones con ritmo vertical
  `clamp(3rem, 6.5vw, 5rem)`.
- Grid/flex con `gap` (no márgenes por-elemento). Mobile-first: todo apila y crece
  en pantalla chica.
- **`.sec-head`** = eyebrow + título + lead (centrado). `.sec-head--left` lo alinea
  a la izquierda (se usa en páginas internas; en la home casi todo va centrado).

---

## 5. Botones

- **Verde WhatsApp** `.wa-btn` (`--sm`, `--lg`, `--full`, `--floating`): la CTA
  principal. Es la acción de conversión → usar con equilibrio, no en todos lados.
- **Dorado** `.btn-gold`: CTA secundaria (ej. "Contame tu caso" en Sobre mí).
  Diferencia visualmente de la conversión de WhatsApp.
- **Chips** `.chip` (derivador): violeta translúcido, borde violeta.
- Regla de equilibrio: pocos verdes por vista. Las tarjetas/filas enrutan con
  enlaces de texto ("Conocer más →"), no con un botón verde cada una.

---

## 6. El "molde" de página de servicio

Orden canónico (ver `site/rituales-y-trabajos/te-hicieron-un-trabajo/` como
referencia; es el prototipo del molde):

1. **Header** (nav 5 categorías + CTA).
2. **Videostage**: breadcrumb + hero de servicio (badge `✦`, H1 con `.gold-accent`,
   subtítulo, lead, CTA WhatsApp, **píldora de urgencia** `.cdo-urgency`, figura de Clara).
3. **Barra de beneficios** `.cdo-benefits` (4; la última es cupos/semana).
4. **Prueba social** `.cdo-socialproof` (IG +123.000 · TikTok +25.000).
5. **¿Qué es?** — eyebrow + `.cdo-servicedesc` (imagen + texto) + **párrafo de poder**
   `.cdo-affirm` (destaque con borde dorado, voz de Clara afirmando capacidad).
6. **¿Cuándo puede ayudarte?** — `.cdo-signals` (6 tarjetas con íconos) + `.cdo-microcta`.
7. **¿Cómo trabajo?** `.cdo-author-block` (retrato grande + método + CTA).
8. **Relacionados** · **Testimonios** · **FAQ** · **CTA central** · disclaimer ·
   footer · WhatsApp flotante.

Las **categorías** (`amarres/`, etc.) siguen el mismo sistema visual: hero de
servicio, prueba social, píldora de urgencia, grilla de tarjetas `.cdo-card`
(violeta), presentación de Clara con `.cdo-affirm`, FAQ y CTA final con urgencia.

---

## 7. Patrones de conversión (CRO)

- **Derivador** (home): chips + texto libre → clasifica contra el árbol de páginas
  (`CDO.classify` en `data.js`) y sugiere la más específica. Debajo, un bloque fijo
  explica "te atiende Clara en persona · cupos limitados" + botón.
- **Urgencia = escasez del beneficio gratis:** el mensaje unificado es
  **"las consultas gratis tienen cupos limitados por semana"**. Aparece en la píldora
  del hero, la barra de beneficios, el microcta, el derivador, el CTA final y la
  burbuja flotante. **El hero de la home va limpio** (sin urgencia): la urgencia
  aparece cuando la persona ya se está decidiendo.
- **Mensaje de WhatsApp:** instrucción clara + **un solo** código de reserva
  (lo arma `app.js`). Ver regla 3 en `CLAUDE.md`.
- **Prueba social real:** IG +123.000 · TikTok +25.000 (números confirmados).

---

## 8. Movimiento y accesibilidad

- Fondos de video (`motion-bg.mp4` hero/derivador, `cta-candles.mp4` CTA central)
  con crossfade entre dos copias para ocultar el salto; pausan fuera de pantalla.
- Reveal on scroll con `.cdo-reveal`. Todo respeta `prefers-reduced-motion`.
- Contraste WCAG-AA. Foco visible (`--focus-ring`). El texto sobre video lleva
  scrim + `text-shadow` (se validó sobre el peor caso: frame claro del video).

---

## 9. Al agregar/editar páginas

- Respetá el molde (sección 6) y las rutas absolutas de páginas internas.
- Incluí SIEMPRE los snippets de `<head>` (Consent Mode + GA4 + GTM), favicon,
  JSON-LD, y los `<script>` del final. Sumá la URL al `sitemap.xml`.
- Adaptá el copy al servicio (voz de Clara, porteño) y respetá el copy prohibido.
- Verificá el balance de tags y probá con servidor local antes de desplegar.
