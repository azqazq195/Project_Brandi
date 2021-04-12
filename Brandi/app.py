# flask packages
from flask import Flask, app
from flask_restful import Api
import logging as logger
import pymongo

# local packages
from api.routes import create_routes


# logger
logger.basicConfig(level="DEBUG")

# local packages
# from api.routes import create_routes

# external packages
import os

# default mongodb configuration
default_config = {
    'MONGODB_SETTINGS': {
        'db': 'user',
        'host': 'localhost',
        'port': 27017,
        'serverSelectionTimeoutMS': 1000}
}


app = Flask(__name__)

def get_flask_app(config: dict = None):
    """
    Initializes Flask app with given configuration.
    Main entry point for wsgi (gunicorn) server.
    :param config: Configuration dictionary
    :return: app
    """
    # init flask
    # flask_app = Flask(__name__)

    # init api and routes
    api = Api(app=app)
    create_routes(api=api)

    # return flask_app


def get_database() -> pymongo.MongoClient():
    # init mongoengine
    try:
        connection = pymongo.MongoClient(
            host="localhost",
            port=27017,
            serverSelectionTimeoutMS=1000
        )
        db = connection.brandi
        connection.server_info()  # trigger exception if cannot connect to db
        print("******************")
        print("Database connected")
        print("******************\n")
        return db
    except:
        print("******************")
        print("ERROR - Cannot connect to db")
        print("******************\n")
        return None


if __name__ == '__main__':
    # Main entry point when run in stand-alone mode.
    logger.debug("Starting the application")
    # app = get_flask_app()
    app.run(
        host="0.0.0.0",
        port=80,
        debug=True,
    )
