[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fredusho/data-science-portfolio/blob/main/machine-learning/machine-learning-regresion-lineal.ipynb)


# Introducción al Machine Learning

## 🧩 Descripción del proyecto
Este proyecto corresponde al módulo **Introducción al Machine Learning**, donde se abordan los fundamentos del aprendizaje supervisado y no supervisado, las diferencias entre ambos enfoques y su aplicación práctica en un modelo predictivo utilizando un conjunto de datos inmobiliarios.  
Se aplica una **regresión lineal** para predecir precios de viviendas en función de características estructurales y de servicios.

---

## ⚙️ Tecnologías y librerías utilizadas
- **Python 3.10+**
- **pandas / numpy**
- **matplotlib / seaborn**
- **scikit-learn**

---

## 🧠 Objetivos principales
1. **Comprender las diferencias conceptuales** entre:
   - Aprendizaje supervisado vs. no supervisado  
   - Regresión vs. clasificación
2. **Aplicar conceptos teóricos** a un caso práctico de predicción de precios.
3. **Implementar un modelo de regresión lineal** con `scikit-learn`.
4. **Evaluar el modelo** con métricas cuantitativas (MSE, R²) y visualización de resultados.

---

## 📊 Flujo de trabajo

1. **Exploración y limpieza de datos**
   - Se analiza el dataset `data-housing.xlsx` (545 registros).  
   - Conversión de variables categóricas (“yes/no”) a binarias (1/0).  
   - Detección de outliers mediante boxplots.  
   - Análisis de correlación entre variables predictoras.

2. **División del dataset**
   - 80% entrenamiento / 20% prueba con `train_test_split()`.

3. **Entrenamiento del modelo**
   - Implementación de `LinearRegression()` de `sklearn`.  
   - Ajuste del modelo sobre los datos de entrenamiento.

4. **Evaluación**
   - Métricas de rendimiento:
     - MSE entrenamiento: **1.14 × 10¹²**
     - MSE prueba: **1.96 × 10¹²**
     - R² entrenamiento: **0.63**
     - R² prueba: **0.61**
   - Interpretación: el modelo explica un **61% de la variabilidad** del precio.

5. **Visualización**
   - Gráficos de correlación, importancia de coeficientes y comparación de valores reales vs. predichos.


