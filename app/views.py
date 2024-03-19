from flask import Flask, jsonify, request, render_template
from sqlalchemy.orm import Session
from models import Data
from database import get_session
import requests

# Definición de la aplicación Flask
app = Flask(__name__)

# Función para obtener datos del servicio externo
def get_external_data(self):
    URL = 'https://dog.ceo/api/breeds/list/all'
    response = requests.get(URL)
    data = response.json()

    # Si la solicitud es exitosa, convertir la respuesta en una lista de objetos de raza
    if response.status_code == 200:
        breeds_to_insert = []
        for breed_name, sub_breeds in data['message'].items():
            breed = Breed(breed_name, sub_breeds)
            breeds_to_insert.append(breed)
        self.insert_breeds(breeds_to_insert)
        return [breed.to_dict() for breed in breeds_to_insert]
    else:
        # Manejar el error
        print('Error al obtener datos de la API')
        return None

# Almacenar los datos en la base de datos

@app.route('/api/data/sync', methods=["POST"])
def sync_data():
    data = get_external_data()
    session = get_session()
    for data_item in data:
        data_model = Data(**data_item)
        session.add(data_model)
    session.commit()
    session.close()

    return jsonify({"success": "Datos sincronizados correctamente"})

    

# Endpoint GET /api/data
@app.route("/api/data", methods=["GET"])
def get_data():
    session = get_session()
    data = session.query(Data).order_by(Data.id.desc()).all()
    session.close()
    return jsonify([data_model.to_dict() for data_model in data])

# Endpoint POST /api/data
@app.route("/api/data", methods=["POST"])
def create_data():
    session = get_session()
    data_model = Data(**request.get_json())
    session.add(data_model)
    session.commit()
    session.close()
    return jsonify(data_model.to_dict())

# Endpoint GET /api/data/{id}
@app.route("/api/data/<int:id>", methods=["GET"])
def get_data_by_id(id):
    session = get_session()
    data = session.query(Data).get(id)
    session.close()
    if data is None:
        return jsonify({"error": "Dato no encontrado"}), 404
    return jsonify(data.to_dict())

# Websocket
@app.route("/websocket")
def websocket_endpoint():
    pass


