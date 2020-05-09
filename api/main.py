from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request
from flask_restful import Resource, Api, abort

from .ext import database

from .resources import UserResource, UserItemResource

# from flask import got_request_exception

app = Flask(__name__)

api = Api(app)

database.init_app(app)

api.add_resource(UserResource, '/users')
api.add_resource(UserItemResource, '/users/<id>')
