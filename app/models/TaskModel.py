import enum
from sqlalchemy import Column, DateTime, Enum, Integer, String, func
from app.db.base import Base

class Task_status(enum.Enum):
    pending = "pendig"
    in_progress = "in_progress"
    done = "done"

class Task(Base):
    __tablename__ = "Tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True) # para busquedas por titulo
    description = Column(String, nullable=True)
    status = Column(Enum(Task_status), default= Task_status.pending, index=True) # Filtros o busqueda por estado
    created_At = Column(DateTime(timezone = True), server_default=func.now())