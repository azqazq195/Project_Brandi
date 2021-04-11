from app import app
from database import db
from flask import Response
import json
from bson.objectid import ObjectId

import os
import sys
import urllib.request

client_id = "3H1it50t27kSv0WWo_Qr"
client_secret = "_1I5uVNpQd"
url = "https://openapi.naver.com/v1/search/shop.json"

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
request.add_header("Content-Type", "application/json")
response = urllib.request.urlopen(request)
rescode = response.getcode()


@app.route("/api/test", methods=["GET"])
def test():
    if (rescode == 200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)


@app.route("/api/products")
def get_products():
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
