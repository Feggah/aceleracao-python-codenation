from jwt import encode, decode, InvalidSignatureError


def create_token(data, secret):
    return encode(data, secret, algorithm='HS256')


def verify_signature(token):
    try:
        return decode(token, 'acelera', algorithms='HS256')
    except InvalidSignatureError:
        return {"error": 2}
