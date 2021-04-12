

class SignUpApi():

    def post(self):
        post_user = User()
        id = post_user.save()
        return Response(
            response=json.dumps({"message": "user created", "id": f"{id}"}),
            status=200,
            mimetype="application/json"
        )