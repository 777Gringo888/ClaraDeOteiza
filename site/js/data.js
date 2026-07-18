/* data.js — sitemap subset, services, derivador routing + testimonios.
   Vanilla port of the home/ prototype's data.jsx. */
(function () {
  "use strict";

  var PHONE = "5491136746858";
  function wa(msg) { return "https://wa.me/" + PHONE + "?text=" + encodeURIComponent(msg); }

  function P(href, label) { return { href: href, label: label }; }

  // Chip → recommended internal pages (Clara habla en primera persona)
  var CHIPS = [
    {
      id: "alejo", label: "Mi pareja se alejó",
      intro: "Cuando alguien que amás se aleja, la incertidumbre pesa. Puedo ayudarte a trabajar el vínculo para reabrir el diálogo y el acercamiento.",
      pages: [
        P("/amarres/retorno-de-pareja/", "Retorno de pareja"),
        P("/amarres/amarres-de-amor/", "Amarres de amor"),
        P("/amarres/", "Ver todos los trabajos de amor")
      ]
    },
    {
      id: "recuperar", label: "Quiero recuperar a alguien",
      intro: "Recuperar un vínculo empieza por entender qué se rompió. Evalúo tu caso antes de recomendarte cualquier trabajo.",
      pages: [
        P("/amarres/amarres-de-amor/", "Amarres de amor"),
        P("/amarres/reconciliacion-de-pareja/", "Reconciliación de pareja"),
        P("/amarres/", "Ver todos los trabajos de amor")
      ]
    },
    {
      id: "infiel", label: "Creo que me engaña",
      intro: "Cuando algo no cierra, primero conviene ver con claridad qué está pasando. Te hago una lectura y, si hay un tercero, trabajo el alejamiento y la reconexión de tu vínculo.",
      pages: [
        P("/tarot-y-videncia/videncia/", "Videncia: saber la verdad"),
        P("/amarres/alejamiento-de-terceros-y-amantes/", "Alejamiento de terceros y amantes")
      ]
    },
    {
      id: "fortalecer", label: "Quiero fortalecer mi relación",
      intro: "Una relación se cuida. Puedo acompañarte con trabajos de armonía y acercamiento para reforzar el vínculo que ya tenés.",
      pages: [
        P("/amarres/endulzamiento/", "Endulzamiento"),
        P("/amarres/amarres-de-amor-eterno/", "Amarres de amor eterno")
      ]
    },
    {
      id: "trabajo", label: "Creo que me hicieron un trabajo",
      intro: "Si sentís que algo externo te está afectando, lo evalúo y, si corresponde, corto y limpio esa energía.",
      pages: [
        P("/rituales-y-trabajos/te-hicieron-un-trabajo/", "¿Te hicieron un trabajo?"),
        P("/rituales-y-trabajos/corte-de-danos/", "Anti-brujería y corte de daños"),
        P("/limpiezas-y-proteccion/limpieza-energetica/", "Limpieza energética")
      ]
    },
    {
      id: "claridad", label: "Necesito claridad sobre mi futuro",
      intro: "Cuando no sabés qué camino tomar, te hago una lectura para ver con más claridad y decidir con calma.",
      pages: [
        P("/tarot-y-videncia/lectura-de-tarot/", "Lectura de tarot"),
        P("/tarot-y-videncia/orientacion-espiritual/", "Orientación espiritual")
      ]
    },
    {
      id: "bloqueos", label: "Siento bloqueos o mala energía",
      intro: "Los bloqueos y la energía pesada los puedo limpiar. Recuperar tu equilibrio es el primer paso.",
      pages: [
        P("/limpiezas-y-proteccion/limpieza-energetica/", "Limpieza energética"),
        P("/limpiezas-y-proteccion/apertura-de-caminos/", "Apertura de caminos")
      ]
    },
    {
      id: "dinero", label: "Problemas de dinero o trabajo",
      intro: "Cuando el dinero o el trabajo se traban, tengo trabajos de apertura y desbloqueo para volver a mover tu energía.",
      pages: [
        P("/prosperidad-y-abundancia/desbloqueo-laboral/", "Desbloqueo laboral y dinero"),
        P("/prosperidad-y-abundancia/prosperidad/", "Prosperidad y abundancia")
      ]
    }
  ];

  function chipById(id) {
    for (var i = 0; i < CHIPS.length; i++) if (CHIPS[i].id === id) return CHIPS[i];
    return null;
  }

  // Empathetic intro per family (used for the free-text result)
  var INTROS = {
    amarres: "Cuando el amor duele o alguien se aleja, puedo trabajar el vínculo con respeto e intención. Estos trabajos pueden acompañarte.",
    amor: "Toda relación se puede cuidar y reconstruir. Por lo que me contás, esto es lo que más se acerca a tu situación.",
    infiel: "Cuando algo no cierra, primero te ayudo a ver con claridad qué está pasando. Y si hay un tercero, trabajo el alejamiento y la reconexión.",
    limpiezas: "Si sentís que algo pesa o te afecta desde afuera, lo evalúo, corto y limpio esa energía.",
    tarot: "Cuando necesitás claridad, te hago una lectura para ver mejor y decidir con calma.",
    prosperidad: "Cuando el dinero o el trabajo se traban, tengo trabajos de apertura y desbloqueo para volver a mover tu energía.",
    rituales: "Cada caso es único. Trabajo a medida y evalúo tu situación antes de recomendarte cualquier ritual."
  };

  // Page index across the sitemap tree — free text is scored against these keywords
  function G(href, label, cat, keys) { return { href: href, label: label, cat: cat, keys: keys }; }
  var PAGES = [
    // Infidelidad / me engaña / dudas
    G("/tarot-y-videncia/videncia/", "Videncia: saber la verdad", "infiel", ["me engana", "me engaña", "engaña", "engana", "me engano", "infiel", "me es infiel", "es infiel", "infidelidad", "sospecho", "me miente", "miente", "mentira", "me oculta", "esconde", "saber la verdad", "quiero saber", "duda", "dudas", "otra mujer", "otro hombre"]),
    G("/amarres/alejamiento-de-terceros-y-amantes/", "Alejamiento de terceros y amantes", "infiel", ["amante", "la otra", "el otro", "tercero", "tercera", "sacar del medio", "cuernos", "engaño"]),
    // Amor / amarres
    G("/amarres/amarres-de-amor/", "Amarres de amor", "amarres", ["amarre", "amarrar", "atar", "que vuelva", "que regrese", "amor"]),
    G("/amarres/retorno-de-pareja/", "Retorno de pareja", "amor", ["se alejo", "se alejó", "se fue", "me dejo", "me dejó", "volver", "vuelva", "regrese", "retorno", "recuperar", "separamos", "separó", "terminamos", "ex"]),
    G("/amarres/reconciliacion-de-pareja/", "Reconciliación de pareja", "amor", ["reconciliar", "reconciliacion", "reconciliación", "pelea", "peleamos", "distante", "no me habla", "reconectar", "volver a estar bien", "amigarnos", "amigarse"]),
    G("/amarres/endulzamiento/", "Endulzamiento", "amor", ["endulzar", "endulzamiento", "que me quiera mas", "carinoso", "cariñoso", "dulce", "amoroso", "frio", "frío", "fría", "se enfrio", "enfrió", "indiferente"]),
    G("/amarres/amarres-de-amor-eterno/", "Amarres de amor eterno", "amor", ["armonizar", "armonia", "armonía", "mejorar relacion", "mejorar la relacion", "fortalecer", "reforzar", "afianzar", "consolidar", "vinculo", "vínculo", "amor eterno", "para siempre", "duradero"]),
    G("/amarres/union-y-matrimonio/", "Unión y matrimonio", "amor", ["unir", "union", "unión", "que estemos juntos", "formalizar", "compromiso", "matrimonio", "casarnos", "casar", "esposo", "esposa", "marido", "casados", "convivir"]),
    G("/amarres/amarre-pasional/", "Amarre pasional", "amor", ["pasion", "pasión", "pasional", "deseo", "sexual", "atraccion", "atracción", "quimica", "química", "intimidad"]),
    G("/amarres/amarres-de-amor/", "Problemas de amor", "amor", ["problema de amor", "problemas de amor", "mal en el amor", "sufro por amor", "corazon roto", "corazón roto"]),
    // Tarot / videncia / futuro
    G("/tarot-y-videncia/lectura-de-tarot/", "Lectura de tarot", "tarot", ["tarot", "carta", "cartas", "tirada", "tirar las cartas"]),
    G("/tarot-y-videncia/tarot-del-amor/", "Tarot del amor", "tarot", ["tarot del amor", "cartas del amor", "tarot de pareja", "me quiere", "que siente por mi", "qué siente"]),
    G("/tarot-y-videncia/videncia/", "Videncia natural", "tarot", ["videncia", "vidente", "vision", "visión", "medium", "médium", "percibir"]),
    G("/tarot-y-videncia/orientacion-espiritual/", "Orientación espiritual", "tarot", ["orientacion", "orientación", "guia", "guía", "no se que hacer", "no sé qué hacer", "consejo", "que camino", "decision", "decisión", "futuro", "que va a pasar", "saber", "adivinar", "claridad", "perdida", "perdido"]),
    // Rituales / anti-brujería / desamarres
    G("/rituales-y-trabajos/te-hicieron-un-trabajo/", "¿Te hicieron un trabajo?", "rituales", ["me hicieron", "hicieron un trabajo", "trabajo en contra", "me hicieron mal", "embrujado", "todo se complico", "todo me sale mal"]),
    G("/rituales-y-trabajos/corte-de-danos/", "Anti-brujería y corte de daños", "rituales", ["dano", "daño", "danos", "daños", "brujeria", "brujería", "corte de danos", "corte de daños", "anti brujeria", "antibrujeria", "sacar el daño", "cortar el daño"]),
    G("/rituales-y-trabajos/contra-hechizos/", "Contra hechizos", "rituales", ["contra hechizo", "me hicieron un hechizo", "hechizada", "hechizado", "hechizo", "maleficio", "hechizo en contra"]),
    G("/rituales-y-trabajos/desamarres/", "Desamarres", "rituales", ["desamarre", "desamarrar", "romper amarre", "quitar amarre", "deshacer amarre", "sacar un amarre", "sacarme un amarre", "sacar el amarre", "amarrado", "atadura", "liberarme", "soltar"]),
    G("/rituales-y-trabajos/rituales/", "Rituales a medida", "rituales", ["ritual", "trabajo espiritual", "trabajo a medida", "no se que necesito", "algo a medida"]),
    // Limpiezas / protección
    G("/limpiezas-y-proteccion/limpieza-energetica/", "Limpieza energética", "limpiezas", ["limpieza", "limpiar", "energia pesada", "energía pesada", "mala energia", "mala energía", "cargado", "pesado", "envidia", "mal de ojo", "ojeado", "me tienen envidia"]),
    G("/limpiezas-y-proteccion/proteccion/", "Protección", "limpiezas", ["proteccion", "protección", "proteger", "protegerme", "escudo", "familia", "mis hijos", "hijos", "mi casa", "la casa", "hogar", "me quieren mal", "envidian"]),
    G("/limpiezas-y-proteccion/apertura-de-caminos/", "Apertura de caminos", "limpiezas", ["bloqueo", "bloqueada", "bloqueado", "trabada", "trabado", "nada me sale", "estancada", "estancado", "abrir caminos", "apertura"]),
    G("/limpiezas-y-proteccion/armonizacion/", "Armonización personal", "limpiezas", ["equilibrio", "paz interior", "ansiedad", "estres", "estrés", "stress", "angustia", "triste", "tristeza", "deprimida", "deprimido", "bajon", "bajón", "mal animo", "ánimo", "armonizacion", "armonización"]),
    // Prosperidad / dinero / trabajo
    G("/prosperidad-y-abundancia/prosperidad/", "Prosperidad y abundancia", "prosperidad", ["prosperidad", "abundancia", "que me vaya bien", "progresar", "crecer", "oportunidades", "dinero", "plata", "deuda", "deudas", "no me alcanza", "sin plata", "problemas de dinero"]),
    G("/prosperidad-y-abundancia/desbloqueo-laboral/", "Desbloqueo laboral y dinero", "prosperidad", ["trabajo", "laburo", "empleo", "sin trabajo", "conseguir trabajo", "desempleo", "problemas laborales", "jefe", "negocio", "local", "comercio", "ventas", "desbloqueo"]),
    G("/prosperidad-y-abundancia/suerte-en-el-juego/", "Suerte en el juego", "prosperidad", ["suerte", "juego", "loteria", "lotería", "quiniela", "apuestas", "casino"])
  ];

  function normalize(s) {
    return (s || "").toLowerCase()
      .replace(/[áàä]/g, "a").replace(/[éèë]/g, "e").replace(/[íìï]/g, "i")
      .replace(/[óòö]/g, "o").replace(/[úùü]/g, "u");
  }

  // Free text → best specific pages of the tree (scored), or a clarifier request
  function classify(text) {
    var raw = (text || "").trim();
    if (!raw) return null;
    var t = normalize(raw);
    var scored = [];
    for (var i = 0; i < PAGES.length; i++) {
      var p = PAGES[i], s = 0;
      for (var k = 0; k < p.keys.length; k++) {
        var key = normalize(p.keys[k]);
        if (t.indexOf(key) !== -1) s += (key.indexOf(" ") !== -1 ? 3 : 1) + key.length * 0.02;
      }
      if (s > 0) scored.push({ p: p, s: s });
    }
    if (!scored.length) return { clarify: true };
    scored.sort(function (a, b) { return b.s - a.s; });
    // de-duplicate by href, keep top 3
    var seen = {}, pages = [], cat = scored[0].p.cat;
    for (var j = 0; j < scored.length && pages.length < 3; j++) {
      var pg = scored[j].p;
      if (seen[pg.href]) continue;
      seen[pg.href] = 1;
      pages.push({ href: pg.href, label: pg.label });
    }
    return { intro: INTROS[cat] || INTROS.rituales, pages: pages, label: null };
  }

  var SERVICES = [
    { id: "amarres", title: "Amarres de Amor", image: "assets/services/amarres-de-amor.webp",
      desc: "Rituales personalizados para fortalecer, recuperar y proteger vínculos afectivos. Cada caso se evalúa individualmente.",
      href: "/amarres/", waMsg: "Hola Clara, quiero una consulta sobre amarres de amor." },
    { id: "amor", title: "Amor y Parejas", image: "assets/services/amor-y-parejas.webp",
      desc: "Retorno de pareja, endulzamientos, reconexión afectiva y armonización de vínculos. Trabajo integral sobre la relación.",
      href: "/amarres/", waMsg: "Hola Clara, quiero una consulta sobre amor y parejas." },
    { id: "tarot", title: "Tarot y Videncia", image: "assets/services/tarot-y-videncia.webp",
      desc: "Lecturas personalizadas para comprender tu situación, tomar decisiones y encontrar claridad en momentos difíciles.",
      href: "/tarot-y-videncia/", waMsg: "Hola Clara, quiero una consulta de tarot y videncia." },
    { id: "limpiezas", title: "Limpiezas y Protección", image: "assets/services/limpiezas-y-proteccion.jpg",
      desc: "Limpieza energética, corte de daños, desamarres y protección espiritual. Restablecé tu equilibrio.",
      href: "/limpiezas-y-proteccion/", waMsg: "Hola Clara, quiero una consulta sobre limpiezas y protección." },
    { id: "prosperidad", title: "Prosperidad y Dinero", image: "assets/services/prosperidad-y-dinero.webp",
      desc: "Apertura de caminos, desbloqueo laboral y trabajo energético para negocios. Removemos lo que traba tu crecimiento.",
      href: "/prosperidad-y-abundancia/", waMsg: "Hola Clara, quiero una consulta sobre prosperidad y dinero." },
    { id: "rituales", title: "Rituales y Trabajos", image: "assets/services/rituales-y-trabajos.webp",
      desc: "Trabajos energéticos a medida según cada caso. Clara evalúa tu situación antes de recomendar cualquier ritual.",
      href: "/rituales-y-trabajos/", waMsg: "Hola Clara, quiero una consulta sobre rituales y trabajos." }
  ];

  // 20 testimonial screenshots
  var TESTIMONIOS = [];
  for (var i = 0; i < 20; i++) {
    var n = String(i + 1);
    if (n.length < 2) n = "0" + n;
    TESTIMONIOS.push("assets/testimonios/testimonio-" + n + ".jpeg");
  }

  // Deterministic subset per page slug (rotates which show on each landing)
  function pickTestimonios(slug, n) {
    n = n || 8;
    var h = 0;
    var s = slug || "home";
    for (var k = 0; k < s.length; k++) h = (h * 31 + s.charCodeAt(k)) >>> 0;
    var start = h % TESTIMONIOS.length;
    var out = [];
    for (var j = 0; j < n; j++) out.push(TESTIMONIOS[(start + j) % TESTIMONIOS.length]);
    return out;
  }

  var INSTAGRAM = [
    "assets/imagery/altar-velas-fuego.jpg",
    "assets/imagery/amarres-rojos.jpg",
    "assets/imagery/altar-velas-rosas.jpg",
    "assets/imagery/altar-angeles.jpg",
    "assets/services/rituales-y-trabajos.webp",
    "assets/services/amarres-de-amor.webp"
  ];

  window.CDO = {
    PHONE: PHONE,
    wa: wa,
    WA_DEFAULT: wa("Hola Clara, me gustaría hacer una consulta."),
    WA_FLOAT: wa("Hola Clara, quiero hacer una consulta."),
    CHIPS: CHIPS,
    classify: classify,
    chipById: chipById,
    SERVICES: SERVICES,
    TESTIMONIOS: TESTIMONIOS,
    pickTestimonios: pickTestimonios,
    INSTAGRAM: INSTAGRAM,
    IG_URL: "https://www.instagram.com/ritualesdeamoreterno.ok/",
    IG_HANDLE: "@ritualesdeamoreterno.ok",
    TIKTOK_URL: "https://www.tiktok.com/@claradeoteiza",
    TIKTOK_HANDLE: "@claradeoteiza",
    SLUG: (window.CDO_SLUG || "home")
  };
})();
