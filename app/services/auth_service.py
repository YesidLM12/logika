
from fastapi import Depends, HTTPException
from app.core.auth import create_access_token
from app.core.security import verify_password
from app.db.session import get_db
from app.models.UserModel import User
from sqlalchemy.orm import Session

from app.schemas.UserLoginRequest import UserLogin


def login_service(user: UserLogin, db: Session = Depends(get_db)):
    # Verificar si el usuario existe
    usuario_existente = db.query(User).filter(User.email == user.email).first()

    if not usuario_existente:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Verificar si la contraseña es correcta
    if not verify_password(user.password, str(usuario_existente.password)):
        raise HTTPException(status_code=400, detail="Contraseña incorrecta")

    # Generar token
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
