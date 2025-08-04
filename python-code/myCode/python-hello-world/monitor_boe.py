import sys; print("executable: " + sys.executable)
sys.path.append("C:\\D\\GitRepos\\Python\\pythonIn100\\python-code\\myCode\\python-hello-world\\.venv\\Lib\\site-packages")
import os; print("cwd: " + os.getcwd())
import sys; print("syspath: "); print(sys.path)
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# Palabras clave a buscar
keywords = ["Convenio colectivo estatal de empresas de consultoria", "estatuto de los trabajadores", "BOE-A-2025-15971"]

# URL base del buscador del BOE
base_url = "https://www.boe.es/buscar/boe.php"
today = datetime.now().strftime('%Y-%m-%d')
two_weeks_ago = (datetime.now() - timedelta(days=15)).strftime('%Y-%m-%d')
print("Checking from " + two_weeks_ago + " until " + today)
# Parámetros de búsqueda
# https://www.boe.es/buscar/boe.php?
# ?campo[0]=ORIS&dato[0][1]=1&dato[0][3]=3&operador[0]=and&campo[1]=TITULOS&dato[1]=&operador[1]=and&campo[2]=DEM&dato[2]=&operador[2]=and&campo[3]=DOC&dato[3]="estatuto+de+los+trabajadores"&operador[3]=and&campo[4]=NBOS&dato[4]=&operador[4]=and&campo[5]=NOF&dato[5]=&operador[5]=and&operador[6]=and&campo[6]=FPU&dato[6][0]=&dato[6][1]=&page_hits=50&sort_field[0]=FPU&sort_order[0]=desc&sort_field[1]=ORI&sort_order[1]=asc&sort_field[2]=REF&sort_order[2]=asc&accion=Buscar
# ?campo[0]=ORIS&dato[0][1]=1&dato[0][3]=3&operador[0]=and&campo[1]=TITULOS&dato[1]=&operador[1]=and&campo[2]=DEM&dato[2]=&operador[2]=and&campo[3]=DOC&dato[3]="estatuto+de+los+trabajadores"&operador[3]=and&campo[4]=NBOS&dato[4]=&operador[4]=and&campo[5]=NOF&dato[5]=&operador[5]=and&operador[6]=and&campo[6]=FPU&dato[6][0]=2025-08-01&dato[6][1]=2025-07-15&page_hits=50&sort_field[0]=FPU&sort_order[0]=desc&sort_field[1]=ORI&sort_order[1]=asc&sort_field[2]=REF&sort_order[2]=asc&accion=Buscar
# ?campo[0]=ORIS&dato[0][1]=1&dato[0][2]=2&dato[0][3]=3&dato[0][4]=4&dato[0][5]=5&dato[0][T]=T&operador[0]=and&campo[1]=TITULOS&dato[1]=&operador[1]=and&campo[2]=DEM&dato[2]=&operador[2]=and&campo[3]=DOC&dato[3]="estatuto+de+los+trabajadores"+"ley"&operador[3]=and&campo[4]=NBOS&dato[4]=&operador[4]=and&campo[5]=NOF&dato[5]=&operador[5]=and&operador[6]=and&campo[6]=FPU&dato[6][0]=2025-07-28&dato[6][1]=2025-08-01&page_hits=50&sort_field[0]=FPU&sort_order[0]=asc&sort_field[1]=ORI&sort_order[1]=asc&sort_field[2]=REF&sort_order[2]=asc&accion=Buscar
# cadenas de búsqueda:
#     "Convenio+colectivo"
#     "\"ley\"+\"estatuto+de+los+trabajadores\"+\"Real+Decreto+Legislativo+2/2015\""
#     "estatuto+de+los+trabajadores"

my_params = {
    "campo[0]": "ORIS",
    "dato[0][1]": "1",
    "dato[0][3]": "3",
    "operador[0]": "and",
    "campo[3]": "DOC",
    "dato[3]": "\"estatuto+de+los+trabajadores\"",
    "operador[3]" : "and",
    "operador[6]" : "and",
    "campo[6]" : "FPU",
    "dato[6][0]" : two_weeks_ago,
    "dato[6][1]" : today,
    "page_hits": "2000",
    "sort_field[0]" : "FPU",
    "sort_order[0]" : "desc",
    "accion" : "Buscar"
}
#my_params = {
#    "n": 10,  # número de resultados
#    #"tn": "1",  # tipo de documento: disposición general
#    "tn": "3",   # tipo de documento: Otras disposiciones
#    "q": " OR ".join(keywords),  # consulta con palabras clave
#    "sort_field": "fecha",
#    "sort_order": "desc"
#}

try:
    # Realizar la solicitud
    response = requests.get(base_url, params=my_params)
    response.raise_for_status()
    #print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extraer resultados
    #print("antes de la consulta")
    #results = soup.select("div.resultado-busqueda")
    #results = soup.select("div.listadoResult")
    results = soup.select("li.resultado-busqueda")
    #print("Resultados:")
    #print(results)

    # Preparar contenido para guardar
    output_lines = []
    output_lines.append(f"Resultados del BOE para {datetime.today().strftime('%Y-%m-%d')}\n")
    output_lines.append("=" * 60 + "\n")
    nof_results = 0
    for result in results:
        #print("procesando:")
        #print(result)

        summary = result.select_one("p")
        summary_text = summary.get_text(strip=True) if summary else "Sin resumen disponible"
        #print("Hemos encontrado resúmen:")
        #print(summary_text)

        #relative_link = result.select_one("a.tittle")["href"]
        relative_link = result.select_one("a")["href"]

        link = "https://www.boe.es/" + relative_link
        #print("hemos encontrado enlace:")
        #print(link)

        #title = result.select_one("a.title").get_text(strip=True)
        title = result.select_one("a")["title"]
        #print("hemos encontrado titulo: ")
        #print(title)

        #summary = result.select_one("div.sumario")
        output_lines.append(f"Título: {title}\nResumen: {summary_text}\nEnlace: {link}\n")
        output_lines.append("-" * 60 + "\n")

        nof_results = nof_results+1

    # Guardar en archivo con fecha
    filename = f"boe_monitor_{datetime.today().strftime('%Y%m%d')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(line + "\n" for line in output_lines)

    print(f"Se han guardado  {nof_results} resultados en el archivo: {filename}")

except Exception as e:
    print("Error al realizar la solicitud o procesar los datos:", e)
