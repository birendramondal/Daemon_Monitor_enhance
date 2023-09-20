from app import app
from app import controller
from flask_cors import CORS, cross_origin
CORS(app, support_credentials=True)

controllerObj=controller.controller.Activity()

app.add_url_rule('/','index',controllerObj.index)
app.add_url_rule('/about','about',controllerObj.about)
app.add_url_rule('/api/show','apiShow',controllerObj.apiShow,methods=['GET'])