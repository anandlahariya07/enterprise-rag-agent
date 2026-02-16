import os
from groq import Groq
from dotenv import load_dotenv
import time

load_dotenv()

class LLMClient:
    def __init__(self):
        self.client = Groq(
            api_key = os.getenv("GROQ_API_KEY")
        )

    def generate(self, prompt: str) -> str:
        start = time.time()
        response = self.client.chat.completions.create(
            model = "llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are an enterprise RAG assistant. Answer only using the provided context. If the answer is not in context, say you don't know."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
        )

        print(f"Groq LLM API call took: {time.time() - start:.2f}s")
        return response.choices[0].message.content