from flask import Response,json,jsonify,Blueprint, request
from util.util_encoder import UtilEncoder
from service.list_se_circ_service import ListSECircService


app_list_se_circ = Blueprint("app_list_se_circ",__name__)

list_se_circ_service = ListSECircService()

@app_list_se_circ.route('/list_se_circ/all')
def get_all_students():
    return Response(status=200,
                    response=json.dumps(list_se_circ_service.get_all_students()
                    ,cls=UtilEncoder),mimetype="application/json")

@app_list_se_circ.route('/list_se_circ/add_to_start',methods=['POST'])
def save_student_to_start():
    data = request.json
    try:
        list_se_circ_service.add_student_to_start(data)
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype="application/json")
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str(e)}), mimetype="application/json")

@app_list_se_circ.route('/list_se_circ/add',methods=['POST'])
def save_student_to_end():
    data = request.json
    try:
        list_se_circ_service.add(data)
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype="application/json")
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str(e)}), mimetype="application/json")
