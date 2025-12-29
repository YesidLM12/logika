from pydantic_settings import BaseSettings

'''
Aqui se centralizan todas las variables de entorno
'''
class Settings(BaseSettings):
    
    # App
    PROJECT_NAME: str = "Prueba Tecnica API"
    
    # DB
    DB_HOST:str
    DB_PORT: int = 5432
    DB_NAME: str
    DB_USER:str
    DB_PASSWORD:str
    
    # Seguridad
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    
    class Config:
        env_file = ".env"
        
settings = Settings() # type: ignore