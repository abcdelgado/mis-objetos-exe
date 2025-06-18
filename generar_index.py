
import os
from pathlib import Path

docs_path = Path(__file__).parent / "docs"
index_file = docs_path / "index.html"

html_content = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Repositorio de Objetos de Aprendizaje</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f4f4; margin: 40px; }
        h1 { color: #1c4273; }
        h2 { margin-top: 30px; color: #333; }
        ul { list-style-type: none; padding: 0; }
        li { background: #ffffff; padding: 10px; margin: 5px 0; border-radius: 5px; }
        a { text-decoration: none; color: #1a0dab; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>Repositorio de Objetos de Aprendizaje</h1>
'''

for asignatura_dir in sorted(docs_path.iterdir()):
    if asignatura_dir.is_dir():
        asignatura_nombre = asignatura_dir.name.replace('-', ' ').title()
        html_content += f"<h2>{asignatura_nombre}</h2><ul>"

        for ova_dir in sorted(asignatura_dir.iterdir()):
            index_ova = ova_dir / "index.html"
            if index_ova.exists():
                titulo_path = ova_dir / "titulo.txt"
                if titulo_path.exists():
                    titulo = titulo_path.read_text(encoding='utf-8').strip()
                else:
                    titulo = ova_dir.name.replace('-', ' ').title()
                link = f"{asignatura_dir.name}/{ova_dir.name}/index.html"
                html_content += f'<li><a href="{link}">{titulo}</a></li>'

        html_content += "</ul>"

html_content += "</body></html>"

with open(index_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ index.html visualmente mejorado generado en: {index_file}")
