from fastapi import FastAPI

from routes import router

app = FastAPI(title="Eternal", description="Eternal FastAPI")
app.include_router(router, prefix="/api")
