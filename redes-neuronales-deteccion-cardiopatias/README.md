[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fredusho/data-science-portfolio/blob/main/redes-neuronales-deteccion-cardiopatias/deteccion-cardiopatia.ipynb)

# Detección de Cardiopatía ❤️‍🩹 — Machine Learning para diagnóstico temprano

## 🧩 Descripción del proyecto
El objetivo de este proyecto es **predecir la presencia de enfermedad cardíaca** a partir de variables clínicas de pacientes, utilizando **modelos de clasificación supervisada basados en ensambles**:  
- **AdaBoost**
- **Gradient Boosting**
- **XGBoost**

Los datos provienen de estudios cardiológicos realizados en diferentes países, combinados en un solo dataset con 720 pacientes.

Este tipo de modelo puede ayudar a **identificar casos de riesgo**, facilitando acciones preventivas en el ámbito clínico.

---

## ⚙️ Tecnologías utilizadas
- Python 3.10+
- pandas, numpy
- seaborn, matplotlib
- scikit-learn
- XGBoost
- Google Colab

---

## 🧠 Objetivos del análisis
1. Limpiar y unificar estructuras de múltiples fuentes de datos médicos.
2. Manejar valores faltantes mediante estrategias mixtas:
   - Eliminación por alto porcentaje de nulos
   - Imputación por clase (pacientes sanos vs enfermos)
3. Crear variables dummies para variables categóricas.
4. Entrenar, comparar y optimizar modelos predictivos.
5. Seleccionar el modelo con mejor balance de precisión y discriminación.

---

## 🩺 Conocimiento médico relevante del dataset
- **thalach**: frecuencia cardíaca máxima alcanzada  
- **threstbps**: presión arterial en reposo  
- **chol**: nivel de colesterol  
- **cp**: tipo de dolor torácico  

Estas variables son clínicamente relevantes en cardiología y altamente predictivas.

---

## 📊 Modelos y resultados

| Modelo | Accuracy | F1-score | AUC ROC | Comentario |
|--------|----------|----------|---------|------------|
| AdaBoost | **0.82** | **0.82** | **0.904** | Mejor capacidad discriminativa |
| Gradient Boosting | 0.82 | 0.82 | 0.882 | Rendimiento sólido |
| XGBoost | 0.80 | 0.80 | 0.875 | Buen desempeño, menor AUC |

✅ **Modelo final recomendado: AdaBoost**  
→ Mejor balance entre sensibilidad y especificidad.  
→ Mayor AUC: separa mejor clases positivas y negativas.

---

## 🔍 Importancia de variables (AdaBoost)
| Variable | Significado | Importancia |
|---------|-------------|------------|
| thalach | Frecuencia cardíaca máxima | ⭐ Más relevante |
| threstbps | Presión arterial | Alta |
| chol | Colesterol | Relevante |

📌 Coincide con factores de riesgo clínicos reales.

---

## 🎯 Conclusiones
- Los modelos de ensamble permiten identificar **pacientes en riesgo** con muy buen desempeño.
- AdaBoost presenta **mayor AUC**, siendo el más confiable para diagnóstico temprano.
- El proyecto demuestra un **flujo completo de ML en salud**: preprocesamiento, EDA, modelado, evaluación y análisis interpretativo.
- En un entorno real se recomienda:
  ✅ Optimizar dataset  
  ✅ Balancear clases  
  ✅ Incorporar datos adicionales (historial familiar, hábitos)
