from fastapi import FastAPI

from routers.user import router
from fastapi.responses import HTMLResponse

app = FastAPI(title="Eternal", description="Eternal FastAPI")
app.include_router(router, prefix="/api")


@app.get("/api", response_class=HTMLResponse)
async def root():
    return f"<body><h1>Eternal API made by Kinesey</h1></body>"
