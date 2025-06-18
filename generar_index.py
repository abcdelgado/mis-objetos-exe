import os
from datetime import datetime

# Ruta principal que contiene carpetas de asignaturas
RUTA_BASE = r"C:\Users\propietario\OneDrive\github\mis-objetos-exe\docs\tecnogia-web-1"

# Diccionario para nombres amigables
NOMBRES_PRESENTABLES = {
    "tecnologia-web-1": "Tecnología Web 1",
    "tecnologia-web-1-gd": "Tecnología Web 1 - Gestión Documental",
}

def generar_index():
    carpetas_asignaturas = sorted([
        carpeta for carpeta in os.listdir(RUTA_BASE)
        if os.path.isdir(os.path.join(RUTA_BASE, carpeta))
    ])

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

    for asignatura in carpetas_asignaturas:
        ruta_index = os.path.join(RUTA_BASE, asignatura, "index.html")
        if os.path.exists(ruta_index):
            nombre = NOMBRES_PRESENTABLES.get(asignatura, asignatura.replace("-", " ").title())
            enlace = f"{asignatura}/index.html"
            contenido.append(f'    <li><a href="{enlace}">{nombre}</a></li>')

    contenido.extend([
        "  </ul>",
        f"  <div class='fecha'>Última actualización: {fecha_actual}</div>",
        "</body>",
        "</html>"
    ])

    index_file_path = os.path.join(RUTA_BASE, "index.html")
    with open(index_file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(contenido))

    print(f"✅ index.html generado correctamente en: {index_file_path}")

if __name__ == "__main__":
    generar_index()
