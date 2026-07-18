# -*- coding: utf-8 -*-
"""Replicación del molde CRO (prototipo te-hicieron-un-trabajo) a las 23 páginas
   restantes. Reutiliza datos de gen_services (AMOR) + gen_services2 (SERVICES),
   la librería de íconos, y agrega el párrafo de poder por servicio."""
import re, os, sys, urllib.parse
sys.path.insert(0, "/tmp")
from gen_services import AMOR
from gen_services2 import SERVICES
from icon_lib import signal_li

SITE = "/home/claude/clara-gh/site"
TPL = open(os.path.join(SITE, "rituales-y-trabajos/te-hicieron-un-trabajo/index.html"), encoding="utf-8").read()

CAT_INFO = {
  "amarres": {"eyebrow": "Amor y amarres", "crumb": "Amor y Amarres", "testi": "Historias de amor que volvieron"},
  "tarot-y-videncia": {"eyebrow": "Tarot y videncia", "crumb": "Tarot y Videncia", "testi": "Consultas que dieron claridad"},
  "limpiezas-y-proteccion": {"eyebrow": "Limpiezas y protección", "crumb": "Limpiezas y Protección", "testi": "Historias de quienes recuperaron su paz"},
  "prosperidad-y-abundancia": {"eyebrow": "Prosperidad y abundancia", "crumb": "Prosperidad y Abundancia", "testi": "Historias de abundancia que llegaron"},
  "rituales-y-trabajos": {"eyebrow": "Rituales y anti-brujería", "crumb": "Rituales, Trabajos y Anti-brujería", "testi": "Historias de quienes se liberaron"},
}

AFFIRM = {
  "/amarres/amarres-de-amor/": "El amor no siempre se pierde: muchas veces solo se traba. Con más de veinte años acompañando a personas que ya habían perdido la esperanza, sé cómo reabrir ese camino y devolverle su lugar al sentimiento.",
  "/amarres/retorno-de-pareja/": "Vi volver a personas que juraban que ya no había nada que hacer. Cuando el vínculo todavía respira, sé exactamente cómo reabrir el camino de vuelta.",
  "/amarres/reconciliacion-de-pareja/": "Ninguna pelea es tan grande como para no poder sanarse cuando las dos partes todavía se aman. Con más de veinte años, sé cómo bajar el enojo y devolverles el diálogo.",
  "/amarres/endulzamiento/": "El trato más frío puede volver a ser cálido. Sé cómo devolverle dulzura a un vínculo que se puso áspero, con trabajos serios y pensados a tu medida.",
  "/amarres/union-y-matrimonio/": "Cuando el amor está pero falta el paso, sé cómo despejar los miedos que lo frenan. Acompañé a muchas parejas a formalizar lo que tanto querían.",
  "/amarres/amarres-de-amor-eterno/": "Un amor fuerte también se cuida. Sé cómo afianzar un vínculo para que perdure en el tiempo, con la seriedad de más de veinte años de trabajo.",
  "/amarres/alejamiento-de-terceros-y-amantes/": "Ninguna tercera persona es más fuerte que un vínculo verdadero bien defendido. Sé cómo apartar esa interferencia y devolverle claridad a tu relación.",
  "/amarres/amarre-pasional/": "La pasión que se apagó se puede volver a encender. Sé cómo reavivar el deseo y la atracción, con trabajos pensados solo para tu caso.",
  "/tarot-y-videncia/lectura-de-tarot/": "Las cartas no mienten, y yo no te digo lo que querés escuchar sino lo que veo. Más de veinte años leyendo me enseñaron a darte claridad real, sin vueltas.",
  "/tarot-y-videncia/tarot-del-amor/": "En el amor, ver claro lo cambia todo. Sé leer lo que esa persona siente y hacia dónde va el vínculo, para que decidas con el corazón pero sin ceguera.",
  "/tarot-y-videncia/videncia/": "Percibo lo que a simple vista no se ve. Más de veinte años afinando esta capacidad me permiten darte una mirada profunda y honesta de tu momento.",
  "/tarot-y-videncia/orientacion-espiritual/": "Nadie tiene que atravesar los momentos difíciles en soledad. Sé acompañar desde la escucha y la experiencia para que vuelvas a encontrar tu fuerza.",
  "/limpiezas-y-proteccion/limpieza-energetica/": "La energía pesada se puede sacar, por más pegada que la sientas. Sé cómo liberarte de eso que no es tuyo y devolverte la liviandad.",
  "/limpiezas-y-proteccion/armonizacion/": "La paz interior no es un lujo, es tu derecho. Sé cómo reequilibrar tu energía para que vuelvas a sentirte en tu centro.",
  "/limpiezas-y-proteccion/proteccion/": "Ninguna envidia ni mala intención tiene que poder con vos. Sé cómo blindar tu energía y la de los tuyos, con la fuerza de más de veinte años de trabajo.",
  "/limpiezas-y-proteccion/apertura-de-caminos/": "Cuando todo se traba, casi siempre hay algo para destrabar. Sé cómo mover esa energía estancada para que las puertas vuelvan a abrirse.",
  "/prosperidad-y-abundancia/prosperidad/": "La abundancia también se trabaja. Sé cómo mover la energía del dinero para que el esfuerzo que ponés por fin empiece a rendir.",
  "/prosperidad-y-abundancia/desbloqueo-laboral/": "Cuando el trabajo no llega por más que lo intentás, casi siempre hay un bloqueo detrás. Sé cómo destrabarlo para que las oportunidades vuelvan a aparecer.",
  "/prosperidad-y-abundancia/suerte-en-el-juego/": "La suerte también se puede alinear a tu favor. Sé cómo mover esa energía para que la racha en contra empiece a cambiar.",
  "/rituales-y-trabajos/corte-de-danos/": "No hay daño tan fuerte que no se pueda cortar. Con más de veinte años y miles de casos, sé exactamente cómo romper lo que te hicieron y devolverte la paz.",
  "/rituales-y-trabajos/contra-hechizos/": "Ningún hechizo es más fuerte que un buen trabajo de magia blanca. Sé cómo neutralizar lo que mandaron en tu contra y frenar sus efectos.",
  "/rituales-y-trabajos/desamarres/": "Toda atadura se puede cortar. Sé cómo liberarte de eso que te mantiene atada para que vuelvas a ser dueña de tu vida.",
  "/rituales-y-trabajos/rituales/": "No hay caso imposible, solo casos que necesitan el trabajo justo. Con más de veinte años, sé armar el ritual exacto que tu situación pide.",
}

# amarres-de-amor no está en AMOR ni SERVICES: lo definimos
AMARRES_DE_AMOR = {
  "cat": "amarres", "slug": "/amarres/amarres-de-amor/", "title": "Amarres de amor",
  "wa": "quiero una consulta sobre amarres de amor",
  "meta": "Amarres de amor de magia blanca con Clara de Oteiza: para reconectar el vínculo cuando la persona que amás se alejó. Primera consulta gratuita por WhatsApp.",
  "og": "Trabajo de magia blanca para reavivar el amor y reconectar el vínculo. Primera consulta gratuita.",
  "h1": "Amarres de amor",
  "sub": "Para que quien amás <span class=\"gold-accent\">vuelva a pensarte, buscarte y elegirte</span>.",
  "lead": "Cuando el amor se enfrió o esa persona se alejó, un amarre de amor ayuda a reabrir el vínculo con respeto y cariño. La primera consulta es gratuita.",
  "hero": "clara-tarot-hero.jpg", "qs": "clara-ritual-vela-pareja.jpg",
  "fig": "/assets/services/amarre-de-amor.jpg", "fig_alt": "Altar de amarre de amor con velas en forma de corazón",
  "ques_h2": "¿Qué es un amarre de amor?",
  "p1": "Un amarre de amor es un trabajo de <strong>magia blanca</strong> que busca reconectar a dos personas que ya tuvieron un lazo afectivo. No se trata de forzar la voluntad de nadie: se trata de despejar lo que se interpuso, como la distancia, los malentendidos o una tercera persona, para que el sentimiento que ya existía pueda volver a fluir.",
  "p2": "Cada historia es única, y por eso no hay dos amarres iguales: cada trabajo se piensa a partir de lo que a vos te está pasando.",
  "signals": ["Tu pareja se alejó sin una explicación clara.", "Sentís que el amor se enfrió y perdió la chispa.", "Apareció una tercera persona que desestabilizó el vínculo.", "Se separaron, pero sentís que esa historia no terminó.", "Querés que esa persona vuelva a pensarte y a elegirte."],
  "cta_h2": "Tu historia de amor <span class=\"gold-accent\">merece una oportunidad.</span>",
}

# related de amarres-de-amor: otros de amor
AMOR_SLUGS = ["/amarres/retorno-de-pareja/", "/amarres/reconciliacion-de-pareja/", "/amarres/endulzamiento/", "/amarres/union-y-matrimonio/", "/amarres/amarres-de-amor-eterno/", "/amarres/alejamiento-de-terceros-y-amantes/"]
AMOR_LABELS = {"/amarres/retorno-de-pareja/": "Retorno de pareja", "/amarres/reconciliacion-de-pareja/": "Reconciliación de pareja", "/amarres/endulzamiento/": "Endulzamiento", "/amarres/union-y-matrimonio/": "Unión y matrimonio", "/amarres/amarres-de-amor-eterno/": "Amarres de amor eterno", "/amarres/alejamiento-de-terceros-y-amantes/": "Alejamiento de terceros y amantes"}
AMARRES_DE_AMOR["related"] = [(sl, AMOR_LABELS[sl]) for sl in AMOR_SLUGS]

SIXTH_SIGNAL = "Querés resolverlo y volver a estar bien."

def accent_ques(q):
    m = re.match(r'(¿Qué es (?:un[ao]?|el|la|los|las) )(.+?)(\?)$', q)
    if m: return m.group(1) + '<span class="gold-accent">' + m.group(2) + '</span>' + m.group(3)
    m = re.match(r'(¿Qué son (?:los|las) )(.+?)(\?)$', q)
    if m: return m.group(1) + '<span class="gold-accent">' + m.group(2) + '</span>' + m.group(3)
    m = re.match(r'(¿Qué es (?:un )?trabajo de )(.+?)(\?)$', q)
    if m: return m.group(1) + '<span class="gold-accent">' + m.group(2) + '</span>' + m.group(3)
    return q

# ---- textos WhatsApp del prototipo (a reemplazar) ----
WA_PROTO = [
  "Hola Clara, quiero asegurar mi consulta gratuita. Creo que me hicieron un trabajo.",
  "Hola Clara, me identifico con varias señales y quiero asegurar mi consulta gratuita.",
]

def build(s):
    h = TPL
    slug = s["slug"]; cat = s["cat"]; ci = CAT_INFO[cat]
    title = s["title"]
    # --- head ---
    h = re.sub(r'<title>.*?</title>', lambda m: f'<title>{title} | Clara de Oteiza — Maestra de Alta Magia</title>', h, count=1)
    h = re.sub(r'<meta name="description" content=".*?" />', lambda m: f'<meta name="description" content="{s["meta"]}" />', h, count=1)
    h = re.sub(r'<link rel="canonical" href=".*?" />', lambda m: f'<link rel="canonical" href="https://claradeoteiza.com{slug}" />', h, count=1)
    h = re.sub(r'<meta property="og:title" content=".*?" />', lambda m: f'<meta property="og:title" content="{title} | Clara de Oteiza" />', h, count=1)
    h = re.sub(r'<meta property="og:description" content=".*?" />', lambda m: f'<meta property="og:description" content="{s["og"]}" />', h, count=1)
    # --- breadcrumb ---
    h = h.replace('<li><a href="/rituales-y-trabajos/">Rituales, Trabajos y Anti-brujería</a></li>',
                  f'<li><a href="/{cat}/">{ci["crumb"]}</a></li>')
    h = h.replace('<li class="cdo-breadcrumb__current" aria-current="page">¿Te hicieron un trabajo?</li>',
                  f'<li class="cdo-breadcrumb__current" aria-current="page">{title}</li>')
    # --- hero ---
    h = h.replace('<h1>¿Te hicieron un trabajo?</h1>', f'<h1>{s["h1"]}</h1>')
    h = re.sub(r'<p class="cdo-hero-servicio__sub">.*?</p>', lambda m: f'<p class="cdo-hero-servicio__sub">{s["sub"]}</p>', h, count=1, flags=re.S)
    h = re.sub(r'<p class="cdo-hero-servicio__lead">.*?</p>', lambda m: f'<p class="cdo-hero-servicio__lead">{s["lead"]}</p>', h, count=1, flags=re.S)
    h = h.replace('src="/assets/brand/clara-ritual-vela-roja.jpg" alt="Clara de Oteiza, Maestra de Alta Magia" loading="eager"',
                  f'src="/assets/brand/{s["hero"]}" alt="Clara de Oteiza, Maestra de Alta Magia" loading="eager"')
    # --- ¿Qué es? block (entre comentarios) ---
    signals = list(s["signals"]) + [SIXTH_SIGNAL]
    lis = "\n          ".join(signal_li(x) for x in signals)
    que_es = (
      '<!-- ¿Qué es? -->\n'
      '        <header class="sec-head sec-head--left cdo-reveal">\n'
      f'          <span class="sec-head__eyebrow"><span class="star" aria-hidden="true">✦</span>{ci["eyebrow"]}</span>\n'
      f'          <h2 class="sec-head__title">{accent_ques(s["ques_h2"])}</h2>\n'
      '        </header>\n'
      '        <div class="cdo-servicedesc cdo-reveal">\n'
      '          <figure class="cdo-servicedesc__media">\n'
      f'            <img src="{s["fig"]}" alt="{s["fig_alt"]}" loading="lazy" width="800" height="800" />\n'
      '          </figure>\n'
      '          <div class="cdo-servicedesc__text">\n'
      f'            <p>{s["p1"]}</p>\n'
      f'            <p>{s["p2"]}</p>\n'
      f'            <p class="cdo-affirm">{AFFIRM[slug]}</p>\n'
      '          </div>\n'
      '        </div>\n\n'
      '        ')
    cuando = (
      '<!-- ¿Cuándo puede ayudarte? -->\n'
      '        <header class="sec-head sec-head--left cdo-reveal cdo-content__sub">\n'
      '          <span class="sec-head__eyebrow"><span class="star" aria-hidden="true">✦</span>Señales</span>\n'
      '          <h2 class="sec-head__title">¿Cuándo puede <span class="gold-accent">ayudarte</span>?</h2>\n'
      '          <p class="sec-head__lead">Suele acompañar cuando te pasa alguna de estas cosas:</p>\n'
      '        </header>\n'
      f'        <ul class="cdo-signals cdo-reveal">\n          {lis}\n        </ul>\n\n'
      '        ')
    # reemplazar desde "<!-- ¿Qué es? -->" hasta antes de "<div class=\"cdo-microcta"
    h = re.sub(r'<!-- ¿Qué es\? -->.*?(?=<div class="cdo-microcta)', que_es + cuando, h, count=1, flags=re.S)
    # --- ¿Cómo trabajo?: foto qs ---
    h = h.replace('src="/assets/brand/clara-4.jpg" alt="Clara de Oteiza en su altar" loading="lazy" width="800" height="1000"',
                  f'src="/assets/brand/{s["qs"]}" alt="Clara de Oteiza en su altar" loading="lazy" width="800" height="1000"')
    # --- related ---
    rel = '<div class="cdo-related__grid">\n          ' + "\n          ".join(
        f'<a class="cdo-related__card" href="{sl}">{lb} <span aria-hidden="true">&#8594;</span></a>' for sl, lb in s["related"]) + '\n        </div>'
    h = re.sub(r'<div class="cdo-related__grid">.*?</div>\s*</div>\s*</section>', rel + '\n      </div>\n    </section>', h, count=1, flags=re.S)
    # --- testimonios heading ---
    h = h.replace('<h2 class="sec-head__title">Historias de quienes se liberaron</h2>',
                  f'<h2 class="sec-head__title">{ci["testi"]}</h2>')
    # --- CTA central h2 ---
    h = re.sub(r'<h2>Salí de la <span class="gold-accent">duda\.</span></h2>', lambda m: f'<h2>{s["cta_h2"]}</h2>', h, count=1)
    # --- WhatsApp: reemplazar los mensajes del prototipo por el del servicio ---
    msg = f'Hola Clara, {s["wa"]}. Quiero asegurar mi cupo para la consulta gratuita.'
    for proto in WA_PROTO:
        h = h.replace(proto, msg)
        h = h.replace(urllib.parse.quote(proto), urllib.parse.quote(msg))
    out = os.path.join(SITE, slug.strip("/"), "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(h)
    return slug

ALL = [AMARRES_DE_AMOR] + AMOR + [s for s in SERVICES if s["slug"] != "/rituales-y-trabajos/te-hicieron-un-trabajo/"]
done = [build(s) for s in ALL]
print("regeneradas:", len(done))
for d in done: print("  ", d)
