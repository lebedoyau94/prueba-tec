from flask import Flask, jsonify, request
import conexionBD

#Creamos la api
app = Flask(__name__)

#Nos traemos la base de datos
conexion = conexionBD.Conexion()

@app.route('/users', methods=['GET'])
def get_users():
    # Obtener datos de usuarios de la base de datos MySQL
    # ...
    return jsonify(users)



@app.route('/search', methods=['GET'])
def search():
  search_term = request.args.get('q')
  json = conexion.busqueda(search_term)
  return json

if __name__ == '__main__':
  app.run(debug=True)