import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Palabras clave a buscar
keywords = ["convenio colectivo", "estatuto de los trabajadores"]

# URL base del buscador del BOE
base_url = "https://www.boe.es/buscar/boe.php"

# Parámetros de búsqueda
params = {
    "n": 10,  # número de resultados
    "tn": "1",  # tipo de documento: disposición general
    "q": " OR ".join(keywords),  # consulta con palabras clave
    "sort_field": "fecha",
    "sort_order": "desc"
}

try:
    # Realizar la solicitud
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    # Extraer resultados
    results = soup.select("div.resultado-busqueda")

    # Preparar contenido para guardar
    output_lines = []
    output_lines.append(f"Resultados del BOE para {datetime.today().strftime('%Y-%m-%d')}\n")
    output_lines.append("=" * 60 + "\n")

    for result in results:
        title = result.select_one("a.titulo").get_text(strip=True)
        link = "https://www.boe.es" + result.select_one("a.titulo")["href"]
        summary = result.select_one("div.sumario")
        summary_text = summary.get_text(strip=True) if summary else "Sin resumen disponible"
        output_lines.append(f"Título: {title}\nResumen: {summary_text}\nEnlace: {link}\n")
        output_lines.append("-" * 60 + "\n")

    # Guardar en archivo con fecha
    filename = f"boe_monitor_{datetime.today().strftime('%Y%m%d')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(line + "\n" for line in output_lines)

    print(f"Se han guardado los resultados en el archivo: {filename}")

except Exception as e:
    print("Error al realizar la solicitud o procesar los datos:", e)
