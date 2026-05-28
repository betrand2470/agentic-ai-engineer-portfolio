import asyncio
import time

from openai_client import ask_openai
#from anthropic_client import ask_claude

PROMPT = "Explain what Agentic AI is in simple terms."

async def main():

    start = time.time()

    openai_task = ask_openai(PROMPT)
#    claude_task = ask_claude(PROMPT)

    results = await asyncio.gather(
        openai_task,
#        claude_task
    )

    end = time.time()

    print("\n===== OPENAI RESPONSE =====\n")
    print(results[0])

#     print("\n===== CLAUDE RESPONSE =====\n")
#     print(results[1])

    print(f"\nCompleted in {end - start:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())