from datetime import datetime, timedelta
from jose import jwt
from app.core.config import settings

'''
- Crear Token
- Validar Token
- get current user
'''
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    
    expire = datetime.utcnow() + (
        expires_delta
        if expires_delta
        else timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    
    