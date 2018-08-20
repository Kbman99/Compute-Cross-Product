def test_calculate_route(test_client):
    response = test_client.get('/calculate')
    print(response)
    assert response.status_code == 200
    assert 'results' in response.json


def test_index_route(test_client):
    response = test_client.get('/', status=404, expect_errors=True)
    assert response.status_code == 404
    assert "<p>Whoops! We couldn't find what you were looking for. " \
           "Make sure you have the route entered correctly.</p>" in response


def test_health_route(test_client):
    response = test_client.get('/health')
    assert response.status_code == 200
    assert response.json['message'] == 'okay'
