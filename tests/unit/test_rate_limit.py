def test_rate_limiting_on_main_route(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/health' page is requested (GET)
    THEN check that the response is valid
    """
    # 2 per day should work
    response = test_client.get('/')
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Hi there!" in response.data

    # 3rd should fail
    response = test_client.get('/')
    assert response.status_code == 429
    assert b"Too Many Requests" in response.data
