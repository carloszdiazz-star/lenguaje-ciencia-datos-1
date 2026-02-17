from conexion import conectar

conn = conectar()

# Forzar codificación correcta
conn.set_charset_collation('utf8mb4')

cursor = conn.cursor()

cursor.execute("SELECT id, id_real, comprension_pct FROM alumnos LIMIT 20")

resultados = cursor.fetchall()

for fila in resultados:
    print(fila)

cursor.close()
conn.close()
