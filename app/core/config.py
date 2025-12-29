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
    
    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg2://{self.DB_USER}:"
            f"{self.DB_PASSWORD}@{self.DB_HOST}:"
            f"{self.DB_PORT}/{self.DB_NAME}"
        )
    
    class Config:
        env_file = ".env"
        
        
settings = Settings() # type: ignore