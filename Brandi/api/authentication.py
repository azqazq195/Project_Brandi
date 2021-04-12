# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource

import json

# project resources
from models.users import Users
from api.errors import unauthorized

# external packages
import datetime


class SignUpApi(Resource):
    """
    Flask-resftul resource for creating new user.
    :Example:
    >>> from flask import Flask
    >>> from flask_restful import Api
    # Create flask app, config, and resftul api, then add SignUpApi route
    >>> app = Flask(__name__)
    >>> app.config.update(default_config)
    >>> api = Api(app=app)
    >>> api.add_resource(SignUpApi, '/authentication/signup')
    """
    @staticmethod
    def post() -> Response:
        """
        POST response method for creating user.
        :return: JSON object
        """
        post_user = Users(request)
        id = post_user.save()
        return Response(
            response=json.dumps({"message": "user created", "id": f"{id}"}),
            status=200,
            mimetype="application/json"
        )