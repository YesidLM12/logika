
from fastapi import APIRouter
from app.api.routes import auth_route, tasks_route


api_router = APIRouter()

api_router.include_router(auth_route.router)
api_router.include_router(tasks_route.router)