# Desafío – Estadística Descriptiva y Probabilidades (Parte I)

**Autor:** Freddy González  
**Fecha:** Octubre 2025  
**Entorno:** Google Colab – Python – Pandas – NumPy

---

## 🧠 Descripción general

Este proyecto aplica **conceptos de estadística descriptiva y análisis exploratorio de datos (EDA)** sobre un dataset de **salarios en Ciencia de Datos**, con el objetivo de calcular métricas fundamentales, explorar variaciones salariales por categoría y analizar la distribución de los cargos mejor remunerados en empresas de Estados Unidos.

El desafío se centra en utilizar herramientas estadísticas básicas para obtener insights reales del mercado laboral de Data Science.

---

## 🎯 Objetivos del proyecto

1. **Cargar y explorar los datos** desde el archivo `ds_salaries.csv`.  
2. **Calcular medidas de tendencia central y dispersión** para la variable `salary_in_usd`:
   - Promedio, desviación estándar, cuartiles (Q1, Q2, Q3) y rango.  
3. **Comparar salarios según categorías**:
   - Nivel de experiencia (`experience_level`)  
   - Tipo de empleo (`employment_type`)  
   - Tamaño de la empresa (`company_size`)  
4. **Identificar cargos mejor pagados en EE.UU.**, filtrando `company_location == 'US'` y agrupando por `job_title`.

---

## 🧩 Dataset utilizado

**Archivo:** `ds_salaries.csv`  
**Tamaño:** 3.755 registros × 11 columnas  
**Principales variables:**
- `work_year`: año de registro
- `experience_level`: nivel de experiencia (`EN`, `MI`, `SE`, `EX`)
- `employment_type`: tipo de contrato (`FT`, `PT`, `CT`, `FL`)
- `job_title`: cargo del empleado
- `salary_in_usd`: salario anual en dólares
- `company_location`: país de la empresa
- `company_size`: tamaño de la organización (`S`, `M`, `L`)

---

## 📈 Análisis estadístico

### 1️⃣ Estadísticos descriptivos de `salary_in_usd`
| Métrica | Valor |
|----------|--------|
| Promedio | 137,570 USD |
| Desviación estándar | 63,055 USD |
| Q1 (25%) | 95,000 USD |
| Q2 (Mediana) | 135,000 USD |
| Q3 (75%) | 175,000 USD |
| Rango | 444,868 USD |

Interpretación:  
Los salarios en Data Science muestran una alta dispersión, con un rango amplio y concentración entre 95k y 175k USD.

---

### 2️⃣ Comparativa por categorías

#### Por nivel de experiencia (`experience_level`)
| Nivel | Media | Mediana | Desv.Std | Mínimo | Máximo |
|--------|--------|----------|----------|--------|--------|
| EN | 78,546 | 70,000 | 52,225 | 5,409 | 300,000 |
| MI | 104,525 | 100,000 | 54,387 | 5,132 | 450,000 |
| SE | 153,051 | 146,000 | 56,896 | 8,000 | 423,834 |
| EX | 194,930 | 196,000 | 70,661 | 15,000 | 416,000 |

> **Conclusión:** el salario aumenta con la experiencia. Los niveles Senior (SE) y Executive (EX) presentan las remuneraciones más altas.

#### Por tipo de empleo (`employment_type`)
- Mayor estabilidad y salario promedio en contratos **Full Time (FT)**.  
- Alta variabilidad entre **Freelance (FL)** y **Part-Time (PT)**, con dispersión significativa en valores.

#### Por tamaño de empresa (`company_size`)
| Tamaño | Media | Mediana | Desv.Std | Mínimo | Máximo |
|--------|--------|----------|----------|--------|--------|
| S | 78,226 | 62,146 | 61,955 | 5,679 | 416,000 |
| M | 143,130 | 140,000 | 58,992 | 5,132 | 450,000 |
| L | 118,300 | 108,500 | 75,832 | 5,409 | 423,834 |

> **Conclusión:** las empresas medianas (`M`) pagan mejor en promedio, mostrando un equilibrio entre salario y estabilidad.

---

### 3️⃣ Cargos mejor pagados en EE.UU.

| Cargo | Salario Promedio (USD) |
|--------|------------------------|
| Data Analytics Lead | 405,000 |
| Data Science Tech Lead | 375,000 |
| Director of Data Science | 294,375 |
| Principal Data Scientist | 255,500 |
| Cloud Data Architect | 250,000 |
| Applied Data Scientist | 238,000 |
| Head of Data | 233,183 |
| Machine Learning Software Engineer | 217,400 |
| Data Lead | 212,500 |
| Head of Data Science | 202,355 |

> **Insight:** los cargos con enfoque estratégico y liderazgo técnico son los mejor remunerados, seguidos por roles especializados en Machine Learning y arquitectura de datos.

---

## 🧮 Conclusiones

- Existe una relación directa entre la **experiencia laboral y el salario**.  
- Los contratos de tiempo completo (`FT`) y las empresas medianas concentran los **niveles salariales más competitivos**.  
- Las posiciones de liderazgo en **Data Science y Machine Learning** dominan el top de ingresos.  
- Se evidencia una **alta dispersión salarial**, reflejo de la madurez desigual del mercado laboral global en ciencia de datos.

---

## 🛠️ Tecnologías utilizadas
- **Python 3.10+**
- **Pandas** (análisis de datos)
- **NumPy** (operaciones numéricas)
- **Google Colab** (entorno de desarrollo)
- **Matplotlib / Seaborn** *(para visualizaciones exploratorias)*

---

## ✍️ Autor
**Freddy González**  
Data Scientist  
[GitHub](https://github.com/fredusho/data-science-portfolio) · [LinkedIn](https://linkedin.com/in/freddygonzalezsandoval)


