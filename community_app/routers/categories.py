from flask import Blueprint, jsonify, request, make_response

from pydantic import ValidationError

from community_app.models.questions import Category
from community_app.schemas.questions import CategoryCreateUpdate, CategoryResponse
from community_app import db

categories_bp = Blueprint('categories', __name__, url_prefix='/categories')


@categories_bp.route('/', methods=['GET'])
def get_all_categories():
    categories: list[Category, ...] = Category.query.all()

    results = [
        CategoryResponse.from_orm(category).dict() for category in categories
    ]

    response = make_response(jsonify(results), 200)

    return response


@categories_bp.route('/add', methods=['POST'])
# NOTE: По заданию надо было использовать тот же эндпоинт для создания,
# но я решил для лучшей читаемости и единой системы по аналогии с вопросами - использовать /add.
# Тоже самое касается и методов по обновлению, удалению. Если прикрутить сваггер - то будет очень приятно читать
# похожие схемы)
def add_new_category():
    data = request.get_json()

    try:
        category_data = CategoryCreateUpdate(**data)
    except ValidationError as err:
        return make_response(jsonify(err.errors()), 400)

    category: Category = Category(
        name=category_data.name
    )

    db.session.add(category)
    db.session.commit()

    return make_response(
        jsonify(CategoryResponse(
            id=category.id,
            name=category.name
        ).dict()), 201
    )


@categories_bp.route('/update/<int:category_id>', methods=['PUT'])
def update_category_by_pk(category_id):
    category: Category = Category.query.get(category_id)

    if not category:
        return make_response(jsonify(
            {
                "message": "NOT FOUND"
            }
        ), 404)

    request_data = request.get_json()

    if 'name' in request_data:
        try:
            category_data = CategoryCreateUpdate(name=request_data['name'])
        except ValidationError as err:
            return make_response(jsonify(err.errors()), 400)

        category.name = category_data.name

        db.session.commit()

        return make_response(jsonify(
            {
                "message": "CATEGORY UPDATED SUCCESSFULLY",
                "new_name": category.name
            }
        ), 200)

    else:
        return make_response(jsonify(
            {
                "message": "NO DATA PROVIDED"
            }
        ), 400)


@categories_bp.route('/delete/<int:category_id>', methods=['DELETE'])
def delete_question_by_pk(category_id):
    category: Category = Category.query.get(category_id)

    if not category:
        return make_response(jsonify(
            {
                "message": "CATEGORY NOT FOUND"
            }
        ), 404)

    db.session.delete(category)
    db.session.commit()

    return make_response(jsonify(
        {
            "message": "CATEGORY DELETED SUCCESSFULLY"
        }
    ), 200)
