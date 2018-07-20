# -*- coding: utf-8 -*-
import sys
import os
import pytest
import json


sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
))


@pytest.fixture
def app():
    from app_example.application import create_app
    return create_app()
