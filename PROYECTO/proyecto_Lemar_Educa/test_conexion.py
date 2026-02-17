from conexion import conectar

try:
    conn = conectar()
    print("✅ Conexión exitosa a MySQL")
    conn.close()
except Exception as e:
    print("❌ Error:", e)
