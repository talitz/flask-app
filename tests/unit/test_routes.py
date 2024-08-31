import base64


def test_json(test_client):
    response = test_client.get('/json')
    assert response.status_code == 200
    assert b"completed" in response.data
    assert b"id" in response.data
    assert b"title" in response.data
    assert b"userId" in response.data


def test_json_with_user_without_creds(test_client):
    response = test_client.get('/json/user/1')
    assert response.status_code == 401


def test_json_with_user_with_creds(test_client):
    # Create a header with the admin credentials
    credentials = base64.b64encode(b'admin:password').decode('utf-8')
    headers = {
        'Authorization': f'Basic {credentials}'
    }

    response = test_client.get('/json/user/1', headers=headers)

    assert response.status_code == 200
    assert b"delectus aut autem" in response.data
