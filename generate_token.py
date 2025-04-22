from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "supersecret123"  # Este debe coincidir exactamente con el que tienes en chat.py

def generate_token(email: str):
    expire = datetime.utcnow() + timedelta(days=30)
    payload = {
        "sub": email,
        "exp": expire
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

print(generate_token("jason@example.com"))
