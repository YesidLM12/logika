
from sqlalchemy import Column, Integer, String, Boolean
from app.db.base import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key = True, index=True)
    username = Column(String, nullable=False, index=True) # Para busquedas por nombre de usuario
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False, index=True)