[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fredusho/data-science-portfolio/blob/main/regresion-lineal/regresion-lineal.ipynb)

# Desafío – Regresión Lineal

**Autor:** Freddy González  
**Fecha:** Octubre 2025  
**Entorno:** Google Colab – Python – Pandas – Scikit-learn – Seaborn – Matplotlib  

---

## 🧠 Descripción general

Este proyecto aplica técnicas de **regresión lineal simple y múltiple** para modelar la relación entre las **dimensiones físicas de peces** (longitudes, altura, ancho y volumen) y su **peso**, utilizando el dataset `Fish.csv`.  

El análisis incluye la creación de una nueva variable geométrica (volumen del pez), el cálculo de correlaciones entre variables, la construcción de modelos predictivos globales y por especie, y la comparación de sus desempeños mediante métricas estadísticas.

---

## 🎯 Objetivos del proyecto

1. **Crear una variable derivada**:  
   Calcular el volumen de cada pez asumiendo su cuerpo como un cilindro:
   \[
   \text{Volumen} = \pi \times \left(\frac{\text{Width}}{2}\right)^2 \times \text{Height}
   \]

2. **Analizar correlaciones** entre las variables numéricas (peso, longitudes, ancho, altura, volumen).

3. **Construir un modelo de regresión lineal simple** para estimar el peso del pez a partir del volumen, evaluando su desempeño con:
   - Error cuadrático medio (MSE)
   - Coeficiente de determinación (R²)

4. **Comparar el modelo por especie**, evaluando los resultados individuales.

5. **Desarrollar un modelo de regresión multivariable** que incorpore todas las dimensiones del pez y evaluar su robustez predictiva.

---

## 🧩 Dataset utilizado

**Archivo:** `Fish.csv`  
**Tamaño:** 159 registros × 7 columnas  

**Variables:**
- `Species`: especie del pez.  
- `Weight`: peso (g).  
- `Length1`, `Length2`, `Length3`: longitudes del pez (cm).  
- `Height`: altura (cm).  
- `Width`: ancho (cm).  
- `Volume`: volumen calculado (cm³).  

---

## 📊 Exploración y correlación de variables

El análisis inicial reveló **altas correlaciones** entre el peso (`Weight`) y las longitudes (`Length1–3`), la altura (`Height`), el ancho (`Width`) y el volumen (`Volume`).

| Variable | Correlación con Weight |
|-----------|------------------------|
| Length1 | 0.92 |
| Length2 | 0.92 |
| Length3 | 0.92 |
| Height | 0.72 |
| Width | 0.89 |
| Volume | 0.88 |

📈 Se utilizó un **mapa de calor (heatmap)** y un **pairplot** de Seaborn para visualizar las relaciones lineales entre variables.

---

## ⚙️ Modelos desarrollados

### 🔹 1. Regresión lineal simple (Volumen → Peso)
- **MSE:** 16,163.84  
- **R²:** 0.89  

> El modelo explica el 89% de la variabilidad del peso a partir del volumen.  
> Sin embargo, existen diferencias entre especies que afectan la generalización.

---

### 🔹 2. Regresiones por especie

| Especie | MSE | R² |
|----------|-----|----|
| Bream | 5,269.55 | 0.84 |
| Roach | 221.53 | 0.98 |
| Whitefish | 5,541.42 | 0.00 |
| Parkki | 57.28 | 0.99 |
| Perch | 4,747.57 | 0.96 |
| Pike | 62,308.96 | 0.80 |
| Smelt | 2.98 | 0.56 |

> Al modelar cada especie por separado, el rendimiento mejora significativamente, evidenciando que cada grupo tiene patrones propios de crecimiento y densidad.

---

### 🔹 3. Regresión multivariable

**Variables predictoras:** `Length1`, `Length2`, `Length3`, `Height`, `Width`, `Volume`  
**Variable dependiente:** `Weight`

- **MSE:** 5,329.84  
- **R²:** 0.96  

📊 **Interpretación:**  
El modelo multivariable explica el **96% de la variabilidad del peso**, con errores moderados. Es un modelo **robusto y altamente predictivo**.

---

## 📈 Visualizaciones

- **Matriz de correlación:** detección de relaciones lineales fuertes.  
- **Gráficos de dispersión (scatter plots):** peso vs volumen, con línea de regresión.  
- **Gráfico de comparación predicción vs realidad:** en el modelo multivariable.

---

## 🧮 Conclusiones

- El volumen calculado geométricamente es un **predictor válido** del peso, aunque limitado cuando se combinan especies.  
- Los modelos por especie logran **ajustes superiores (R² > 0.9)**, lo que indica patrones biológicos diferenciados.  
- La **regresión multivariable** ofrece un modelo global sólido con **R² = 0.96**, evidenciando un excelente poder explicativo.  
- Se recomienda explorar modelos polinomiales o de regularización (Ridge/Lasso) para mejorar la precisión.

---

## 🛠️ Tecnologías utilizadas
- **Python 3.10+**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Seaborn**
- **Matplotlib**
- **Google Colab**


---

## ✍️ Autor
**Freddy González**  
Data Scientist  
📂 [GitHub](https://github.com/fredusho/data-science-portfolio)  
💼 [LinkedIn](https://linkedin.com/in/freddygonzalezsandoval)


