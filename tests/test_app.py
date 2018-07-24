# -*- coding: utf-8 -*-
import json


def test_add_member_validation(client):
    response = client.post('/members')
    assert 400 == response.status_code

    response = client.post(
        '/members',
        content_type='application/json',
        data=json.dumps({
            'name': '',
        })
    )
    assert 400 == response.status_code

    response = client.post(
        '/members',
        content_type='application/json',
        data=json.dumps({
            'name': 'Member 1',
            'x': '100',
        })
    )
    assert 400 == response.status_code

    response = client.post(
        '/members',
        content_type='application/json',
        data=json.dumps({
            'name': 'Member 1',
            'x': '100',
            'y': '200.20'
        })
    )
    assert 200 == response.status_code
    assert response.json['status'] == 'OK'


def test_add_member(client):
    response = client.post(
        '/members',
        content_type='application/json',
        data=json.dumps({
            'name': 'Member 1',
            'x': '100',
            'y': '200.20'
        })
    )
    assert 200 == response.status_code
    assert response.json['status'] == 'OK'
