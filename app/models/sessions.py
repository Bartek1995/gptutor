from datetime import datetime
from typing import Any, Literal, Optional

from pydantic import BaseModel, Field

SessionStatus = Literal["active", "ended"]

class SessionStartIn(BaseModel):
    user_id: str = Field(..., min_length=1, max_length=128)

class SessionStartOut(BaseModel):
    session_id: str
    status: SessionStatus
    started_at: datetime


class SessionEndIn(BaseModel):
    session_id: str = Field(..., min_length=1, max_length=128)
    
class SessionEndOut(BaseModel):
    session_id: str
    ended: bool