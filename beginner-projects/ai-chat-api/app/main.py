from fastapi import FastAPI

from app.routes.chat import router as chat_router

app = FastAPI(
    title="AI Chat API",
    version="1.0.0"
)

app.include_router(chat_router)

@app.get("/")
async def root():

    return {
        "message": "AI Chat API Running"
    }

@app.get("/health")
async def health():

    return {
        "status": "healthy"
    }