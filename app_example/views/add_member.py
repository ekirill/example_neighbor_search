# -*- coding: utf-8 -*-
from flask.views import MethodView
from . import OK_RESULT


class AddMember(MethodView):
    def get(self):
        return OK_RESULT()
