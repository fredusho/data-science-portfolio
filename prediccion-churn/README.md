[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fredusho/data-science-portfolio/blob/main/prediccion-churn/prediccion-churn.ipynb)

# Predicción de Fuga de Clientes (Churn Prediction)

## 🧩 Descripción del proyecto
Este proyecto implementa un modelo de **aprendizaje supervisado para predecir la fuga de clientes (churn)** en una empresa de telecomunicaciones, utilizando técnicas de clasificación con Python y scikit-learn.  
El objetivo es identificar a los clientes con mayor probabilidad de abandonar el servicio, apoyando estrategias de retención y marketing personalizado.

---

## ⚙️ Tecnologías y librerías utilizadas
- **Python 3.10+**
- **pandas / numpy**
- **matplotlib / seaborn**
- **scikit-learn**
- **Google Colab**

---

## 🧠 Objetivos principales
1. Analizar y limpiar el dataset `Telco-Customer-Churn.xlsx`.  
2. Preparar los datos mediante **codificación, normalización y manejo de valores nulos**.  
3. Entrenar y comparar tres modelos de clasificación:
   - **Regresión Logística**
   - **Árbol de Decisión**
   - **Random Forest**
4. Evaluar el rendimiento con métricas de clasificación, precisión y AUC-ROC.  
5. Determinar el modelo más eficiente para predecir la fuga de clientes.

---

## 📊 Flujo de trabajo

### 1️⃣ Análisis exploratorio y calidad de datos
- Dataset con **7.043 registros** y **20 columnas** (numéricas y categóricas).  
- Solo la columna `TotalCharges` presentó 11 valores nulos (0.16%).  
- Se detectaron y eliminaron columnas irrelevantes como `customerID`.  
- Codificación de variables categóricas con `LabelEncoder`.  
- Estandarización de variables numéricas (`tenure`, `MonthlyCharges`, `TotalCharges`) mediante `StandardScaler`.

### 2️⃣ División del dataset
- 80% entrenamiento / 20% prueba, estratificado por la variable `Churn`.  
- Distribución de clases: **73.4% no fugados**, **26.6% fugados**.

### 3️⃣ Entrenamiento y optimización
Modelos entrenados con **GridSearchCV** y validación cruzada (5 folds).  
- **Regresión Logística:** mejor configuración → `C=0.01, penalty='l2', solver='saga'`.  
- **Árbol de Decisión:** `max_depth=5, min_samples_leaf=2, min_samples_split=10`.  
- **Random Forest:** `n_estimators=50, max_depth=10, min_samples_leaf=2, min_samples_split=10`.

### 4️⃣ Resultados de rendimiento

| Modelo | Accuracy | AUC-ROC | Especificidad | Comentario |
|--------|-----------|----------|----------------|-------------|
| Regresión Logística | 0.787 | 0.829 | 0.892 | Buen equilibrio entre precisión y recall |
| Árbol de Decisión | 0.782 | 0.819 | 0.884 | Modelo interpretable, menor generalización |
| Random Forest | **0.790** | **0.833** | **0.899** | Mejor desempeño global y estabilidad |

---

## 🎯 Conclusiones
- El modelo de **Random Forest** obtuvo los mejores resultados (AUC = 0.833, Accuracy = 79%).  
- Todos los modelos mostraron un **alto desempeño en la clase “no fugado”**, pero dificultades para identificar correctamente a los clientes que sí se fugan.  
- Se recomienda:
  - Ajustar el umbral de clasificación.  
  - Aplicar técnicas de **balanceo de clases (SMOTE o undersampling)**.  
  - Evaluar modelos más complejos como **XGBoost** o **LightGBM**.



