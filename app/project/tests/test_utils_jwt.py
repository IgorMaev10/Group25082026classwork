from utils_jwt import create_jwt, extract_payload_from_jwt
from time import sleep
import jwt
import pytest

class TestJWTUtils:
    def test_create(self):
        payload = {}
        subject = 111
        token =  create_jwt(subject=subject, payload=payload, lifetime_sec=10)
        assert token
        assert isinstance(token, str)

    def test_full_flow_success(self):
        payload = {'user': 'Maiev'}
        subject = 222
        token =  create_jwt(subject=subject, payload=payload, lifetime_sec=10)
        data = extract_payload_from_jwt(token)
        assert data['user'] == payload['user']
        assert data['sub'] == str(subject)

    def test_expiration(self):
        payload = {'user': 'Maiev'}
        subject = 333
        token =  create_jwt(subject=subject, payload=payload, lifetime_sec=1)
        sleep(2)
        with pytest.raises(jwt.exceptions.ExpiredSignatureError):
            extract_payload_from_jwt(token)
