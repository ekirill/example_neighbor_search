from .application import db


class Member(db.Model):
    __tablename__ = 'members'
    name = db.Column(db.String(128), primary_key=True, nullable=False)
    x = db.Column(db.Float, nullable=False)
    y = db.Column(db.Float, nullable=False)

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
