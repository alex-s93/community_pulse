from flask import Blueprint

response_bp = Blueprint('response', __name__, url_prefix='/response')


@response_bp.route('/')
def get_all_response():
    return "GETTING ALL RESPONSE"


@response_bp.route('/add', methods=['POST'])
def add_new_response():
    return "WE ARE ADDED A NEW RESPONSE"
