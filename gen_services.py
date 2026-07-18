import re, os, urllib.parse

SITE = "/home/claude/repo/site"
TPL = open(os.path.join(SITE, "amarres/amarres-de-amor/index.html")).read()

GENERIC_COMO = ("Antes de encender una sola vela, te escucho. En nuestra primera charla por WhatsApp me "
  "contás qué te está pasando y cómo es tu situación. Con esa información leo la energía y te digo con "
  "honestidad si este trabajo es el camino, o si primero conviene otro.")
GENERIC_COMO2 = "Recién ahí armo un ritual pensado especialmente para tu caso, y te acompaño en cada paso."
GENERIC_ESP = ("No trabajo con plazos exactos ni prometo resultados asegurados: cada persona y cada situación "
  "es distinta. Lo que sí puedo ofrecerte es dedicación, seriedad y acompañamiento real en cada paso del proceso.")
GENERIC_ESP2 = ("Muchas de las personas que trabajaron conmigo empezaron a notar cambios que parecían imposibles. "
  "Cada proceso es único, y por eso lo importante es que primero conversemos tu caso.")

FAQ = ('<div class="cdo-faq__list">\n'
  '          <details class="cdo-faq__item"><summary>¿Los trabajos son magia negra?</summary>'
  '<p>No. Todo lo que realizo es de <strong>magia blanca</strong> y no causa daño a ninguna persona. Trabajo siempre desde el respeto y el bienestar.</p></details>\n'
  '          <details class="cdo-faq__item"><summary>¿Es confidencial?</summary>'
  '<p>Sí, totalmente. Cada consulta es privada y queda entre vos y yo.</p></details>\n'
  '          <details class="cdo-faq__item"><summary>¿Tengo que ir presencialmente?</summary>'
  '<p>No hace falta. Podemos hacer todo a distancia. Me escribís por WhatsApp y coordinamos desde ahí.</p></details>\n'
  '          <details class="cdo-faq__item"><summary>¿Cómo es la primera consulta?</summary>'
  '<p>Es gratuita y sin compromiso. Me escribís, me contás qué te pasa y vemos juntos cómo puedo ayudarte, sin apuros.</p></details>\n'
  '        </div>')

WA_OLD = "quiero una consulta sobre amarres de amor"

def img_hero(f, alt): return f'<img src="/assets/brand/{f}" alt="{alt}" loading="eager" width="340" height="425" />'
def img_qs(f, alt): return f'<img src="/assets/brand/{f}" alt="{alt}" loading="lazy" width="240" height="300" />'

def related_html(items):
    return ('<div class="cdo-related__grid">\n          '
      + "\n          ".join(f'<a class="cdo-related__card" href="{h}">{l} <span aria-hidden="true">&#8594;</span></a>' for h,l in items)
      + '\n        </div>')

def content_html(s):
    sig = "\n            ".join(f"<li>{x}</li>" for x in s["signals"])
    return (f'<h2>{s["ques_h2"]}</h2>\n'
      f'          <figure class="cdo-figure">\n'
      f'            <img src="{s["fig"]}" alt="{s["fig_alt"]}" loading="lazy" width="800" height="800" />\n'
      f'            <figcaption>{s["fig_cap"]}</figcaption>\n'
      f'          </figure>\n'
      f'          <p>{s["p1"]}</p>\n'
      f'          <p>{s["p2"]}</p>\n\n'
      f'          <h2>¿Cuándo puede <span class="gold-accent">ayudarte</span>?</h2>\n'
      f'          <p>{s["cuando"]}</p>\n'
      f'          <ul class="cdo-signals">\n            {sig}\n          </ul>\n\n'
      f'          <h2>Cómo trabajo yo</h2>\n'
      f'          <p>{GENERIC_COMO}</p>\n          <p>{GENERIC_COMO2}</p>\n\n'
      f'          <h2>Qué podés esperar</h2>\n'
      f'          <p>{GENERIC_ESP}</p>\n          <p>{GENERIC_ESP2}</p>\n\n          ')

def build(s):
    h = TPL
    h = re.sub(r'<title>.*?</title>', lambda m: f'<title>{s["title"]} | Clara de Oteiza — Maestra de Alta Magia</title>', h, count=1)
    h = re.sub(r'<meta name="description" content=".*?" />', lambda m: f'<meta name="description" content="{s["meta"]}" />', h, count=1)
    h = re.sub(r'<link rel="canonical" href=".*?" />', lambda m: f'<link rel="canonical" href="https://claradeoteiza.com{s["slug"]}" />', h, count=1)
    h = re.sub(r'<meta property="og:title" content=".*?" />', lambda m: f'<meta property="og:title" content="{s["title"]} | Clara de Oteiza" />', h, count=1)
    h = re.sub(r'<meta property="og:description" content=".*?" />', lambda m: f'<meta property="og:description" content="{s["og"]}" />', h, count=1)
    h = h.replace('<li class="cdo-breadcrumb__current" aria-current="page">Amarres de Amor</li>',
                  f'<li class="cdo-breadcrumb__current" aria-current="page">{s["title"]}</li>')
    h = h.replace('<h1>Amarres de Amor</h1>', f'<h1>{s["h1"]}</h1>')
    h = re.sub(r'<p class="cdo-hero-servicio__sub">.*?</p>', lambda m: f'<p class="cdo-hero-servicio__sub">{s["sub"]}</p>', h, count=1)
    h = re.sub(r'<p class="cdo-hero-servicio__lead">.*?</p>', lambda m: f'<p class="cdo-hero-servicio__lead">{s["lead"]}</p>', h, count=1)
    h = re.sub(r'<img src="/assets/brand/[^"]*" alt="[^"]*" loading="eager" width="340" height="425" />', lambda m: img_hero(s["hero"], "Clara de Oteiza, Maestra de Alta Magia"), h, count=1)
    h = re.sub(r'<img src="/assets/brand/[^"]*" alt="[^"]*" loading="lazy" width="240" height="300" />', lambda m: img_qs(s["qs"], "Clara de Oteiza en su altar"), h, count=1)
    # content article (from ¿Qué es hasta antes del prose__cta)
    h = re.sub(r'<h2>¿Qué es un amarre de amor\?.*?(?=<div class="cdo-prose__cta">)', lambda m: content_html(s), h, count=1, flags=re.S)
    # related grid
    h = re.sub(r'<div class="cdo-related__grid">.*?</div>', lambda m: related_html(s["related"]), h, count=1, flags=re.S)
    # FAQ
    h = re.sub(r'<div class="cdo-faq__list">.*?</div>', lambda m: FAQ, h, count=1, flags=re.S)
    # cta central h2
    h = h.replace('<h2>Tu historia de amor <span class="gold-accent">merece una oportunidad.</span></h2>', f'<h2>{s["cta_h2"]}</h2>')
    # WhatsApp
    h = h.replace(WA_OLD, s["wa"])
    h = h.replace(urllib.parse.quote(WA_OLD), urllib.parse.quote(s["wa"]))
    out = os.path.join(SITE, s["slug"].strip("/"), "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write(h)
    print("escrito", s["slug"])

# ---- Amor y Amarres: 7 servicios ----
AMOR = [
  {"slug":"/amarres/retorno-de-pareja/","title":"Retorno de pareja","wa":"quiero una consulta sobre retorno de pareja",
   "meta":"Retorno de pareja con Clara de Oteiza: trabajo de magia blanca para que quien se fue vuelva a buscarte. Primera consulta gratuita por WhatsApp.",
   "og":"Trabajo de magia blanca para reabrir el camino de vuelta de quien se alejó. Primera consulta gratuita por WhatsApp.",
   "h1":"Retorno de pareja","sub":"Para que quien se fue vuelva a <span class=\"gold-accent\">pensarte, buscarte y elegirte</span>.",
   "lead":"Si tu pareja se fue y sentís que esa historia todavía no terminó, te acompaño con un trabajo de magia blanca para reabrir el camino de vuelta, con respeto y cariño. La primera consulta es gratuita.",
   "hero":"clara-tarot-2.jpg","qs":"clara-ritual-vela-roja.jpg","fig":"/assets/services/card-retorno.jpg",
   "fig_alt":"Ritual de retorno de pareja en el altar de Clara","fig_cap":"Cada retorno se trabaja en el altar, según lo que pasó en tu vínculo.",
   "ques_h2":"¿Qué es el retorno de pareja?",
   "p1":"El retorno de pareja es un trabajo de <strong>magia blanca</strong> pensado para reconectar el vínculo con alguien que se alejó o se fue. No se trata de forzar a nadie: se trata de despejar lo que se interpuso, ya sea una pelea, la distancia, el orgullo o un tercero, para que el amor que existía pueda volver a encontrar su lugar.",
   "p2":"Cada separación tiene su historia. Por eso, antes de cualquier trabajo, escucho la tuya y la leo con honestidad.",
   "cuando":"Este trabajo suele acompañar cuando:",
   "signals":["Tu pareja se fue y no lográs volver a acercarte.","Terminaron en medio de una pelea o un malentendido.","Apareció un tercero o la distancia enfrió todo.","Sentís que fue una decisión del momento, no del corazón.","Querés que te vuelva a buscar y a elegir."],
   "cta_h2":"Esa historia <span class=\"gold-accent\">todavía puede continuar.</span>"},

  {"slug":"/amarres/reconciliacion-de-pareja/","title":"Reconciliación de pareja","wa":"quiero una consulta sobre reconciliación de pareja",
   "meta":"Reconciliación de pareja con Clara de Oteiza: trabajo de magia blanca para sanar la relación después de una pelea o separación. Primera consulta gratuita.",
   "og":"Trabajo de magia blanca para sanar la relación y volver a estar bien. Primera consulta gratuita por WhatsApp.",
   "h1":"Reconciliación de pareja","sub":"Para <span class=\"gold-accent\">sanar la relación</span> después de una pelea o una separación.",
   "lead":"Cuando una pelea o una distancia dejó heridas, el vínculo se puede sanar. Te acompaño con un trabajo de magia blanca para volver a acercarlos con calma y cariño. La primera consulta es gratuita.",
   "hero":"clara-3.jpg","qs":"clara-ritual-vela-pareja.jpg","fig":"/assets/services/card-reconciliacion.jpg",
   "fig_alt":"Ritual de reconciliación de pareja","fig_cap":"El altar se prepara según lo que necesita tu relación.",
   "ques_h2":"¿Qué es la reconciliación de pareja?",
   "p1":"La reconciliación es un trabajo de <strong>magia blanca</strong> para sanar un vínculo lastimado por peleas, malentendidos o una separación reciente. Busca bajar el enojo, abrir el diálogo y devolverle al amor el espacio que la discusión le quitó.",
   "p2":"No hay dos parejas iguales. Escucho tu caso y trabajo a partir de lo que a ustedes realmente les pasó.",
   "cuando":"Este trabajo suele acompañar cuando:",
   "signals":["Vienen de una pelea fuerte y no logran volver a hablar.","Se dijeron cosas que dejaron heridas.","El orgullo no deja que ninguno dé el primer paso.","Se separaron hace poco y los dos siguen dolidos.","Querés recuperar la calma y el cariño que había."],
   "cta_h2":"Todavía están <span class=\"gold-accent\">a tiempo de sanar.</span>"},

  {"slug":"/amarres/endulzamiento/","title":"Endulzamiento","wa":"quiero una consulta sobre endulzamiento",
   "meta":"Endulzamiento con Clara de Oteiza: trabajo de magia blanca para que esa persona te trate con más cariño y dulzura. Primera consulta gratuita por WhatsApp.",
   "og":"Trabajo de magia blanca para endulzar el trato y traer más cariño a tu vínculo. Primera consulta gratuita.",
   "h1":"Endulzamiento","sub":"Para que esa persona te trate con más <span class=\"gold-accent\">cariño, dulzura y atención</span>.",
   "lead":"Cuando el trato se puso áspero o distante, un endulzamiento puede devolverle suavidad al vínculo. Te acompaño con un trabajo de magia blanca, con respeto. La primera consulta es gratuita.",
   "hero":"clara-4.jpg","qs":"clara-ritual-vela-rosa.jpg","fig":"/assets/services/card-endulzamiento.jpg",
   "fig_alt":"Ritual de endulzamiento en el altar","fig_cap":"El endulzamiento se prepara con elementos elegidos para tu caso.",
   "ques_h2":"¿Qué es un endulzamiento?",
   "p1":"El endulzamiento es un trabajo de <strong>magia blanca</strong> que busca suavizar el trato de una persona hacia vos: menos distancia, menos aspereza, más cariño y atención. Ayuda a que el vínculo vuelva a sentirse cálido.",
   "p2":"Cada relación tiene su tono. Escucho el tuyo y armo el trabajo a tu medida.",
   "cuando":"Este trabajo suele acompañar cuando:",
   "signals":["Sentís a esa persona fría, cortante o indiferente.","El trato se volvió tenso y perdió la dulzura.","Querés que te preste más atención y te trate mejor.","Notás que el cariño está, pero no se expresa.","Buscás reavivar la ternura del día a día."],
   "cta_h2":"Devolvele <span class=\"gold-accent\">dulzura a tu vínculo.</span>"},

  {"slug":"/amarres/union-y-matrimonio/","title":"Unión y matrimonio","wa":"quiero una consulta sobre unión y matrimonio",
   "meta":"Unión y matrimonio con Clara de Oteiza: trabajo de magia blanca para afianzar el compromiso y dar el próximo paso juntos. Primera consulta gratuita por WhatsApp.",
   "og":"Trabajo de magia blanca para afianzar el compromiso y la unión de la pareja. Primera consulta gratuita.",
   "h1":"Unión y matrimonio","sub":"Para <span class=\"gold-accent\">afianzar el compromiso</span> y dar juntos el próximo paso.",
   "lead":"Cuando querés consolidar la relación y que dé el próximo paso, hay trabajos que acompañan esa decisión. Te ayudo con magia blanca, desde el respeto. La primera consulta es gratuita.",
   "hero":"clara-ritual-vela-pareja.jpg","qs":"clara-tarot-hero.jpg","fig":"/assets/services/card-union.jpg",
   "fig_alt":"Ritual de unión de pareja","fig_cap":"La unión se trabaja en el altar con la vela de pareja.",
   "ques_h2":"¿Qué es un trabajo de unión?",
   "p1":"El trabajo de unión es un ritual de <strong>magia blanca</strong> para afianzar el compromiso de la pareja y acompañar el deseo de formalizar, convivir o casarse. Busca fortalecer el lazo y despejar las dudas y miedos que frenan el próximo paso.",
   "p2":"Cada pareja tiene su ritmo. Escucho tu situación y trabajo a partir de lo que ustedes necesitan.",
   "cuando":"Este trabajo suele acompañar cuando:",
   "signals":["Querés que la relación se formalice o dé un paso más.","Sentís miedo o dudas que frenan el compromiso.","Buscás consolidar la convivencia o el casamiento.","Hay amor, pero falta la decisión de avanzar.","Querés reforzar el lazo para el largo plazo."],
   "cta_h2":"Es momento de <span class=\"gold-accent\">dar el próximo paso.</span>"},

  {"slug":"/amarres/amarres-de-amor-eterno/","title":"Amarres de amor eterno","wa":"quiero una consulta sobre amarres de amor eterno",
   "meta":"Amarres de amor eterno con Clara de Oteiza: trabajo de magia blanca para un amor duradero que se afiance en el tiempo. Primera consulta gratuita por WhatsApp.",
   "og":"Trabajo de magia blanca para un amor que perdure y se afiance en el tiempo. Primera consulta gratuita.",
   "h1":"Amarres de amor eterno","sub":"Para un amor que <span class=\"gold-accent\">se afiance en el tiempo</span> y perdure con fuerza.",
   "lead":"Cuando querés que el amor no solo vuelva, sino que se quede y se fortalezca, el amarre de amor eterno acompaña esa intención. Trabajo de magia blanca, con respeto. La primera consulta es gratuita.",
   "hero":"clara-ritual-vela-roja.jpg","qs":"clara-3.jpg","fig":"/assets/services/card-eterno.jpg",
   "fig_alt":"Ritual de amarre de amor eterno","fig_cap":"El trabajo se prepara para acompañar un vínculo duradero.",
   "ques_h2":"¿Qué es un amarre de amor eterno?",
   "p1":"El amarre de amor eterno es un trabajo de <strong>magia blanca</strong> orientado a un vínculo duradero: no solo reconectar, sino afianzar el amor para que perdure y se fortalezca con el tiempo. Trabaja la profundidad y la estabilidad del lazo.",
   "p2":"Cada historia es distinta. Escucho la tuya y armo el trabajo pensando en el largo plazo.",
   "cuando":"Este trabajo suele acompañar cuando:",
   "signals":["Querés un amor estable y para toda la vida.","Sentís que el vínculo es fuerte pero querés protegerlo.","Buscás profundidad y compromiso duradero.","Temés que el tiempo o la rutina desgasten la relación.","Querés afianzar lo que ya reconectaste."],
   "cta_h2":"Un amor <span class=\"gold-accent\">para toda la vida.</span>"},

  {"slug":"/amarres/alejamiento-de-terceros-y-amantes/","title":"Alejamiento de terceros y amantes","wa":"quiero una consulta sobre alejamiento de terceros y amantes",
   "meta":"Alejamiento de terceros y amantes con Clara de Oteiza: trabajo de magia blanca para sacar del medio a quien se metió en tu pareja. Primera consulta gratuita por WhatsApp.",
   "og":"Trabajo de magia blanca para alejar a esa tercera persona que interfiere en tu vínculo. Primera consulta gratuita.",
   "h1":"Alejamiento de terceros y amantes","sub":"Para <span class=\"gold-accent\">sacar del medio</span> a quien se metió en tu pareja.",
   "lead":"Cuando una tercera persona interfiere en tu vínculo, se puede trabajar para alejarla y devolverle claridad a la relación. Trabajo de magia blanca, con respeto. La primera consulta es gratuita.",
   "hero":"clara-tarot-hero.jpg","qs":"clara-4.jpg","fig":"/assets/services/card-alejamiento.jpg",
   "fig_alt":"Ritual de alejamiento de terceros","fig_cap":"El trabajo de alejamiento se prepara según tu situación.",
   "ques_h2":"¿Qué es el alejamiento de terceros?",
   "p1":"El alejamiento de terceros es un trabajo de <strong>magia blanca</strong> para apartar la influencia de una tercera persona, ya sea un amante o alguien que interfiere, que está desestabilizando tu vínculo, y devolverle claridad y espacio a tu relación.",
   "p2":"Cada caso es distinto. Escucho el tuyo y trabajo con respeto, sin dañar a nadie.",
   "cuando":"Este trabajo suele acompañar cuando:",
   "signals":["Apareció alguien que se metió entre vos y tu pareja.","Sentís que un tercero está desestabilizando la relación.","Sospechás de un amante o una tercera persona.","Querés recuperar el espacio y la claridad del vínculo.","Necesitás sacar del medio esa interferencia."],
   "cta_h2":"Recuperá <span class=\"gold-accent\">el espacio de tu vínculo.</span>"},

  {"slug":"/amarres/amarre-pasional/","title":"Amarre pasional","wa":"quiero una consulta sobre amarre pasional",
   "meta":"Amarre pasional con Clara de Oteiza: trabajo de magia blanca para reavivar el deseo y la pasión que se apagó. Primera consulta gratuita por WhatsApp.",
   "og":"Trabajo de magia blanca para reavivar el deseo y la pasión en tu vínculo. Primera consulta gratuita.",
   "h1":"Amarre pasional","sub":"Para <span class=\"gold-accent\">reavivar el deseo y la pasión</span> que se apagó.",
   "lead":"Cuando la pasión se enfrió y el deseo dejó de estar, se puede trabajar para reavivar esa chispa. Trabajo de magia blanca, con respeto. La primera consulta es gratuita.",
   "hero":"clara-ritual-vela-rosa.jpg","qs":"clara-tarot-2.jpg","fig":"/assets/services/card-pasional.jpg",
   "fig_alt":"Ritual de amarre pasional","fig_cap":"El amarre pasional se trabaja con velas y elementos para tu caso.",
   "ques_h2":"¿Qué es un amarre pasional?",
   "p1":"El amarre pasional es un trabajo de <strong>magia blanca</strong> orientado a reavivar el deseo y la atracción física entre dos personas, cuando la pasión se enfrió o se apagó con el tiempo. Busca devolverle fuego e intensidad al vínculo.",
   "p2":"Cada pareja tiene su historia. Escucho la tuya y armo el trabajo a tu medida.",
   "cuando":"Este trabajo suele acompañar cuando:",
   "signals":["Sentís que la pasión y el deseo se apagaron.","La rutina enfrió la intimidad de la pareja.","Querés recuperar la atracción que había al principio.","Notás distancia física con tu pareja.","Buscás reavivar el fuego del vínculo."],
   "cta_h2":"Volvé a encender <span class=\"gold-accent\">esa chispa.</span>"},
]

# related = los otros servicios de amor (hasta 6)
LABELS = {x["slug"]: x["title"] for x in AMOR}
LABELS["/amarres/amarres-de-amor/"] = "Amarres de amor"
ALL_AMOR = ["/amarres/amarres-de-amor/"] + [x["slug"] for x in AMOR]
for s in AMOR:
    rel = [sl for sl in ALL_AMOR if sl != s["slug"]][:6]
    s["related"] = [(sl, LABELS[sl]) for sl in rel]
    s["cat"] = "amarres"

if __name__ == "__main__":
    for s in AMOR:
        build(s)
    print("OK amor:", len(AMOR))
