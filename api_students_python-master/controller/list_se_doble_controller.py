from flask import Response,json,jsonify,Blueprint, request
from util.util_encoder import UtilEncoder
from service.list_se_doble_service import ListSEDobleService

app_list_doble = Blueprint("app_list_se_doble",__name__)

list_se_service = ListSEDobleService()

@app_list_doble.route('/list_se_doble/all')
def get_all_students():
    return Response(status=200,
                    response=json.dumps(list_se_service.get_all_students()
                    ,cls=UtilEncoder),mimetype="application/json")

@app_list_doble.route('/list_se_doble/add_to_start',methods=['POST'])
def save_student_to_start():
    data = request.json
    try:
        list_se_service.add_student(data)
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype="application/json")
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str(e)}), mimetype="application/json")

@app_list_doble.route('/list_se_doble/invert')
def invert():
    return Response(status=200,response=json.dumps(list_se_service.invert()),
                    mimetype="application/json")

@app_list_doble.route('/list_se_doble/exchange_extremes')
def exchange_extremes():
    return Response(status=200,response=json.dumps(list_se_service.exchange_extremes()),
                    mimetype="application/json")