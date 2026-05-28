from openai import AsyncOpenAI

from app.core.config import OPENAI_API_KEY

client = AsyncOpenAI(
    api_key=OPENAI_API_KEY
)

async def generate_response(prompt: str):

    response = await client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content