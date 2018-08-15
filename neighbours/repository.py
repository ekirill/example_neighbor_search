from neighbours.db import db
from neighbours.kdtree import KDTree, Point, square_distance
from neighbours.models import Member


_MEMBERS_KD_TREE = None


def _load_members():
    tree = KDTree()

    for member in db.session.query(Member):
        tree.add(Point(member.x, member.y), member.name)

    return tree


def get_members() -> KDTree:
    global _MEMBERS_KD_TREE
    if _MEMBERS_KD_TREE is None:
        _MEMBERS_KD_TREE = _load_members()

    return _MEMBERS_KD_TREE


def add_member(member: Member):
    db.session.add(member)
    db.session.commit()
    get_members().add(Point(member.x, member.y), member.name)
