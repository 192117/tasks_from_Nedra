from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_emplty_history_get():
    response = client.get('/history')
    assert response.status_code == 200
    assert response.json() == []


def test_correct_calc_get():
    response = client.get('/calc', params={'value': '+100'})
    assert response.status_code == 200
    assert response.json() == '100'


def test_correct_long_calc_get():
    response = client.get('/calc', params={'value': '100-5*20+5'})
    assert response.status_code == 200
    assert response.json() == '5'


def test_incorrect_calc_get():
    response = client.get('/calc', params={'value': '100+-5'})
    assert response.status_code == 200
    assert response.json() == 'Incorrect expression'


def test_correct_float_calc_post():
    response = client.post('/calc', json={'value': '2./1.'})
    assert response.status_code == 200
    assert response.json() == '2.0'


def test_correct_float_long_calc_post():
    response = client.post('/calc', json={'value': '2.*5.63+0.741'})
    assert response.status_code == 200
    assert response.json() == '12.001'


def test_correct_int_long_calc_post():
    response = client.post('/calc', json={'value': '100*5+500-900'})
    assert response.status_code == 200
    assert response.json() == '100'


def test_incorrect_calc_post():
    response = client.post('/calc', json={'value': '100+-5'})
    assert response.status_code == 200
    assert response.json() == 'Incorrect expression'


def test_incorrect_no_calc_post():
    response = client.post('/calc', json={'value': ''})
    assert response.status_code == 422
    assert response.json()['detail'][0]['msg'] == 'It is necessary to send arguments'


def test_history_get():
    response = client.get('/history')
    assert response.status_code == 200
    assert len(response.json()) == 7


def test_history_success_post():
    response = client.post('/history', json={'limit': 10, 'status': 'success'})
    assert response.status_code == 200
    assert len(response.json()) == 5


def test_history_success_limit_post():
    response = client.post('/history', json={'limit': 2, 'status': 'success'})
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_history_fail_limit_post():
    response = client.post('/history', json={'limit': 5, 'status': 'fail'})
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_history_max_get():
    for i in range(25):
        client.get('/calc', params={'value': '+100'})
    response = client.get('/history')
    assert response.status_code == 200
    assert len(response.json()) == 30


def test_incorrect_limit_history_post():
    response = client.post('/history', json={'limit': 0, 'status': 'success'})
    assert response.status_code == 422
    assert response.json()['detail'][0]['msg'] == 'It should be from 1 to 30'


def test_incorrect_status_history_post():
    response = client.post('/history', json={'limit': 2, 'status': 'true'})
    assert response.status_code == 422
    assert response.json()['detail'][0]['msg'] == 'success or fail'


def test_incorrect_history_post():
    response = client.post('/history', json={'limit': 2, 'status': 'true'})
    assert response.status_code == 422
