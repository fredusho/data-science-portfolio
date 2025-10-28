[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fredusho/data-science-portfolio/blob/main/proyecto-clasificacion-ramen/desafio-clasificacion-ramen.ipynb)


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

