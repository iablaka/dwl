from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/dwl_local"
mongo = PyMongo(app)

from iam.rights_routers import rights_api

app.register_blueprint(rights_api, url_prefix='/iam')

