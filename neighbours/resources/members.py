# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse

from neighbours.models import Member
from neighbours.repository import add_member
from . import OK_RESULT


def non_blank_str(value):
    if not value:
        raise ValueError("The parameter must not be blank.")

    return value


parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('name', type=non_blank_str, required=True, nullable=False, location='json')
parser.add_argument('x', type=float, required=True, nullable=False, location='json')
parser.add_argument('y', type=float, required=True, nullable=False, location='json')


class MembersResource(Resource):
    def post(self):
        member_data = parser.parse_args()

        add_member(Member(**member_data))

        return OK_RESULT()
