from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.chat import chat_router
from routes.auth import auth_router
from routes.messages import messages_router

app = FastAPI()

# ✅ Middleware CORS para permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringir a ["http://127.0.0.1:5500"] si usas Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Rutas
app.include_router(chat_router)
app.include_router(auth_router)
app.include_router(messages_router)

# ✅ Ruta raíz
@app.get("/")
def root():
    return {"message": "Messenger API is running!"}
