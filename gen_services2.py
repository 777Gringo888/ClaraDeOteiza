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
AUTHOR_OLD = "<p>Hace más de veinte años acompaño a personas que atraviesan momentos difíciles en el amor. Me especializo en amarres, tarot, videncia natural y trabajos energéticos.</p>"
AUTHOR_NEW = "<p>Hace más de veinte años acompaño a personas que atraviesan momentos difíciles. Me especializo en amarres, tarot, videncia natural, limpiezas y trabajos energéticos.</p>"

# ----- category-level settings -----
CATS = {
  "tarot-y-videncia": {"label":"Tarot y Videncia", "related_h":"Otras consultas de tarot y videncia", "testi_h":"Consultas que dieron claridad"},
  "limpiezas-y-proteccion": {"label":"Limpiezas y Protección", "related_h":"Otros trabajos de limpieza y protección", "testi_h":"Historias de quienes recuperaron su paz"},
  "prosperidad-y-abundancia": {"label":"Prosperidad y Abundancia", "related_h":"Otros trabajos de prosperidad", "testi_h":"Historias de abundancia que llegaron"},
  "rituales-y-trabajos": {"label":"Rituales, Trabajos y Anti-brujería", "related_h":"Otros rituales y trabajos", "testi_h":"Historias de quienes se liberaron"},
}

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
    cat = s["cat"]; c = CATS[cat]
    h = TPL
    h = re.sub(r'<title>.*?</title>', lambda m: f'<title>{s["title"]} | Clara de Oteiza — Maestra de Alta Magia</title>', h, count=1)
    h = re.sub(r'<meta name="description" content=".*?" />', lambda m: f'<meta name="description" content="{s["meta"]}" />', h, count=1)
    h = re.sub(r'<link rel="canonical" href=".*?" />', lambda m: f'<link rel="canonical" href="https://claradeoteiza.com{s["slug"]}" />', h, count=1)
    h = re.sub(r'<meta property="og:title" content=".*?" />', lambda m: f'<meta property="og:title" content="{s["title"]} | Clara de Oteiza" />', h, count=1)
    h = re.sub(r'<meta property="og:description" content=".*?" />', lambda m: f'<meta property="og:description" content="{s["og"]}" />', h, count=1)
    # breadcrumb parent
    h = h.replace('<li><a href="/amarres/">Amarres</a></li>', f'<li><a href="/{cat}/">{c["label"]}</a></li>')
    h = h.replace('<li class="cdo-breadcrumb__current" aria-current="page">Amarres de Amor</li>',
                  f'<li class="cdo-breadcrumb__current" aria-current="page">{s["title"]}</li>')
    h = h.replace('<h1>Amarres de Amor</h1>', f'<h1>{s["h1"]}</h1>')
    h = re.sub(r'<p class="cdo-hero-servicio__sub">.*?</p>', lambda m: f'<p class="cdo-hero-servicio__sub">{s["sub"]}</p>', h, count=1)
    h = re.sub(r'<p class="cdo-hero-servicio__lead">.*?</p>', lambda m: f'<p class="cdo-hero-servicio__lead">{s["lead"]}</p>', h, count=1)
    h = re.sub(r'<img src="/assets/brand/[^"]*" alt="[^"]*" loading="eager" width="340" height="425" />', lambda m: img_hero(s["hero"], "Clara de Oteiza, Maestra de Alta Magia"), h, count=1)
    h = re.sub(r'<img src="/assets/brand/[^"]*" alt="[^"]*" loading="lazy" width="240" height="300" />', lambda m: img_qs(s["qs"], "Clara de Oteiza en su altar"), h, count=1)
    h = re.sub(r'<h2>¿Qué es un amarre de amor\?.*?(?=<div class="cdo-prose__cta">)', lambda m: content_html(s), h, count=1, flags=re.S)
    h = re.sub(r'<div class="cdo-related__grid">.*?</div>', lambda m: related_html(s["related"]), h, count=1, flags=re.S)
    h = re.sub(r'<div class="cdo-faq__list">.*?</div>', lambda m: FAQ, h, count=1, flags=re.S)
    h = h.replace('<h2>Tu historia de amor <span class="gold-accent">merece una oportunidad.</span></h2>', f'<h2>{s["cta_h2"]}</h2>')
    # category-level headings + author
    h = h.replace('<h2 class="sec-head__title">Otros caminos para el amor</h2>', f'<h2 class="sec-head__title">{c["related_h"]}</h2>')
    h = h.replace('<h2 class="sec-head__title">Historias de amor que volvieron</h2>', f'<h2 class="sec-head__title">{c["testi_h"]}</h2>')
    h = h.replace(AUTHOR_OLD, AUTHOR_NEW)
    # WhatsApp
    h = h.replace(WA_OLD, s["wa"])
    h = h.replace(urllib.parse.quote(WA_OLD), urllib.parse.quote(s["wa"]))
    out = os.path.join(SITE, s["slug"].strip("/"), "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write(h)
    print("escrito", s["slug"])

CUANDO = "Este trabajo suele acompañar cuando:"

SERVICES = [
  # ===================== TAROT Y VIDENCIA =====================
  {"cat":"tarot-y-videncia","slug":"/tarot-y-videncia/lectura-de-tarot/","title":"Lectura de tarot","wa":"quiero una lectura de tarot",
   "meta":"Lectura de tarot con Clara de Oteiza: una consulta clara y honesta para ver qué está pasando y qué camino tomar. Primera consulta gratuita por WhatsApp.",
   "og":"Una lectura honesta de las cartas para entender tu situación y decidir con claridad. Primera consulta gratuita.",
   "h1":"Lectura de tarot","sub":"Para ver con <span class=\"gold-accent\">claridad</span> qué está pasando y qué camino tomar.",
   "lead":"Cuando hay dudas que no te dejan tranquila, una lectura de tarot te ayuda a poner luz sobre tu situación y decidir con más calma. La primera consulta es gratuita.",
   "hero":"clara-tarot-hero.jpg","qs":"clara-tarot-2.jpg","fig":"/assets/services/card-lectura-tarot.jpg",
   "fig_alt":"Cartas de tarot sobre el altar de Clara","fig_cap":"Cada tirada se lee según lo que necesitás mirar.",
   "ques_h2":"¿Qué es una lectura de tarot?",
   "p1":"La lectura de tarot es una consulta en la que las cartas me ayudan a leer la energía de tu situación: lo que está pasando, lo que se mueve por debajo y los caminos que se abren. No es adivinar el futuro fijo, sino ver con más claridad para que vos puedas decidir mejor.",
   "p2":"Cada consulta es distinta. Me contás qué te preocupa y trabajamos sobre eso, con honestidad.",
   "cuando":CUANDO,
   "signals":["Estás en una decisión y no sabés qué camino tomar.","Sentís que algo no fluye y no entendés por qué.","Querés claridad sobre una relación, un trabajo o un cambio.","Necesitás una mirada honesta desde afuera.","Buscás calma para dejar de dar vueltas al mismo tema."],
   "cta_h2":"Poné <span class=\"gold-accent\">luz sobre tu situación.</span>"},

  {"cat":"tarot-y-videncia","slug":"/tarot-y-videncia/tarot-del-amor/","title":"Tarot del amor","wa":"quiero una consulta de tarot del amor",
   "meta":"Tarot del amor con Clara de Oteiza: una lectura enfocada en tu vida sentimental para entender qué pasa con esa persona. Primera consulta gratuita por WhatsApp.",
   "og":"Una lectura de cartas enfocada en el amor y tus vínculos. Primera consulta gratuita por WhatsApp.",
   "h1":"Tarot del amor","sub":"Para entender qué pasa en tu <span class=\"gold-accent\">corazón</span> y con esa persona.",
   "lead":"Cuando el amor te tiene con dudas, una lectura enfocada en lo sentimental te ayuda a ver qué está pasando de verdad. La primera consulta es gratuita.",
   "hero":"clara-tarot-2.jpg","qs":"clara-ritual-vela-rosa.jpg","fig":"/assets/services/card-tarot-amor.jpg",
   "fig_alt":"Lectura de tarot del amor en el altar","fig_cap":"Las cartas del amor se leen mirando tu vínculo puntual.",
   "ques_h2":"¿Qué es el tarot del amor?",
   "p1":"El tarot del amor es una lectura enfocada en tu vida sentimental: cómo está esa relación, qué siente la otra persona, qué se interpone y hacia dónde puede ir el vínculo. Sirve para entender antes de tomar una decisión del corazón.",
   "p2":"Cada historia de amor es única. Me contás la tuya y leemos las cartas sobre tu caso concreto.",
   "cuando":CUANDO,
   "signals":["No sabés qué siente realmente esa persona.","Estás dudando si seguir o soltar una relación.","Apareció alguien y querés saber si vale la pena.","Terminaron y necesitás claridad sobre qué pasó.","Querés entender el rumbo de tu vínculo."],
   "cta_h2":"Entendé qué pasa en <span class=\"gold-accent\">tu corazón.</span>"},

  {"cat":"tarot-y-videncia","slug":"/tarot-y-videncia/videncia/","title":"Videncia natural","wa":"quiero una consulta de videncia",
   "meta":"Videncia natural con Clara de Oteiza: una consulta desde la percepción para ver lo que no se ve a simple vista. Primera consulta gratuita por WhatsApp.",
   "og":"Una consulta de videncia natural para percibir lo que está más allá de lo evidente. Primera consulta gratuita.",
   "h1":"Videncia natural","sub":"Para percibir lo que <span class=\"gold-accent\">no se ve</span> a simple vista.",
   "lead":"Cuando sentís que hay algo más detrás de lo que estás viviendo, la videncia natural te ayuda a percibirlo y a entenderlo. La primera consulta es gratuita.",
   "hero":"clara-3.jpg","qs":"clara-tarot-hero.jpg","fig":"/assets/services/card-videncia.jpg",
   "fig_alt":"Clara de Oteiza en una consulta de videncia","fig_cap":"La videncia acompaña la lectura con lo que percibo de tu energía.",
   "ques_h2":"¿Qué es la videncia natural?",
   "p1":"La videncia natural es una capacidad de percibir lo que no está a la vista: energías, intenciones y situaciones que influyen en tu vida sin que las veas con claridad. La uso para acompañar la consulta y darte una mirada más profunda de lo que estás atravesando.",
   "p2":"Cada persona trae su propia energía. Te escucho y te comparto con honestidad lo que percibo.",
   "cuando":CUANDO,
   "signals":["Sentís que hay algo más detrás de lo que vivís.","Percibís malas energías a tu alrededor.","Querés entender una situación que no cierra.","Necesitás una mirada profunda sobre tu momento.","Buscás orientación desde la percepción, no solo la lógica."],
   "cta_h2":"Descubrí lo que <span class=\"gold-accent\">no se ve.</span>"},

  {"cat":"tarot-y-videncia","slug":"/tarot-y-videncia/orientacion-espiritual/","title":"Orientación espiritual","wa":"quiero una consulta de orientación espiritual",
   "meta":"Orientación espiritual con Clara de Oteiza: un acompañamiento para encontrar tu centro y el rumbo cuando estás perdida. Primera consulta gratuita por WhatsApp.",
   "og":"Un acompañamiento espiritual para reencontrar tu centro y tu rumbo. Primera consulta gratuita.",
   "h1":"Orientación espiritual","sub":"Para reencontrar tu <span class=\"gold-accent\">centro</span> y tu rumbo cuando estás perdida.",
   "lead":"Cuando te sentís perdida, sin fuerzas o sin saber para dónde ir, un acompañamiento espiritual te ayuda a volver a tu eje. La primera consulta es gratuita.",
   "hero":"clara-4.jpg","qs":"clara-3.jpg","fig":"/assets/services/card-orientacion.jpg",
   "fig_alt":"Espacio de orientación espiritual de Clara","fig_cap":"La orientación se adapta al momento que estás viviendo.",
   "ques_h2":"¿Qué es la orientación espiritual?",
   "p1":"La orientación espiritual es un acompañamiento para esos momentos en que te sentís perdida, sin rumbo o con el ánimo caído. No se trata de darte respuestas hechas, sino de ayudarte a reconectar con tu fuerza y ver con más claridad el paso que sigue.",
   "p2":"Cada momento de vida es distinto. Te escucho sin juzgar y te acompaño desde donde estás.",
   "cuando":CUANDO,
   "signals":["Te sentís perdida o sin rumbo.","Estás atravesando un duelo o un cambio grande.","Perdiste la fuerza y las ganas.","Necesitás alguien que te escuche sin juzgar.","Buscás reconectar con tu paz interior."],
   "cta_h2":"Volvé a <span class=\"gold-accent\">tu centro.</span>"},

  # ===================== LIMPIEZAS Y PROTECCIÓN =====================
  {"cat":"limpiezas-y-proteccion","slug":"/limpiezas-y-proteccion/limpieza-energetica/","title":"Limpieza energética","wa":"quiero una limpieza energética",
   "meta":"Limpieza energética con Clara de Oteiza: trabajo de magia blanca para sacarte de encima las malas energías y volver a sentirte liviana. Primera consulta gratuita.",
   "og":"Trabajo de magia blanca para liberar las malas energías y recuperar tu bienestar. Primera consulta gratuita.",
   "h1":"Limpieza energética","sub":"Para sacarte de encima las <span class=\"gold-accent\">malas energías</span> y volver a sentirte liviana.",
   "lead":"Cuando cargás con un peso que no es tuyo y todo se pone cuesta arriba, una limpieza energética te ayuda a soltar eso y volver a respirar. La primera consulta es gratuita.",
   "hero":"clara-ritual-vela-roja.jpg","qs":"clara-4.jpg","fig":"/assets/services/card-limpieza.jpg",
   "fig_alt":"Ritual de limpieza energética con velas","fig_cap":"La limpieza se prepara según lo que estés cargando.",
   "ques_h2":"¿Qué es una limpieza energética?",
   "p1":"La limpieza energética es un trabajo de <strong>magia blanca</strong> para liberar la energía pesada que se te fue pegando: envidias, malas vibras, ambientes cargados o rachas que no aflojan. Busca sacarte ese peso de encima y devolverte liviandad y claridad.",
   "p2":"Cada persona carga cosas distintas. Escucho tu caso y armo la limpieza a tu medida.",
   "cuando":CUANDO,
   "signals":["Sentís un cansancio o una pesadez que no se va.","Todo se te complica y nada fluye.","Notás malas energías en tu casa o tu entorno.","Andás de mal humor o angustiada sin razón clara.","Querés empezar una etapa nueva, liviana."],
   "cta_h2":"Volvé a <span class=\"gold-accent\">sentirte liviana.</span>"},

  {"cat":"limpiezas-y-proteccion","slug":"/limpiezas-y-proteccion/armonizacion/","title":"Armonización personal","wa":"quiero una armonización personal",
   "meta":"Armonización personal con Clara de Oteiza: trabajo de magia blanca para reequilibrar tu energía y recuperar la calma. Primera consulta gratuita por WhatsApp.",
   "og":"Trabajo de magia blanca para reequilibrar tu energía y recuperar la calma interior. Primera consulta gratuita.",
   "h1":"Armonización personal","sub":"Para reequilibrar tu energía y recuperar la <span class=\"gold-accent\">calma</span>.",
   "lead":"Cuando andás desbordada, ansiosa o sin paz, una armonización te ayuda a volver a tu equilibrio. La primera consulta es gratuita.",
   "hero":"clara-ritual-vela-rosa.jpg","qs":"clara-ritual-vela-roja.jpg","fig":"/assets/services/card-armonizacion.jpg",
   "fig_alt":"Ritual de armonización personal","fig_cap":"La armonización busca devolverte el equilibrio interior.",
   "ques_h2":"¿Qué es una armonización personal?",
   "p1":"La armonización personal es un trabajo de <strong>magia blanca</strong> que busca reequilibrar tu energía cuando sentís que perdiste la calma. Después de una limpieza, o en momentos de mucho estrés, ayuda a que vuelvas a tu centro y a sentirte en paz con vos misma.",
   "p2":"Cada persona necesita algo distinto para reencontrar su equilibrio. Te escucho y trabajo sobre eso.",
   "cuando":CUANDO,
   "signals":["Andás ansiosa, desbordada o sin paz.","Sentís que perdiste tu equilibrio.","Venís de una etapa de mucho estrés.","Querés reforzar tu energía después de una limpieza.","Buscás sentirte más tranquila y centrada."],
   "cta_h2":"Recuperá tu <span class=\"gold-accent\">equilibrio.</span>"},

  {"cat":"limpiezas-y-proteccion","slug":"/limpiezas-y-proteccion/proteccion/","title":"Protección energética","wa":"quiero un trabajo de protección energética",
   "meta":"Protección energética con Clara de Oteiza: trabajo de magia blanca para blindarte de envidias, malas energías y daños. Primera consulta gratuita por WhatsApp.",
   "og":"Trabajo de magia blanca para protegerte de envidias, malas energías y daños. Primera consulta gratuita.",
   "h1":"Protección energética","sub":"Para <span class=\"gold-accent\">blindarte</span> de envidias, malas energías y daños.",
   "lead":"Cuando sentís que algo o alguien te quiere hacer mal, un trabajo de protección te ayuda a blindar tu energía y la de los tuyos. La primera consulta es gratuita.",
   "hero":"clara-tarot-hero.jpg","qs":"clara-ritual-vela-rosa.jpg","fig":"/assets/imagery/altar-angeles.jpg",
   "fig_alt":"Altar de protección con velas","fig_cap":"La protección se arma como un escudo para vos y tu familia.",
   "ques_h2":"¿Qué es un trabajo de protección?",
   "p1":"La protección energética es un trabajo de <strong>magia blanca</strong> que actúa como un escudo: te resguarda de envidias, malas intenciones y energías que buscan hacerte daño. Es especialmente útil cuando sentís que alguien te tiene mala o que algo te está afectando.",
   "p2":"Cada situación necesita su resguardo. Escucho tu caso y armo la protección a tu medida.",
   "cuando":CUANDO,
   "signals":["Sentís que alguien te tiene envidia o mala.","Notás que te quieren hacer daño.","Después de una limpieza querés blindarte.","Querés proteger a tu familia o tu casa.","Buscás andar más tranquila y resguardada."],
   "cta_h2":"Andá por la vida <span class=\"gold-accent\">protegida.</span>"},

  {"cat":"limpiezas-y-proteccion","slug":"/limpiezas-y-proteccion/apertura-de-caminos/","title":"Apertura de caminos","wa":"quiero un trabajo de apertura de caminos",
   "meta":"Apertura de caminos con Clara de Oteiza: trabajo de magia blanca para destrabar lo que está frenado y que las cosas empiecen a fluir. Primera consulta gratuita.",
   "og":"Trabajo de magia blanca para destrabar lo que está frenado y abrir nuevas oportunidades. Primera consulta gratuita.",
   "h1":"Apertura de caminos","sub":"Para destrabar lo que está <span class=\"gold-accent\">frenado</span> y que todo empiece a fluir.",
   "lead":"Cuando sentís que todas las puertas se cierran y nada avanza, un trabajo de apertura de caminos ayuda a destrabar y volver a mover la energía. La primera consulta es gratuita.",
   "hero":"clara-4.jpg","qs":"clara-tarot-2.jpg","fig":"/assets/services/card-apertura.jpg",
   "fig_alt":"Ritual de apertura de caminos","fig_cap":"La apertura de caminos busca destrabar lo que está frenado.",
   "ques_h2":"¿Qué es la apertura de caminos?",
   "p1":"La apertura de caminos es un trabajo de <strong>magia blanca</strong> para esos momentos en que sentís que todo está trabado: no aparece el trabajo, no llega la plata, las oportunidades se caen. Busca destrabar esa energía estancada para que las puertas vuelvan a abrirse.",
   "p2":"Cada bloqueo tiene su raíz. Escucho tu situación y trabajo para destrabar lo que te frena.",
   "cuando":CUANDO,
   "signals":["Sentís que todas las puertas se te cierran.","Nada avanza por más que te esfuerces.","Se te caen las oportunidades una tras otra.","Estás en una racha que no afloja.","Querés que las cosas vuelvan a fluir."],
   "cta_h2":"Que se te <span class=\"gold-accent\">abran las puertas.</span>"},

  # ===================== PROSPERIDAD Y ABUNDANCIA =====================
  {"cat":"prosperidad-y-abundancia","slug":"/prosperidad-y-abundancia/prosperidad/","title":"Prosperidad y abundancia","wa":"quiero un trabajo de prosperidad y abundancia",
   "meta":"Prosperidad y abundancia con Clara de Oteiza: trabajo de magia blanca para atraer dinero, trabajo y oportunidades. Primera consulta gratuita por WhatsApp.",
   "og":"Trabajo de magia blanca para atraer prosperidad, dinero y nuevas oportunidades. Primera consulta gratuita.",
   "h1":"Prosperidad y abundancia","sub":"Para atraer <span class=\"gold-accent\">dinero, trabajo y oportunidades</span> a tu vida.",
   "lead":"Cuando la plata no alcanza y las oportunidades no llegan, un trabajo de prosperidad ayuda a mover esa energía y abrir la abundancia. La primera consulta es gratuita.",
   "hero":"clara-tarot-2.jpg","qs":"clara-3.jpg","fig":"/assets/services/card-prosperidad.jpg",
   "fig_alt":"Ritual de prosperidad y abundancia","fig_cap":"El trabajo de prosperidad se prepara según tu situación económica.",
   "ques_h2":"¿Qué es un trabajo de prosperidad?",
   "p1":"El trabajo de prosperidad y abundancia es un ritual de <strong>magia blanca</strong> pensado para atraer dinero, trabajo y oportunidades. Busca destrabar la energía económica cuando sentís que por más que te esforzás, la plata no rinde y las puertas no se abren.",
   "p2":"Cada economía tiene su historia. Escucho la tuya y armo el trabajo pensando en tu abundancia.",
   "cuando":CUANDO,
   "signals":["La plata no te alcanza por más que trabajes.","Sentís que la abundancia no llega a tu vida.","Querés atraer nuevas oportunidades de dinero.","Venís de una racha económica difícil.","Buscás estabilidad y prosperidad."],
   "cta_h2":"Abrí la puerta a la <span class=\"gold-accent\">abundancia.</span>"},

  {"cat":"prosperidad-y-abundancia","slug":"/prosperidad-y-abundancia/desbloqueo-laboral/","title":"Desbloqueo laboral y dinero","wa":"quiero un trabajo de desbloqueo laboral",
   "meta":"Desbloqueo laboral con Clara de Oteiza: trabajo de magia blanca para destrabar tu trabajo y tus ingresos cuando todo está frenado. Primera consulta gratuita.",
   "og":"Trabajo de magia blanca para destrabar tu trabajo y tus ingresos. Primera consulta gratuita por WhatsApp.",
   "h1":"Desbloqueo laboral y dinero","sub":"Para <span class=\"gold-accent\">destrabar</span> tu trabajo y tus ingresos.",
   "lead":"Cuando el trabajo no aparece o el dinero no fluye por más que lo intentás, un desbloqueo ayuda a mover esa energía frenada. La primera consulta es gratuita.",
   "hero":"clara-3.jpg","qs":"clara-tarot-2.jpg","fig":"/assets/services/card-trabajo.jpg",
   "fig_alt":"Ritual de desbloqueo laboral","fig_cap":"El desbloqueo se enfoca en lo que traba tu trabajo y tu dinero.",
   "ques_h2":"¿Qué es un desbloqueo laboral?",
   "p1":"El desbloqueo laboral y de dinero es un trabajo de <strong>magia blanca</strong> enfocado en destrabar lo que frena tu vida económica: la entrevista que no sale, el ascenso que no llega, el negocio que no arranca, los ingresos que no rinden. Busca abrir el camino para que el trabajo y la plata vuelvan a fluir.",
   "p2":"Cada bloqueo tiene su causa. Escucho tu situación laboral y trabajo sobre lo que te frena.",
   "cuando":CUANDO,
   "signals":["Buscás trabajo y nunca se concreta.","Tu negocio o emprendimiento no arranca.","Sentís que estás estancada en lo laboral.","El dinero entra pero no rinde.","Querés destrabar tu economía de una vez."],
   "cta_h2":"Destrabá <span class=\"gold-accent\">tu trabajo y tu dinero.</span>"},

  {"cat":"prosperidad-y-abundancia","slug":"/prosperidad-y-abundancia/suerte-en-el-juego/","title":"Suerte en el juego","wa":"quiero un trabajo para la suerte en el juego",
   "meta":"Suerte en el juego con Clara de Oteiza: trabajo de magia blanca para atraer la buena fortuna y cambiar tu racha. Primera consulta gratuita por WhatsApp.",
   "og":"Trabajo de magia blanca para atraer la buena suerte y cambiar tu racha. Primera consulta gratuita.",
   "h1":"Suerte en el juego","sub":"Para atraer la <span class=\"gold-accent\">buena fortuna</span> y cambiar tu racha.",
   "lead":"Cuando sentís que la suerte te da la espalda, un trabajo enfocado en la fortuna ayuda a mover esa energía a tu favor. La primera consulta es gratuita.",
   "hero":"clara-4.jpg","qs":"clara-tarot-hero.jpg","fig":"/assets/services/card-suerte.jpg",
   "fig_alt":"Ritual para la suerte y la fortuna","fig_cap":"El trabajo de suerte busca mover la fortuna a tu favor.",
   "ques_h2":"¿Qué es un trabajo de suerte?",
   "p1":"El trabajo de suerte en el juego es un ritual de <strong>magia blanca</strong> orientado a atraer la buena fortuna y cambiar una racha que viene en contra. Busca alinear la energía para que la suerte empiece a acompañarte.",
   "p2":"La suerte también se puede trabajar. Escucho tu caso y armo el ritual para atraerla.",
   "cuando":CUANDO,
   "signals":["Sentís que la suerte te da la espalda.","Venís de una racha en contra.","Querés atraer la buena fortuna.","Buscás un cambio en tu energía de suerte.","Necesitás que las cosas empiecen a salirte."],
   "cta_h2":"Que la suerte <span class=\"gold-accent\">te acompañe.</span>"},

  # ===================== RITUALES, TRABAJOS Y ANTI-BRUJERÍA =====================
  {"cat":"rituales-y-trabajos","slug":"/rituales-y-trabajos/te-hicieron-un-trabajo/","title":"¿Te hicieron un trabajo?","wa":"creo que me hicieron un trabajo y quiero una consulta",
   "meta":"¿Te hicieron un trabajo? Clara de Oteiza te ayuda a saberlo y a revertirlo con magia blanca. Primera consulta gratuita por WhatsApp.",
   "og":"Descubrí si te hicieron un trabajo y cómo revertirlo con magia blanca. Primera consulta gratuita.",
   "h1":"¿Te hicieron un trabajo?","sub":"Para <span class=\"gold-accent\">saberlo</span> y, si es así, revertirlo.",
   "lead":"Cuando de golpe todo se te complica sin explicación, puede que te hayan hecho un trabajo. Te ayudo a saberlo y a revertirlo con magia blanca. La primera consulta es gratuita.",
   "hero":"clara-ritual-vela-roja.jpg","qs":"clara-4.jpg","fig":"/assets/services/card-te-hicieron.jpg",
   "fig_alt":"Ritual para detectar y revertir un trabajo","fig_cap":"Primero leo tu energía para saber si hay un trabajo hecho.",
   "ques_h2":"¿Cómo saber si te hicieron un trabajo?",
   "p1":"A veces la vida se complica de golpe y sin explicación: se cae todo junto, aparecen peleas, enfermedades raras, mala suerte que no afloja. En algunos casos eso puede ser señal de un trabajo hecho en tu contra. Con una lectura leo tu energía y te digo con honestidad si hay algo, y qué se puede hacer.",
   "p2":"No todo es un trabajo, por eso primero miro con seriedad. Si lo hay, se puede revertir con magia blanca.",
   "cuando":CUANDO,
   "signals":["De golpe se te complicó todo, junto y sin razón.","Peleas, enfermedades o mala suerte que no aflojan.","Sentís un bloqueo que no tiene explicación.","Tenés la sensación de que alguien te quiere mal.","Querés saber con certeza qué te está pasando."],
   "cta_h2":"Salí de la <span class=\"gold-accent\">duda.</span>"},

  {"cat":"rituales-y-trabajos","slug":"/rituales-y-trabajos/corte-de-danos/","title":"Anti-brujería y corte de daños","wa":"quiero un trabajo de anti-brujería y corte de daños",
   "meta":"Anti-brujería y corte de daños con Clara de Oteiza: trabajo de magia blanca para cortar lo que te hicieron y sacarte el daño de encima. Primera consulta gratuita.",
   "og":"Trabajo de magia blanca para cortar la brujería y el daño que te hicieron. Primera consulta gratuita.",
   "h1":"Anti-brujería y corte de daños","sub":"Para <span class=\"gold-accent\">cortar</span> lo que te hicieron y sacarte el daño de encima.",
   "lead":"Cuando confirmaste que hay un daño hecho en tu contra, un trabajo de corte ayuda a romper eso y devolverte tu paz. La primera consulta es gratuita.",
   "hero":"clara-tarot-hero.jpg","qs":"clara-ritual-vela-roja.jpg","fig":"/assets/services/card-corte-danos.jpg",
   "fig_alt":"Ritual de corte de daños y anti-brujería","fig_cap":"El corte se trabaja para romper el daño y protegerte después.",
   "ques_h2":"¿Qué es un corte de daños?",
   "p1":"El corte de daños, o anti-brujería, es un trabajo de <strong>magia blanca</strong> para romper la energía negativa que alguien mandó en tu contra: un trabajo, una brujería, una mala intención pesada. Busca cortar ese daño de raíz y devolverte la tranquilidad.",
   "p2":"Cada daño es distinto. Primero confirmo qué hay, y después armo el corte para sacártelo de encima.",
   "cuando":CUANDO,
   "signals":["Confirmaste que te hicieron un trabajo.","Sentís un daño pesado que no se va.","Todo empeora desde un momento puntual.","Querés cortar de raíz lo que te hicieron.","Necesitás recuperar tu paz y protegerte."],
   "cta_h2":"Cortá el daño <span class=\"gold-accent\">de raíz.</span>"},

  {"cat":"rituales-y-trabajos","slug":"/rituales-y-trabajos/contra-hechizos/","title":"Contra hechizos","wa":"quiero un trabajo contra hechizos",
   "meta":"Contra hechizos con Clara de Oteiza: trabajo de magia blanca para devolver y neutralizar un hechizo hecho en tu contra. Primera consulta gratuita por WhatsApp.",
   "og":"Trabajo de magia blanca para neutralizar un hechizo hecho en tu contra. Primera consulta gratuita.",
   "h1":"Contra hechizos","sub":"Para <span class=\"gold-accent\">neutralizar</span> un hechizo hecho en tu contra.",
   "lead":"Cuando sentís el peso de un hechizo sobre vos o tu familia, un trabajo contra hechizos ayuda a neutralizarlo. La primera consulta es gratuita.",
   "hero":"clara-ritual-vela-rosa.jpg","qs":"clara-tarot-2.jpg","fig":"/assets/services/card-contra-hechizos.jpg",
   "fig_alt":"Ritual contra hechizos","fig_cap":"El trabajo busca neutralizar el hechizo y blindarte.",
   "ques_h2":"¿Qué es un trabajo contra hechizos?",
   "p1":"El trabajo contra hechizos es un ritual de <strong>magia blanca</strong> pensado para neutralizar un hechizo o maleficio hecho en tu contra. Busca desactivar esa energía negativa y frenar sus efectos sobre tu vida, tu salud o tu familia.",
   "p2":"Cada hechizo actúa distinto. Leo tu energía, confirmo qué hay y armo el trabajo para neutralizarlo.",
   "cuando":CUANDO,
   "signals":["Sentís el peso de un hechizo sobre vos.","Hay efectos raros que se repiten sin explicación.","Sospechás de una mala intención muy fuerte.","Querés neutralizar lo que te hicieron.","Buscás blindarte para que no vuelva a pasar."],
   "cta_h2":"Neutralizá lo que <span class=\"gold-accent\">te hicieron.</span>"},

  {"cat":"rituales-y-trabajos","slug":"/rituales-y-trabajos/desamarres/","title":"Desamarres","wa":"quiero un trabajo de desamarre",
   "meta":"Desamarres con Clara de Oteiza: trabajo de magia blanca para liberarte de una atadura o un amarre que no te deja avanzar. Primera consulta gratuita por WhatsApp.",
   "og":"Trabajo de magia blanca para liberarte de una atadura o amarre que te frena. Primera consulta gratuita.",
   "h1":"Desamarres","sub":"Para <span class=\"gold-accent\">liberarte</span> de una atadura que no te deja avanzar.",
   "lead":"Cuando sentís que estás atada a alguien o a algo que ya no te hace bien, un desamarre ayuda a cortar ese lazo y liberarte. La primera consulta es gratuita.",
   "hero":"clara-3.jpg","qs":"clara-ritual-vela-rosa.jpg","fig":"/assets/services/card-desamarres.jpg",
   "fig_alt":"Ritual de desamarre","fig_cap":"El desamarre corta el lazo que te mantiene atada.",
   "ques_h2":"¿Qué es un desamarre?",
   "p1":"El desamarre es un trabajo de <strong>magia blanca</strong> para cortar una atadura energética que te mantiene ligada a una persona o a una situación que ya no te hace bien. Sirve cuando sentís que no podés soltar, avanzar ni rehacer tu vida, como si algo te tuviera atada.",
   "p2":"Cada lazo se formó a su manera. Escucho tu caso y trabajo para liberarte con cuidado.",
   "cuando":CUANDO,
   "signals":["Sentís que no podés soltar a esa persona.","Hay una atadura que no te deja avanzar.","Querés cerrar un vínculo que te hace mal.","Sospechás que te hicieron un amarre.","Necesitás recuperar tu libertad y tu paz."],
   "cta_h2":"Liberate y <span class=\"gold-accent\">seguí tu camino.</span>"},

  {"cat":"rituales-y-trabajos","slug":"/rituales-y-trabajos/rituales/","title":"Rituales y trabajos","wa":"quiero una consulta sobre un ritual o trabajo",
   "meta":"Rituales y trabajos con Clara de Oteiza: rituales de magia blanca hechos a medida para tu situación puntual. Primera consulta gratuita por WhatsApp.",
   "og":"Rituales de magia blanca hechos a medida para lo que estés atravesando. Primera consulta gratuita.",
   "h1":"Rituales y trabajos","sub":"Rituales de magia blanca <span class=\"gold-accent\">hechos a medida</span> para tu caso.",
   "lead":"Cuando lo que te pasa no entra en una categoría fija, armamos un ritual pensado especialmente para tu situación. La primera consulta es gratuita.",
   "hero":"clara-ritual-vela-roja.jpg","qs":"clara-4.jpg","fig":"/assets/services/card-rituales.jpg",
   "fig_alt":"Altar con velas para un ritual a medida","fig_cap":"Cada ritual se arma según lo que necesitás.",
   "ques_h2":"¿Qué son los rituales y trabajos a medida?",
   "p1":"No todo lo que se vive entra en una etiqueta. Los rituales y trabajos a medida son ceremonias de <strong>magia blanca</strong> que armo especialmente para tu situación, combinando lo que hace falta según lo que estés atravesando. Primero escucho tu caso y después decidimos juntos el camino.",
   "p2":"Cada persona trae algo único. Por eso lo primero siempre es conversar y entender tu historia.",
   "cuando":CUANDO,
   "signals":["Lo que te pasa no entra en una categoría fija.","Necesitás un trabajo pensado para tu caso puntual.","Ya probaste otras cosas y querés algo a medida.","Tenés dudas sobre qué ritual te conviene.","Buscás un acompañamiento serio y personalizado."],
   "cta_h2":"Armemos el ritual <span class=\"gold-accent\">para tu caso.</span>"},
]

# related = otros servicios de la misma categoría (hasta 6), más el hub de la categoría
LABELS = {s["slug"]: s["title"] for s in SERVICES}
# incluir amarres para cross-links dentro de amor? no; cada categoría se relaciona internamente
BY_CAT = {}
for s in SERVICES:
    BY_CAT.setdefault(s["cat"], []).append(s["slug"])

for s in SERVICES:
    sibs = [sl for sl in BY_CAT[s["cat"]] if sl != s["slug"]]
    rel = [(sl, LABELS[sl]) for sl in sibs][:6]
    s["related"] = rel

if __name__ == "__main__":
    for s in SERVICES:
        build(s)
    print("OK total:", len(SERVICES))
