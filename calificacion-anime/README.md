[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fredusho/data-science-portfolio/blob/main/calificacion-anime/calificacion-anime.ipynb)


# Preprocesamiento de Datos 🎬

## 🧩 Descripción del proyecto
Este proyecto tiene como objetivo **limpiar, transformar y analizar un dataset de títulos de anime y películas** extraído de IMDb, compuesto por más de **45 000 registros**.  
Se desarrolló un flujo completo de **preprocesamiento de datos** para garantizar la calidad de la información antes de su uso en modelos predictivos o análisis exploratorios.

---

## ⚙️ Tecnologías y librerías utilizadas
- **Python 3.10+**
- **pandas / numpy**
- **matplotlib / seaborn**
- **scipy.stats**
- **scikit-learn**
- **Google Colab**

---

## 🧠 Objetivos principales
1. Identificar y eliminar **duplicados y valores nulos**.  
2. Estandarizar formatos de columnas con datos inconsistentes (`Runtime`, `Number of Votes`, `Gross`).  
3. Convertir variables numéricas almacenadas como texto a tipo numérico.  
4. Detectar **outliers** con métodos estadísticos (IQR y Z-score).  
5. Aplicar transformaciones logarítmicas a variables sesgadas.  
6. Analizar correlaciones y relaciones entre variables clave.  
7. Seleccionar las variables predictivas más relevantes mediante **correlación** y **Forward Selection**.

---

## 🧹 Limpieza y transformación
- Se eliminaron **874 registros duplicados** y columnas con altos porcentajes de nulos (`Metascore`, `Year`, `Certificate`, `Summary`, `Stars`, `Episode Title`).  
- Se transformaron columnas de texto con valores numéricos mal formateados (`Number of Votes`, `Gross`, `Runtime`), eliminando comas, unidades y valores literales erróneos.  
- Se convirtieron los tipos de datos a `float64` para su análisis cuantitativo.  
- Se crearon variables logarítmicas:
  - `Number of Votes Log`
  - `Gross Log`

---

## 📊 Análisis exploratorio
### Distribuciones y outliers
- **User Rating:** distribución sesgada a calificaciones altas (7–9).  
- **Runtime:** concentración fuerte en 24 minutos → la mayoría son episodios de series animadas.  
- **Gross y Votes:** sesgo positivo; pocos títulos concentran la popularidad y el ingreso.  
- Se identificaron outliers en `Runtime` y `Gross` con IQR y Z-score, sin evidencia de errores sistemáticos.

### Correlaciones
- `Number of Votes` y `Gross` mostraron **correlación positiva** con `User Rating`.  
- `Runtime` no evidenció correlación significativa.  
- Se aplicó análisis de correlación de Pearson y visualización con `heatmap`.

---

## 🔍 Selección de variables
- Variables con **|correlación| > 0.2** respecto a `User Rating`:  
  `Episode`, `Number of Votes Log`, `Gross Log`.  
- Ambos métodos (correlación y **Forward Selection**) coincidieron en estas tres como las más relevantes para explicar la calificación de usuario.

---

## 🎯 Conclusiones
- El preprocesamiento permitió transformar un dataset caótico en una base confiable y analizable.  
- Se confirmaron **tendencias esperadas**: mayor número de votos → mayor rating y ganancias.  
- La metodología implementada —limpieza, transformación, detección de outliers y selección de variables— constituye un **pipeline robusto de preparación de datos** aplicable a futuros modelos predictivos.  

---
