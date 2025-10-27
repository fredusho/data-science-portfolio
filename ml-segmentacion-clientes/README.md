[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fredusho/data-science-portfolio/blob/main/ml-segmentacion-clientes/ml-segmentacion-clientes.ipynb)

📄 [Ver instrucciones del desafío (PDF)](https://github.com/fredusho/data-science-portfolio/blob/main/proyecto-segmentacion-clientes/docs/ml-segmentacion-clientes.pdf)

# Segmentación de Clientes con Machine Learning

## 🧩 Descripción del proyecto
Este proyecto aplica **técnicas de segmentación de clientes mediante aprendizaje no supervisado**, utilizando los algoritmos **K-Means** y **DBSCAN** sobre un dataset de transacciones comerciales.  
El objetivo es identificar patrones de comportamiento de compra y clasificar a los clientes según su **recencia, frecuencia y monto (RFM)**, para optimizar estrategias de marketing y retención.

---

## ⚙️ Tecnologías y librerías utilizadas
- **Python 3.10+**
- **pandas / numpy**
- **matplotlib / seaborn**
- **scikit-learn**
- **Google Colab**

---

## 🧠 Objetivos principales
1. Realizar un **análisis exploratorio y de calidad de datos**.
2. **Depurar y limpiar** el dataset eliminando outliers y valores negativos.
3. Generar las **variables RFM (Recencia, Frecuencia y Monto)**.
4. Aplicar los algoritmos de **K-Means** y **DBSCAN** para la segmentación.
5. Evaluar la calidad de los clusters e interpretar los perfiles resultantes.

---

## 📊 Flujo de trabajo

### 1️⃣ Limpieza y depuración de datos
- Se eliminan valores negativos en las variables `Quantity` y `price_total`.
- Se remueven outliers usando el método **IQR**, reduciendo un 16% de los datos (≈ 3000 registros).
- Se mejora la distribución de los datos y la calidad para el clustering.

### 2️⃣ Generación de variables RFM
Cada cliente se caracteriza por:
- **Recencia:** días desde la última compra.  
- **Frecuencia:** número de facturas únicas.  
- **Monto:** gasto total acumulado.

### 3️⃣ Normalización
Las variables se escalan mediante `StandardScaler()` para evitar sesgos por diferencias de magnitud entre las dimensiones R, F y M.

### 4️⃣ Aplicación de modelos de clustering
- **K-Means:** Se determina el número óptimo de clusters con el **método del codo**, seleccionando **k = 4**.
- **DBSCAN:** Se aplica para detectar posibles agrupaciones naturales sin un número predefinido de clusters.

---

## 🧩 Resultados principales (segmentos K-Means)

| Cluster | Recencia Promedio (días) | Frecuencia Promedio | Monto Promedio (USD) | Perfil |
|----------|---------------------------|----------------------|----------------------|---------|
| **0** | 17.3 | 15.3 | 4,742 | Cliente Frecuente |
| **1** | 45.9 | 3.1 | 839 | Cliente Ocasional |
| **2** | 5.9 | 82.1 | 22,944 | Cliente VIP |
| **3** | 246.9 | 1.5 | 378 | Cliente Inactivo |

---

## 🎯 Conclusiones
- El modelo permitió **identificar cuatro perfiles de clientes** claros y accionables.  
- Los **clientes VIP (Cluster 2)** concentran gran parte de los ingresos y requieren estrategias de fidelización.  
- Los **clientes inactivos (Cluster 3)** representan oportunidades de reactivación mediante campañas personalizadas.  
- El enfoque **RFM + K-Means** resultó efectivo para segmentar comportamientos y optimizar decisiones comerciales.

---

## 🗂️ Estructura del proyecto

