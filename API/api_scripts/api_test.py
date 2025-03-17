import requests
import json

BASE_URL = 'https://api.example.com/v1/user'
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer <token'
           }
Payload = {
    "username": "Alice",
    "password": "123456",
    "email": "test_example.com"
}

def test_post():
    response = requests.post(BASE_URL, headers=HEADERS, json=Payload)
    print(f"Response status code: {response.status_code}")
    print(f"Response text: {response.text}")

    assert response.status_code == 201, f"Expexted status code is 201, but actually got {response.status_code}"
    
    response_json = response.json()
    assert response_json.get("ststus") == "success", f"Expected status is success, actually got {response_json.get('ststus')}"
    assert "data" in response_json, "Response does not contain data key"
    assert response_json["data"].get("user_id") is not None, "Missing user_id in response data"

if __name__ == "__main__":
    test_post()
