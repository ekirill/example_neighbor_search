# -*- coding: utf-8 -*-
from flask_restful import Resource
from . import OK_RESULT


class Members(Resource):
    def get(self):
        return OK_RESULT()
