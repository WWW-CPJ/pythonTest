# pytest 和 unittest 都是 Python 中常用的单元测试框架。每个框架都有其优点和使用场景，选择使用哪个框架取决于你项目的需求、团队的习惯以及个人偏好。

# Pytest is a third-party testing framework
# pip install pytest

# Run test
# pytest test_pytest.py
# We can add -v to the end of the command to get more information and output
# pytest test_pytest.py -v

import requests

def test_get_users():
    url = "http://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert 'name' in response.json()[0]
    # Use the assert mechanism to verify that the request is functional and that the response is as expected.

def test_create_user():
    url = "http://jsonplaceholder.typicode.com/users"
    new_user = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "john@example.com"
    }
    response = requests.post(url, json=new_user)
    assert response.status_code == 201
    created_user = response.json()
    assert created_user['name'] == new_user['name']
    assert created_user['username'] == new_user['username']

def test_update_user():
    url = "http://jsonplaceholder.typicode.com/users/1"
    update_data = {
        "name": "Updated Name",
        "username": "updatedusername"
    }
    response = requests.put(url, json=update_data)
    assert response.status_code == 200
    update_user = response.json()
    assert update_user['name'] == update_data['name']
    assert update_user['username'] == update_data['username']

def test_delete_user():
    url = "http://jsonplaceholder.typicode.com/user/1"
    response = requests.delete(url)
    assert response.status_code == 404
    response_after_delete = requests.get(url)
    assert response_after_delete.status_code == 404

