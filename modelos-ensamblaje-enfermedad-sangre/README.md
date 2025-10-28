
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fredusho/data-science-portfolio/blob/main/modelos-ensamblaje-enfermedad-sangre/enfermedad-sangre.ipynb)

# Detección de Enfermedad en la Sangre 🩸 — Modelos Predictivos en Salud

## 🧩 Descripción del proyecto
El objetivo de este proyecto es **predecir la presencia de posibles enfermedades en la sangre** (principalmente relacionadas a función hepática) utilizando datos clínicos como indicadores sanguíneos, enzimas hepáticas y colesterol.

Se realizaron procesos completos de:
✅ Limpieza de datos  
✅ Imputación de valores faltantes  
✅ Detección y tratamiento de outliers (Winsorization)  
✅ Estandarización  
✅ Entrenamiento de modelos supervisados  
✅ Comparación de desempeño

---

## ⚙️ Librerías y tecnologías utilizadas
- **Python + Google Colab**
- pandas / numpy
- seaborn / matplotlib / plotly
- scikit-learn (LogisticRegressionCV)
- XGBoost
- SciPy

---

## 🧠 Objetivos del análisis
1. Identificar marcadores sanguíneos asociados a enfermedad hepática.
2. Preparar los datos correctamente para modelos ML clínicos.
3. Comparar el desempeño entre:
   - **Regresión Logística ElasticNet**
   - **XGBoost**
4. Identificar variables clínicas de mayor impacto en la predicción.
5. Evaluar mediante métricas robustas de clasificación.

---

## 🩺 Variables clínicas evaluadas
| Variable | Descripción |
|---------|-------------|
| AST, ALT, GGT | Enzimas hepáticas clave |
| CHOL, BIL, ALB | Marcadores de metabolismo |
| Age, Sex | Variables demográficas |

Estas son **estándar en diagnósticos hepáticos clínicos**.

---

## 🧪 Limpieza y preprocesamiento
- Eliminación de columnas irrelevantes (ID)
- Codificación de categorías objetivo (`0 = Donante sano`, `1 = En riesgo`)
- Imputación según clase cuando los faltantes superaban 1%
- Winsorización del 5% en variables con muchos outliers
- **Estandarización con StandardScaler**
- Visualización post–winsor y post–scaling para validación

✅ Dataset listo para aplicaciones en salud digital

---

## 📊 Modelos y resultados

| Modelo | Precision | Recall | F1-score | Accuracy |
|--------|----------|--------|----------|----------|
| **Logistic Regression (ElasticNet)** | **0.96** | 0.80 | **0.87** | **0.97** |
| **XGBoost (GridSearchCV)** | 0.95 | **0.80** | 0.84 | 0.96 |

📌 Conclusión:  
- **Ambos modelos entregan un excelente rendimiento**
- **ElasticNet**: mejor balance general  
- **XGBoost**: más robusto frente a relaciones no lineales  

---

## 🔍 Variables más importantes (ElasticNet)
| Variable | Interpretación |
|---------|----------------|
| AST | Daño hepático → aumenta riesgo |
| GGT | Otro marcador hepático → crítico |
| ALT | Relación inversa en este dataset puntual |

✅ Coincide con fisiología clínica real

---

## 🎯 Conclusiones
- Se logró **detectar casos en riesgo con alta efectividad**
- Flujo aplicado es **apto para proyectos médicos reales**
- Modelos permiten **alerta temprana** para intervención preventiva
- Se aconseja aplicar:
  - Balanceo de clases
  - Más datos demográficos y de historial clínico

> El resultado es una base sólida para implementar un **sistema inteligente de apoyo clínico**.
---
