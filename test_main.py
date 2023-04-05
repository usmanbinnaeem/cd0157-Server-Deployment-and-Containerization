'''
Tests for jwt flask app.
'''
import os
import json
import pytest

import main

SECRET = 'usman123'
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODE5MTA0MTMsIm5iZiI6MTY4MDcwMDgxMywiZW1haWwiOiJ1c21hbkBnbWFpbC5jb20ifQ.gcMocnxUyMMfAydTjOxiTp4fcOBo6aMj2Ug3oxpSPtU'
EMAIL = 'usman@gmail.com'
PASSWORD = '@Usman123'

@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client



def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'


def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
