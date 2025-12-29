from fastapi import FastAPI, Depends
from app.db.initial_data import init_db
from app.db.session import get_db
from app.api.router import api_router
import uvicorn

app = FastAPI()


# incia la DB al levantar la app
@app.on_event("startup")
def on_startup():
    init_db()


app.include_router(api_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/db-check")
def db_check(db=Depends(get_db)):
    return {"status": "ok"}


if __name__ == "__main__":
    config = uvicorn.Config("app.main:app", port=8000)
    server = uvicorn.Server(config)
    server.run()
