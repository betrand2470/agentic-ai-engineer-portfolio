import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.AsyncAnthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

async def ask_claude(prompt: str):

    response = await client.messages.create(
        model="claude-3-5-sonnet-latest",
        max_tokens=300,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.content[0].text