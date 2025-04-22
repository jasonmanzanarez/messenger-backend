from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends, Query
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse
from jose import jwt, JWTError
from datetime import datetime
import os
from database.mongo import messages_collection
from websocket_manager import ConnectionManager

chat_router = APIRouter()
manager = ConnectionManager()
SECRET_KEY = os.environ.get("SECRET_KEY", "supersecret123")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


@chat_router.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket, token: str = Query(...)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        sender_email = payload.get("sub")
        if sender_email is None:
            await websocket.close()
            return
    except JWTError:
        await websocket.close()
        return

    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            chat_data = {
                "sender": sender_email,
                "message": data,
                "timestamp": datetime.utcnow().isoformat()
            }
            messages_collection.insert_one(chat_data)
            await manager.broadcast(f"{sender_email} said: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)


@chat_router.get("/messages")
async def get_messages(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        sender_email = payload.get("sub")
        if sender_email is None:
            return JSONResponse(status_code=401, content={"detail": "Token inválido"})
        
        messages = list(messages_collection.find({}, {"_id": 0}).sort("timestamp", -1).limit(20))
        return messages[::-1]
    except JWTError:
        return JSONResponse(status_code=401, content={"detail": "Token inválido o expirado"})
