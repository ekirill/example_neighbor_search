# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api

from .resources.members import Members


def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Members, '/members')

    return app
