#!/usr/bin/env python
import os

from flask.cli import FlaskGroup

from neighbours.application import db


if not os.getenv("FLASK_APP"):
    os.environ["FLASK_APP"] = "neighbours/application.py"


cli = FlaskGroup()


@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    cli()
