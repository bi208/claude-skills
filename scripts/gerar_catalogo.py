#!/usr/bin/env python3
"""Gera o catálogo de skills (CATALOGO.md e o mapa do maestro) a partir dos SKILL.md.
Uso: python3 scripts/gerar_catalogo.py
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
PLUGINS = ROOT / "plugins"
TITULOS = {
    "june-agencia": "June — maestro e skills da agência (donas da entrega)",
    "mkt-growth-cro-crm": "Mercado — Growth, CRO, CRM, copy, SEO (Corey Haines, MIT)",
    "mkt-local-gmn": "Mercado — SEO local e Google Meu Negócio (Garrett Smith + claude-seo, MIT)",
    "mkt-geo-ia": "Mercado — GEO / visibilidade em IA (Zubair Trabzada, MIT)",
    "mkt-midia-ecommerce": "Mercado — Mídia paga, analytics e ecommerce (Rebecca Rae Barton, MIT)",
}

def frontmatter(path):
    txt = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", txt, re.S)
    meta = {}
    if not m:
        return meta
    lines = m.group(1).splitlines()
    i = 0
    while i < len(lines):
        km = re.match(r"^([a-zA-Z_-]+):\s*(.*)$", lines[i])
        if km:
            key, val = km.group(1), km.group(2).strip()
            if val in (">", "|", ">-", "|-"):
                buf = []
                i += 1
                while i < len(lines) and (lines[i].startswith(" ") or not lines[i].strip()):
                    buf.append(lines[i].strip()); i += 1
                meta[key] = " ".join(b for b in buf if b); continue
            meta[key] = val.strip('"').strip("'")
        i += 1
    return meta

def main():
    out = ["# Catálogo de skills", "", "Gerado por `scripts/gerar_catalogo.py`. Não edite à mão.", ""]
    total = 0
    for plugin in sorted(PLUGINS.iterdir(), key=lambda p: (p.name != "june-agencia", p.name)):
        skills = sorted(plugin.glob("skills/*/SKILL.md"))
        out += [f"## {TITULOS.get(plugin.name, plugin.name)}", f"Plugin: `{plugin.name}` · {len(skills)} skills", "",
                "| Skill | Para que serve |", "|---|---|"]
        for s in skills:
            meta = frontmatter(s)
            desc = meta.get("description", "").replace("|", "/")
            if len(desc) > 260:
                desc = desc[:257].rsplit(" ", 1)[0] + "…"
            out.append(f"| `{meta.get('name', s.parent.name)}` | {desc} |")
            total += 1
        out.append("")
    out.insert(3, f"Total: **{total} skills** em {len(list(PLUGINS.iterdir()))} plugins.\n")
    texto = "\n".join(out)
    (ROOT / "CATALOGO.md").write_text(texto, encoding="utf-8")
    mapa = ROOT / "plugins/june-agencia/skills/june-maestro/references/mapa-de-skills.md"
    mapa.write_text(texto.replace("# Catálogo de skills", "# Mapa de skills (referência do maestro)", 1), encoding="utf-8")
    print(f"{total} skills catalogadas")

if __name__ == "__main__":
    main()
