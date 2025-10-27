[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fredusho/data-science-portfolio/blob/main/Aprendizaje%20supervisado%20y%20no%20supervisado%20-%20Segmentaci%C3%B3n%20de%20clientes/Desafio_2_Segmentacion_2.ipynb)


 ## Segmentación de Clientes

**Autor:** Freddy González  
**Entorno:** Google Colab – Python – Pandas – Scikit-learn – Seaborn – Matplotlib  

---

## 🧠 Descripción general

Este proyecto aborda la **segmentación de clientes** de una empresa minorista utilizando **técnicas no supervisadas de clustering (K-Means y DBSCAN)**.  
El objetivo es identificar patrones de comportamiento basados en variables derivadas del análisis **RFM (Recencia, Frecuencia, Monto)**, lo que permite caracterizar diferentes tipos de clientes: frecuentes, ocasionales, VIP e inactivos.

El proceso incluye limpieza de datos, eliminación de outliers, estandarización de variables y evaluación de la calidad de los clusters resultantes.

---

## 🎯 Objetivos del proyecto

1. **Analizar la calidad y consistencia de los datos** provenientes de transacciones minoristas (`Retail_Invoices.xlsx`).  
2. **Eliminar registros inválidos o atípicos**, incluyendo valores negativos en `Quantity` y `price_total`.  
3. **Detectar y tratar outliers** mediante el rango intercuartílico (IQR).  
4. **Construir variables RFM** (Recencia, Frecuencia, Monto) para representar el comportamiento de compra de cada cliente.  
5. **Aplicar algoritmos de clustering**:
   - **K-Means**, con selección de número óptimo de clusters mediante el método del codo.  
   - **DBSCAN**, como técnica alternativa basada en densidad.  
6. **Interpretar los segmentos resultantes** con base en sus patrones de compra y valor para el negocio.

---

## 🧩 Dataset utilizado

**Archivo:** `Retail_Invoices.xlsx`  
**Tamaño:** 18.532 registros × 6 columnas  

**Variables originales:**
- `InvoiceNo`: número de factura  
- `InvoiceDate`: fecha de compra  
- `CustomerID`: identificador único de cliente  
- `Quantity`: cantidad de artículos comprados  
- `price_total`: monto total de la transacción  
- `StockCode`: código del producto  

---

## ⚙️ Metodología

### 1️⃣ Análisis de calidad de datos
Se aplicó una función personalizada `calidad_datos()` que calcula:
- Porcentaje de nulos, ceros y valores únicos.  
- Medidas estadísticas básicas (media, mediana, desviación).  
- Detección de outliers con límites inferior/superior.  

**Resultado:**  
No se observaron valores nulos, pero existían registros con valores negativos en `Quantity` y `price_total`, los cuales fueron eliminados.

---

### 2️⃣ Limpieza y tratamiento de outliers
- Eliminación de valores negativos.  
- Aplicación del método **IQR** sobre `Quantity`, `price_total` y `StockCode`.  
- Se eliminaron ≈ 16% de los registros (de 18.532 a 15.450).  

📊 **Conclusión:** la distribución resultante de las variables mostró una mejora significativa tras la limpieza.

---

### 3️⃣ Generación de variables RFM

Cada cliente fue descrito mediante:
- **Recencia:** días desde su última compra.  
- **Frecuencia:** número de facturas únicas.  
- **Monto:** gasto total acumulado.  

Las variables fueron normalizadas con **StandardScaler** para asegurar igual ponderación en el clustering.

---

### 4️⃣ Modelado de clusters

#### 🔹 Método K-Means
- Se utilizó el **método del codo** para definir el número óptimo de clusters → **k = 4**.  
- Se generaron los siguientes segmentos:

| Cluster | Recencia Media | Frecuencia Media | Monto Medio | Perfil |
|----------|----------------|------------------|--------------|---------|
| 0 | 17.3 días | 15.3 compras | 4,741.7 | **Cliente Frecuente** |
| 1 | 45.9 días | 3.1 compras | 839.6 | **Cliente Ocasional** |
| 2 | 5.9 días | 82.1 compras | 22,943.9 | **Cliente VIP** |
| 3 | 246.9 días | 1.5 compras | 378.0 | **Cliente Inactivo** |

#### 🔹 Método DBSCAN
Se probó como alternativa para detectar agrupamientos de alta densidad sin necesidad de definir k previamente.  
Los resultados mostraron menor definición de grupos comparado con K-Means.

---

### 5️⃣ Visualización de resultados
- **Boxplots** y **distribuciones** antes/después de la limpieza.  
- **Heatmap de correlación** entre variables numéricas (`Quantity`, `price_total`, `StockCode`).  
- **Gráficos de dispersión** para visualizar los clusters RFM.

---

## 📊 Conclusiones

- La limpieza y normalización de datos mejoró notablemente la estabilidad de los resultados.  
- El modelo **K-Means con 4 clusters** permitió identificar con claridad los distintos perfiles de clientes.  
- Los **clientes VIP (Cluster 2)** concentran el mayor gasto y frecuencia de compra.  
- Los **clientes inactivos (Cluster 3)** son un grupo estratégico para campañas de reactivación.  
- DBSCAN no fue el modelo óptimo, pero permitió contrastar la robustez del K-Means.

---

## 🛠️ Tecnologías utilizadas
- **Python 3.10+**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Matplotlib**
- **Seaborn**
- **Google Colab**

---

## ✍️ Autor
**Freddy González**  
Data Scientist  
📂 [GitHub](https://github.com/fredusho/data-science-portfolio)  
💼 [LinkedIn](https://linkedin.com/in/freddygonzalezsandoval)



