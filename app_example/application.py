# -*- coding: utf-8 -*-
from flask import Flask
from .views.add_member import AddMember


def create_app():
    app = Flask(__name__)

    app.add_url_rule('/add', view_func=AddMember.as_view('index'))

    return app
