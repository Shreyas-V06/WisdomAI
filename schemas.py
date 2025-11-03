from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage

class State(TypedDict):
    """Conversation state passed between nodes"""
    messages: Annotated[list[BaseMessage], add_messages]  # chat history for this request
    thread_id: str                                        # maps to Mem0 user record


