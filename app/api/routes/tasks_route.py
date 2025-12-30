from fastapi import APIRouter, Depends, Query, status
from app.core.auth import get_current_user
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.schemas.Task_request import TaskRead, TaskCreate, TaskUpdate
from app.services.Tasks_service import TasksService

'''
todos los endpoints requiren autenticacion
'''

router = APIRouter(
    prefix="/tasks", tags=["tasks"], dependencies=[Depends(get_current_user)])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return TasksService(db=db).create_task(task=task)


@router.get("/", response_model=list[TaskRead])
def list_tasks(
        page: int = Query(1, ge=1),
        page_size: int = Query(10, ge=1, le=100),
        db: Session = Depends(get_db)):
    return TasksService(db=db).list_tasks(page=page, page_size=page_size)


@router.get("/{task_id}", response_model=TaskRead)
def get_task(task_id: int, db: Session = Depends(get_db)):
    return TasksService(db=db).get_task(task_id=task_id)


@router.put("/{task_id}")
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    return TasksService(db=db).update_task(task_id=task_id, task_data=task)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return TasksService(db=db).delete_task(task_id=task_id)
