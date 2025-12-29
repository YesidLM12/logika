from fastapi import FastAPI, Depends
from app.db.session import get_db
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/db-check")
def db_check(db = Depends(get_db)):
    return {"status": "ok"}


if __name__ == "__main__":
    config = uvicorn.Config("app.main:app", port=8000)
    server = uvicorn.Server(config)
    server.run()
