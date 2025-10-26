# Desafío – Manipulación y Transformación de Datos (Parte I)

**Autor:** Freddy González  
**Fecha:** Octubre 2025  
**Entorno:** Google Colab – Python – Pandas

---

## 🧠 Descripción general

Este proyecto aborda dos ejercicios fundamentales de **manipulación, limpieza e integración de datos** en Python, aplicando transformaciones con **Pandas** sobre distintos conjuntos de datos en formato `pkl` y `csv`.  
El objetivo principal es poner en práctica técnicas de análisis exploratorio, unión de fuentes, detección de duplicados, recodificación, discretización y generación de tablas dinámicas (pivot tables) para obtener **insights descriptivos**.

---

## 🎯 Objetivos principales

### 🔹 Parte 1: Integración de datos policiales
1. Cargar tres archivos `.pkl`:  
   - `officers.pkl`  
   - `subjects.pkl`  
   - `incidents.pkl`
2. Unir los DataFrames mediante `case_number`, aplicando `suffixes` para evitar conflictos de nombres.  
3. Verificar duplicados y eliminarlos.  
4. Contar:
   - Total de sujetos de género femenino.  
   - Número de casos con al menos una sospechosa mujer (`gender_subject == 'F'`).  
5. Crear una **tabla pivote** con el género del oficial en filas y el del sujeto en columnas, interpretando la distribución de incidentes por combinación de géneros.

**Hallazgos destacados:**  
- Se identificaron **9 sujetos de género femenino**.  
- Existen **7 casos** con al menos una sospechosa mujer.  
- La tabla pivote muestra que la mayoría de los incidentes involucran oficiales hombres y sujetos hombres, con pocas interacciones entre oficiales mujeres y sujetos femeninos.

---

### 🔹 Parte 2: Limpieza y análisis de datos laborales (`Cleaned_DS_Jobs.csv`)

1. **Carga de datos:** lectura del dataset con `pd.read_csv()`.  
2. **Normalización de valores nulos:** reemplazo de múltiples representaciones (`"na"`, `"null"`, `-1`, `"0"`, `"N/A"`, etc.) por `NaN` usando `replace()`.  
3. **Eliminación de filas incompletas** con `.dropna()`.  
4. **Extracción de rangos salariales:** creación de dos columnas:
   - `Salario Mínimo`  
   - `Salario Máximo`  
   aplicando una función `apply()` que separa los valores del campo `Salary Estimate`.  
5. **Recodificación de tamaño de empresa (`Size`)** según un diccionario de categorías:

   | Rango original | Categoría asignada |
   |----------------|-------------------|
   | 10,000+ employees | Mega Empresas |
   | 5,001–10,000 | Grandes Empresas |
   | 1,001–5,000 | Medianas Empresas |
   | 201–500 | Pequeñas Empresas |
   | 51–200 | Pequeñas Grandes Empresas |
   | 501–1,000 | Microempresas |
   | Unknown | Empresas sin Información |

6. **Análisis salarial**: tabla pivote con la **media de salario mínimo y máximo** por categoría de empresa.

**Resultados principales:**

| Descripción | Salario Mínimo Promedio | Salario Máximo Promedio |
|--------------|--------------------------|--------------------------|
| Mega Empresas | 97.9 | 151.1 |
| Grandes Empresas | 92.1 | 138.9 |
| Medianas Empresas | 93.9 | 137.5 |
| Microempresas | 100.2 | 146.2 |
| Pequeñas Empresas | 93.6 | 141.1 |
| Empresas sin Información | 73.0 | 110.5 |

---

## ⚙️ Herramientas y librerías utilizadas
- **Python 3.10+**
- **Pandas** – manipulación y transformación de datos
- **NumPy** – operaciones numéricas
- **Google Colab** – entorno de desarrollo
- **Matplotlib / Seaborn** *(opcional para visualización de resultados)*

---

## 📁 Estructura sugerida del proyecto

proyecto-1-manipulacion-transformacion/
├── notebook.ipynb
├── README.md
├── data/
│ ├── officers.pkl
│ ├── subjects.pkl
│ ├── incidents.pkl
│ └── Cleaned_DS_Jobs.csv
└── src/
└── funciones.py


---

## 💬 Conclusión

El proyecto consolida competencias en:
- **Integración de múltiples fuentes de datos** (merge y validación).  
- **Limpieza y estandarización** de información con valores nulos y duplicados.  
- **Creación de variables derivadas** (rango salarial, categorías).  
- **Uso de tablas dinámicas** para resumir y comparar información clave.  

Demuestra un manejo sólido de **Pandas**, buenas prácticas de análisis exploratorio y una lógica clara en la resolución de desafíos de datos.

---

## ✍️ Autor
**Freddy González**  
Data Analyst & Future Data Scientist  
[LinkedIn](linkedin.com/in/freddygonzalezsandoval · [GitHub](https://github.com/fredusho/data-science-portfolio)

