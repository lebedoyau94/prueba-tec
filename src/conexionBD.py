import pymysql
import os

from flask import Flask, jsonify

class Conexion:

  def __init__(self):
    self.conn = pymysql.connect(
      host='localhost',
      user='root',
      password='',
      db='Vacantes'
    )
    self.cursor = self.conn.cursor()

  def insertar(self, titulo, empresa, ubicacion):
    print("\n {}, {}, {}".format(titulo, empresa, ubicacion))
    #Creamos la consulta SQL para insertar los datos de la vacante
    sql = "INSERT INTO Trabajos(titulo, empresa, ubicacion) VALUES ('{}', '{}', '{}')".format(titulo, empresa, ubicacion)
    self.cursor.execute(sql)
    self.conn.commit()
    print("Datos ingresados correctamente a la base de datos")

  def busqueda(self,termino_busqueda):
    # Consulta SQL para obtener los primeros 10 resultados más parecidos en base a un termino de busqueda
    query = "SELECT * FROM Trabajos WHERE Titulo LIKE %s ORDER BY Titulo LIMIT 10"

    # Ejecutar consulta
    self.cursor.execute(query, ('%'+termino_busqueda+'%',))

    # Obtener resultados
    results = self.cursor.fetchall()

    # Cerrar cursor
    self.conn.commit()

    # Devolver resultados en formato JSON
    return jsonify(results)
