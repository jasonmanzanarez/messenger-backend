# 💬 Messenger Backend with FastAPI, WebSocket, JWT & MongoDB

This project is a secure real-time messaging backend built with **FastAPI**, **WebSockets**, **JWT Authentication**, and **MongoDB**. It includes a minimal frontend (HTML + JS) that connects to the WebSocket server and displays live chat with authentication.

---

## 🚀 Features

- ✅ User registration and login with JWT token generation
- 🔐 Secure WebSocket connection with token validation
- 💾 Message storage in MongoDB
- 📜 Chat history fetching via REST API
- 🧪 Interactive API docs with Swagger UI (`/docs`)

---

## ⚙️ Requirements

- Python 3.9+
- MongoDB running locally (`mongodb://localhost:27017`)

### 📦 Install dependencies

Create and activate a virtual environment:

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
Install required packages:

bash
Copy
Edit
pip install -r requirements.txt
If you don’t have a requirements.txt yet, create one with:

txt
Copy
Edit
fastapi
uvicorn[standard]
pymongo
python-jose[cryptography]
python-multipart
passlib[bcrypt]
▶️ Running the Server
Start the FastAPI server:

bash
Copy
Edit
uvicorn main:app --reload
Server runs at: http://127.0.0.1:8000

Swagger documentation: http://127.0.0.1:8000/docs

🔐 Authentication Flow
Register a user
POST /auth/register
Example:

json
Copy
Edit
{
  "email": "jason@example.com",
  "username": "jason",
  "password": "123456"
}
Login
POST /auth/login
Response returns an access_token.

Use the token to:

🔌 Connect to WebSocket:
ws://127.0.0.1:8000/ws/chat?token=YOUR_TOKEN

📜 Access message history:
GET /messages with header:

makefile
Copy
Edit
Authorization: Bearer YOUR_TOKEN
🖥️ Frontend Preview
Open frontend/index.html in your browser.
Paste your token, click Connect, and start sending messages!

Real-time chat updates via WebSocket

Messages stored in MongoDB

Chat history fetched from /messages

📁 Project Structure
bash
Copy
Edit
messenger-backend/
├── auth/
│   └── dependencies.py           # Authentication dependencies
├── database/
│   └── mongo.py                  # MongoDB connection
├── frontend/
│   └── index.html                # WebSocket + JWT chat client
├── models/
│   ├── user.py                   # Pydantic models for auth
│   └── message.py                # (optional) Message structure
├── routes/
│   ├── auth.py                   # JWT registration/login
│   ├── chat.py                   # WebSocket + message handling
│   └── messages.py               # GET /messages history endpoint
├── websocket_manager.py          # WebSocket connection handler
├── main.py                       # App entry point
├── requirements.txt              # Project dependencies
├── .gitignore                    # Files excluded from Git
└── README.md                     # Project documentation
📌 Author
Jason Manzanarez
GitHub: @jasonmanzanarez

📜 License
This project is open-source and available under the MIT License.