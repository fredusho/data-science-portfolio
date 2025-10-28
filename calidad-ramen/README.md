[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fredusho/data-science-portfolio/blob/main/calidad-ramen/clasificacion-calidad-ramen.ipynb)

# Clasificación de Calidad de Ramen 🍜

## 🧩 Descripción del proyecto
Este proyecto aborda la **clasificación de la calidad de ramen** en función de sus características (marca, país, estilo, entre otros) mediante técnicas de **aprendizaje supervisado**.  
Se busca construir un modelo capaz de predecir si un ramen es **"Good" (bueno)** o **"Bad" (malo)** según sus valoraciones, utilizando un conjunto de datos con más de 2.500 observaciones de productos evaluados.

---

## ⚙️ Tecnologías y librerías utilizadas
- **Python 3.10+**
- **pandas / numpy**
- **matplotlib**
- **scikit-learn**
- **Google Colab**

---

## 🧠 Objetivos principales
1. Analizar la calidad y estructura de los datos del dataset `ramen-ratings.xlsx`.  
2. Limpiar y transformar los datos eliminando columnas irrelevantes y valores nulos.  
3. Crear una variable objetivo binaria (`Good` vs `Bad`) basada en las estrellas (`Stars`).  
4. Codificar las variables categóricas mediante `get_dummies`.  
5. Entrenar y comparar los modelos:
   - **Regresión Logística**
   - **Support Vector Machine (SVM)**  
6. Evaluar el desempeño con métricas de clasificación (precision, recall, F1, AUC-ROC).

---

## 📊 Flujo de trabajo

### 1️⃣ Análisis y limpieza de datos
- Se eliminó la columna `Top Ten` por contener **98.4% de valores nulos**.  
- `Stars` fue convertida a tipo numérico y los valores no válidos se imputaron con la mediana.  
- `Style` se rellenó con `"Unknown"`.  
- Se unificaron marcas poco frecuentes en la categoría `"Other"`.  

### 2️⃣ Creación de la variable objetivo
Se definió la variable binaria **`Rating`**:
```python
df['Rating'] = df['Stars'].apply(lambda x: 1 if x >= 3.5 else 0)

1 → Ramen de buena calidad (“Good”)
0 → Ramen de baja calidad (“Bad”)
3️⃣ Preprocesamiento
Variables categóricas codificadas con pd.get_dummies.
Estandarización mediante StandardScaler.
División entrenamiento/prueba 80/20.
🤖 Modelos y resultados
🔹 Regresión Logística

| Métrica      | Clase 0 (Bad) | Clase 1 (Good) | Global   |
| ------------ | ------------- | -------------- | -------- |
| Precisión    | 0.57          | 0.87           | -        |
| Recall       | 0.69          | 0.80           | -        |
| F1-Score     | 0.62          | 0.83           | -        |
| **Accuracy** |               |                | **0.77** |

🔹 Support Vector Machine (SVM)

| Métrica      | Clase 0 (Bad) | Clase 1 (Good) | Global   |
| ------------ | ------------- | -------------- | -------- |
| Precisión    | 0.54          | 0.89           | -        |
| Recall       | 0.74          | 0.76           | -        |
| F1-Score     | 0.63          | 0.82           | -        |
| **Accuracy** |               |                | **0.76** |
| **AUC-ROC**  |               |                | **0.85** |

🎯 Conclusiones
Ambos modelos presentan un desempeño sólido (76–77% de exactitud).
SVM logra una mejor discriminación general (AUC = 0.85), mostrando una ligera ventaja en capacidad predictiva.
Regresión Logística ofrece interpretabilidad y mayor recall para la clase “Good”, ideal si se busca identificar productos de buena calidad con menor riesgo de omisión.
El proyecto demuestra un flujo de clasificación supervisada completo, desde limpieza hasta evaluación comparativa de modelos.

