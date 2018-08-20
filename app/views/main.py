from sqlalchemy_utils.functions import database_exists

from flask import render_template, Blueprint, jsonify, request, current_app
from flask_cors import CORS


from app.models import ResultList
from app.core import db
from app.schemas import ValidationSchema, ResultListSchema, AllResultsListSchema
from app.toolbox.results import AllResults

api = Blueprint('api', __name__, static_folder='../static', template_folder='../templates')

CORS(api)


@api.route('/', defaults={'path': ''})
@api.route('/<path:path>')
def catch_all(path):
    return render_template('error.html', message='404 not found'), 404


@api.route('/calculate', methods=['POST', 'GET'])
def calculate():
    if request.method == 'POST':
        req_data = request.get_json()
        data, errors_validation = ValidationSchema().load(req_data)
        if errors_validation:
            return jsonify(errors_validation), 400
        result = ResultList(req_data['vector1'], req_data['vector2'])
        db.session.add(result)
        try:
            db.session.commit()
        except Exception as e:
            # this shouldn't happen
            return jsonify({'error': e}), 500
        final_result, errors_results = ResultListSchema().dump(result)
        return jsonify(final_result) if not errors_results else jsonify(errors_results), 400
    else:
        results = ResultList.query.all()
        results_obj = AllResults(results)
        all_results, errors = AllResultsListSchema().dump(results_obj)
        return jsonify(all_results) if not errors else jsonify(errors), 400


@api.route('/health', methods=['GET'])
def health():
    return jsonify({'message': 'okay'})
