from flask import render_template, Blueprint, jsonify, request
from flask_cors import CORS

from app.models import Result
from app.core import db
import app.schemas as s
from app.toolbox import vectors as v

api = Blueprint('api', __name__, static_folder='../static', template_folder='../templates')

CORS(api)


@api.route('/', defaults={'path': ''})
@api.route('/<path:path>')
def catch_all(path):
    return render_template('error.html', message='404 not found')


@api.route('/calculate', methods=['POST', 'GET'])
def testit():
    if request.method == 'POST':
        req_data = request.get_json()
        data, error = s.ValidateSchema().load(req_data)
        if error:
            return jsonify(error), 400
        vector = v.Vectors(data['vector1'], data['vector2'])
        result = Result(v1=[v1 for v1 in vector.vector1], v2=[v2 for v2 in vector.vector2],
                        cp=[cp for cp in vector.result])
        vector.created = result.created
        db.session.add(result)
        try:
            db.session.commit()
            vector.id = result.id
        except Exception as e:
            return jsonify({'woops': 'sorry'})
        return jsonify(s.ResultListSchema().dump(vector).data)
    else:
        results = Result.query.all()
        all_results = v.AllVectors()
        for result in results:
            vector = v.Vectors(v1=[result.vector_one_x, result.vector_one_y, result.vector_one_z],
                               v2=[result.vector_two_x, result.vector_two_y, result.vector_two_z],
                               result=[result.cross_product_x, result.cross_product_y, result.cross_product_z])
            vector.id, vector.created = result.id, result.created
            all_results.results.append(vector)
        dump = s.AllResultsListSchema().dump(all_results).data
        data, errors = s.AllResultsListSchema().load(dump)
        if errors:
            return jsonify(errors)
        return jsonify(dump)


# @api.route('/calculate', methods=['POST', 'GET'])
# def calculate():
#     if request.method == 'POST':
#         print(request.get_json())
#         data = request.get_json()
#         try:
#
#             vector_data = v.Vectors1(data['vector1'], data['vector2'])
#             result = Result(v1=[v1.val for v1 in vector_data.vector1], v2=[v2.val for v2 in vector_data.vector2],
#                             cp=[cp.val for cp in vector_data.result])
#         except (ValueError, IndexError):
#             return ge.make_error(400, 'Invalid vector size in request. Both vectors must be of length 3.')
#         except TypeError:
#             return ge.make_error(400, 'Invalid argument types. Ensure you include only floats or integers')
#         vector_data.created = result.created
#         db.session.add(result)
#         try:
#             db.session.commit()
#             vector_data.id = result.id
#         except Exception as e:
#             print(e)
#         data, errors = s.ResultSchema().dump(vector_data)
#         print(errors)
#         return jsonify(data) if not errors else jsonify(errors)
#     else:
#         results = Result.query.all()
#         all_results = v.AllVectors()
#         for result in results:
#             vector = v.Vectors1([result.vector_one_x, result.vector_one_y, result.vector_one_z],
#                                 [result.vector_two_x, result.vector_two_y, result.vector_two_z],
#                                 [result.cross_product_x, result.cross_product_y, result.cross_product_z])
#             vector.created = result.created
#             vector.id = result.id
#             all_results.results.append(vector)
#         return jsonify(s.AllResultsSchema().dump(all_results).data)


@api.route('/health')
def health():
    return jsonify({'message': 'okay'})


@api.route('/test')
def test():
    return jsonify()
