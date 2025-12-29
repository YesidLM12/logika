from sqlalchemy.orm import Session

from app.db.session import SessionLocal

from app.core.security import hash_password
from app.models.UserModel import User


def init_db() -> None:
    db: Session = SessionLocal()

    try:
        # Verificar si ya existe el email
        admin = db.query(User).filter(User.email == "admin@admin.com").first()

        if admin:
            print("Usuario admin ya existe")
            return

        # Crear los datos iniciales
        admin = User(
            username="admin",
            email="admin@admin.com",
            password=hash_password("admin123"),
            is_active=True
        )

        # Guardar los datos en DB
        db.add(admin)
        db.commit()
        print("Usuario admin creado correctamente")

    except Exception as e:
        db.rollback()
        print("Error creando datos iniciales:", e)

    finally:
        db.close()
