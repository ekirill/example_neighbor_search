# -*- coding: utf-8 -*-
import json
import random


def test_add_member_validation(client):
    response = client.post('/member')
    assert 400 == response.status_code

    response = client.post(
        '/member',
        content_type='application/json',
        data=json.dumps({
            'name': '',
        })
    )
    assert 400 == response.status_code

    response = client.post(
        '/member',
        content_type='application/json',
        data=json.dumps({
            'name': 'Member 1',
            'x': '100',
        })
    )
    assert 400 == response.status_code

    response = client.post(
        '/member',
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
    from neighbours.models import Member

    response = client.post(
        '/member',
        content_type='application/json',
        data=json.dumps({
            'name': 'Member 1',
            'x': '100',
            'y': '200.20'
        })
    )
    assert 200 == response.status_code
    assert response.json['status'] == 'OK'

    assert Member.query.count() == 1
    member = Member.query.first()
    assert member.name == 'Member 1'
    assert member.x == 100
    assert member.y == 200.20


def test_search_neighbours(client):
    x_k = 2.5
    y_k = 1.5

    for i in range(200):
        client.post(
            '/member',
            content_type='application/json',
            data=json.dumps({
                'name': 'Member %s' % i,
                'x': i * x_k,
                'y': i * y_k,
            })
        )

    response = client.get('/neighbours?x={}&y={}&limit=2'.format(20 * x_k, 20 * y_k))
    assert 200 == response.status_code
    assert 'OK' == response.json['status']
    assert 2 == len(response.json['data'])
    assert ['Member 20', 'Member 19'] == [_m['name'] for _m in response.json['data']]

    response = client.get('/neighbours?x={}&y={}&limit=5'.format(150 * x_k, 150 * y_k))
    assert 200 == response.status_code
    assert 'OK' == response.json['status']
    assert 5 == len(response.json['data'])
    assert ['Member 150', 'Member 149', 'Member 151', 'Member 148', 'Member 152'] \
        == [_m['name'] for _m in response.json['data']]

    response = client.get('/neighbours?x={}&y={}&limit=4'.format(150 * -x_k, 150 * y_k))
    assert 200 == response.status_code
    assert 'OK' == response.json['status']
    assert 4 == len(response.json['data'])
    assert ['Member 0', 'Member 1', 'Member 2', 'Member 3'] == [_m['name'] for _m in response.json['data']]
