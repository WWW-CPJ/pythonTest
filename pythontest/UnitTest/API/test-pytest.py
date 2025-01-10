# pytest 和 unittest 哪个更好用，哪个更广泛
# pytest 和 unittest 都是 Python 中常用的单元测试框架。每个框架都有其优点和使用场景，选择使用哪个框架取决于你项目的需求、团队的习惯以及个人偏好。
# 怎么选择用那种来进行测试
# pytest 是一个功能强大、灵活的第三方测试框架，它支持 Python 2 和 Python 3。pytest 是社区非常推荐的测试框架，得到了广泛的使用。

# 需要安装 pytest
# pip install pytest
# 运行测试
# pytest test_pytest.py

import requests

def test_get_users():
    url = "http://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert 'name' in response.json()[0]

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

