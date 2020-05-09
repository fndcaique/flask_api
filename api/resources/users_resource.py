from flask import request
from flask_restful import Resource
from api.models import User


class UserResource(Resource):
    def get(self):
        users = User.query.all()
        users = [u.to_dict() for u in users]

        return users

    def post(self):
        user = request.json
        new_user = User(name=user['name'])

        new_user.save()

        user['id'] = new_user.id

        return user
