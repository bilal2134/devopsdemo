def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"yum" in response.data
