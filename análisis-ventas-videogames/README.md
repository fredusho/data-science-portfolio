

Análisis de Ventas Globales de Videojuegos (Kaggle – Video Game Sales)
Este repositorio contiene un análisis exploratorio de datos (EDA) del dataset “Video Game Sales” de Kaggle.
El objetivo es entender la evolución del mercado de videojuegos, identificar las plataformas y géneros más importantes y profundizar en el pico histórico de ventas del año 2008.
🗂 Dataset
Fuente: Kaggle – Video Game Sales Dataset de Volodymyr Pivoshenko
Archivo usado: video_games_sales.csv
Granularidad: nivel juego/plataforma
Campos principales:
Rank: ranking global de ventas
Name: nombre del videojuego
Platform: plataforma (Wii, DS, PS2, PS3, X360, etc.)
Year: año de lanzamiento
Genre: género (Action, Sports, Racing, Role-Playing, etc.)
Publisher: distribuidor/desarrollador
NA_Sales, EU_Sales, JP_Sales, Other_Sales: ventas por región
Global_Sales: ventas globales (en millones de copias)
Global_Sales ≈ NA_Sales + EU_Sales + JP_Sales + Other_Sales, con pequeñas diferencias por redondeo.
🎯 Objetivos del proyecto
EDA general del mercado de videojuegos
Evolución de las ventas globales en el tiempo.
Ranking de plataformas más importantes.
Distribución de ventas por género.
Profundizar en el año 2008
Entender por qué es el punto máximo de ventas.
Analizar el aporte de cada plataforma, género y publisher.
Generar visualizaciones profesionales para compartir en LinkedIn.
Dejar una base reutilizable
Código limpio en Python (Google Colab).
Gráficos interactivos con Plotly para presentaciones y redes.
🧹 Preparación y limpieza de los datos
1. Estandarización de columnas
Se normalizan los nombres de columnas para trabajar de forma consistente en Python:
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
)
Columnas finales:
['rank', 'name', 'platform', 'year', 'genre', 'publisher',
 'na_sales', 'eu_sales', 'jp_sales', 'other_sales', 'global_sales']
2. Tipos de datos
rank: entero
name, platform, genre, publisher: categóricas (object)
year: convertida de float64 a entero “nullable” (Int64)
*_sales: float64 (ventas en millones de copias)
Conversión de year:
df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")
3. Validación de ventas
Se crea una columna auxiliar para validar Global_Sales:
df["ventas_regiones"] = (
    df["na_sales"] + df["eu_sales"] + df["jp_sales"] + df["other_sales"]
)

(df["global_sales"] - df["ventas_regiones"]).describe()
El resultado muestra diferencias en el rango [-0.02, 0.02] millones → compatible con redondeos.
4. Manejo de años
Distribución de registros por año:
Datos desde 1980 hasta 2016 con buena densidad.
Muy pocos registros en 2017 y 2020.
271 filas con year = <NA>.
Para análisis temporal se crea un dataframe filtrado:
df_year = df[df["year"].notna()].copy()
df_year = df_year[df_year["year"].between(1980, 2016)]
📊 Visualizaciones principales
Todas las visualizaciones se generan con Plotly para obtener gráficos interactivos y con estética profesional.
1. Evolución de las ventas globales (1980–2016)
Gráfico de línea que muestra las ventas globales por año:
Fuerte crecimiento desde finales de los 90.
Pico máximo en 2008–2009.
Caída progresiva posterior, asociada a cambios en el modelo de negocio (digitalización, móviles, etc., fuera del alcance del dataset).
Variables:
Eje X: year
Eje Y: global_sales (millones de copias)
2. Top 10 plataformas por ventas globales acumuladas
Gráfico de barras horizontales:
Muestra las 10 plataformas con mayor volumen de ventas globales.
Consolas de Nintendo, PlayStation y Xbox dominan el ranking.
Destacan consolas como PS2, Wii, DS, PS3, X360, entre otras.
3. Ventas globales por género
Gráfico de barras por genre:
Géneros como Action, Sports y Shooter concentran buena parte del mercado.
Géneros más nicho (Strategy, Puzzle, Adventure) presentan menor volumen, pero son relevantes para la diversidad del catálogo.
🔎 Análisis específico del año 2008
El año 2008 aparece como el máximo histórico en ventas globales dentro del dataset.
1. Magnitud del año 2008
Nº de juegos registrados: ≈ 1.428
Ventas globales agregadas: ≈ 679 millones de copias
2. Plataformas líderes en 2008
Agregación por platform:
Wii
Nintendo DS (DS)
Xbox 360 (X360)
PlayStation 3 (PS3)
Estas cuatro plataformas concentran la mayor parte de las ventas de 2008, reflejando la madurez de la séptima generación de consolas.
3. Géneros dominantes en 2008
Agregación por genre:
Action
Sports
Misc (party/familiares, muy asociados a Wii/DS)
Racing
Role-Playing
Shooter
La combinación de blockbusters de acción y shooters HD (GTA, Call of Duty, etc.) con títulos familiares y casuales (Wii, DS) explica gran parte del pico de ventas.
4. Publishers protagonistas en 2008
Agregación por publisher:
Nintendo
Electronic Arts
Activision
Ubisoft
Take-Two Interactive
Otros: Sega, THQ, Konami, Sony Computer Entertainment, Disney, etc.
Nintendo domina con Wii y DS, mientras que EA, Activision, Ubisoft y Take-Two aportan grandes franquicias multiplataforma.
5. Treemap 2008: plataforma → género → publisher
Para visualizar en un solo gráfico la composición del mercado 2008, se construye un treemap interactivo con la jerarquía:
Nivel 1: platform
Nivel 2: genre
Nivel 3: publisher (solo top publishers para evitar ruido visual)
El tamaño de cada bloque corresponde a global_sales (millones de copias) y permite ver de forma intuitiva:
El peso relativo de Wii y DS frente a otras plataformas.
Qué géneros lideran en cada plataforma.
Cómo se distribuyen las ventas entre los principales publishers.
🧪 Tecnologías utilizadas
Python
Pandas → carga, limpieza y agregación de datos
Plotly Express → gráficos interactivos
Google Colab → entorno de ejecución
▶️ Cómo ejecutar el análisis
Clonar este repositorio:
git clone https://github.com/fredusho/data-science-portfolio.git
Abrir el notebook correspondiente a este proyecto (ruta sugerida, ajusta según tu estructura):
video-game-sales/video_game_sales_eda.ipynb
Cargar el dataset video_games_sales.csv en la ruta esperada (por ejemplo /content/video_games_sales.csv si usas Colab).
Ejecutar las celdas secuencialmente:
Importación de librerías
Carga y limpieza de datos
Análisis exploratorio
Visualizaciones globales
Análisis detallado del año 2008
🚀 Posibles extensiones
Modelos de machine learning para predecir Global_Sales en función de plataforma, género, año y publisher.
Análisis específico por región:
Comparación de preferencias entre NA, EU, JP.
Análisis de vida útil por consola:
Ventas por plataforma a lo largo de su ciclo (año de lanzamiento vs madurez).
Segmentación de juegos por perfil (casual vs core, familia vs competitivo, etc.).
👤 Autor
Proyecto desarrollado por Freddy González – Data Scientist.
Portafolio GitHub:
👉 https://github.com/fredusho/data-science-portfolio
LinkedIn:
👉 https://linkedin.com/in/freddygonzalezsandoval
Si utilizas este trabajo como base para tus propios análisis o visualizaciones, se agradece la mención al autor y al dataset original de Kaggle.
