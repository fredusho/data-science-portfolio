[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fredusho/data-science-portfolio/blob/main/redes-neuronales-renuncia-clientes/renuncia-clientes.ipynb)

# Predicción de Renuncia de Clientes — Modelos de Machine Learning para Telecomunicaciones

## 🎯 Objetivo del Proyecto
Desarrollar modelos de Machine Learning para **predecir cuándo un cliente renunciará (Churn)** en una empresa de telecomunicaciones, permitiendo activar estrategias de retención con foco en clientes de alto valor.

Se aplicó un stack completo de data science:

✅ Preparación del dataset  
✅ EDA automatizado con *ydata_profiling*  
✅ Manejo de desbalance con **SMOTE**  
✅ Feature importance para priorizar insights  
✅ Modelos supervisados y métricas de clasificación  
✅ Curva ROC & AUC para evaluación robusta

📌 Dataset original: **3150 clientes**  
📌 Problema: **desbalance extremo** (Churn = 16%)

---

## 🧠 Modelos Aplicados

| Modelo | Accuracy | F1-score | AUC | Observación |
|--------|----------|---------|-----|-------------|
| **Random Forest** | **97%** | **0.97** | — | Mejor desempeño general |
| **Red Neuronal (7 mejores features)** | 93% | — | **0.95** | Excelente capacidad de discriminación |

🔍 La señal de churn es **altamente separable** tras preprocesamiento y balanceo.

---

## 🔑 Variables más importantes
Según Random Forest:

| Feature | Interpretación |
|---------|----------------|
| Status | Estado del cliente → driver principal |
| Complains | Quejas recientes → alerta crítica |
| Subscription_Length | Clientes nuevos renuncian más |
| Frequency_of_use | Menor uso = alto riesgo |
| Customer_Value | Churn peligroso si son clientes valiosos |

📌 Insights directamente accionables por estrategia comercial.

---

## 📊 Flujo de Trabajo (ETL + Modelado)
1. Carga y limpieza del dataset  
2. Normalización con **StandardScaler**  
3. Balanceo con **SMOTE**  
4. Entrenamiento y validación con **train/test split**  
5. Reportes y visualizaciones ejecutivas:
   - Matriz de clasificación
   - Feature importance
   - Curva ROC

---

## 🚀 Tecnologías utilizadas
- Python (Google Colab)
- pandas · numpy
- seaborn · matplotlib · plotly
- scikit-learn
- TensorFlow + Keras
- imblearn

---

## 🧾 Conclusiones Ejecutivas
✅ El modelo identifica clientes churn con **altísima precisión**  
✅ Feature importance permite **acciones de retención inmediatas**  
✅ Integrable fácilmente en un **pipeline MLOps real**  
✅ Caso sólido para ROI en segmentación y customer experience



