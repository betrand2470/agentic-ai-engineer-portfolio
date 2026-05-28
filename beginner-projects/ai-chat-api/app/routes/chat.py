from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.models.chat_models import (
    ChatRequest,
    ChatResponse
)

from app.services.openai_service import (
    generate_response
)

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    ai_response = await generate_response(
        request.prompt
    )

    return ChatResponse(
        response=ai_response
    )


async def fake_stream():

    words = [
        "Agentic ",
        "AI ",
        "systems ",
        "can ",
        "reason ",
        "and ",
        "act."
    ]

    for word in words:
        yield word
        
@router.get("/stream")
async def stream():

    return StreamingResponse(
        fake_stream(),
        media_type="text/plain"
    )
