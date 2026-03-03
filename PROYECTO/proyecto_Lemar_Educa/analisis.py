import pandas as pd
from conexion import conectar


class AnalisisLector:

    def __init__(self):
        self.df = None

    #  CARGAR DATOS DESDE MYSQL
    def cargar_datos(self):
        conn = conectar()
        query = "SELECT * FROM alumnos"
        self.df = pd.read_sql(query, conn)
        conn.close()

        #  LIMPIEZA DE TEXTO
        self.df["seccion"] = self.df["seccion"].str.strip().str.upper()
        self.df["id_real"] = self.df["id_real"].str.strip()

        return self.df

    #  CLASIFICACIÓN DE RIESGO
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

    #  ESTADÍSTICA DESCRIPTIVA
    def estadistica_descriptiva(self):

        if self.df is None:
            raise ValueError("Primero debe cargar los datos.")

        return self.df.describe()

    #  ANÁLISIS INSTITUCIONAL POR GRADO
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

    #  CORRELACIÓN
    def correlacion_velocidad_comprension(self):

        if self.df is None:
            raise ValueError("Primero debe cargar los datos.")

        return round(
            self.df["comprension_pct"].corr(self.df["velocidad_ppm"]), 3
        )

    def calcular_ifel(self):
        """
        Crea el Índice de Fluidez Efectiva Lemar (IFEL).
        IFEL = comprensión_pct * factor_fluidez

        factor_fluidez:
        - velocidad < 80   -> 0.85
        - 80 a 160         -> 1.00
        - > 160            -> 0.90
        - velocidad null   -> 0.70 (penalización mayor)
        """

        if self.df is None or self.df.empty:
            raise ValueError("Primero debes cargar los datos (cargar_datos).")

        # Asegurar riesgo_lector (útil para reportes y coherencia)
        if "riesgo_lector" not in self.df.columns:
            self.clasificar_riesgo()

        def factor_fluidez(vel):
            if pd.isna(vel):
                return 0.70
            if vel < 80:
                return 0.85
            elif vel <= 160:
                return 1.00
            else:
                return 0.90

        self.df["factor_fluidez"] = self.df["velocidad_ppm"].apply(factor_fluidez)
        self.df["ifel"] = (self.df["comprension_pct"] * self.df["factor_fluidez"]).round(2)

        return self.df

    def reporte_ifel(self, top_n=10):
        """
        Devuelve:
        - promedio IFEL por grado
        - top N alumnos por IFEL
        - alertas útiles (casos típicos del negocio)
        """
        if "ifel" not in self.df.columns:
            self.calcular_ifel()

        # Promedio IFEL por grado
        prom_ifel_grado = (
            self.df.groupby("grado")["ifel"]
            .mean()
            .round(2)
            .sort_index()
        )

        # Top N (solo alumnos con velocidad disponible para que sea más justo)
        df_con_vel = self.df.dropna(subset=["velocidad_ppm"]).copy()
        top = (
            df_con_vel.sort_values(by="ifel", ascending=False)
            .head(top_n)[["id_real", "grado", "seccion", "comprension_pct", "velocidad_ppm", "ifel", "riesgo_lector"]]
        )

        # Casos típicos (muy útiles para Lemar):
        # 1) Rápidos pero no comprenden
        rapidos_sin_comp = df_con_vel[
            (df_con_vel["velocidad_ppm"] > 160) & (df_con_vel["comprension_pct"] < 75)
        ][["id_real", "grado", "seccion", "comprension_pct", "velocidad_ppm", "ifel"]].sort_values("ifel")

        # 2) Comprenden bien pero muy lentos
        lentos_con_comp = df_con_vel[
            (df_con_vel["velocidad_ppm"] < 80) & (df_con_vel["comprension_pct"] >= 75)
        ][["id_real", "grado", "seccion", "comprension_pct", "velocidad_ppm", "ifel"]].sort_values("ifel")

        return prom_ifel_grado, top, rapidos_sin_comp, lentos_con_comp  