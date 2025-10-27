[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fredusho/data-science-portfolio/blob/main/inferencias-e-hipotesis/inferencias-hipotesis.ipynb)
📄 [Ver instrucciones del desafío (PDF)](https://github.com/fredusho/data-science-portfolio/blob/main/inferencias-e-hipotesis/docs/inferencia-hipotesis.pdf)
# Desafío – Inferencias e Hipótesis

**Autor:** Freddy González  
**Fecha:** Octubre 2025  
**Entorno:** Google Colab – Python – Pandas – SciPy – Statsmodels  

---

## 🧠 Descripción general

Este proyecto aborda el uso de **pruebas de hipótesis e inferencias estadísticas** aplicadas a un conjunto de datos con variables demográficas, de salud y de ingresos.  
A través de distintos experimentos, se evalúan medias poblacionales, proporciones y diferencias entre grupos mediante **t-tests** y **z-tests**, aplicando criterios de decisión según distintos niveles de significancia (α = 0.01, 0.05, 0.10).

---

## 🎯 Objetivos del proyecto

1. **Realizar pruebas de hipótesis univariadas** sobre variables continuas:
   - `earn` (ingreso anual),
   - `height` (altura),
   - `age` (edad).
   Utilizando diferentes valores hipotéticos de media (`μ₀`) y niveles de significancia.

2. **Implementar una función de prueba t personalizada**
   - Calcular el estadístico t, p-valor y la decisión (aceptar o rechazar H₀).  
   - Probar hipótesis tanto bilaterales como unilaterales (“greater” y “less”).

3. **Evaluar proporciones mediante pruebas z**
   - Estimar la proporción de hombres (`male = 1`) en una muestra aleatoria de 50 individuos.  
   - Contrastar con la proporción real en la población total.  
   - Aplicar pruebas a niveles de α = 0.05 y α = 0.01.

4. **Comparar medias de dos grupos independientes**
   - Analizar si el género influye en el salario (`earn`) utilizando una prueba **t de Student** para muestras independientes.

---

## 🧩 Dataset utilizado

**Archivo:** `earnings.csv`  
**Tamaño:** 1.000 registros (aprox.)  
**Principales variables:**
- `earn`: ingresos anuales en dólares.  
- `height`: altura (pulgadas).  
- `weight`: peso (libras).  
- `male`: variable binaria (1 = hombre, 0 = mujer).  
- `education`: años de educación formal.  
- `smokenow`: hábito actual de fumar.  
- `age`: edad en años.  

---

## ⚙️ Metodología

### 1️⃣ Pruebas t para medias
Se definió la función:

```python
def hypothesis_test(sample, mu, alpha, alternative='two-sided'):
    t_stat, p_value = stats.ttest_1samp(sample, mu)
    if alternative == 'greater':
        p_value = 1 - stats.t.cdf(t_stat, df=len(sample)-1)
    elif alternative == 'less':
        p_value = stats.t.cdf(t_stat, df=len(sample)-1)
    reject_null = p_value < alpha
    return t_stat, p_value, reject_null

Se probaron hipótesis para earn, height y age con distintas medias hipotéticas (μ₀) y niveles de confianza.
Se concluyó que:
Altura (height) presenta diferencias significativas con respecto a los valores esperados.
Edad (age) no mostró diferencias estadísticamente relevantes.
Ingresos (earn) varían significativamente según el valor hipotético de comparación.
2️⃣ Estimación de proporción de hombres
Se aplicó la función proportions_ztest del paquete statsmodels para verificar si la proporción observada en una muestra de 50 individuos difiere de la proporción real poblacional (≈ 37.17%).

| α    | Proporción Muestra | Z     | p-valor | Resultado    |
| ---- | ------------------ | ----- | ------- | ------------ |
| 0.05 | 0.32               | -0.78 | 0.43    | Se acepta H₀ |
| 0.01 | 0.44               | 0.97  | 0.33    | Se acepta H₀ |


Conclusión: No se evidencian diferencias significativas entre la proporción muestral y la poblacional.

3️⃣ Comparación de ingresos por género
Se realizó una t-test para muestras independientes:

| Grupo   | Media (USD) | N   | Desv.Std |
| ------- | ----------- | --- | -------- |
| Hombres | 50,879      | 496 | 23,455   |
| Mujeres | 37,660      | 504 | 19,382   |


Resultados:
Estadístico t = 13.68
p-valor = 1.23e-40
→ Se rechaza H₀ con un 95% de confianza.
Conclusión: existen diferencias significativas entre los ingresos de hombres y mujeres.

📊 Conclusiones generales
Las pruebas t univariadas permitieron validar hipótesis sobre medias poblacionales con distintos niveles de confianza.
Las proporciones muestrales y poblacionales no mostraron diferencias significativas.
La variable male influye de manera estadísticamente significativa en los ingresos (earn).
El trabajo refuerza la comprensión práctica de la inferencia estadística aplicada a poblaciones reales.

🛠️ Tecnologías utilizadas
Python 3.10+
Pandas
NumPy
SciPy (stats)
Statsmodels
Google Colab

✍️ Autor
Freddy González
Data Scientist







