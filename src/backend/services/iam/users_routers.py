from json import dumps
from flask import Blueprint, request, Response
from bson import ObjectId

from iam.app import mongo

users_api = Blueprint('users_api', __name__)

@users_api.get('/users')
# @api_key_required
def list_users():
    response = {"users": []}
    users_cursor = mongo.db.users.find()
    for user in users_cursor:
        response["users"].append({
            "id": format(user, "_id", "str"),
            "name": format(user, "name", "str"),
            "groupRights": format(user, "groupRights", "list"),
            "personalRights": format(user, "personalRights", "list")
        })
    return Response(dumps(response), status=200, mimetype='application/json')

@users_api.post('/users')
def new_user():
    if request.json and "name" in request.json.keys():
        #make sure this name is not already in database
        if mongo.db.users.count_documents({"name": request.json["name"].lower()}) == 0:
            if "personalRights" in request.json.keys():
                result = mongo.db.users.insert_one({"name": request.json["name"], "personalRights": request.json["personalRights"]})
            else:
                result = mongo.db.users.insert_one({"name": request.json["name"]})

            return Response(
                dumps({"id": str(result.inserted_id), "name": request.json["name"]}),
                status=201, mimetype='application/json'
            )
        else:
            return Response('{"Error": "user already exists"}', status=409, mimetype='application/json')
    return Response('{"Error": "Invalid body. Missing name field"}', status=400, mimetype='application/json')

@users_api.delete('/users/<id>')
def delete_user(id):
    if mongo.db.users.count_documents({"_id": ObjectId(id)}) > 0:
        mongo.db.users.delete_many({"_id": ObjectId(id)})
        return Response("", status=200, mimetype='application/json')
    else:
        return Response('{"Error": "user does not exist"}', status=409, mimetype='application/json')

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