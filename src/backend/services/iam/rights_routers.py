from json import dumps
from flask import Blueprint, request, Response
from bson import ObjectId

from iam.app import mongo

rights_api = Blueprint('api', __name__)

@rights_api.get('/rights')
def list_rights():
    response = {"rights": []}
    rights_cursor = mongo.db.rights.find()
    for right in rights_cursor:
        response["rights"].append({"id": str(right["_id"]), "name": right["name"]})
    return Response(dumps(response), status=200, mimetype='application/json')

@rights_api.post('/rights')
def new_right():
    if request.json and "name" in request.json.keys():
        #make sure this name is not already in database
        if mongo.db.rights.count_documents({"name": request.json["name"].lower()}) == 0:
            result = mongo.db.rights.insert_one({"name": request.json["name"].lower()})
            return Response(
                dumps({"id": str(result.inserted_id), "name": request.json["name"].lower()}),
                status=201, mimetype='application/json'
            )
        else:
            return Response('{"Error": "Right already exists"}', status=409, mimetype='application/json')
    return Response('{"Error": "Invalid body. Missing name field"}', status=400, mimetype='application/json')

@rights_api.delete('/rights/<id>')
def delete_right(id):
    if mongo.db.rights.count_documents({"_id": ObjectId(id)}) > 0:
        mongo.db.rights.delete_many({"_id": ObjectId(id)})
        return Response("", status=200, mimetype='application/json')
    else:
        return Response('{"Error": "Right does not exist"}', status=409, mimetype='application/json')
