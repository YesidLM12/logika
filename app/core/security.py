from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Encripta la contraseña


def hash_password(password: str) -> str:
    return pwd_context.hash(password[:72])

# verifica que la contraseña ingresada sea igual a la contraseña encriptada


def verify_password(plainPassword: str, hashPassword: str) -> bool:
    return pwd_context.verify(plainPassword, hashPassword)
