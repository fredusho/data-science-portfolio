import pandas as pd

# Función 1: Filtrar un DataFrame por fechas
def filtrar_por_fecha(df, columna_fecha, fecha_inicio, fecha_fin):
    """
    Filtra un DataFrame por un rango de fechas.

    Parámetros:
        df (DataFrame): El DataFrame a filtrar.
        columna_fecha (str): Nombre de la columna de fechas.
        fecha_inicio (str): Fecha de inicio en formato 'YYYY-MM-DD'.
        fecha_fin (str): Fecha de fin en formato 'YYYY-MM-DD'.

    Retorna:
        DataFrame: El DataFrame filtrado por el rango de fechas.
    """
    df[columna_fecha] = pd.to_datetime(df[columna_fecha])
    mask = (df[columna_fecha] >= fecha_inicio) & (df[columna_fecha] <= fecha_fin)
    return df[mask]

# Función 2: Generar reportes con pivot tables
def generar_reporte_pivot(df, filas, columnas, valores, funcion_agrupadora):
    """
    Genera un reporte en formato pivot table.

    Parámetros:
        df (DataFrame): El DataFrame base para generar el reporte.
        filas (str o list): Columnas que serán las filas en la tabla pivote.
        columnas (str o list): Columnas que serán las columnas en la tabla pivote.
        valores (str): Columna que contiene los valores a resumir.
        funcion_agrupadora (str): Función de agregación para los valores (e.g., 'sum').

    Retorna:
        DataFrame: El DataFrame pivotado.
    """
    return pd.pivot_table(df, index=filas, columns=columnas, values=valores, 
                          aggfunc=funcion_agrupadora, fill_value=0)

# Función 3: Guardar DataFrame en PostgreSQL
def guardar_en_postgre(df, nombre_tabla, engine, if_exists='replace'):
    """
    Guarda un DataFrame en PostgreSQL.

    Parámetros:
        df (DataFrame): El DataFrame a guardar.
        nombre_tabla (str): Nombre de la tabla en la base de datos.
        engine (SQLAlchemy Engine): Conexión a la base de datos.
        if_exists (str): Comportamiento si la tabla existe ('replace', 'append', 'fail').

    Retorna:
        None
    """
    df.to_sql(nombre_tabla, engine, if_exists=if_exists, index=False)
