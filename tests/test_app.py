# -*- coding: utf-8 -*-


def test_add(client):
    response = client.get('/add')
    assert response.status_code == 200
    assert response.json['status'] == 'OK'
