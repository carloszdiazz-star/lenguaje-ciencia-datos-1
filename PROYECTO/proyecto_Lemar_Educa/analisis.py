import pandas as pd
from conexion import conectar


class AnalisisLector:

    def __init__(self):
        self.df = None

    # 🔹 CARGAR DATOS DESDE MYSQL
    def cargar_datos(self):
        conn = conectar()
        query = "SELECT * FROM alumnos"
        self.df = pd.read_sql(query, conn)
        conn.close()

        # 🔹 LIMPIEZA DE TEXTO
        self.df["seccion"] = self.df["seccion"].str.strip().str.upper()
        self.df["id_real"] = self.df["id_real"].str.strip()

        return self.df

    # 🔹 CLASIFICACIÓN DE RIESGO
    def clasificar_riesgo(self):

        if self.df is None:
            raise ValueError("Primero debe cargar los datos usando cargar_datos()")

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

        self.df["riesgo_lector"] = self.df.apply(calcular_riesgo, axis=1)

        return self.df

    # 🔹 ESTADÍSTICA DESCRIPTIVA
    def estadistica_descriptiva(self):

        if self.df is None:
            raise ValueError("Primero debe cargar los datos.")

        return self.df.describe()

    # 🔹 ANÁLISIS INSTITUCIONAL POR GRADO
    def analisis_por_grado(self):

        if self.df is None:
            raise ValueError("Primero debe cargar los datos.")

        if "riesgo_lector" not in self.df.columns:
            self.clasificar_riesgo()

        resumen_grado = self.df.groupby("grado").agg(
            promedio_comprension=("comprension_pct", "mean"),
            promedio_velocidad=("velocidad_ppm", "mean"),
            desviacion_comprension=("comprension_pct", "std"),
            total_alumnos=("id", "count")
        ).round(2)

        ranking = resumen_grado.sort_values(by="promedio_comprension")

        riesgo_filtrado = self.df[
            self.df["riesgo_lector"].isin(["Riesgo Alto", "Riesgo Crítico"])
        ]

        riesgo_por_grado = riesgo_filtrado.groupby("grado")["id"].count()
        total_por_grado = self.df.groupby("grado")["id"].count()

        porcentaje_riesgo = ((riesgo_por_grado / total_por_grado) * 100).round(2)

        peor_grado = ranking.index[0]
        valor_peor_promedio = ranking.iloc[0]["promedio_comprension"]

        mayor_riesgo = porcentaje_riesgo.idxmax()
        valor_mayor_riesgo = porcentaje_riesgo.max()

        alertas = {
            "peor_grado": peor_grado,
            "valor_peor_promedio": valor_peor_promedio,
            "mayor_riesgo": mayor_riesgo,
            "valor_mayor_riesgo": valor_mayor_riesgo
        }

        return resumen_grado, ranking, porcentaje_riesgo, riesgo_por_grado, alertas

    # 🔹 CORRELACIÓN
    def correlacion_velocidad_comprension(self):

        if self.df is None:
            raise ValueError("Primero debe cargar los datos.")

        return round(
            self.df["comprension_pct"].corr(self.df["velocidad_ppm"]), 3
        )