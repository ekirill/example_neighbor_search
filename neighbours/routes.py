from .resources.members import MembersResource


def init_routes(api):
    api.add_resource(MembersResource, '/members')
