from flask_restful import Resource
import logging as logger
from .controller import *


class Routes(Resource):
    def post(self):
        logger.debug("Inside post method")
        return create_user(request)
        pass
