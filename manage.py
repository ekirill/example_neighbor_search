#!/usr/bin/env python

from flask.cli import FlaskGroup

from neighbours.application import app, db


cli = FlaskGroup()


@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    cli()
