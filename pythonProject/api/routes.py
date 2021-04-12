# flask packages
from flask_restful import Api

# project resources
from authentication import SignUpApi

def create_routes(api: Api):
    """Adds resources to the api
    :param api: Flask_RESTFul Api Object
    :Example:
        api.add_resource(Foo, '/foo', endpoint="foo"
    """

    api.add_resource()

