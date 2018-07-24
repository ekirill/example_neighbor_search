# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from .resources.member import Member


db = SQLAlchemy()


def init(config_name='neighbours.config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config_name)
    db.init_app(app)

    api = Api(app)
    api.add_resource(Member, '/members')

    return app


app = init()
