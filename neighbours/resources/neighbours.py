from math import hypot

from flask_restful import Resource, reqparse

from neighbours.db import db
from neighbours.models import Member
from . import OK_RESULT


parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('x', type=float, required=True, nullable=False, location='args')
parser.add_argument('y', type=float, required=True, nullable=False, location='args')
parser.add_argument('limit', type=int, required=False, nullable=True, location='args')


class NeighboursResource(Resource):
    DEFAULT_NEIGHBOURS_LIMIT = 100

    @classmethod
    def _distance(cls, x1: float, y1: float, x2: float, y2: float):
        return hypot(x2 - x1, y2 - y1)

    def get(self):
        request_data = parser.parse_args()
        x, y, limit = request_data['x'], request_data['y'], request_data.get('limit') or self.DEFAULT_NEIGHBOURS_LIMIT

        members_with_distance = {}
        for member in db.session.query(Member):
            members_with_distance[(member.name, member.x, member.y)] = self._distance(x, y, member.x, member.y)

        result = []
        for _member_data, distance in sorted(members_with_distance.items(), key=lambda _x: (_x[1], _x[0])):
            if len(result) == limit:
                break

            result.append({
                'name': _member_data[0],
                'x': _member_data[1],
                'y': _member_data[2],
            })

        return OK_RESULT(result)
