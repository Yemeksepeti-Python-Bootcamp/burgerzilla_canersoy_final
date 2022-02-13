import json
from app import app

from tests.base import BaseCase

class TestLogin(BaseCase):
    def test_login(self):
        email = "omerk@restoran.nett"
        password = "123"
        payload = json.dumps({
            "email": email,
            "password": password
        })

        response = self.client.get('/currentUser',
        content_type="application/json")
        print(response.data.decode())