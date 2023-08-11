from flask import (Flask, request, Response)
from flask_pymongo import PyMongo
# from markupsafe import escape

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/dwl_local"
mongo = PyMongo(app)

@app.get('/iam/rights')
def list_iam_rights():
    response = {"rights": []}
    rights_cursor = mongo.db.rights.find()
    for right in rights_cursor:
        response["rights"].append(right["name"])
    return Response(response, status=200, mimetype='application/json')

@app.post('/iam/rights')
def new_iam_rights():
    if request.json and "name" in request.json.keys():
        #make sure this name is not already in database
        if mongo.db.rights.count_documents({"name": request.json["name"]}) == 0:
            mongo.db.rights.insert_one({"name": request.json["name"]})
            return Response("", status=201, mimetype='application/json')
        else:
            return Response('{"Error": "Right already exists"}', status=409, mimetype='application/json')
    return Response('{"Error": "Invalid body. Missing name field"}', status=400, mimetype='application/json')