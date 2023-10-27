from hello import app

with app.test_client() as c:
    response = c.get('/')
    assert response.data == b'<p>Hello World2!</p>'
    assert response.status_code == 402