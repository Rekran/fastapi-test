from fastapi import FastAPI
import uvicorn
from backend.modules.user.routes import router

app = FastAPI()

app.include_router(router)
