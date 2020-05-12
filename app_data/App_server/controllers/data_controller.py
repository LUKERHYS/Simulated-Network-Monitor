from flask import Blueprint, Response

from models.static_data import StaticData
from schemas.static_data_schema import static_data_schema


data_blueprint = Blueprint('data_blueprint', __name__)

@data_blueprint.route('/presentation-data', methods=['GET'])
def get_presentation_data():
    devices = StaticData.query.all()
    
    result = static_data_schema.dumps(devices)
    response = Response(result, status=200, mimetype='application/json')
    return response
