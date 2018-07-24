from .application import db


class User(db.Model):
    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), primary_key=True, nullable=False)
    x = db.Column(db.Float, nullable=False)
    y = db.Column(db.Float, nullable=False)

    def __init__(self, username, x, y):
        self.username = username
        self.x = x
        self.y = y
