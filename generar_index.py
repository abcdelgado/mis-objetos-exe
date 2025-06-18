import os

# Ruta local donde están las carpetas de los objetos (ajustar si es necesario)
RUTA_DOCS = r"C:\Users\propietario\OneDrive\github\mis-objetos-exe\docs"

# Diccionario para traducir nombres de carpeta a nombres presentables (se puede ampliar)
NOMBRES_PRESENTABLES = {
    "tecweb1": "Tecnología Web 1",
    "informatica-basica": "Informática Básica",
    "algoritmos": "Algoritmos",
}

def generar_index():
    carpetas = sorted([d for d in os.listdir(RUTA_DOCS) if os.path.isdir(os.path.join(RUTA_DOCS, d))])

    contenido = [
        "<!DOCTYPE html>",
        "<html lang='es'>",
        "<head>",
        "  <meta charset='UTF-8'>",
        "  <title>Mis Objetos de Aprendizaje</title>",
        "</head>",
        "<body>",
        "  <h1>Repositorio de Objetos de Aprendizaje</h1>",
        "  <ul>"
    ]

    for carpeta in carpetas:
        index_path = os.path.join(RUTA_DOCS, carpeta, "index.html")
        if os.path.exists(index_path):
            nombre = NOMBRES_PRESENTABLES.get(carpeta, carpeta)
            enlace = f"{carpeta}/index.html"
            contenido.append(f'    <li><a href="{enlace}">{nombre}</a></li>')

    contenido.extend([
        "  </ul>",
        "</body>",
        "</html>"
    ])

    index_file_path = os.path.join(RUTA_DOCS, "index.html")
    with open(index_file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(contenido))

    print(f"✅ Archivo index.html generado correctamente en: {index_file_path}")

if __name__ == "__main__":
    generar_index()
