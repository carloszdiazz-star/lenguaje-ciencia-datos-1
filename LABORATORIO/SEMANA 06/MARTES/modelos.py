
import mysql.connector

class Conexion:
    def conectar(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Yaurilla2020",
            database="colegio_sistema"
        )

class Estudiante(Conexion):
   
   def insertar(self,nombre):
       db = self.conectar()
       cursor = db.cursor()
       sql = "INSERT INTO estudiante (nombre) VALUES (%s)"
       valores = (nombre,)
       cursor.execute(sql,valores)
       db.commit()
       db.close()

   def listar(self):
       db = self.conectar()
       cursor = db.cursor()
       sql = "SELECT * FROM estudiante"
       cursor.execute(sql)
       res = cursor.fetchall()
       db.close()
       return res

class Curso(Conexion):

    def insertar(self,nombre):
        db = self.conectar()
        cursor = db.cursor()
        sql = "INSERT INTO curso (nombre_curso) VALUES (%s)"
        valores = (nombre,)
        cursor.execute(sql,valores)
        db.commit()
        db.close()

    def listar(self):
        db = self.conectar()
        cursor = db.cursor()
        sql = "SELECT * FROM curso"
        cursor.execute(sql)
        res = cursor.fetchall()
        db.close()
        return res    

class Matricula(Conexion):
    def registrar_matricula(self,id_est,id_cur):
        db = self.conectar()
        cursor = db.cursor()
        sql = "INSERT INTO matricula (id_estudiante,id_curso) VALUES (%s,%s)"
        valores = (id_est,id_cur)
        cursor.execute(sql,valores)
        db.commit()
        db.close()

    def listar_todo(self):
        db = self.conectar()
        cursor = db.cursor()
        sql = """
            SELECT m.id_matricula,e.nombre,c.nombre_curso
            FROM matricula m
            JOIN estudiante e ON m.id_estudiante = e.id_estudiante
            JOIN curso c ON m.id_curso = c.id_curso            
        """
        cursor.execute(sql)
        res = cursor.fetchall()
        db.close()
        return res