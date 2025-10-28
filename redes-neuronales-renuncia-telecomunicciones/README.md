[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fredusho/data-science-portfolio/blob/main/redes-neuronales-renuncia-telecomunicciones/renuncia-telecomunicaciones.ipynb)

# Predicción de Renuncia de Clientes en Telecomunicaciones 📡📉

## 🧩 Descripción del proyecto
El objetivo de este proyecto es **predecir la renuncia (churn)** de clientes de una empresa de telecomunicaciones utilizando modelos de **aprendizaje supervisado**, con enfoque en **árboles de decisión y técnicas de ensamble** como **Bagging** y **Random Forest**.

Se desarrolla un flujo completo de análisis exploratorio, correlaciones, selección de variables, modelado, optimización de hiperparámetros y validación.

---

## ⚙️ Tecnologías y librerías utilizadas
- Python 3.10+
- pandas / numpy
- seaborn / matplotlib
- scikit-learn
- Google Colab

---

## 🧠 Objetivos principales
1. Analizar los factores que influyen en la renuncia de clientes.
2. Entrenar un modelo predictivo para identificar clientes en riesgo.
3. Mejorar los modelos con técnicas de ensamble y tunning (GridSearchCV).
4. Evaluar el modelo mediante métricas de clasificación (Accuracy, F1-Score).
5. Identificar los clientes con mayor probabilidad de abandono.

---

## 📊 Flujo analítico y resultados

### 🔹 Modelo Árbol de Decisión (básico)
- **Accuracy:** 0.892
- Evidente **overfitting** (100% en entrenamiento vs 89% en test)

### 🔹 Árbol de Decisión optimizado (GridSearchCV)
- **Accuracy:** 0.905
- Mejor generalización → sobreajuste controlado

### 🔹 Bagging heterogéneo
- **Accuracy:** 1.000
- **F1-score:** 1.000  
- Clasificación perfecta en test

### 🔹 Random Forest (modelo final)
- **Accuracy en test:** **1.000**
- **F1-score:** **1.000**
- **OOB Score:** 0.943 (confirmando buena generalización)
- Variables más importantes:
  1. CustServCalls
  2. DayMins
  3. MonthlyCharge
  4. AccountWeeks

📌 Insights clave:  
- Clientes con **alto uso de minutos**, **mayor facturación** y **más llamadas a soporte** son los que más renuncian.
- El modelo permite **detectar riesgo temprano** y aplicar estrategias de retención.

---

## 🎯 Conclusiones
- Los modelos basados en ensamble (**Random Forest y Bagging**) obtuvieron el mejor desempeño.
- Se logró una predicción perfecta en test en este dataset.
- Se recomienda monitorear el **desbalance de clases** y utilizar métricas más estrictas en escenarios reales.
- Los índices de importancia facilitan el **diseño de campañas de retención** enfocadas en clientes críticos.
