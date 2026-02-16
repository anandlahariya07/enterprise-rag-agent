class PromptBuilder:
    @staticmethod
    def build(context: str, question: str, history: str = "") -> str:
        return f"""
Use the following context to answer the question.
If the answer is not in context, say you don't know.

Conversation History:
{history}

Context:
{context}

Question:
{question}

Answer professionally and clearly:
"""
