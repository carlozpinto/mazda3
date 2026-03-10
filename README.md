\# Mazda 3 Market Analysis - Kavak Scraper



Este proyecto automatiza la extracción de datos de vehículos \*\*Mazda 3\*\* publicados en el portal de Kavak México. El objetivo es consolidar un dataset estructurado para realizar análisis de mercado sobre precios y disponibilidad de seminuevos.



\## 🛠 Tecnologías Utilizadas

\- \*\*Python\*\*: Lenguaje base para la automatización.

\- \*\*Selenium\*\*: Herramienta de navegación automatizada para manejar contenido dinámico.

\- \*\*Pandas\*\*: Procesamiento y estructuración de datos en formato CSV.

\- \*\*Chrome WebDriver\*\*: Motor de renderizado para la interacción web.



\## 🚀 Cómo funciona

1\. \*\*Navegación Dinámica\*\*: El script utiliza una estructura de bucle para iterar sobre las páginas del catálogo, modificando dinámicamente el parámetro `page` en la URL.

2\. \*\*Extracción\*\*: Mediante la inyección de JavaScript en el DOM, se extraen campos clave: Modelo, Detalles (versión/año) y Precio.

3\. \*\*Limpieza\*\*: Se eliminan duplicados y se normaliza el formato para asegurar un dataset limpio.



\## 📊 Dataset

El resultado es un archivo `datos\_kavak\_mazda3\_final.csv` con los registros obtenidos.



---

\*Desarrollado como parte de un proyecto de automatización y análisis de datos.\*

