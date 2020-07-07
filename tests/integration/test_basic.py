def test_with_valid_param(client):
    """test the status code and fibonacci value"""

    response = client.get('/calculate_fibonacci?n=42')
    assert response.status_code == 200
    assert response.data == b'{"value":"267914296"}\n'

def test_with_invalid_param(client):
    """test with non-numeric param"""

    response = client.get('/calculate_fibonacci?n=abc')
    assert response.status_code == 200
    assert response.data == b'{"error":"Please use a number as the \'n\' argument"}\n'
