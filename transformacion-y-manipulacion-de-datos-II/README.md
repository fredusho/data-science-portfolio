
# Desafío – Transformación y Manipulación de Datos (Parte II) VENTAS REGIONALES EEUU

**Autor:** Freddy González  
**Fecha:** Octubre 2025  
**Entorno:** Google Colab – Python – Pandas

---

## 🧠 Descripción general

Este proyecto tiene como objetivo demostrar el dominio de técnicas de **transformación, integración y análisis de datos** usando **Python (Pandas)** sobre un conjunto de hojas de cálculo Excel con información de ventas regionales de EE.UU.  

El desafío replica un flujo de trabajo real de analítica empresarial: desde la carga de datos crudos hasta la creación de indicadores clave (KPIs), clasificación de tiempos de entrega, y análisis de rentabilidad y comisiones de equipos de ventas.

---

## 🎯 Objetivos del proyecto

1. Cargar todas las hojas del archivo `US_Regional_Sales_Data.xlsx` en DataFrames independientes.  
2. **Unificar** la información mediante joins validados (`many_to_one`) entre:
   - Pedidos (`Sales Orders`)
   - Clientes (`Customers`)
   - Tiendas (`Store Locations`)
   - Productos (`Products`)
   - Equipos de ventas (`Sales Team`)
3. Calcular métricas temporales:
   - `ProcurementDays` = `OrderDate` – `ProcuredDate`
   - `ShippingDays` = `ShipDate` – `OrderDate`
   - `DeliveryDays` = `DeliveryDate` – `ShipDate`
   - `CustomerDays` = `ShippingDays` + `DeliveryDays`
4. Crear una variable categórica `CustomerDaysInterval` para clasificar tiempos de entrega.
5. Generar **tablas dinámicas (pivot tables)** con conteos de órdenes por **equipo de ventas** y **rango de tiempo**.
6. Calcular rentabilidad:
   - `GrossMargin` = margen bruto por pedido.
   - `CommissionsPercentage` = % de comisión según margen.
   - `CommissionsAmount` = monto de comisión.
   - `NetMargin` = margen neto tras comisión.
7. Resumir resultados en una tabla pivote con totales por **Sales Team**.

---

## 🧩 Dataset utilizado

**Archivo:** `US_Regional_Sales_Data.xlsx`  
**Hojas incluidas:**
- `Sales Orders Sheet`
- `Customers Sheet`
- `Store Locations Sheet`
- `Products Sheet`
- `Sales Team Sheet`

**Características:**
- Fechas normalizadas a tipo `datetime64[ns]`
- Identificadores unificados por `_CustomerID`, `_StoreID`, `_ProductID`, `_SalesTeamID`
- Datos simulados de órdenes, productos, precios, costos, descuentos y equipos de ventas

---

## ⚙️ Metodología

1. **Carga del archivo Excel** mediante `pd.ExcelFile()` y lectura iterativa por hoja.  
2. **Integración controlada** con `pd.merge()` aplicando `validate='many_to_one'` para mantener consistencia referencial.  
3. **Cálculos derivados** (ProcurementDays, DeliveryDays, etc.) mediante operaciones de resta entre fechas.  
4. **Discretización de tiempos de entrega** con `pd.cut()` y etiquetas de intervalos (0–15, 15–30, etc.).  
5. **Agregaciones** con `pivot_table()`:
   - Conteo de órdenes por equipo de ventas y rango de entrega.  
   - Totales de margen, comisión y margen neto por vendedor.  
6. **Cálculo de rentabilidad:**
   ```python
   df_base['GrossMargin'] = df_base['Order Quantity'] * (
       (df_base['Unit Price'] * (1 - df_base['Discount Applied'])) - df_base['Unit Cost']
   )

   df_base['CommissionsPercentage'] = pd.cut(
       df_base['GrossMargin'],
       bins=[0, 100, 1000, 10000, 100000, float('inf')],
       labels=[0.05, 0.10, 0.15, 0.20, 0.25],
       right=False
   ).astype(float)

   df_base['CommissionsAmount'] = df_base['GrossMargin'] * df_base['CommissionsPercentage']
   df_base['NetMargin'] = df_base['GrossMargin'] - df_base['CommissionsAmount']



## 📊 Resultados principales
Análisis temporal: clasificación de pedidos según tiempos de entrega promedio (0–15, 15–30, 30–45 días, etc.).
Eficiencia operativa: tiempos de entrega más frecuentes en el rango de 15–30 días.
Desempeño comercial: identificación de equipos con mayor número de órdenes completadas.
Rentabilidad:
Cálculo de margen bruto (GrossMargin), comisión (CommissionsAmount) y margen neto (NetMargin) por equipo.
Resultados consolidados en una tabla pivote:
Métrica	Descripción
GrossMargin	Margen bruto total
CommissionsAmount	Monto total de comisiones
NetMargin	Margen neto después de comisiones


## 🛠️ Tecnologías utilizadas
Python 3.10+
Pandas para manipulación de datos
NumPy para cálculos numéricos
Google Colab como entorno de desarrollo
Excel (.xlsx) como fuente de datos
Pivot Tables y pd.cut() para segmentación y agregación

## 📁 Estructura sugerida del proyecto
proyecto-2-transformacion-datos/
├── notebook.ipynb
├── README.md
├── src/
│   └── funciones.py
└── data/
    └── US_Regional_Sales_Data.xlsx

    
## 💬 Conclusión
El proyecto evidencia el manejo completo del flujo ETL (Extracción, Transformación y Carga) con enfoque analítico:
Integración de múltiples fuentes tabulares.
Enriquecimiento con nuevas métricas derivadas.
Construcción de reportes ejecutivos por equipo de ventas.
Aplicación de segmentaciones discretas y cálculos financieros.
Demuestra competencias sólidas en data wrangling, business analytics y automatización de reportes con Pandas.
