[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fredusho/data-science-portfolio/blob/main/preparacion-de-datos-y-graficos/prep-datos-graficos.ipynb)


# Preparación de Datos y Gráficos

**Autor:** Freddy González  
**Fecha:** Octubre 2025  
**Entorno:** Google Colab – Python – Pandas – Seaborn – Matplotlib  

---

## 🧠 Descripción general

Este proyecto tiene como objetivo realizar un **análisis exploratorio y limpieza de datos a nivel mundial**, utilizando el dataset `world-data-2023.csv`.  
Se implementan técnicas de **transformación, normalización, detección de outliers** y **visualización de correlaciones** entre variables demográficas, económicas y sanitarias.

El análisis abarca más de 190 países e incluye variables como población, PIB, tasa de natalidad, expectativa de vida, mortalidad materna e infantil, y cantidad de médicos por cada mil habitantes.

---

## 🎯 Objetivos del proyecto

1. **Explorar y limpiar el dataset original**
   - Conversión de columnas con porcentajes, símbolos monetarios y comas a formato numérico.
   - Estandarización de tipos de datos.
   - Eliminación de columnas irrelevantes para el análisis.

2. **Analizar correlaciones entre variables clave**
   - Construcción de una **matriz de correlación** completa y un **mapa de calor**.
   - Identificación de relaciones lineales fuertes (positivas y negativas).

3. **Evaluar pares de variables con mayor correlación**
   - Expectativa de vida vs. mortalidad materna.  
   - Expectativa de vida vs. mortalidad infantil.  
   - Expectativa de vida vs. médicos por cada mil habitantes.

4. **Aplicar métodos de limpieza estadística**
   - Eliminación de valores faltantes y outliers mediante el rango intercuartílico (IQR).  
   - Comparación de correlaciones antes y después del proceso de limpieza.

5. **Visualizar relaciones clave**
   - Gráficos de dispersión para las correlaciones mencionadas.  
   - Representación de la relación entre población y PIB utilizando escalas logarítmicas.

---

## 📊 Resultados principales

| Relación Analizada | Correlación Antes | Correlación Después | Interpretación |
|--------------------|------------------|---------------------|----------------|
| Expectativa de vida vs. Mortalidad materna | -0.87 | -0.81 | Fuerte relación negativa, los países con mayor expectativa de vida presentan menor mortalidad materna. |
| Expectativa de vida vs. Mortalidad infantil | -0.92 | -0.91 | Correlación negativa robusta, eliminando valores extremos se mejora la precisión. |
| Expectativa de vida vs. Médicos por 1000 hab. | +0.70 | +0.74 | Mayor cantidad de médicos se asocia a una mayor esperanza de vida. |

El **gráfico Población vs PIB** evidenció una **tendencia positiva**: los países con mayor población tienden a tener un PIB más alto, aunque con gran dispersión.  
La escala logarítmica permitió observar mejor la distribución global de los datos.

---

## ⚙️ Metodología

1. Limpieza de columnas con funciones personalizadas:
   - `clean_percentage()` → elimina “%” y convierte a float.  
   - `clean_currency()` → remueve símbolos monetarios y comas.  
   - `clean_numeric()` → convierte números con separadores a formato flotante.

2. Detección y tratamiento de valores faltantes:
   - Eliminación directa (`dropna`) o imputación con medidas centrales.

3. Detección de outliers:
   - Aplicación del método del **IQR (Interquartile Range)**.

4. Visualización:
   - **Heatmaps** de correlación (`seaborn.heatmap`)  
   - **Scatter plots** comparativos antes y después de la limpieza.  
   - **Distribuciones** (`sns.histplot`) y gráficos bivariados.

---

## 🛠️ Tecnologías utilizadas
- **Python 3.10+**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Google Colab**

## 📈 Conclusiones

- La limpieza de datos es esencial para obtener correlaciones confiables.  
- El **IQR** es un método eficaz para remover valores atípicos sin sesgar los resultados.  
- Las variables sanitarias (mortalidad y médicos) tienen alta relación con la esperanza de vida.  
- Se evidencian fuertes dependencias lineales negativas entre mortalidad y longevidad.  
- El análisis demuestra la importancia de la estandarización y la correcta selección de gráficos para comunicar resultados.

---

## ✍️ Autor
**Freddy González**  
Data Scientist  
📂 [GitHub](https://github.com/fredusho/data-science-portfolio)  
💼 [LinkedIn](https://linkedin.com/in/freddygonzalezsandoval)


