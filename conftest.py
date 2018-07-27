# -*- coding: utf-8 -*-
import sys
import os
import pytest


sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
))


@pytest.fixture
def app():
    from neighbours.application import init
    from neighbours.db import db
    app, api = init(config_name="neighbours.config.TestingConfig")
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()  # looks like db.session.close() would work as well
        db.drop_all()
