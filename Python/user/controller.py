import uuid

from app import app
from database import db
from flask import Response, request
import json
from bson.objectid import ObjectId


#############################################################################################
def get_some_users():
    try:
        data = list(db.users.find())
        return Response(
            response=json.dumps(data),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({
                "message": "cannot read user"
            }),
            status=500,
            mimetype="application/json"
        )


#############################################################################################
def get_users(id):
    try:
        # data = db.users.find_one({"_id": ObjectId(id)})
        # data["_id"] = str(data["_id"])
        data = db.users.find_one({"_id": id})
        return Response(
            response=json.dumps(data),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({
                "message": "cannot find user"
            }),
            status=500,
            mimetype="application/json"
        )


#############################################################################################
def create_user(request):
    try:
        user = json.loads(request.form["user"])
        user["_id"] = uuid.uuid4().hex
        dbResponse = db.users.insert_one(user)
        print(dbResponse.inserted_id)
        # for attr in dir(response):
        #     print(attr)
        return Response(
            response=json.dumps({"message": "user created", "id": f"{dbResponse.inserted_id}"}),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({
                "message": "cannot create user"
            }),
            status=500,
            mimetype="application/json"
        )


#############################################################################################
def update_user(id):
    try:
        dbResponse = db.users.update_one(
            {"_id": id},
            {"$set": {
                "name": request.form["name"],
                "email": request.form["email"]
            },
            }
        )
        if dbResponse.modified_count == 1:
            return Response(
                response=json.dumps({
                    "message": "user updated"
                }),
                status=200,
                mimetype="application/json"
            )
        else:
            return Response(
                response=json.dumps({
                    "message": "nothing to update"
                }),
                status=200,
                mimetype="application/json"
            )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({
                "message": "cannot update user"
            }),
            status=500,
            mimetype="application/json"
        )


#############################################################################################
def delete_user(id):
    try:
        dbResponse = db.users.delete_one({"_id": ObjectId(id)})
        if dbResponse.deleted_count == 1:
            return Response(
                response=json.dumps({
                    "message": "user deleted",
                    "id": f"{id}"
                }),
                status=200,
                mimetype="application/json"
            )
        else:
            return Response(
                response=json.dumps({
                    "message": "user not found to delete"
                }),
                status=200,
                mimetype="application/json"
            )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({
                "message": "cannot delete user"
            }),
            status=500,
            mimetype="application/json"
        )


#############################################################################################
@app.route("/api/user/login", methods=["POST"])
def login_user():
    try:
        user = json.loads(request.form["user"])
        dbResponse = db.users.find_one({
            "email": user["email"],
        })
        if dbResponse is not None:
            if user["password"] == dbResponse["password"]:
                return Response(
                    response=json.dumps({
                        "message": "login completed",
                        "user": {
                            "_id": dbResponse["_id"],
                            "name": dbResponse["name"],
                            "email": dbResponse["email"]
                        }
                    }),
                    status=200,
                    mimetype="application/json"
                )
            else:
                print(dbResponse["email"])
                print(dbResponse["password"])
                return Response(
                    response=json.dumps({
                        "message": "Wrong password",
                        "user": {
                            "email": dbResponse["email"]
                        }
                    }),
                    status=200,
                    mimetype="application/json"
                )
        else:
            return Response(
                response=json.dumps({
                    "message": "Cannot find user",
                    "user": {
                            "email": user["email"]
                        }
                }),
                status=200,
                mimetype="application/json"
            )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({
                "message": "cannot login user"
            }),
            status=500,
            mimetype="application/json"
        )
