from fastapi import APIRouter, Depends
from database.mongo import messages_collection
from auth.dependencies import get_current_user

messages_router = APIRouter()

@messages_router.get("/messages")
def get_all_messages(user: str = Depends(get_current_user)):
    messages = list(messages_collection.find({}, {"_id": 0}))
    return {"user": user, "messages": messages}
