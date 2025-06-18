import os
from datetime import datetime

RUTA_BASE = r"C:\Users\propietario\OneDrive\github\mis-objetos-exe\docs"

NOMBRES_ASIGNATURAS = {
    "tecnologia-web-1": "Tecnología Web 1",
    "inteligencia-artificial": "Inteligencia Artificial"
}

NOMBRES_OVAS = {
    "tecnologia-web-1": "OVA: Fundamentos de la Web",
    "tecnologia-web-1-gd": "OVA: Gestión Documental",
    "ia-basica": "OVA: Introducción a IA",
    "ia-avanzada": "OVA: IA Avanzada"
}

def generar_index():
    fecha_actual = datetime.now().strftime("%d de %B de %Y")
    contenido = [
        "<!DOCTYPE html>",
        "<html lang='es'>",
        "<head>",
        "  <meta charset='UTF-8'>",
        "  <meta name='viewport' content='width=device-width, initial-scale=1.0'>",
        "  <title>Repositorio de Objetos de Aprendizaje</title>",
        "  <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css'>",
        "  <style>",
        "    body { font-family: Arial, sans-serif; background-color: #f4f6f9; margin: 0; padding: 0; }",
        "    header { background-color: #2a5081; color: white; padding: 20px 0; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }",
        "    main { max-width: 900px; margin: auto; padding: 30px; }",
        "    section { margin-bottom: 40px; }",
        "    h2 { color: #1c4273; border-bottom: 2px solid #ddd; padding-bottom: 5px; }",
        "    ul { list-style: none; padding: 0; }",
        "    li { margin: 10px 0; }",
        "    a { text-decoration: none; color: #1c4273; background-color: #fff; padding: 12px 16px; display: flex; align-items: center; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); transition: background-color 0.3s ease; }",
        "    a:hover { background-color: #e6f0ff; }",
        "    a i { margin-right: 10px; color: #2a5081; }",
        "    footer { text-align: center; font-size: 14px; color: #666; padding: 20px; margin-top: 50px; }",
        "  </style>",
        "</head>",
        "<body>",
        "  <header>",
        "    <h1><i class='fas fa-folder-open'></i> Repositorio de Objetos de Aprendizaje</h1>",
        "  </header>",
        "  <main>"
    ]

    for asignatura in sorted(os.listdir(RUTA_BASE)):
        ruta_asignatura = os.path.join(RUTA_BASE, asignatura)
        if os.path.isdir(ruta_asignatura):
            nombre_asignatura = NOMBRES_ASIGNATURAS.get(asignatura, asignatura.replace("-", " ").title())
            subcarpetas = sorted(os.listdir(ruta_asignatura))
            ovas_encontradas = []

            for ova in subcarpetas:
                ruta_ova = os.path.join(ruta_asignatura, ova)
                index_path = os.path.join(ruta_ova, "index.html")
                if os.path.isdir(ruta_ova) and os.path.exists(index_path):
                    nombre_ova = NOMBRES_OVAS.get(ova, ova.replace("-", " ").title())
                    enlace = f"{asignatura}/{ova}/index.html"
                    ovas_encontradas.append((nombre_ova, enlace))

            if ovas_encontradas:
                contenido.append(f"<section><h2><i class='fas fa-book'></i> {nombre_asignatura}</h2><ul>")
                for nombre_ova, enlace in ovas_encontradas:
                    contenido.append(f"<li><a href='{enlace}'><i class='fas fa-file-alt'></i> {nombre_ova}</a></li>")
                contenido.append("</ul></section>")

    contenido.extend([
        f"<footer>Última actualización: {fecha_actual}</footer>",
        "  </main>",
        "</body>",
        "</html>"
    ])

    index_path = os.path.join(RUTA_BASE, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write("\n".join(contenido))

    print(f"✅ index.html visualmente mejorado generado en: {index_path}")

if __name__ == "__main__":
    generar_index()
