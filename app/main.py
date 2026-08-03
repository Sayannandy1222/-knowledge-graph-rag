from fastapi import FastAPI

from app.api.chat import router as chat_router
from app.api.health import router as health_router
from app.api.upload import router as upload_router

app = FastAPI(
    title="Knowledge Graph RAG API",
    version="1.0.0",
)

app.include_router(health_router)
app.include_router(chat_router)
app.include_router(upload_router)


@app.get("/")
def root():
    return {
        "message": "Knowledge Graph RAG API is running!"
    }