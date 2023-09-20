import app.models.models as mod
from flask import render_template,jsonify

class Activity:
    @classmethod
    def index(cls):
        return render_template('index.html')

    @classmethod
    def about(cls):
        return "This is a test Flask page"

    @classmethod
    def apiShow(cls):
        ALL_DAEMONS_SELECT_QRY="select * from DaemonDetails"
        db_connect= mod.DBConnect()
        db_connect.connect()
        result, row_count = db_connect.select(ALL_DAEMONS_SELECT_QRY)
        result=db_connect.touple_list_to_dict(result)
        # print("result", result)
        response = jsonify(result)
        return response