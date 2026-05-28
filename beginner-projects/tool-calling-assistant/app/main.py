from openai import OpenAI
from dotenv import load_dotenv

import json
import os

from tools import get_weather

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather information",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string"
                    }
                },
                "required": ["city"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "user",
            "content": "What's the weather in Dallas?"
        }
    ],
    tools=tools
)

tool_call = response.choices[0].message.tool_calls[0]

arguments = json.loads(
    tool_call.function.arguments
)

result = get_weather(
    arguments["city"]
)

print(result)