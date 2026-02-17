import pandas as pd
from conexion import conectar

def cargar_datos():
    conn = conectar()
    query = "SELECT * FROM alumnos"
    df = pd.read_sql(query, conn)
    conn.close()

    # 🔹 LIMPIEZA DE TEXTO
    df["seccion"] = df["seccion"].str.strip().str.upper()
    df["id_real"] = df["id_real"].str.strip()

    return df
"""Se realizó un proceso de normalización de variables 
categóricas para evitar duplicidad por inconsistencias de formato."""


def clasificar_riesgo(df):

    def calcular_riesgo(fila):
        comprension = fila["comprension_pct"]
        velocidad = fila["velocidad_ppm"]

        if pd.isna(velocidad):
            velocidad = 0

        if comprension < 50 and velocidad < 80:
            return "Riesgo Crítico"
        elif comprension < 60:
            return "Riesgo Alto"
        elif comprension < 80:
            return "Riesgo Medio"
        else:
            return "Riesgo Bajo"

    df["riesgo_lector"] = df.apply(calcular_riesgo, axis=1)
    return df
