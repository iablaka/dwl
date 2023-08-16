from json import dumps
from flask import Blueprint, request, Response
from bson import ObjectId

from iam.app import mongo

groups_api = Blueprint('groups_api', __name__)

@groups_api.get('/groups')
# @api_key_required
def list_groups():
    response = {"groups": []}
    groups_cursor = mongo.db.groups.find()
    for group in groups_cursor:
        response["groups"].append({
            "id": format(group, "_id", "str"),
            "name": format(group, "name", "str"),
            "rights": format(group, "rights", "list")
        })
    return Response(dumps(response), status=200, mimetype='application/json')

@groups_api.post('/groups')
def new_group():
    if request.json and "name" in request.json.keys():
        #make sure this name is not already in database
        if mongo.db.groups.count_documents({"name": request.json["name"].lower()}) == 0:
            if "rights" in request.json.keys():
                result = mongo.db.groups.insert_one({"name": request.json["name"].lower(), "rights": request.json["rights"]})
            else:
                result = mongo.db.groups.insert_one({"name": request.json["name"].lower()})

            return Response(
                dumps({"id": str(result.inserted_id), "name": request.json["name"].lower()}),
                status=201, mimetype='application/json'
            )
        else:
            return Response('{"Error": "group already exists"}', status=409, mimetype='application/json')
    return Response('{"Error": "Invalid body. Missing name field"}', status=400, mimetype='application/json')

@groups_api.delete('/groups/<id>')
def delete_group(id):
    if mongo.db.groups.count_documents({"_id": ObjectId(id)}) > 0:
        mongo.db.groups.delete_many({"_id": ObjectId(id)})
        return Response("", status=200, mimetype='application/json')
    else:
        return Response('{"Error": "group does not exist"}', status=409, mimetype='application/json')

def format(record, field, type_format):
    if field in record.keys():
        if field == "_id":
            return str(record[field])
        else:
            return record[field]
    else:
        if type_format == "str":
            return ""
        elif type_format == "list":
            return []