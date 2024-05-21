from flask import Blueprint

questions_bp = Blueprint('questions', __name__, url_prefix='/questions')


@questions_bp.route('/')
def get_all_questions():
    return "GETTING ALL QUESTIONS"


@questions_bp.route('/add', methods=['POST'])
def add_new_question():
    return "WE ARE ADDED A NEW QUESTION"


@questions_bp.route('/<int:question_id>')
def get_question_by_id(question_id):
    return f"GETTING QUESTION BY ID - '{question_id}'"


@questions_bp.route('/update/<int:question_id>', methods=['PUT'])  # 127.0.0.1:5000/questions/update/5
def update_question_by_pk(question_id):
    return f"UPDATE QUESTION BY QUESTION ID - '{question_id}'"


@questions_bp.route('/delete/<int:question_id>', methods=['DELETE'])
def delete_question_by_pk(question_id):
    return f"DELETE QUESTION BY QUESTION ID - '{question_id}'"
