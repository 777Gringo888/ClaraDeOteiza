# -*- coding: utf-8 -*-
"""Librería de íconos para los bullets de señales.
   Cada ícono es el contenido interno de un <svg> (paths).
   pick_icon(texto) devuelve el ícono que mejor matchea por palabras clave.
   Se usa en la replicación (gen_services) para asignar íconos automáticamente."""

# Inner SVG (Lucide-style, stroke). Se envuelven con el <svg> del componente.
ICONS = {
    "alert":     '<path d="m21.73 18-8-14a2 2 0 0 0-3.46 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><path d="M12 9v4"/><path d="M12 17h.01"/>',
    "health":    '<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>',
    "block":     '<circle cx="12" cy="12" r="10"/><path d="m4.9 4.9 14.2 14.2"/>',
    "eye":       '<path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/>',
    "search":    '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    "loop":      '<path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/>',
    "heart":     '<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8l1 1.1L12 21l7.8-7.5 1-1.1a5.5 5.5 0 0 0 0-7.8Z"/>',
    "heartbreak":'<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8l1 1.1L12 21l7.8-7.5 1-1.1a5.5 5.5 0 0 0 0-7.8Z"/><path d="m12 6-2 4h4l-2 4"/>',
    "money":     '<line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
    "shield":    '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/>',
    "spark":     '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M18.4 5.6l-2.8 2.8M8.4 15.6l-2.8 2.8"/>',
    "link":      '<path d="M9 17H7A5 5 0 0 1 7 7h2"/><path d="M15 7h2a5 5 0 0 1 0 10h-2"/><line x1="8" y1="12" x2="16" y2="12"/>',
    "flame":     '<path d="M12 2s4 4 4 8a4 4 0 0 1-8 0c0-1 .5-2 1-2.5C8 10 12 8 12 2Z"/>',
    "clock":     '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "star":      '<path d="m12 3 2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.7 6.8 19.1l1-5.8-4.3-4.1 5.9-.9Z"/>',
    "compass":   '<circle cx="12" cy="12" r="10"/><path d="m16.2 7.8-2.9 6.5-6.5 2.9 2.9-6.5 6.5-2.9Z"/>',
    "user-x":    '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="m17 8 5 5M22 8l-5 5"/>',
    "sad":       '<circle cx="12" cy="12" r="10"/><path d="M16 16s-1.5-2-4-2-4 2-4 2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/>',
    "check":     '<path d="M20 6 9 17l-5-5"/>',
}

# keyword -> icon name (primer match gana; el orden va de lo más específico a lo general)
KEYWORDS = [
    (["probaste de todo","nada cambia","nada funciona","nada termina","vueltas","siempre lo mismo","una y otra vez"], "loop"),
    (["se fue","se alejo","se alej","me dejo","me dej","separamos","separ","terminamos","termino con","ruptura","ya no me","distante"], "heartbreak"),
    (["pasion","pasión","deseo","atracc","chispa","intim"], "flame"),
    (["tercero","tercera","amante","la otra","el otro","otro hombre","otra mujer","envidia","te quiere mal","mala intenc","observ","vigil"], "eye"),
    (["unir","union","unión","matrimonio","casar","compromiso","atadura","amarr","lazo"], "link"),
    (["reconcil","pareja","corazon","corazón","volver","vuelva","enamor","amor"], "heart"),
    (["salud","enferm","dolor","cuerpo","malestar","peleas","pelea"], "health"),
    (["dinero","plata","deuda","laboral","empleo","conseguir trabajo","sin trabajo","negocio","venta","prosper","abundan","ingres"], "money"),
    (["juego","loteria","lotería","quiniela","apuest","fortuna","buena suerte","la suerte"], "star"),
    (["proteg","protec","escudo","blind","familia","mis hijos","mi casa","hogar","resguard"], "shield"),
    (["limpi","energia pesada","energía pesada","liviana","liber","soltar","descarg"], "spark"),
    (["bloque","trabad","estanc","frenad","cerr","no avanza","no fluye","abrir camino"], "block"),
    (["golpe","de repente","sin razon","sin razón","sin explica","todo junto","complic","caos"], "alert"),
    (["perdid","rumbo","camino","orient","decision","decisión","no se que hacer","no sé qué","futuro"], "compass"),
    (["saber","certeza","duda","averigu","descubr","confirm","enterar"], "search"),
    (["triste","angust","deprim","bajon","bajón","vacio","vacío","animo","ánimo","paz interior"], "sad"),
    (["alejar","sacar del medio","apart"], "user-x"),
]

def _norm(s):
    s = s.lower()
    for a,b in [("á","a"),("é","e"),("í","i"),("ó","o"),("ú","u")]:
        s = s.replace(a,b)
    return s

def pick_icon(text):
    t = _norm(text)
    for keys, name in KEYWORDS:
        for k in keys:
            if _norm(k) in t:
                return ICONS[name]
    return ICONS["check"]  # fallback neutro

def signal_li(text):
    """Devuelve el <li> completo del bullet con su ícono contextual."""
    ico = pick_icon(text)
    return ('<li><span class="cdo-signals__ico"><svg viewBox="0 0 24 24" fill="none" '
            'stroke="currentColor" stroke-width="1.9" stroke-linecap="round" '
            'stroke-linejoin="round" aria-hidden="true">' + ico + '</svg></span>'
            '<span>' + text + '</span></li>')

if __name__ == "__main__":
    tests = [
        "De golpe se te complicó todo, junto y sin razón.",
        "Peleas, problemas de salud o mala suerte que no aflojan.",
        "Sentís un bloqueo que no tiene explicación.",
        "Tenés la sensación de que alguien te quiere mal.",
        "Querés saber con certeza qué te está pasando.",
        "Probaste de todo y sentís que nada termina de cambiar.",
        "Tu pareja se fue y no lográs volver a acercarte.",
        "Se apagó la pasión y el deseo.",
        "No te alcanza la plata y el trabajo no aparece.",
        "Querés proteger a tu familia de las malas energías.",
    ]
    for t in tests:
        # imprime qué ícono eligió
        for keys, name in KEYWORDS:
            if any(_norm(k) in _norm(t) for k in keys):
                print(f"{name:12} <- {t}"); break
        else:
            print(f"{'check':12} <- {t}")
