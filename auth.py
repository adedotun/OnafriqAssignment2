import requests
import json


class AuthenticationPage:
    base_url = "https://restful-booker.herokuapp.com"

    def __init__(self):
        self.token = None

    def authenticate(self):
        url = f"{self.base_url}/auth"
        headers = {"Content-Type": "application/json"}
        payload = {"username": "admin", "password": "password123"}
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        self.token = response.json()['token']
        return self.token
