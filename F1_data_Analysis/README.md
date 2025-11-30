# Fórmula 1 1950–2025 – Análisis Exploratorio de Datos (EDA)

Este proyecto realiza un análisis exploratorio de datos del Campeonato Mundial de Fórmula 1 desde 1950 hasta la temporada 2025, utilizando datos tabulares y visualizaciones interactivas para responder preguntas típicas de negocio y performance deportiva.

El foco está en:
- Evolución del calendario (número de carreras por temporada).
- Pilotos y constructores más ganadores.
- Campeones por temporada.
- Análisis por circuito (quién domina en cada pista).

---

## 📂 Dataset

El dataset proviene de Kaggle:

- **Nombre:** Formula 1 Championships 1950–2025  
- **Origen:** Kaggle – `rockyt07/formula-1-championships-1950-2025`  

Archivos utilizados:

- `circuits.csv`  
- `constructors.csv`  
- `drivers.csv`  
- `races.csv`  
- `results.csv`  
- `driver_standings.csv`  
- `constructor_standings.csv`  
- `qualifying.csv`  

### Estructura resumida de las tablas

- **`circuits.csv`**
  - `circuit_id`, `name`, `lat`, `long`, `locality`, `country`, `Wikipedia_url`
- **`constructors.csv`**
  - `constructor_id`, `name`, `nationality`, `Wikipedia_url`
- **`drivers.csv`**
  - `driver_id`, `givenName`, `familyName`, `nationality`, `dob`
- **`races.csv`**
  - `race_id`, `season`, `round`, `race_name`, `date`, `time`, `circuit_id`
- **`results.csv`**
  - `race_id`, `driver_id`, `constructor_id`, `grid`, `position`, `position_order`, `points`, `laps`, `status`
- **`driver_standings.csv`**
  - `season`, `round`, `driver_id`, `position`, `points`, `wins`
- **`constructor_standings.csv`**
  - `season`, `round`, `constructor_id`, `position`, `points`, `wins`
- **`qualifying.csv`**
  - `race_id`, `driver_id`, `constructor_id`, `position`, `q1`, `q2`, `q3`

---

## 🛠️ Tecnologías utilizadas

- **Lenguaje:** Python  
- **Librerías principales:**
  - `pandas` – manipulación de datos
  - `plotly.express` – visualizaciones interactivas
  - `matplotlib` (mínimo uso)
- **Opcional (Kaggle Notebooks):**
  - `kagglehub` – para descargar la última versión del dataset directamente desde Kaggle

Ejemplo de descarga automática en entorno Kaggle:

```python
import kagglehub

path = kagglehub.dataset_download("rockyt07/formula-1-championships-1950-2025")
print("Path to dataset files:", path)


👤 Autor
Freddy González – Data Scientist
GitHub: https://github.com/fredusho/data-science-portfolio
LinkedIn: https://linkedin.com/in/freddygonzalezsandoval
