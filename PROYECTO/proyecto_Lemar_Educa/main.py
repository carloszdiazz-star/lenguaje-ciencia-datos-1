from analisis import cargar_datos, clasificar_riesgo

def mostrar_menu():
    print("\n========================================")
    print("     SISTEMA DE ANÁLISIS LEMAR EDUCA")
    print("========================================")
    print("1. Mostrar datos")
    print("2. Estadística descriptiva")
    print("3. Análisis por grado")
    print("4. Clasificación de riesgo lector")
    print("5. Relación velocidad vs comprensión")
    print("6. Salir")
    print("========================================")

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
            print("\n========== ANÁLISIS POR GRADO ==========")

            resumen_grado = df.groupby("grado").agg(
                promedio_comprension=("comprension_pct", "mean"),
                promedio_velocidad=("velocidad_ppm", "mean"),
                desviacion_comprension=("comprension_pct", "std"),
                total_alumnos=("id", "count")
                ).round(2)

            print(resumen_grado)

            print("\n========== ANÁLISIS POR GRADO Y SECCIÓN ==========")

            resumen_seccion = df.groupby(["grado", "seccion"]).agg(
                promedio_comprension=("comprension_pct", "mean"),
                promedio_velocidad=("velocidad_ppm", "mean"),
                total_alumnos=("id", "count")
                ).round(2)

            print(resumen_seccion)

           # Ranking automático
            peor_grado = resumen_grado["promedio_comprension"].idxmin()
            mejor_grado = resumen_grado["promedio_comprension"].idxmax()

            print("\n========== INSIGHT AUTOMÁTICO ==========")
            print(f"⚠ El grado con menor promedio de comprensión es: {peor_grado}")
            print(f"🏆 El grado con mayor promedio de comprensión es: {mejor_grado}")


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


