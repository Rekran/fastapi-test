from fastapi import FastAPI
from models import Base
from database import engine
import uvicorn


app = FastAPI()


from routes import routerCsv

app.include_router(routerCsv)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    
    uvicorn.run(app, host="127.0.0.1", port=8080)