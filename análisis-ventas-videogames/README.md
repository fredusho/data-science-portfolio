
# Análisis de Ventas Globales de Videojuegos (Kaggle – Video Game Sales)

Este repositorio contiene un análisis exploratorio de datos (EDA) del dataset **“Video Game Sales”** de Kaggle.  
El objetivo es entender la evolución del mercado de videojuegos, identificar las plataformas y géneros más importantes y profundizar en el **pico histórico de ventas del año 2008**.

---

## 🗂 Dataset

- **Fuente:** Kaggle – *Video Game Sales Dataset* de Volodymyr Pivoshenko  
- **Archivo usado:** `video_games_sales.csv`
- **Granularidad:** nivel juego/plataforma
- **Campos principales:**
  - `Rank`: ranking global de ventas
  - `Name`: nombre del videojuego
  - `Platform`: plataforma (Wii, DS, PS2, PS3, X360, etc.)
  - `Year`: año de lanzamiento
  - `Genre`: género (Action, Sports, Racing, Role-Playing, etc.)
  - `Publisher`: distribuidor/desarrollador
  - `NA_Sales`, `EU_Sales`, `JP_Sales`, `Other_Sales`: ventas por región  
  - `Global_Sales`: ventas globales (en **millones de copias**)

> Nota: `Global_Sales ≈ NA_Sales + EU_Sales + JP_Sales + Other_Sales`, con pequeñas diferencias por redondeo.

---

## 🎯 Objetivos del proyecto

1. **EDA general del mercado de videojuegos**:
   - Evolución de las ventas globales en el tiempo.
   - Ranking de plataformas más importantes.
   - Distribución de ventas por género.

2. **Profundizar en el año 2008**:
   - Entender por qué es el punto máximo de ventas.
   - Analizar el aporte de cada **plataforma**, **género** y **publisher**.
   - Generar visualizaciones profesionales para compartir en LinkedIn.

3. **Dejar una base reutilizable**:
   - Código limpio en Python (Google Colab).
   - Gráficos interactivos con Plotly para presentaciones y redes.

---

## 🧹 Preparación y limpieza de los datos

### 1. Estandarización de columnas

Se normalizan los nombres de columnas para trabajar de forma consistente en Python:

```python
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
)   


#fggfdg
