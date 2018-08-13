from flask_restful import Resource, reqparse

from neighbours.db import db
from neighbours.kdtree import KDTree, Point
from neighbours.models import Member
from . import OK_RESULT


parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('x', type=float, required=True, nullable=False, location='args')
parser.add_argument('y', type=float, required=True, nullable=False, location='args')
parser.add_argument('limit', type=int, required=False, nullable=True, location='args')


class NeighboursResource(Resource):
    DEFAULT_NEIGHBOURS_LIMIT = 100

    def get(self):
        request_data = parser.parse_args()
        x, y, limit = request_data['x'], request_data['y'], request_data.get('limit') or self.DEFAULT_NEIGHBOURS_LIMIT

        tree = KDTree()

        for member in db.session.query(Member):
            tree.add(Point(member.x, member.y), member.name)

        neighbours = tree.get_neighbours(Point(x, y), limit)
        result = []
        for idx, neighbour in enumerate(neighbours):
            result.append({
                'name': neighbour[1],
                'x': neighbour[0].x,
                'y': neighbour[0].y,
                'distance': neighbours.get_item_distance(idx),
            })

        return OK_RESULT(result)
