from app.agents.llm_client import LLMClient
from app.agents.prompt_builder import PromptBuilder
# from app.rag.retriever import get_retriever
from app.memory.memory_manager import MemoryManager
import time

memory = MemoryManager()

def answer_question(session_id: str, question: str, retriever):
    total_start = time.time()
    retrieval_start = time.time()
    memory.add_user_message(session_id, question)

    # retriever = get_retriever(metadata_filter=metadata_filter)
    docs = retriever.invoke(question)
    print(f"Retrieval time: {time.time() - retrieval_start:.2f}s")

    if not docs:
        return "Answer not found in documents."

    history_start = time.time()
    history = memory.get_recent_history(session_id)
    print(f"Memory fetch time: {time.time() - history_start:.2f}s")

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt_start = time.time()
    prompt = PromptBuilder.build(context, question, history)
    print(f"Prompt build time: {time.time() - prompt_start:.2f}s")

    llm_start = time.time()
    llm = LLMClient()
    answer = llm.generate(prompt)

    print(f"LLM time: {time.time() - llm_start:.2f}s")

    print(f"Total RAG time: {time.time() - total_start:.2f}s")

    memory.add_assistant_message(session_id, answer)

    return answer