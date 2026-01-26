def answer_question(context, question):
    """
    Simple answer generator.
    In production, this would call an LLM (OpenAI / Azure OpenAI).
    """
    if not context.strip():
        return "Answer not found in the provided documents."

    return f"Based on the documents:\n{context}"
