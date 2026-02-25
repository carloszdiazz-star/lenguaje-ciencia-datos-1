from analisis import AnalisisLector
import pandas as pd


def mostrar_menu():
    print("\n========================================================")
    print("     SISTEMA DE ANÁLISIS EVALUACIÓN COMPRENSIÓN LECTORA")
    print("========================================================")
    print("1. Mostrar datos")
    print("2. Estadística descriptiva")
    print("3. Análisis institucional por grado")
    print("4. Análisis detallado por año escolar")
    print("5. Clasificación de riesgo lector")
    print("6. ÍNDICE DE FLUIDEZ EFECTIVA LEMAR (IFEL)")
    print("7. Salir")
    print("========================================================")


def main():
    analisis = AnalisisLector()
    analisis.cargar_datos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        # ==================================================
        if opcion == "1":
            # Asegurar riesgo
            if "riesgo_lector" not in analisis.df.columns:
                analisis.clasificar_riesgo()

            # Pedir grado
            while True:
                try:
                    grado = int(input("Ingrese el año escolar (3,4,5,6): "))
                    if grado in [3, 4, 5, 6]:
                        break
                    print("Ingrese solo 3, 4, 5 o 6.")
                except ValueError:
                    print("Ingrese un número válido.")

            # Pedir sección
            seccion = input("Ingrese la sección (A, B, C): ").strip().upper()

            # Filtrar salón
            df_salon = analisis.df[
                (analisis.df["grado"] == grado) & (analisis.df["seccion"] == seccion)
            ].copy()

            if df_salon.empty:
                print(f"\nNo se encontraron alumnos para {grado}° {seccion}. Verifique grado/sección.")
            else:
                total_alumnos = len(df_salon)

                # Resumen
                prom_comp = df_salon["comprension_pct"].mean()
                prom_vel = df_salon["velocidad_ppm"].mean()
                vel_txt = "N/A" if pd.isna(prom_vel) else f"{prom_vel:.2f} ppm"

                # Riesgo Alto + Crítico
                en_riesgo = df_salon[df_salon["riesgo_lector"].isin(["Riesgo Alto", "Riesgo Crítico"])]
                cant_riesgo = len(en_riesgo)
                pct_riesgo = (cant_riesgo / total_alumnos) * 100

                # Impresión tipo reporte
                print("\n========================================================")
                print(f"           LISTADO DE ALUMNOS – {grado}° {seccion}")
                print("========================================================\n")

                print(f"Total alumnos: {total_alumnos}\n")

                print("Resumen del salón:")
                print("----------------------------------------")
                print(f"Promedio comprensión: {prom_comp:.2f}%")
                print(f"Promedio velocidad:   {vel_txt}")
                print(f"En Riesgo Alto/Crítico: {cant_riesgo} alumnos ({pct_riesgo:.2f}%)")
                print("----------------------------------------\n")

                print("Listado de estudiantes:\n")

                # Mostrar todo el salón, ordenado por nombre (opcional)
                df_salon = df_salon.sort_values(by="id_real")

                # Tabla “bonita”
                print("Nombre                              Comprensión   Velocidad   Riesgo")
                print("-----------------------------------------------------------------------")

                for _, fila in df_salon.iterrows():
                    nombre = str(fila["id_real"])[:32].ljust(32)  # recorta y alinea
                    comp = f"{fila['comprension_pct']:.2f}%".rjust(10)

                    if pd.isna(fila["velocidad_ppm"]):
                        vel = "N/A".rjust(10)
                    else:
                        vel = f"{fila['velocidad_ppm']:.2f}".rjust(10)

                    riesgo = str(fila["riesgo_lector"]).replace("Riesgo ", "")
                    print(f"{nombre} {comp} {vel}   {riesgo}")

        # ==================================================
        elif opcion == "2":
            print("\nResumen estadístico:")
            print(analisis.estadistica_descriptiva())

        # ==================================================
        elif opcion == "3":
            print("\n========================================================")
            print("        ANÁLISIS INSTITUCIONAL POR GRADO")
            print("========================================================")

            # 🔹 Asegurar columna riesgo_lector
            if "riesgo_lector" not in analisis.df.columns:
                analisis.clasificar_riesgo()

            # 🔹 Resumen por grado
            resumen_grado = analisis.df.groupby("grado").agg(
                total_alumnos=("id", "count"),
                prom_comprension=("comprension_pct", "mean"),
                prom_velocidad=("velocidad_ppm", "mean")
            ).round(2)

            # 🔹 Riesgo Alto + Crítico (cantidad y %)
            riesgo_filtrado = analisis.df[
                analisis.df["riesgo_lector"].isin(["Riesgo Alto", "Riesgo Crítico"])
            ]

            riesgo_por_grado = riesgo_filtrado.groupby("grado")["id"].count()
            total_por_grado = analisis.df.groupby("grado")["id"].count()
            porcentaje_riesgo = ((riesgo_por_grado / total_por_grado) * 100).round(2)

            # Asegurar que todos los grados aparezcan (si alguno tiene 0 riesgo)
            riesgo_por_grado = riesgo_por_grado.reindex(total_por_grado.index, fill_value=0)
            porcentaje_riesgo = porcentaje_riesgo.reindex(total_por_grado.index, fill_value=0)

            # 🔹 Imprimir resumen general
            print("\nResumen General (por año):\n")
            print("Año | Total | Prom. Comprensión | Prom. Velocidad")
            print("--------------------------------------------------")

            for grado, fila in resumen_grado.iterrows():
                total = int(fila["total_alumnos"])
                pc = fila["prom_comprension"]
                pv = fila["prom_velocidad"]
                pv_txt = "N/A" if pd.isna(pv) else f"{pv:.2f} ppm"
                print(f"{grado}°  | {total:<5} | {pc:>7.2f}%           | {pv_txt}")

            # 🔹 Imprimir indicadores de riesgo
            print("\n\nIndicadores de Riesgo (Alto + Crítico):\n")
            print("Año | En Riesgo | % Riesgo")
            print("--------------------------")

            for grado in resumen_grado.index:
                cant = int(riesgo_por_grado.loc[grado])
                pct = float(porcentaje_riesgo.loc[grado])
                print(f"{grado}°  | {cant:<9} | {pct:.2f}%")

            # 🔹 Ranking institucional por comprensión
            ranking = resumen_grado.sort_values(by="prom_comprension")
            orden = "  →  ".join([f"{g}°" for g in ranking.index])

            # 🔹 Alertas automáticas
            peor_grado = ranking.index[0]
            peor_valor = ranking.iloc[0]["prom_comprension"]

            mejor_grado = ranking.index[-1]
            mejor_valor = ranking.iloc[-1]["prom_comprension"]

            mayor_riesgo_grado = porcentaje_riesgo.idxmax()
            mayor_riesgo_pct = porcentaje_riesgo.max()

            print("\n\nRanking institucional (Comprensión):\n")
            print(f"Peor → Mejor: {orden}")

            print("\n\n========================================================")
            print("                 ALERTAS AUTOMÁTICAS")
            print("========================================================")
            print(f"⚠  El {peor_grado}° año de primaria presenta el menor promedio de comprensión lectora ({peor_valor:.2f}%).")
            print(f"🚨 El {mayor_riesgo_grado}° año de primaria presenta el mayor porcentaje de estudiantes en Riesgo Alto o Crítico ({mayor_riesgo_pct:.2f}%).")
            print(f"🏆 El {mejor_grado}° año de primaria presenta el mejor promedio de comprensión lectora ({mejor_valor:.2f}%).")
            print("\n(Nota: “En Riesgo” = Riesgo Alto + Riesgo Crítico)")

        # ==================================================
        elif opcion == "4":
            # Análisis detallado por año escolar (grado)

            # Asegurar riesgo
            if "riesgo_lector" not in analisis.df.columns:
                analisis.clasificar_riesgo()

            # Pedir grado
            while True:
                try:
                    grado_ingresado = int(input("Ingrese el año escolar (3,4,5,6): "))
                    if grado_ingresado in [3, 4, 5, 6]:
                        break
                    print("Ingrese solo 3, 4, 5 o 6.")
                except ValueError:
                    print("Ingrese un número válido (3,4,5,6).")

            df_grado = analisis.df[analisis.df["grado"] == grado_ingresado].copy()

            print("\n========================================================")
            print(f"        ANÁLISIS DETALLADO – {grado_ingresado}° AÑO")
            print("========================================================")

            # Promedios generales del grado
            prom_grado_comp = df_grado["comprension_pct"].mean()
            prom_grado_vel = df_grado["velocidad_ppm"].mean()  # puede ser NaN si faltan datos

            vel_txt = "N/A" if pd.isna(prom_grado_vel) else f"{prom_grado_vel:.2f} ppm"

            print(f"\nPromedio general {grado_ingresado}°:")
            print(f"- Comprensión: {prom_grado_comp:.2f}%")
            print(f"- Velocidad:   {vel_txt}\n")

            # ---------------------------------------------------------
            # Tabla resumen por sección
            # ---------------------------------------------------------
            # Promedios por sección
            resumen_sec = df_grado.groupby("seccion").agg(
                total=("id", "count"),
                prom_comp=("comprension_pct", "mean"),
                prom_vel=("velocidad_ppm", "mean")
            ).round(2)

            # % riesgo alto + crítico por sección
            riesgo_ac = df_grado[df_grado["riesgo_lector"].isin(["Riesgo Alto", "Riesgo Crítico"])]
            cant_riesgo_sec = riesgo_ac.groupby("seccion")["id"].count()
            total_sec = df_grado.groupby("seccion")["id"].count()
            pct_riesgo_sec = ((cant_riesgo_sec / total_sec) * 100).round(2)

            # Asegurar secciones con 0 riesgo
            pct_riesgo_sec = pct_riesgo_sec.reindex(total_sec.index, fill_value=0)
            cant_riesgo_sec = cant_riesgo_sec.reindex(total_sec.index, fill_value=0)

            # Unimos a resumen
            resumen_sec["pct_riesgo_alto_critico"] = pct_riesgo_sec

            # Ordenar por comprensión (de mejor a peor)
            resumen_sec = resumen_sec.sort_values(by="prom_comp", ascending=False)

            print("Resumen por sección:\n")
            print("Sección | Total | Prom. Comprensión | Prom. Velocidad | % Riesgo (Alto+Crítico)")
            print("---------------------------------------------------------------------------")

            for seccion, fila in resumen_sec.iterrows():
                total = int(fila["total"])
                pc = fila["prom_comp"]
                pv = fila["prom_vel"]
                pv_txt = "N/A" if pd.isna(pv) else f"{pv:.2f} ppm"
                pct = float(fila["pct_riesgo_alto_critico"])
                print(f"{grado_ingresado}° {seccion:<3} | {total:<5} | {pc:>7.2f}%           | {pv_txt:<12} | {pct:>6.2f}%")

            # ---------------------------------------------------------
            # Distribución de riesgo por sección (conteo)
            # ---------------------------------------------------------
            print("\nDistribución de riesgo por sección (conteo):\n")

            riesgos_orden = ["Riesgo Bajo", "Riesgo Medio", "Riesgo Alto", "Riesgo Crítico"]

            for seccion in resumen_sec.index:
                sub = df_grado[df_grado["seccion"] == seccion]
                conteo = sub["riesgo_lector"].value_counts().reindex(riesgos_orden, fill_value=0)

                print(
                    f"Sección {grado_ingresado}° {seccion} → "
                    f"Bajo: {int(conteo['Riesgo Bajo'])} | "
                    f"Medio: {int(conteo['Riesgo Medio'])} | "
                    f"Alto: {int(conteo['Riesgo Alto'])} | "
                    f"Crítico: {int(conteo['Riesgo Crítico'])}"
                )

            # ---------------------------------------------------------
            # Sección prioritaria
            # (criterio: mayor % Alto+Crítico; si empate, menor comprensión)
            # ---------------------------------------------------------
            peor_por_riesgo = resumen_sec.sort_values(
                by=["pct_riesgo_alto_critico", "prom_comp"],
                ascending=[False, True]
            ).iloc[0]

            seccion_prioritaria = resumen_sec.sort_values(
                by=["pct_riesgo_alto_critico", "prom_comp"],
                ascending=[False, True]
            ).index[0]

            prom_prioritaria = peor_por_riesgo["prom_comp"]
            pct_prioritaria = peor_por_riesgo["pct_riesgo_alto_critico"]

            print("\n⚠ Sección prioritaria:", f"{grado_ingresado}° {seccion_prioritaria}")
            print(f"- Menor desempeño (según prioridad): {prom_prioritaria:.2f}%")
            print(f"- Mayor % de Alto+Crítico: {pct_prioritaria:.2f}%")

            # ---------------------------------------------------------
            # Impacto si se excluye la sección más baja en comprensión
            # ---------------------------------------------------------
            seccion_menor_comp = resumen_sec.sort_values(by="prom_comp").index[0]

            df_sin_peor = df_grado[df_grado["seccion"] != seccion_menor_comp]
            prom_sin_peor = df_sin_peor["comprension_pct"].mean()

            impacto = prom_sin_peor - prom_grado_comp  # positivo = sube
            print(f"\nSi se excluyera {grado_ingresado}° {seccion_menor_comp}:")
            print(f"Promedio estimado de comprensión del {grado_ingresado}° año: {prom_sin_peor:.2f}%")
            print(f"Impacto (sube): +{impacto:.2f} puntos porcentuales")

        # ==================================================
        elif opcion == "5":
            # Asegurar riesgo
            if "riesgo_lector" not in analisis.df.columns:
                analisis.clasificar_riesgo()

            print("\n========================================================")
            print("        VISUALIZAR ALUMNOS POR NIVEL DE RIESGO")
            print("========================================================")
            print("1. Riesgo Bajo")
            print("2. Riesgo Medio")
            print("3. Riesgo Alto")
            print("4. Riesgo Crítico")

            mapa = {
                "1": "Riesgo Bajo",
                "2": "Riesgo Medio",
                "3": "Riesgo Alto",
                "4": "Riesgo Crítico"
            }

            # Pedir nivel
            while True:
                op_riesgo = input("Seleccione el nivel de riesgo (1-4): ").strip()
                if op_riesgo in mapa:
                    riesgo_seleccionado = mapa[op_riesgo]
                    break
                print("Opción inválida. Ingrese un número del 1 al 4.")

            # Filtrar
            df_riesgo = analisis.df[analisis.df["riesgo_lector"] == riesgo_seleccionado].copy()

            total = len(df_riesgo)

            print("\n========================================================")
            print(f"              ALUMNOS EN {riesgo_seleccionado.upper()}")
            print("========================================================")
            print(f"Total alumnos en este nivel: {total}\n")

            if total == 0:
                print("No se encontraron alumnos en este nivel de riesgo.")
            else:
                # Distribución por grado
                dist_grado = df_riesgo.groupby("grado")["id"].count().sort_index()

                print("Distribución por año escolar:")
                for g, c in dist_grado.items():
                    print(f"{g}° → {int(c)} alumnos")

                # Preguntar cuántos mostrar
                while True:
                    try:
                        cantidad = int(input("\n¿Cuántos alumnos desea visualizar?: "))
                        if 1 <= cantidad <= total:
                            break
                        print(f"Ingrese un número entre 1 y {total}")
                    except ValueError:
                        print("Ingrese un número válido.")

                # Ordenar para que se vea profesional:
                # primero grado, luego sección, luego comprensión ascendente (más bajo primero)
                df_riesgo = df_riesgo.sort_values(
                    by=["grado", "seccion", "comprension_pct", "velocidad_ppm"],
                    ascending=[True, True, True, True]
                )

                print("\nListado de alumnos (ordenado por grado y desempeño):\n")
                print(df_riesgo[
                    ["id_real", "grado", "seccion", "comprension_pct", "velocidad_ppm"]
                ].head(cantidad).to_string(index=False))
        # ==================================================
        elif opcion == "6":
            print("\n========================================================")
            print("     ÍNDICE DE FLUIDEZ EFECTIVA LEMAR (IFEL)")
            print("========================================================")

            # Calcular IFEL (crea columnas ifel y factor_fluidez)
            analisis.calcular_ifel()

            # Pedir top
            while True:
                try:
                    top_n = int(input("¿Cuántos alumnos mostrar en el TOP? (ej: 10): "))
                    if top_n > 0:
                        break
                    print("Ingrese un número mayor a 0.")
                except ValueError:
                    print("Ingrese un número válido.")

            prom_ifel_grado, top, rapidos_sin_comp, lentos_con_comp = analisis.reporte_ifel(top_n=top_n)

            print("\n--- Promedio IFEL por grado ---")
            for grado, valor in prom_ifel_grado.items():
                print(f"{grado}° → {valor}")

            print(f"\n--- TOP {top_n} Lectores más eficientes (IFEL) ---")
            print(top.to_string(index=False))

            print("\n--- Casos: Muy rápidos pero con baja comprensión (vel>160 y comp<75) ---")
            if rapidos_sin_comp.empty:
                print("No se encontraron casos en este criterio.")
            else:
                print(rapidos_sin_comp.head(top_n).to_string(index=False))

            print("\n--- Casos: Comprenden bien pero leen muy lento (vel<80 y comp>=75) ---")
            if lentos_con_comp.empty:
                print("No se encontraron casos en este criterio.")
            else:
                print(lentos_con_comp.head(top_n).to_string(index=False))
        # ==================================================
        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        # ==================================================
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()