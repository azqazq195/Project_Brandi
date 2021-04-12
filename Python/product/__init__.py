from flask_restful import Api

from app import app
from .Routes import Routes

restServer = Api(app)
