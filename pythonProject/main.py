from flask import Flask, app
from flask_restful import Api
import logging as logger
from database import get_database


# logger
logger.basicConfig(level="DEBUG")


# flask_app
def get_flask_app() -> app.Flask:
    flask_app = Flask(__name__)
    api = Api(app=flask_app)
    return flask_app


db = get_database()

# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    logger.debug("Starting the application")
    app = get_flask_app()
    app.run(
        host="0.0.0.0",
        port=80,
        debug=True,
    )

