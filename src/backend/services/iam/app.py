from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/dwl_local"
mongo = PyMongo(app)

from iam.rights_routers import rights_api
from iam.groups_routers import groups_api
from iam.users_routers import users_api

app.register_blueprint(rights_api, url_prefix='/iam')
app.register_blueprint(groups_api, url_prefix='/iam')
app.register_blueprint(users_api, url_prefix='/iam')
