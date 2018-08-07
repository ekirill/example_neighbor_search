# -*- coding: utf-8 -*-
import json


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


def test_search_neighbours(client, points):
    for i, point in enumerate(points):
        client.post(
            '/member',
            content_type='application/json',
            data=json.dumps({
                'name': 'Member %s' % i,
                'x': point[0],
                'y': point[1],
            })
        )

    response = client.get('/neighbours?x={}&y={}&limit=2'.format(150.22, -500.77))
    assert 200 == response.status_code
    assert 'OK' == response.json['status']
    assert 2 == len(response.json['data'])
    assert ['Member 925', 'Member 795'] == [_m['name'] for _m in response.json['data']]

    response = client.get('/neighbours?x={}&y={}&limit=5'.format(-900.222212, 1000.0))
    assert 200 == response.status_code
    assert 'OK' == response.json['status']
    assert 5 == len(response.json['data'])
    assert ['Member 201', 'Member 142', 'Member 114', 'Member 198', 'Member 521'] \
        == [_m['name'] for _m in response.json['data']]

    response = client.get('/neighbours?x={}&y={}&limit=4'.format(0.0, -10.1232))
    assert 200 == response.status_code
    assert 'OK' == response.json['status']
    assert 4 == len(response.json['data'])
    assert ['Member 52', 'Member 573', 'Member 311', 'Member 520'] == [_m['name'] for _m in response.json['data']]
