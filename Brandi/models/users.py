from flask import Response, request

import app


class Users(request):
    """
    Template for a mongoengine document, which represents a user.
    Password is automatically hashed before saving.
    :param name: option string username
    :param email: unique required email-string value
    :param password: required string value, longer than 6 characters
    :Example:
    # >>> import mongoengine
    # >>> from app import default_config
    # >>> mongoengine.connect(**default_config['MONGODB_SETTINGS'])
    MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True, read_preference=Primary())
    # Create test user
    >>> new_user = Users(email="spam@ham-and-eggs.com", password="hunter2", access={"admin": True})
    >>> new_user.save()
    >>> new_user.name = "spammy"
    >>> new_user.save()
    # Remove test user
    >>> new_user.delete()
    .. seealso:: :class:`Access`, :class:`Phone`, :class:`models.meals.Meals`
    """

    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]

    def save(self):
        db = app.get_database().user
        db_response = db.insert_one(Users)
        return db_response.inserted_id
