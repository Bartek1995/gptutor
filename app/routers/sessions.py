from datetime import datetime, timezone
from email.policy import HTTP

from fastapi import APIRouter, HTTPException
from bson import ObjectId

from app.models.sessions import SessionStartIn, SessionStartOut, SessionEndIn, SessionEndOut
from app.db.mongo import db

router = APIRouter(prefix="/sessions", tags=["sessions"])

@router.post("/start", response_model=SessionStartOut)
async def start_session(payload: SessionStartIn):
    now = datetime.now(timezone.utc)

    doc = {
        "user_id": payload.user_id,
        "status": "active",
        "started_at": now,
        "ended_at": None,
    }

    res = db["sessions"].insert_one(doc)

    return SessionStartOut(
        session_id=str(res.inserted_id),
        status="active",
        started_at=now,
    )

@router.post("/end", response_model=SessionEndOut)
async def end_session(payload: SessionEndIn):
    now = datetime.now(timezone.utc)
    try:
        ObjectId(payload.session_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid session_id format")
    
    result = db["sessions"].update_one(
        {"_id": ObjectId(payload.session_id), "status": "active"},
        {"$set": {"status": "ended", "ended_at": now}},
    )

    return SessionEndOut(
        session_id=payload.session_id,
        ended=result.modified_count == 1,
    )