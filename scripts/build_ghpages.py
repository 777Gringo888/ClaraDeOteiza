import re, os, shutil
SRC = "/home/claude/clara-gh/site"
OUT = "/tmp/ghpages-build"
BASE = "/ClaraDeOteiza"
if os.path.exists(OUT): shutil.rmtree(OUT)
shutil.copytree(SRC, OUT)

html_re = re.compile(r'="/(?!/)')      # href/src/content/poster="/x  (no //)
js_re   = re.compile(r'"/(?!/)')       # "/x" site paths in JS (no //)

n_html = n_js = 0
for root, _, files in os.walk(OUT):
    for fn in files:
        p = os.path.join(root, fn)
        if fn.endswith(".html"):
            s = open(p, encoding="utf-8").read()
            s2 = html_re.sub('="' + BASE + '/', s)
            if s2 != s: open(p,"w",encoding="utf-8").write(s2); n_html += 1
        elif fn.endswith(".js"):
            s = open(p, encoding="utf-8").read()
            s2 = js_re.sub('"' + BASE + '/', s)
            if s2 != s: open(p,"w",encoding="utf-8").write(s2); n_js += 1
open(os.path.join(OUT,".nojekyll"),"w").write("")
print("HTML reescritos:", n_html, "| JS reescritos:", n_js)
