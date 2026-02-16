from collections import defaultdict


class SessionStore:
    """
    In-memory session storage.
    Stores chat history per session_id.
    No business logic here.
    """

    def __init__(self):
        self.sessions = defaultdict(list)

    def add_message(self, session_id: str, role: str, content: str):
        self.sessions[session_id].append({
            "role": role,
            "content": content
        })

    def get_history(self, session_id: str):
        return self.sessions.get(session_id, [])

    def replace_history(self, session_id: str, new_history: list):
        self.sessions[session_id] = new_history

    def clear_session(self, session_id: str):
        if session_id in self.sessions:
            del self.sessions[session_id]
