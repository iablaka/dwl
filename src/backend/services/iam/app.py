from json import dumps
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/dwl_local"
mongo = PyMongo(app)

@app.route("/iam/rights")
def list_iam_rights():
    response = {"rights": []}
    rights_cursor = mongo.db.rights.find()
    for right in rights_cursor:
        response["rights"].append(right["name"])
    return response