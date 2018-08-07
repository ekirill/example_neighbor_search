from .resources.members import MembersResource
from .resources.neighbours import NeighboursResource


def init_routes(api):
    api.add_resource(MembersResource, '/member')
    api.add_resource(NeighboursResource, '/neighbours')
