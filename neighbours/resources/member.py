# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse
from . import OK_RESULT


def non_blank_str(value):
    if not value:
        raise ValueError("The parameter must not be blank.")

    return value


parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('name', type=non_blank_str, required=True, nullable=False, location='json')
parser.add_argument('x', type=float, required=True, nullable=False, location='json')
parser.add_argument('y', type=float, required=True, nullable=False, location='json')


class Member(Resource):
    def post(self):
        args = parser.parse_args()
        print(args)

        return OK_RESULT()
