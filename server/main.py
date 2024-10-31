from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configura la conexión a la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:contraseña@localhost:5432/nombre_basededatos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Ruta raíz
@app.route('/')
def home():
    return jsonify({"message": "¡Bienvenido a la API Flask!"})

# Ruta de ejemplo
@app.route('/api')
def api():
    return jsonify({"message": "¡Hola desde la API Flask!"})

if __name__ == '__main__':
    app.run(debug=True)



