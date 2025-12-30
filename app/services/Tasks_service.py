from click import DateTime
from fastapi import Depends, HTTPException, Query
from app.db.session import get_db
from sqlalchemy.orm import Session

from app.models.tasks_model import Task
from app.schemas.Task_request import TaskRead, TaskCreate, TaskUpdate
from datetime import datetime


class TasksService:
    # Constructor
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    # Crear tarea
    def create_task(self, task: TaskCreate):
        # Datos de la tarea
        db_task = Task(
            title=task.title,
            description=task.description,
            status=task.status,
        )

        # se guarda en la DB
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return {"message": "Tarea creada con éxito", "data": db_task}
    

    # Listar tareas
    def list_tasks(self, page: int = Query(1, ge=1), page_size: int = Query(10, ge=1)):
        '''
        (1-1)* 10 = 0 => quiere decir que no hay desplazamiento
        se muestra desde la primera tarea
        (2-1)* 10 = 10 => empieza desde la tarea 11
        '''
        offset = (page - 1) * page_size
        tasks = self.db.query(Task).offset(offset).limit(page_size).all()
        return tasks
    

    # Obtener tarea por id
    def get_task(self, task_id: int):
        '''
        Se busca la tarea por en la base de datos
        si el id no coincide con algun dato, lanza 
        una excepcion 404 not found, y si lo encuentra, devuelve la tarea.
        '''
        task = self.db.query(Task).filter(Task.id == task_id).first()
        if not task:
            raise HTTPException(status_code=404, detail="Tarea no encontrada")
        return task
    

    # Actualizar tarea
    def update_task(self, task_id: int, task_data: TaskUpdate):
        db_task = self.db.query(Task).filter(Task.id == task_id).first()

        if not db_task:
            raise HTTPException(status_code=404, detail="Tarea no encontrada")

        for key, value in task_data.dict(exclude_unset=True).items():
            '''
            para cada para campo -> valor
            modifica dinamicamente el atributo del objeto task
            lo que seria lo mismo que hacer:
            task.title = "nuevo titulo"
            task.description = "nueva descripcion"
            '''
            setattr(db_task, key, value)

        self.db.commit()
        self.db.refresh(db_task)
        return db_task
    
    
    ## Eliminar Tarea
    def delete_task(self, task_id: int):
        db_task = self.db.query(Task).filter(Task.id == task_id).first()
        
        if not db_task:
            raise HTTPException(status_code=404, detail="Tarea no encontrada")
        
        self.db.delete(db_task)
        self.db.commit()
        return {"message": "Tarea eliminada con éxito"}
    

