from flask import request
from flask_restful import Resource
from api.models import User


class UserItemResource(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()

        if user == None:
            return {'Error': 'User not found'}, 404

        return user.to_dict()

    def put(self, id):

        user = User.query.filter_by(id=id).first()

        if user == None:
            return {'Error': 'User not found'}, 404
        data = request.json
        user.name = data['name']

        user.save()

        return user.to_dict()

    def delete(self, id):

        user = User.query.filter_by(id=id).first()

        if user == None:
            return {'Error': 'User not found'}, 404

        user.delete()

        return user.to_dict()
