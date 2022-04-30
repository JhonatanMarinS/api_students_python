from flask import Response,json,jsonify,Blueprint, request
from util.util_encoder import UtilEncoder
from service.list_double_service import ListDoubleService

app_list_double = Blueprint("app_list_double",__name__)

list_double_service = ListDoubleService()

@app_list_double.route('/list_double/all')
def get_all_students():
    return Response(status=200,
                    response=json.dumps(list_double_service.get_all_students()
                    ,cls=UtilEncoder),mimetype="application/json")

@app_list_double.route('/list_double/add_to_start',methods=['POST'])
def save_student_to_start():
    data = request.json
    try:
        list_double_service.add_student_to_start(data)
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype="application/json")
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str(e)}), mimetype="application/json")

@app_list_double.route('/list_double/add', methods=['POST'])
def save_student_to_end():
    data = request.json
    try:
        list_double_service.add(data)
        return Response(status=200, response=json.dumps({"message": "Adicionado exitosamente"}),
                        mimetype="application/json")
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str(e)}), mimetype="application/json")


@app_list_double.route('/list_double/add_to_position/<position>', methods=['POST'])
def save_student_to_position(position):
    data = request.json
    try:
        list_double_service.add_student_to_position(data, id)
        return Response(status=200, response=json.dumps({"message": "Adicionado exitosamente"}),
                        mimetype="application/json")
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str(e)}), mimetype="application/json")

@app_list_double.route('/list_double/delete_to_position<position>',methods=['POST'])
def delete_student_to_position(position):
    data = request.json
    try:
        list_double_service.delete_student_to_position(data)
        return Response(status=200,response=json.dumps({"message":"Eliminado exitosamente"}),
                    mimetype="application/json")
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str(e)}), mimetype="application/json")


@app_list_double.route('/list_double/invert')
def invert():
    return Response(status=200,response=json.dumps(list_double_service.invert()),
                    mimetype="application/json")

@app_list_double.route('/list_double/exchange_extremes')
def exchange_extremes():
    return Response(status=200,response=json.dumps(list_double_service.exchange_extremes()),
                    mimetype="application/json")

@app_list_double.route('/list_double/delete_to_age<age>')
def delete_to_age(age):
    return Response(status=200,response=json.dumps(list_double_service.invert()),
                    mimetype="application/json")