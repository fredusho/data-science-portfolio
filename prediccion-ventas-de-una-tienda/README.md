[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fredusho/data-science-portfolio/blob/main/prediccion-ventas-de-una-tienda/prediciendo-ventas-de-una-tienda.ipynb)

# Predicción de Ventas 🧾📈

## 🧩 Descripción del proyecto
Este proyecto aplica **modelos de series temporales ARIMA** para predecir las ventas mensuales de una empresa, utilizando datos históricos comprendidos entre **2015 y 2018**.  
El análisis contempla el proceso completo: desde la exploración de datos, pruebas de estacionariedad, descomposición estacional y ajuste del modelo ARIMA, hasta la evaluación del desempeño y la proyección de ventas futuras.

---

## ⚙️ Tecnologías y librerías utilizadas
- **Python 3.10+**
- **pandas / numpy**
- **matplotlib / seaborn**
- **statsmodels**
- **pmdarima**
- **scikit-learn**
- **Google Colab**

---

## 🧠 Objetivos principales
1. Analizar la evolución temporal de las ventas.  
2. Evaluar la estacionariedad mediante la prueba **Dickey-Fuller aumentada (ADF)**.  
3. Identificar los parámetros óptimos **(p, d, q)** para el modelo ARIMA usando ACF y PACF.  
4. Entrenar y ajustar el modelo con los datos históricos.  
5. Realizar predicciones para los próximos 12 meses.  
6. Evaluar el desempeño con métricas de error (**MAE**, **MSE**).

---

## 📊 Proceso de análisis

### 1️⃣ Carga y exploración inicial
Se utilizó el dataset `Sales_Data.xlsx`, conteniendo las columnas:
- **Order Date** (fecha del pedido)
- **Sales** (monto de ventas)

Se transformó la columna de fechas a tipo `datetime` y se estableció como índice temporal.

---

### 2️⃣ Visualización y descomposición
Se graficó la serie temporal para observar tendencia y estacionalidad.  
Se aplicó una **descomposición aditiva**, revelando un claro patrón estacional de frecuencia anual.

---

### 3️⃣ Prueba de estacionariedad
- **ADF Statistic:** -4.416  
- **p-value:** 0.00027  
✅ La serie es estacionaria (p < 0.05).  
Sin embargo, también se probó la diferenciación simple (d = 1) para confirmar la estabilidad.

---

### 4️⃣ Determinación de parámetros (p, d, q)
- A partir de los gráficos de **ACF** y **PACF** se establecieron:
  - **p = 3**
  - **d = 1**
  - **q = 2**

Estos parámetros se validaron empíricamente con `auto_arima()`.

---

### 5️⃣ Entrenamiento del modelo
El modelo final fue **ARIMA(3, 1, 2)**, ajustado con `statsmodels`.  
Resumen del modelo:

| Métrica | Valor |
|----------|--------|
| AIC | 1089.51 |
| BIC | 1100.61 |
| HQIC | 1093.68 |
| Ljung–Box (p) | 0.73 |
| Jarque–Bera (p) | 0.72 |

👉 Los residuos no presentan autocorrelación ni heterocedasticidad significativa, indicando un ajuste razonable.

---

### 6️⃣ Evaluación y predicciones
- **División 80/20:** entrenamiento y prueba.  
- **Predicciones a 12 meses:** el modelo fue capaz de seguir la tendencia general, aunque con desviaciones en los picos de ventas.  

**Métricas de desempeño:**
| Métrica | Valor |
|----------|--------|
| MSE | 939 690 234.88 |
| MAE | 22 237.99 |

📊 El modelo captura bien la tendencia, pero presenta errores moderados en magnitud absoluta, posiblemente atribuibles a estacionalidad no modelada o eventos externos.

---

## 🎯 Conclusiones
- El modelo **ARIMA(3, 1, 2)** se ajusta de forma adecuada a los datos históricos y genera proyecciones razonables.  
- Los resultados sugieren que el modelo **no sobreajusta** y mantiene residuos aproximadamente normales.  
- Para mejorar la precisión, se podrían explorar modelos **SARIMA** o **Prophet**, incorporando componentes estacionales explícitos.  
- El flujo de trabajo completo demuestra dominio de análisis temporal, selección de parámetros y validación estadística.

---
