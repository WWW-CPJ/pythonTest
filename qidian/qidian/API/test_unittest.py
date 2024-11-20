# pip install requests
# unittest 是python 自带的库吗，不需要单独安装吗
# 是的，unittest 是 Python 自带的标准库之一，你 不需要单独安装 它。它是 Python 语言内置的，自带的单元测试框架，用于编写和运行测试用例。
# 继承 unittest.TestCase 类，并编写测试方法。每个测试方法都应该以 test_ 开头，这样 unittest 可以识别它们。

import requests
import unittest

class TestAPI (unittest.TestCase):
    base_url = "http://jsonplaceholder.typicode.com" # 示例 API

    # 测试 GET 请求
    def test_get_users(self):
        url = f"{self.base_url}/users"
        response = requests.get(url)

        # 验证返回的状态码是200
        self.assertEqual(response.status_code, 200)

        # 验证返回的数据是否是列表
        self.assertIsInstance(response.json(), list)

        # 可选，验证返回的第一个用户包含 'name' 字段
        users = response.json()
        self.assertIn('name', users[0])

    # 测试 POST 请求
    def test_create_user(self):
        url = f"{self.base_url}/users/1"
        updated_data = {
            "name": "Updated Name",
            "username": "updatedusername"
        }
        response = requests.put(url, json=updated_data)

        # 验证返回的状态码是 200
        self.assertAlmostEqual(response.status_code, 200)

        # 验证返回的数据中是否更新了用户名
        updated_user = response.json()
        self.assertEqual(updated_user['name'], updated_data['name'])
        self.assertEqual(updated_user['username'], updated_data['username'])

        print (response.json())


    # 测试 delete 请求
    def test_delete_user(self):
        url = f"{self.base_url}/users/1"
        response = requests.delete(url)

        # 验证返回的状态码是 200 （表示删除成功）
        self.assertEqual(response.status_code, 200)

        print (response.status_code)
        print (response.json())

        # 可选：再次发送 GET 请求检查用户是否已删除
        response_after_delete = requests.get(url)
        self.assertEqual(response_after_delete.status_code, 200)   # 应该返回 404，应为该用户已被删除，根据接口的实际情况，返回200

if __name__ == "__main__":
    unittest.main()

# python -m unittest test test_unittest.py
# python -m unittest test_unittest.py