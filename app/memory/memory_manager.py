from app.memory.session_store import SessionStore
from app.agents.llm_client import LLMClient


SUMMARY_TRIGGER_LIMIT = 20


class MemoryManager:
    """
    Controls how conversation history is managed.
    Handles summarization logic.
    """

    def __init__(self):
        self.store = SessionStore()
        self.llm = LLMClient()

    def add_user_message(self, session_id: str, message: str):
        self.store.add_message(session_id, "user", message)
        self._check_and_summarize(session_id)

    def add_assistant_message(self, session_id: str, message: str):
        self.store.add_message(session_id, "assistant", message)
        self._check_and_summarize(session_id)

    def get_recent_history(self, session_id: str):
        return self.store.get_history(session_id)

    def _check_and_summarize(self, session_id: str):
        history = self.store.get_history(session_id)

        if len(history) <= SUMMARY_TRIGGER_LIMIT:
            return

        # Keep last 2 messages untouched
        recent_messages = history[-2:]
        old_messages = history[:-2]

        summary_text = self._summarize(old_messages)

        new_history = [
            {"role": "system", "content": f"Conversation summary: {summary_text}"}
        ] + recent_messages

        self.store.replace_history(session_id, new_history)

    def _summarize(self, messages: list) -> str:
        conversation_text = "\n".join(
            f"{m['role']}: {m['content']}" for m in messages
        )

        summary_prompt = f"""
        Summarize the following conversation briefly while preserving key facts:

        {conversation_text}
        """

        return self.llm.generate(summary_prompt)
