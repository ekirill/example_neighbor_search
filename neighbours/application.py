# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api

from neighbours.db import db
from neighbours.routes import init_routes


def init(config_name='neighbours.config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config_name)
    db.init_app(app)

    api = Api(app)
    init_routes(api)

    return app, api


app, api = init()
