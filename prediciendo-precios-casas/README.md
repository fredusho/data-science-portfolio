[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fredusho/data-science-portfolio/blob/main/prediciendo-precios-casas/prediciendo-precios-casas.ipynb)


# Predicción de Precios de Casas 🏠

## 🧩 Descripción del proyecto
El objetivo de este proyecto fue **predecir el precio de viviendas** a partir de sus características estructurales, ubicación y estado general, aplicando diferentes modelos de **regresión supervisada**.  
El dataset, que contiene más de 21 000 registros, fue sometido a un proceso riguroso de limpieza, exploración, análisis de correlaciones y modelado predictivo.

---

## ⚙️ Tecnologías y librerías utilizadas
- **Python 3.10+**
- **pandas**, **numpy**
- **matplotlib**, **seaborn**
- **scikit-learn**
- **Google Colab**

---

## 🧠 Objetivos principales
1. Analizar la calidad de los datos y eliminar valores atípicos y extremos.  
2. Transformar y limpiar las variables relevantes (`price`, `sqft_living`, `bedrooms`, `bathrooms`, etc.).  
3. Evaluar la correlación entre variables y el precio de las casas.  
4. Dividir el dataset en conjuntos de entrenamiento y prueba.  
5. Implementar y comparar los siguientes modelos:
   - **Regresión Ridge**
   - **Regresión Lasso**
   - **Elastic Net**
   - **Árbol de Decisión (DecisionTreeRegressor)**  
6. Evaluar el rendimiento de cada modelo utilizando **R²**, **RMSE** y **Score de entrenamiento y prueba**.

---

## 🧹 Limpieza y transformación de datos
- Se eliminaron valores atípicos mediante el rango intercuartílico (IQR) en variables críticas.  
- Se transformaron fechas a tipo `datetime`.  
- Se descartaron registros con valores absurdos (`bedrooms = 33`, `price > 7M`).  
- Se detectó que variables como `waterfront`, `view` y `yr_renovated` presentaban alto desbalance, lo cual se consideró en el análisis.

Después del proceso de limpieza, el dataset pasó de **21 613 a 16 803 registros válidos**, garantizando una muestra sólida y representativa.

---

## 📈 Análisis exploratorio
- Las variables **grade (0.56)**, **sqft_living (0.55)** y **lat (0.47)** mostraron la mayor correlación positiva con el precio.  
- Se confirmaron relaciones esperables: casas más grandes, con mejor calificación o mejor ubicación, tienden a tener precios más altos.  
- El análisis visual incluyó **mapas de calor de correlaciones**, **resúmenes estadísticos** y **distribuciones de precios**.

---

## 🤖 Modelado y evaluación

| Modelo | RMSE | R² | Train Score | Test Score |
|---------|------|----|--------------|-------------|
| Ridge | 107 894 | 0.687 | 0.679 | 0.687 |
| Lasso | 107 893 | 0.687 | 0.679 | 0.687 |
| Elastic Net | 107 893 | 0.687 | 0.679 | 0.687 |
| Árbol de Regresión | **101 895** | **0.721** | 0.998 | **0.721** |

---

## 📊 Resultados y conclusiones
- Los modelos **Ridge, Lasso y Elastic Net** obtuvieron resultados similares, con un **R² ≈ 0.68**, explicando cerca del 68 % de la variabilidad del precio.  
- El **Árbol de Decisión** mejoró el desempeño general (**R² = 0.72**) pero mostró signos de sobreajuste, con un puntaje de entrenamiento casi perfecto (0.998).  
- El modelo más equilibrado en términos de precisión y estabilidad fue **Ridge Regression con α ≈ 10**, evitando underfitting y manteniendo un error estable.  
- En términos prácticos, el modelo logra una **predicción razonable del valor de vivienda** y puede ampliarse fácilmente con variables de ubicación, amenidades y entorno.

---
