from service.list_se_service import ListSEService
from flask import Response,json,jsonify,Blueprint, request
from util.util_encoder import UtilEncoder

app_list_se = Blueprint("app_list_se",__name__)

list_se_service = ListSEService()

@app_list_se.route('/list_se/all')
def get_all_students():
    return Response(status=200,
                    response=json.dumps(list_se_service.get_all_students()
                    ,cls=UtilEncoder),mimetype="application/json")

@app_list_se.route('/list_se/add_to_start',methods=['POST'])
def save_student_to_start():
    data = request.json
    try:
        list_se_service.add_student_to_start(data)
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype="application/json")
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str(e)}), mimetype="application/json")

@app_list_se.route('/list_se/add',methods=['POST'])
def save_student_to_end():
    data = request.json
    try:
        list_se_service.add(data)
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype="application/json")
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str(e)}), mimetype="application/json")

@app_list_se.route('/list_se/add_to_position',methods=['POST'])
def save_student_to_position():
    data = request.json
    try:
        list_se_service.add_student_to_position(data, id)
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype="application/json")
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str(e)}), mimetype="application/json")

@app_list_se.route('/list_se/delete_to_position',methods=['POST'])
def delete_student_to_position():
    data = request.json
    try:
        list_se_service.delete_student_to_position(data)
        return Response(status=200,response=json.dumps({"message":"Eliminado exitosamente"}),
                    mimetype="application/json")
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str(e)}), mimetype="application/json")


@app_list_se.route('/list_se/invert')
def invert():
    return Response(status=200,response=json.dumps(list_se_service.invert()),
                    mimetype="application/json")

@app_list_se.route('/list_se/exchange_extremes')
def exchange_extremes():
    return Response(status=200,response=json.dumps(list_se_service.exchange_extremes()),
                    mimetype="application/json")









