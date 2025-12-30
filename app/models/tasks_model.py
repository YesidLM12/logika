import enum
from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, func
from app.db.base import Base


class Task_status(enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"


class Task(Base):
    __tablename__ = "Tasks"

    id = Column(Integer, primary_key=True, index=True)
    # para busquedas por titulo
    title = Column(String, nullable=False, index=True)
    description = Column(String, nullable=True)
    status = Column(Enum(Task_status), default=Task_status.pending,
                    nullable=False, index=True)  # Filtros o busqueda por estado
    created_At = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
