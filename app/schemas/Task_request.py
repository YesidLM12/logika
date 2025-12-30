from enum import Enum
from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class Task_status(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: Task_status = Task_status.pending


class TaskRead(TaskCreate):
    id: int
    created_At: datetime

    model_config = {
        "from_attributes": True,
        "json_encoders": {
            datetime: lambda dt: dt.strftime("%Y-%m-%d %H:%M:%S"),
        },
    }


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[Task_status] = None
