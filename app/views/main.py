from flask import render_template, Blueprint, jsonify, request
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
        if errors_results:
            jsonify(errors_results), 400
        return jsonify(final_result)
    else:
        results = ResultList.query.all()
        results_obj = AllResults(results)
        all_results, errors_all_results = AllResultsListSchema().dump(results_obj)
        if errors_all_results:
            jsonify(errors_all_results), 400
        return jsonify(all_results)


@api.route('/health', methods=['GET'])
def health():
    return jsonify({'message': 'okay'})
