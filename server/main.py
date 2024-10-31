from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configura la conexión a la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/postgres'
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

# Ruta de ejemplo con datos ficticios
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"data": "Este es un dato de ejemplo "})

class Cargos(db.Model):
    idcargo = db.Column(db.Integer, primary_key=True)
    nombrecargo = db.Column(db.String(50), nullable=False)


# Ruta de ejemplo para agregar un nuevo cargo
@app.route('/api/cargos/crear', methods=['POST'])
def add_cargos():
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Invalid input, JSON expected'}), 400
    
    if 'nombrecargo' not in data:
        return jsonify({'error': 'Missing field: nombrecargo'}), 400

    nuevo_cargo = Cargos(nombrecargo=data['nombrecargo'])
    db.session.add(nuevo_cargo)
    db.session.commit()
    return jsonify({'message': 'Cargo creado'}), 201


# Ruta de ejemplo para obtener todos los cargos
@app.route('/api/cargos', methods=['GET'])
def get_cargos():
    cargos = Cargos.query.all()
    return jsonify([{ 'idcargo': c.idcargo, 'nombrecargo': c.nombrecargo } for c in cargos]), 200



if __name__ == '__main__':
    app.run(debug=True)



