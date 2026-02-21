from analisis import cargar_datos, clasificar_riesgo

def mostrar_menu():
    print("\n========================================================")
    print("     SISTEMA DE ANÁLISIS EVALUACIÓN COMPRENSIÓN LECTORA")
    print("==========================================================")
    print("1. Mostrar datos")
    print("2. Estadística descriptiva")
    print("3. Análisis por grado")
    print("4. Clasificación de riesgo lector")
    print("5. Relación velocidad vs comprensión")
    print("6. Salir")
    print("==========================================================")

def main():
    df = cargar_datos()
    print("Valores únicos de sección:")
    print(df["seccion"].unique())


    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nPrimeros 5 registros:")
            print(df.head())

        elif opcion == "2":
            print("\nResumen estadístico:")
            print(df.describe())

        elif opcion == "3":

            print("\n========== ANÁLISIS INSTITUCIONAL POR GRADO ==========")

          # 🔹 Aseguramos que exista la clasificación de riesgo
            if "riesgo_lector" not in df.columns:
               df = clasificar_riesgo(df)

          # 🔹 Resumen general por grado
            resumen_grado = df.groupby("grado").agg(
              promedio_comprension=("comprension_pct", "mean"),
              promedio_velocidad=("velocidad_ppm", "mean"),
              desviacion_comprension=("comprension_pct", "std"),
              total_alumnos=("id", "count")
            ).round(2)

            print("\n--- Resumen General por Año ---")
            print(resumen_grado)

         # 🔹 Ranking de peor a mejor según comprensión
            ranking = resumen_grado.sort_values(by="promedio_comprension")

            print("\n--- Ranking (Menor a Mayor Comprensión) ---")
            print(ranking[["promedio_comprension"]])

         # 🔹 Cálculo del % de Riesgo Alto + Crítico
            riesgo_filtrado = df[df["riesgo_lector"].isin(["Riesgo Alto", "Riesgo Crítico"])]

            riesgo_por_grado = riesgo_filtrado.groupby("grado")["id"].count()
            total_por_grado = df.groupby("grado")["id"].count()

            porcentaje_riesgo = ((riesgo_por_grado / total_por_grado) * 100).round(2)

            print("\n--- % de Estudiantes en Riesgo Alto o Crítico ---")
            print(porcentaje_riesgo)

         # 🔹 Identificación automática
            peor_grado = ranking.index[0]
            valor_peor_promedio = ranking.iloc[0]["promedio_comprension"]

            mayor_riesgo = porcentaje_riesgo.idxmax()
            valor_mayor_riesgo = porcentaje_riesgo.max()

            print("\n========== ALERTAS AUTOMÁTICAS ==========")
            print(f"⚠ El {peor_grado}to año de primaria presenta el menor promedio de comprensión lectora ({valor_peor_promedio}%).")
            print(f"🚨 El {mayor_riesgo}to año de primaria presenta el mayor porcentaje de estudiantes en Riesgo Alto o Crítico ({valor_mayor_riesgo}%).")
            print("\nCantidad real de alumnos en riesgo por grado:")
            print(riesgo_por_grado)
        elif opcion == "4":
            df = clasificar_riesgo(df)

            total = len(df)
            print(f"\nTotal de alumnos registrados: {total}")

            while True:
                try:
                    cantidad = int(input("¿Cuántos alumnos deseas visualizar? "))

                    if 1 <= cantidad <= total:
                        break
                    else:
                        print(f"Ingrese un número entre 1 y {total}")

                except ValueError:
                    print("Ingrese un número válido.")

            print("\nResultados:")
            print(df[[
                
                "id_real",
                "comprension_pct",
                "velocidad_ppm",
                "grado",
                "seccion",
                "riesgo_lector"
            ]].head(cantidad).to_string())


            print("\nDistribución general de riesgo:")
            print(df["riesgo_lector"].value_counts())

        elif opcion == "5":
            print("\nRelación Velocidad vs Comprensión:")
            correlacion = df["comprension_pct"].corr(df["velocidad_ppm"])
            print("Correlación:", round(correlacion, 3))

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
#Version 1.0 21/02/2026

