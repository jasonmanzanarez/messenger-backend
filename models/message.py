from pydantic import BaseModel
from typing import Optional

class ChatMessage(BaseModel):
    sender: str
    message: str
    timestamp: Optional[str] = None
