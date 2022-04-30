from flask import Flask, jsonify
from controller.student_controller import app_student
from controller.listse_controller import app_list_se
from controller.list_double_controller import app_list_double

app = Flask(__name__)
app.register_blueprint(app_student)
app.register_blueprint(app_list_se)
app.register_blueprint(app_list_double)

if __name__ == '__main__':
    app.run()
