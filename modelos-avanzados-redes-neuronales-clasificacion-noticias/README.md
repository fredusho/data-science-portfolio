
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fredusho/data-science-portfolio/blob/main/modelos-avanzados-redes-neuronales-clasificacion-noticias/clasificacion-noticias.ipynb)

# Clasificación de Noticias — Fake vs Real 📰🧠

## 🧩 Descripción del proyecto
Este proyecto, correspondiente al examen final del módulo de Procesamiento de Lenguaje Natural (NLP), tiene como objetivo **detectar noticias falsas** mediante técnicas de aprendizaje profundo.

Se desarrolla un flujo completo:
✅ Preprocesamiento de texto  
✅ Embeddings Word2Vec preentrenados  
✅ Entrenamiento de una **Red Neuronal LSTM Bidireccional**  
✅ Evaluación en datos no vistos  
✅ Predicción final entregable

---

## ⚙️ Tecnologías y librerías utilizadas
- Python 3.10+
- pandas / numpy
- nltk / re / WordCloud
- TensorFlow · Keras (Bidirectional LSTM)
- scikit-learn
- Google Colab

---

## 🧠 Objetivos principales
1. Tratar y limpiar texto eliminando ruido lingüístico
2. Representar palabras como vectores usando **Word2Vec (Google News 300d)**
3. Entrenar modelo secuencial con dropout preventivo
4. Predecir nuevas noticias (entrega final)
5. Evaluar con métricas de clasificación y curvas ROC

---

## 🧹 Preprocesamiento aplicado
- Conversión a minúsculas
- Eliminación de puntuaciones, números y símbolos
- Tokenización paso a paso
- Lemmatización & stopwords NLTK
- Secuencias padded → entradas uniformes

---

## 🤖 Modelado y evaluación

### 📌 Modelo Final: Bidirectional LSTM
- Early Stopping para evitar sobreajuste
- Capas densas con activadores ReLU y Sigmoid

| Métrica | Valor |
|--------|------|
| **Accuracy** | **92.12%** |
| AUC ROC | **> 0.90 (Excelente)** |

📌 El modelo discrimina claramente entre noticias reales y falsas ✅

---

## 🔎 Análisis adicional
- WordCloud y frecuencia de términos
- Políticas → alta fuente de error por contenido ambiguo
- El modelo puede integrarse en pipelines reales de detección de desinformación

---
