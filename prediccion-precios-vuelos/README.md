[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fredusho/data-science-portfolio/blob/main/prediccion-precios-vuelos/prediccion-precios-vuelos.ipynb)


# Predicción del Precio de Vuelos ✈️💸

## 🧩 Descripción del proyecto
El objetivo de este proyecto fue **predecir el precio de boletos de avión** mediante técnicas de **Machine Learning supervisado**, utilizando datos históricos de vuelos clasificados en **economy** y **business**.  
La finalidad es ofrecer a una agencia de viajes en línea una herramienta predictiva que permita estimar precios de vuelos antes de la compra, optimizando la experiencia del cliente y las estrategias comerciales.

---

## ⚙️ Tecnologías y librerías utilizadas
- **Python 3.10+**
- **pandas / numpy**
- **matplotlib / seaborn**
- **scikit-learn**
- **xgboost / randomforest**
- **Google Colab**

---

## 🧠 Metodología: CRISP-DM
El flujo de trabajo se basó en la metodología **CRISP-DM**, que abarca:

1. **Comprensión del negocio** → Identificar el impacto del modelo para la agencia.  
2. **Comprensión de los datos** → Análisis de los datasets `economy.xlsx` y `business.xlsx`.  
3. **Preparación de los datos** → Limpieza, imputación de nulos, ingeniería de características y tratamiento de outliers.  
4. **Modelado** → Entrenamiento y comparación de distintos algoritmos de regresión.  
5. **Evaluación** → Medición del desempeño con métricas MAE, RMSE y R².  
6. **Despliegue (conceptual)** → Recomendaciones para producción y visualización.

---

## 🧹 Limpieza y preprocesamiento
- Se unificaron los datasets **economy** y **business** con una nueva variable `class`.  
- Se corrigieron valores inconsistentes en columnas como `stop` y `time_taken`.  
- Se creó la variable **`duration_min`**, convirtiendo la duración de formato “Xh Ym” a minutos.  
- Se eliminaron columnas redundantes (`ch_code`, `dep_time`, `arr_time`, etc.).  
- Se eliminaron **108 valores nulos (0.03%)** y **15 outliers** detectados mediante el rango intercuartílico (IQR).  
- Se estandarizó el precio a tipo `float64` para los cálculos posteriores.

---

## 📊 Análisis exploratorio (EDA)
- **Distribución de precios:** sesgada positivamente, con mayoría de vuelos económicos y pocos de alto valor.  
- **Curtosis:** -0.43 → distribución platicúrtica (más aplanada que la normal).  
- **Precio promedio por aerolínea:**

| Aerolínea | Precio promedio (₹) |
|------------|--------------------|
| Vistara | 30 325 |
| Air India | 23 506 |
| SpiceJet | 6 179 |
| Indigo | 5 324 |
| AirAsia | 4 091 |

- **Insight clave:** las aerolíneas premium (Vistara, Air India) mantienen precios significativamente más altos que las de bajo costo.  
- Los vuelos **business** presentan un precio medio **6× mayor** que los de clase economy.  
- Los vuelos **1-stop** son más costosos que los directos y los de múltiples escalas.

---

## ✈️ Ingeniería de características
- Conversión de variables categóricas con `pd.get_dummies()`.  
- Creación de variables derivadas:
  - `duration_min` → duración en minutos.  
  - `day` → día de la semana derivado de `date`.  
- Se identificaron patrones semanales: algunos vuelos presentan precios más bajos los **miércoles y jueves**, tendencia útil para estrategias dinámicas.

---

## 🤖 Modelado y evaluación
Se probaron los siguientes modelos de regresión:

| Modelo | R² | MAE | RMSE | Observaciones |
|---------|----|------|------|---------------|
| Regresión Lineal | 0.74 | 1 950 | 2 430 | Buen baseline, pero sensible a outliers. |
| Árbol de Decisión | 0.87 | 980 | 1 280 | Captura relaciones no lineales. |
| Random Forest | **0.92** | **790** | **1 020** | Mejor equilibrio precisión–generalización. |
| XGBoost | **0.94** | **715** | **970** | Mejor rendimiento general y estabilidad. |

✅ **Modelo final seleccionado:** `XGBoostRegressor` — por su mejor desempeño en R² y menor error absoluto.

---

## 🎯 Conclusiones
- La combinación de **características temporales y de vuelo** permitió capturar variaciones reales de precios.  
- Se comprobó que la clase del vuelo y la aerolínea son los factores más influyentes.  
- El modelo XGBoost logró un rendimiento predictivo robusto (**R² = 0.94**), ideal para una integración en entornos productivos.  
- La metodología puede extenderse a **predicción dinámica de tarifas aéreas** y sistemas de recomendación.

---
