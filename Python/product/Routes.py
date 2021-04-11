from flask_restful import Resource
import logging as logger
from .controller import *


class Routes(Resource):
    def get(self):
        logger.debug("Inside post method")
        return get_products(request)
        pass
