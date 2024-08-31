def test_healthiness_with_fixture(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/health' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get('/health')
    assert response.status_code == 200
    assert b"healthy" in response.data