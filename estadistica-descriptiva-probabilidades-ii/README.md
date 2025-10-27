
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fredusho/data-science-portfolio/blob/main/estadistica-descriptiva-probabilidades-ii/estadistica-descriptiva-ii.ipynb)


# Desafío – Estadística Descriptiva y Probabilidades (Parte II)

**Autor:** Freddy González  
**Fecha:** Octubre 2025  
**Entorno:** Google Colab – Python – Pandas – NumPy  

---

## 🧠 Descripción general

Este proyecto tiene como objetivo aplicar los **principios de probabilidad y estadística inferencial** sobre un conjunto de datos correspondiente a los **equipos del Mundial de Fútbol 2014**, analizando su rendimiento por continente y calculando distintas probabilidades simples, conjuntas y condicionales.

El análisis busca cuantificar la relación entre variables como el continente de procedencia, el número de partidos ganados y la clasificación a la segunda ronda, utilizando técnicas fundamentales de estadística descriptiva en Python.

---

## 🎯 Objetivos del proyecto

1. **Cargar y explorar el dataset** `worldcup2014.csv`, que contiene información sobre 32 equipos clasificados.  
2. **Calcular probabilidades básicas**:
   - Pertenecer a un continente específico (África, Europa, Asia, Norteamérica, Sudamérica).  
   - Clasificar a la segunda ronda (`clasificado == 1`).  
   - Ganar al menos un partido (`juegos_ganados > 0`).  
3. **Obtener probabilidades conjuntas y disyuntivas**, por ejemplo:
   - P(A ∩ B): Pertenecer a un continente y clasificar.  
   - P(A ∪ B): Pertenecer a un continente o clasificar.  
4. **Analizar probabilidades condicionales**, tales como:
   - P(Europa | Clasificó)  
   - P(Sudamérica | Clasificó)  
   - P(África | Ganó al menos un partido)  
   - P(Ganar al menos un partido | Clasificó)  
   - P(Ganar al menos un partido | Norteamérica)  
   - P(No clasificar | África)

---

## 🧩 Dataset utilizado

**Archivo:** `worldcup2014.csv`  
**Tamaño:** 32 registros × 8 columnas  

**Variables principales:**
- `team`: nombre del país o selección.  
- `continent`: continente de origen.  
- `group`: grupo asignado (A–H).  
- `group_pos`: posición dentro del grupo.  
- `cantidad_juegos`: cantidad total de partidos jugados (fase de grupos).  
- `juegos_ganados`: cantidad de victorias.  
- `clasificado`: indicador binario (1 = clasificó a segunda ronda, 0 = eliminado).

---

## ⚙️ Metodología

1. **Carga y exploración inicial**
   ```python
   import pandas as pd
   import numpy as np

   data = pd.read_csv('/content/worldcup2014.csv')
   total_teams = len(data)

2.**Definicion de FUncionea Auxiliares**
def calculate_probability(condition):
    count = len(data[condition])
    return count / total_teams

def calculate_conditional_probability(condition_A, condition_B):
    count_B = len(data[condition_B])
    if count_B == 0:
        return 0
    count_A_and_B = len(data[condition_A & condition_B])
    return count_A_and_B / count_B

3. Cálculo de probabilidades simples, conjuntas y condicionales usando operadores lógicos (&, |) y filtrado booleano.

4. Interpretación estadística de los resultados obtenidos.

   1️⃣ Probabilidades simples
| Evento              | Probabilidad |
| ------------------- | ------------ |
| P(África)           | 0.15625      |
| P(Asia)             | 0.125        |
| P(Europa)           | 0.40625      |
| P(Norteamérica)     | 0.125        |
| P(Sudamérica)       | 0.1875       |
| P(Clasificar)       | 0.50         |
| P(Ganar ≥1 partido) | 0.71875      |

2️⃣ Probabilidades conjuntas y disyuntivas

| Evento                           | Descripción                          | Probabilidad |
| -------------------------------- | ------------------------------------ | ------------ |
| P(África ∩ Clasificar)           | Equipos africanos que clasificaron   | 0.0625       |
| P(Europa ∩ Clasificar)           | Equipos europeos que clasificaron    | 0.1875       |
| P(Sudamérica ∩ Clasificar)       | Equipos sudamericanos clasificados   | 0.15625      |
| P(Norteamérica ∩ Clasificar)     | Equipos norteamericanos clasificados | 0.09375      |
| P(Europa ∪ Clasificar)           | Equipos europeos o clasificados      | 0.71875      |
| P(Ganar ≥1 partido ∩ Clasificar) | Equipos que ganaron y clasificaron   | 0.50         |

3️⃣ Probabilidades condicionales

| Evento             | Interpretación   | Probabilidad                                            |        |
| ------------------ | ---------------- | ------------------------------------------------------- | ------ |
| P(Europa           | Clasificó)       | Probabilidad de ser europeo dado que clasificó          | 0.375  |
| P(Sudamérica       | Clasificó)       | Probabilidad de ser sudamericano dado que clasificó     | 0.3125 |
| P(África           | Ganó ≥1 partido) | Probabilidad de ser africano dado que ganó              | 0.1304 |
| P(Ganar ≥1 partido | Clasificó)       | Probabilidad de haber ganado dado que clasificó         | 1.0    |
| P(Ganar ≥1 partido | Norteamérica)    | Probabilidad de ganar dado que pertenece a Norteamérica | 0.75   |
| P(No clasificar    | África)          | Probabilidad de no clasificar dado que es africano      | 0.60   |


🧮 Conclusiones
La mitad de los equipos (50%) lograron clasificar a la segunda ronda.
Europa y Sudamérica dominan el torneo, con las mayores probabilidades conjuntas de clasificación y victorias.
Asia muestra la menor probabilidad tanto de victorias como de clasificación.
Las probabilidades condicionales confirman que clasificar implica casi siempre haber ganado al menos un partido (P=1.0).
El rendimiento africano presenta la mayor proporción de equipos que no clasificaron (60%), reflejando una brecha competitiva respecto a otros continentes.


🛠️ Tecnologías utilizadas
Python 3.10+
Pandas (análisis y filtrado de datos)
NumPy (operaciones estadísticas)
Google Colab (entorno de ejecución)
CSV dataset (worldcup2014.csv)

✍️ Autor
Freddy González
Data Scientist
📂 [GitHub](https://github.com/fredusho/data-science-portfolio)  
💼 [LinkedIn](https://linkedin.com/in/freddygonzalezsandoval)



