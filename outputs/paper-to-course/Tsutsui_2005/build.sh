#!/usr/bin/env bash
# Assemble index.html from _base.html + modules/*.html + _footer.html,
# inlining styles.css and main.js so index.html works as a single file.
set -euo pipefail
cd "$(dirname "$0")"

python3 - <<'EOF'
import glob
base = open("_base.html", encoding="utf-8").read()
css = open("styles.css", encoding="utf-8").read()
js = open("main.js", encoding="utf-8").read()
base = base.replace('<link rel="stylesheet" href="styles.css">', "")
base = base.replace('<script src="main.js" defer></script>', "")
base = base.replace("<!-- INLINE_CSS -->", "<style>\n" + css + "\n</style>")
# main.js queries the DOM on load, so run it after parsing
base = base.replace("<!-- INLINE_JS -->", "<script>\ndocument.addEventListener('DOMContentLoaded', function () {\n" + js + "\n});\n</script>")
modules = "\n".join(open(f, encoding="utf-8").read() for f in sorted(glob.glob("modules/*.html")))
footer = open("_footer.html", encoding="utf-8").read()
open("index.html", "w", encoding="utf-8").write(base + "\n" + modules + "\n" + footer)
print("index.html written")
EOF

# Optional: Markdown + PPTX via the paper-to-course pipeline, then tidy README whitespace.
# Usage: P2C_SCRIPTS=/path/to/paper-to-course/scripts bash build.sh
if [ -n "${P2C_SCRIPTS:-}" ]; then
  node "$P2C_SCRIPTS/build-all.js" . --md --pptx
  python3 - <<'PY'
import re
s = open("README.md", encoding="utf-8").read()
lines = [l.strip() for l in s.splitlines()]
s = re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip() + "\n"
open("README.md", "w", encoding="utf-8").write(s)
PY
fi
