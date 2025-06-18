import os
from datetime import datetime

RUTA_BASE = r"C:\Users\propietario\OneDrive\github\mis-objetos-exe\docs\tecnogia-web-1"

NOMBRES_PRESENTABLES = {
    "tecnogia-web-1": "Tecnología Web 1",
    "tecnogia-web-1-gd": "Tecnología Web 1 - Gestión Documental"
}

def generar_index():
    print(f"🔍 Explorando: {RUTA_BASE}")
    carpetas = sorted([
        carpeta for carpeta in os.listdir(RUTA_BASE)
        if os.path.isdir(os.path.join(RUTA_BASE, carpeta))
    ])

    print("📁 Subcarpetas encontradas:")
    for c in carpetas:
        print(f" - {c}")

    fecha_actual = datetime.now().strftime("%d de %B de %Y")

    contenido = [
        "<!DOCTYPE html>",
        "<html lang='es'>",
        "<head>",
        "  <meta charset='UTF-8'>",
        "  <title>Repositorio de Objetos de Aprendizaje</title>",
        "  <style>",
        "    body { font-family: Arial; background-color: #f9f9f9; padding: 40px; }",
        "    h1 { text-align: center; color: #2a5081; }",
        "    ul { list-style: none; padding: 0; max-width: 800px; margin: auto; }",
        "    li { margin: 10px 0; }",
        "    a { text-decoration: none; color: #1c4273; font-size: 18px; display: block; padding: 10px; background-color: #ffffff; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }",
        "    .fecha { text-align: center; margin-top: 30px; color: #555; font-size: 14px; }",
        "  </style>",
        "</head>",
        "<body>",
        "  <h1>Repositorio de Objetos de Aprendizaje</h1>",
        "  <ul>"
    ]

    for carpeta in carpetas:
        index_path = os.path.join(RUTA_BASE, carpeta, "index.html")
        print(f"🔎 Verificando: {index_path}")
        if os.path.exists(index_path):
            nombre = NOMBRES_PRESENTABLES.get(carpeta, carpeta.replace("-", " ").title())
            enlace = f"{carpeta}/index.html"
            contenido.append(f'    <li><a href="{enlace}">{nombre}</a></li>')
        else:
            print(f"⚠️ No se encontró index.html en: {carpeta}")

    contenido.extend([
        "  </ul>",
        f"  <div class='fecha'>Última actualización: {fecha_actual}</div>",
        "</body>",
        "</html>"
    ])

    output_path = os.path.join(RUTA_BASE, "index.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(contenido))

    print(f"✅ index.html generado en: {output_path}")

if __name__ == "__main__":
    generar_index()
