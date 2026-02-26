import mysql.connector

def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Yaurilla2020",
        database="lemar_lectura",
        charset="utf8mb4",
        collation="utf8mb4_general_ci"
    )
    return conexion
