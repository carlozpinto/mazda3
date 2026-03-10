import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuración
chrome_options = Options()
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)

# URL base
base_url = "https://www.kavak.com/mx/seminuevos/mazda/mazda-3?page="
lista_datos_total = []

try:
    # Recorremos de la página 1 a la 6 directamente cambiando la URL
    for pagina in range(0, 7):
        url = f"{base_url}{pagina}"
        print(f"Accediendo a: {url}")
        driver.get(url)
        time.sleep(5)  # Espera robusta para cargar el contenido de cada página

        # Inyección de JS para extraer datos de la página actual
        js_script = """
        return Array.from(document.querySelectorAll('.results_results__container__tcF4_ > div > a')).map(auto => {
            return {
                modelo: auto.querySelector('[class*="title__"]')?.innerText || 'N/A',
                detalles: auto.querySelector('[class*="subtitle__"]')?.innerText || 'N/A',
                precio: auto.querySelector('.uki-amount')?.innerText || 'N/A'
            };
        });
        """
        datos_pagina = driver.execute_script(js_script)

        # Si la página está vacía, terminamos
        if not datos_pagina or all(d['modelo'] == 'N/A' for d in datos_pagina):
            print("No se encontraron más datos. Fin del proceso.")
            break

        lista_datos_total.extend(datos_pagina)
        print(
            f"Página {pagina} extraída. Total acumulado: {len(lista_datos_total)}")

    # Guardar
    df = pd.DataFrame(lista_datos_total)
    df = df[df['modelo'] != 'N/A'].drop_duplicates()
    df.to_csv("datos_kavak_mazda3_final.csv",
              index=False, encoding='utf-8-sig')
    print(f"¡Éxito! Se guardaron {len(df)} registros totales.")

finally:
    driver.quit()
