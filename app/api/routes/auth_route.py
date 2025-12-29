
from fastapi import APIRouter,Depends

from app.schemas.UserLoginRequest import UserLogin
from app.services.auth_service import  login_service
from app.db.session import get_db
from sqlalchemy.orm import Session



router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def l(user: UserLogin, db: Session = Depends(get_db)):
    return login_service(
        user=user,
        db=db
)
