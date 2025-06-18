
import os
from pathlib import Path

docs_path = Path(__file__).parent / "docs"
index_file = docs_path / "index.html"

html_content = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Repositorio de Objetos de Aprendizaje</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #eef1f7;
            margin: 0;
            padding: 40px;
            display: flex;
            justify-content: center;
        }
        .container {
            background: #ffffff;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            width: 100%;
            max-width: 900px;
        }
        h1 {
            color: #1c4273;
            text-align: center;
            margin-bottom: 40px;
        }
        h2 {
            color: #333;
            margin-top: 30px;
            border-bottom: 2px solid #ccc;
            padding-bottom: 5px;
        }
        ul {
            list-style-type: none;
            padding-left: 0;
        }
        li {
            background-color: #f9f9f9;
            margin: 10px 0;
            padding: 12px 16px;
            border-radius: 8px;
            transition: background 0.3s;
            display: flex;
            align-items: center;
        }
        li:hover {
            background-color: #e0ebff;
        }
        a {
            text-decoration: none;
            color: #1a0dab;
            font-weight: bold;
            flex-grow: 1;
        }
        .icon {
            margin-right: 10px;
            color: #1c4273;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Repositorio de Objetos de Aprendizaje</h1>
'''

for asignatura_dir in sorted(docs_path.iterdir()):
    if asignatura_dir.is_dir():
        asignatura_nombre = asignatura_dir.name.replace('-', ' ').title()
        html_content += f"<h2><i class='fas fa-folder-open icon'></i> {asignatura_nombre}</h2><ul>"

        for ova_dir in sorted(asignatura_dir.iterdir()):
            index_ova = ova_dir / "index.html"
            if index_ova.exists():
                titulo_path = ova_dir / "titulo.txt"
                if titulo_path.exists():
                    titulo = titulo_path.read_text(encoding='utf-8').strip()
                else:
                    titulo = ova_dir.name.replace('-', ' ').title()
                link = f"{asignatura_dir.name}/{ova_dir.name}/index.html"
                html_content += f"<li><i class='fas fa-book icon'></i><a href='{link}' target='_blank'>{titulo}</a></li>"

        html_content += "</ul>"

html_content += "</div></body></html>"

with open(index_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ index.html visualmente mejorado con iconos y centrado generado en: {index_file}")
