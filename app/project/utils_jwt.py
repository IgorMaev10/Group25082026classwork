import jwt
from time import sleep
import datetime

JWT_SECRET = 'TestSecret12345678910111213141516171819rsjfkgmnwslbnfwegrhsvmdyhjdb'

payload = {
    "sub": '123321',
    "iat": datetime.datetime.now(datetime.UTC),
    "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(seconds=500),
    "user": 'Maiev',
    'group': 25082026
}

def create_jwt(subject, payload: dict, lifetime_sec: int) -> str:
    base_payload = {
        "sub": str(subject),
        "iat": datetime.datetime.now(datetime.UTC),
        "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(seconds=lifetime_sec),
    }
    final_payload = payload | base_payload

    encode_jwt = jwt.encode(
        payload=final_payload,
        key=JWT_SECRET,
        algorithm='HS256'
    )
    print(encode_jwt)
    return encode_jwt

def extract_payload_from_jwt(jwt_token: str) -> dict:
    decode = jwt.decode(
        jwt=jwt_token,
        key=JWT_SECRET,
        algorithms=['HS256']
    )
    print(decode)
    return decode

extract_payload_from_jwt(create_jwt(subject=111, payload=payload, lifetime_sec=50))
