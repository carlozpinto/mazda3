Mazda 3 Market Analysis - Data Science Portfolio
Este proyecto consiste en un análisis integral del mercado de seminuevos Mazda 3 en México, utilizando datos extraídos de la plataforma Kavak. El objetivo es identificar tendencias de depreciación, jerarquías de precios por versión y detectar oportunidades de compra mediante técnicas de Ciencia de Datos.

🛠 Tecnologías Utilizadas
Python: Lenguaje principal de análisis.

Selenium: Extracción y navegación web (Web Scraping).

Pandas & NumPy: Procesamiento, limpieza y estructuración de datos.

Matplotlib & Seaborn: Análisis Exploratorio de Datos (EDA) y visualización estadística.

Git/GitHub: Control de versiones y gestión de repositorio.

🚀 Flujo de Trabajo (Pipeline)
Extracción (Scraping): Automatización mediante Selenium para la recolección de datos en tiempo real desde el portal de Kavak.

Limpieza (Preprocessing): Normalización de tipos de datos, eliminación de duplicados y estructuración para análisis.

Análisis Exploratorio (EDA):

Correlación de variables: Uso de Mapas de Calor (Heatmaps) para cuantificar el impacto del año y kilometraje sobre el precio.

Análisis de Depreciación: Visualización mediante Scatter plots y Boxplots para identificar comportamientos por versión.

Detección de Anomalías: Identificación de oportunidades de mercado (valores atípicos en precio/año).

📊 Hallazgos Principales
El Año de fabricación es la variable con mayor correlación positiva con el precio (0.89).

El Kilometraje tiene una relación negativa fuerte con el precio (-0.76).

Identificación de ofertazos: Se detectaron unidades (ej. año 2020) con desviaciones de precio que permiten compras estratégicas por debajo del valor de mercado.

📂 Estructura del Proyecto
limpieza_datos.ipynb: Notebook de limpieza y preparación de datos.

02_analisis_visual.ipynb: Notebook de análisis estadístico y gráficas.

mazda3_limpio.csv: Dataset final procesado y listo para uso.




PD: La elección del modelo es muy simple, es un auto que me gusta mucho y me compraré uno eventualmente.
