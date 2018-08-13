# Nearest Neighbor Search Example

In this example project I use Flask with Flask-Restful
to produce simple service for searching neighbours.
SQLite is used for storing the members. Nearest neighbour search
algorithm is based on
k-d Tree (https://en.wikipedia.org/wiki/K-d_tree) data structure.

### Methods
It has two methods:

```POST /member```

Adds member to db. Body must contain JSON with _name_, _x_ and _y_ keys.


```GET /neighbours?x=100.100&y=200.201&limit=10```

Find <=10 nearest members.

### Runnung
Create venv in project folder.

```
$ python3.6 -m venv env
$ source env/bin/activate
$ pip install -r ./requirements.txt
```

Init sqlite database file.
```
$ FLASK_APP=neighbours/application.py ./manage.py recreate_db
```


Run development server.
```
$ FLASK_APP=neighbours/application.py ./manage.py run
```

The service should be accesible at http://localhost:5000
