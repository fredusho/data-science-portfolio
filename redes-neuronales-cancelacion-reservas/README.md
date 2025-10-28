[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fredusho/data-science-portfolio/blob/main/redes-neuronales-cancelacion-reservas/cancelacion-reservas.ipynb)


# Predicción de Cancelación de Reservas en Hoteles

## 🎯 Objetivo del Proyecto
Construir y optimizar **modelos de redes neuronales** para determinar la probabilidad de cancelación de reservas hoteleras, con impacto directo en:

- Revenue Management 💵
- Ocupación proyectada 📊
- Estrategias de overbooking y retención 🏨

Se aplicaron técnicas avanzadas de Machine Learning incluyendo:
✅ Limpieza y tratamiento de datos (nulos + outliers)  
✅ Feature Engineering + dummies  
✅ Estandarización de variables  
✅ Modelos multicapa + Grid Search con 3-fold CV  
✅ Curva ROC para evaluación robusta  

---

## 📈 Resultados Principales

| Modelo | Accuracy Entrenamiento | Accuracy Validación Cruzada | Observaciones |
|--------|----------------------|----------------------------|---------------|
| NN Modelo 1 (tanh-relu-tanh) | ~82% | — | Convergencia rápida y estable |
| NN Modelo 2 (tanh-tanh-tanh) | ~82% | — | Rendimiento sólido |
| **Mejor Modelo (Grid Search + Dropout)** | **82.17%** | **82% en test** | Regularización + arquitectura óptima |

📌 Mejor AUC ROC ≈ **0.82** → Modelo **muy útil** para clasificación real ✅

---

## 🔍 Insights accionables
Variables con mayor relación a cancelación:

| Variable | Insight estratégico |
|---------|----------------|
| lead_time | Reservas con mucha anticipación = **mayor riesgo** |
| previous_cancellations | Historial negativo → alerta inmediata |
| deposit_type | *No-Refund* reduce cancelaciones |
| is_repeated_guest | Los clientes recurrentes cancelan menos |
| total_of_special_requests | A más solicitudes → mayor compromiso |

---

## 📊 Flujo de Trabajo
1️⃣ Análisis exploratorio (EDA)  
2️⃣ Limpieza: eliminación & imputación de nulos  
3️⃣ Outliers en precio (ADR) → IQR + imputación inteligente  
4️⃣ Dummy encoding + escalado con StandardScaler  
5️⃣ Entrenamiento y optimización con GridSearchCV  
6️⃣ Métricas: Confusion Matrix / F1 / ROC-AUC

---

## 🚀 Tecnologías utilizadas
- Python · Google Colab  
- pandas · numpy · seaborn · matplotlib  
- TensorFlow · Keras · scikeras  
- scikit-learn · GridSearchCV  
- ROC-AUC para evaluación clínica del clasificador  

---

## ✅ Conclusiones Ejecutivas
✔ El modelo reduce incertidumbre en la gestión de reservas  
✔ Ayuda a prevenir baja ocupación y pérdidas por cancelación  
✔ Implementable en **pipelines de revenue management**  
✔ Identifica huéspedes de riesgo con excelente precisión  

> 💡 Beneficio directo: decisiones más inteligentes en overbooking, pricing y retención.

