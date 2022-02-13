import json

from tests.base import BaseCase

class TestLogin(BaseCase):
    def test_login(self):
        email = "omerk@restoran.nett"
        password = "123"
        payload = json.dumps({
            "email": email,
            "password": password
        })

        response = self.client.post('/login', 
            headers={"Content-Type": "application/json"},
            data=payload)
        print(response.data.decode())