[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fredusho/data-science-portfolio/blob/main/tvariable-aleatoria-tabaquismo-y-gestacion/tabquismo-gestacion.ipynb)

# Desafío – Variable Aleatoria y Tabaquismo

**Autor:** Freddy González  
**Fecha:** Octubre 2025  
**Entorno:** Google Colab – Python – Pandas – NumPy – SciPy  

---

## 🧠 Descripción general

Este proyecto analiza la **relación entre el tabaquismo materno y el peso de los recién nacidos**, utilizando métodos de **estadística descriptiva, inferencial y teoría de la probabilidad**.  

A partir del dataset `baby.csv`, se estudian las diferencias entre madres fumadoras y no fumadoras, se evalúa la normalidad de los datos, se realizan comparaciones de medias mediante pruebas de hipótesis, y se modelan probabilidades con distribuciones **normal** y **binomial**.

---

## 🎯 Objetivos del proyecto

1. **Explorar y describir el dataset** `baby.csv`:
   - Identificar variables relevantes: peso del bebé, edad gestacional, edad y estatura materna, tabaquismo.  
   - Calcular medidas de tendencia central y dispersión.  
   - Analizar la proporción de madres fumadoras y no fumadoras.

2. **Evaluar la distribución del peso al nacer**:
   - Graficar la distribución y ajustar un modelo de **distribución normal**.  
   - Aplicar la **prueba de normalidad Shapiro-Wilk** para determinar si los datos se distribuyen normalmente.  

3. **Comparar pesos entre bebés de madres fumadoras y no fumadoras**:
   - Realizar una **prueba t de Student** para muestras independientes.  
   - Analizar significancia estadística (p-valor).  

4. **Modelar la probabilidad de tabaquismo**:
   - Calcular la probabilidad individual de que una madre fume.  
   - Modelar la distribución **binomial** para un grupo de 5 madres seleccionadas al azar.  
   - Simular 1.000 muestras de tamaño 8 y analizar la distribución de las medias muestrales.

---

## 🧩 Dataset utilizado

**Archivo:** `baby.csv`  
**Tamaño:** 1.174 registros × 7 columnas  

**Variables principales:**
- `Birth.Weight`: peso del bebé (en gramos)  
- `Gestational.Days`: días de gestación  
- `Maternal.Age`: edad materna  
- `Maternal.Height`: altura de la madre (en pulgadas)  
- `Maternal.Pregnancy.Weight`: peso de la madre durante el embarazo (libras)  
- `Maternal.Smoker`: variable booleana (True = fuma, False = no fuma)

---

## ⚙️ Metodología

1. **Exploración inicial de los datos**  
   - Se usaron métodos como `df.describe()`, `df.info()` y conteos proporcionales (`value_counts(normalize=True)`).  
   - Se determinó que el 39.1% de las madres eran fumadoras.

2. **Distribución del peso al nacer**  
   - Media ≈ 119.46, desviación estándar ≈ 18.33.  
   - El histograma mostró una forma aproximadamente normal, pero con desviaciones leves.  
   - La **prueba Shapiro-Wilk (p = 0.0019)** llevó a rechazar la hipótesis de normalidad perfecta.

3. **Comparación entre madres fumadoras y no fumadoras**

| Grupo | Media Peso (g) | Desviación | Min | Max |
|--------|----------------|------------|-----|-----|
| Fumadoras | 113.82 | 18.30 | 58 | 163 |
| No Fumadoras | 123.09 | 17.42 | 55 | 176 |

> **Prueba t de Student:**  
> Estadístico = -8.63, p-valor < 0.001  
> → **Conclusión:** Los bebés de madres fumadoras pesan significativamente menos.

4. **Modelado probabilístico**
   - P(fuma) = 0.391  
   - Distribución binomial (n=5, p=0.391):

| Madres fumadoras | Probabilidad |
|------------------|--------------|
| 0 | 0.0838 |
| 1 | 0.2689 |
| 2 | 0.3453 |
| 3 | 0.2217 |
| 4 | 0.0712 |
| 5 | 0.0091 |

   - Simulación de 1.000 muestras de tamaño 8 →  
     Media de medias muestrales = **0.3937**,  
     Desviación estándar = **0.1717**.

---

## 📊 Conclusiones

- Los **pesos de los bebés** siguen aproximadamente una distribución normal, aunque no perfectamente ajustada.  
- Existe una **diferencia estadísticamente significativa** entre los pesos de bebés de madres fumadoras y no fumadoras.  
- La probabilidad de tabaquismo en la muestra es cercana al **39%**.  
- El modelo **binomial** refleja adecuadamente la variabilidad esperada en grupos pequeños.  
- El estudio demuestra el impacto negativo del tabaquismo materno en el peso neonatal.

---

## 🛠️ Tecnologías utilizadas
- **Python 3.10+**  
- **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**  
- **SciPy (stats)** – pruebas de hipótesis, Shapiro-Wilk, t-test, binomial  
- **Google Colab** – entorno de desarrollo

---

## ✍️ Autor
**Freddy González**  
Data Scientist  
📂 [GitHub](https://github.com/fredusho/data-science-portfolio)  
💼 [LinkedIn](https://linkedin.com/in/freddygonzalezsandoval)


