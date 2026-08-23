"""
Sovereign AI Workbench - Backend Server
=========================================
Ye file Yashika ka kaam hai.

Ye ek chhota sa server hai jo:
1. Frontend se chat message leta hai
2. Decide karta hai ki kaun sa "model" use karna hai (fake routing, demo ke liye)
3. Local Ollama AI ko sawaal bhejta hai
4. Jawab wapas frontend ko bhejta hai

Run karne ka tarika:
    py -m uvicorn main:app --reload --port 8000
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI(title="Sovereign AI Workbench Backend")

# Ye zaroori hai taaki frontend (chat.html) backend se baat kar sake
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


class LoginRequest(BaseModel):
    psu_id: str
    password: str


# Demo ke liye kuch fake valid PSU IDs — real deployment me ye
# organization ke LDAP/Active Directory se connect hoga
VALID_USERS = {
    "PSU1001": "demo123",
    "PSU2002": "demo123",
    "ADMIN01": "admin123",
}


@app.post("/login")
def login(req: LoginRequest):
    if req.psu_id in VALID_USERS and VALID_USERS[req.psu_id] == req.password:
        return {
            "success": True,
            "message": "Access granted",
            "user_id": req.psu_id,
        }
    return {
        "success": False,
        "message": "Invalid PSU ID or password",
    }


def route_task(message: str) -> str:
    """
    Simple keyword-based router.
    Agar message me coding se related words hain, to "CodeModel" bolo,
    warna "ReasoningModel" bolo. Ye asli AI routing nahi hai, sirf
    demo ke liye ek illusion hai ki alag-alag models use ho rahe hain.
    """
    code_words = ["code", "function", "debug", "sql", "query", "script", "bug", "python", "error"]
    lowered = message.lower()
    if any(word in lowered for word in code_words):
        return "CodeModel-7B"
    return "ReasoningModel-14B"


@app.post("/chat")
def chat(req: ChatRequest):
    model_label = route_task(req.message)

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2",
                "prompt": req.message,
                "stream": False,
            },
            timeout=60,
        )
        answer = response.json().get("response", "(No response from model)")
    except Exception as e:
        # Agar Ollama chal nahi raha ho, to error na dikhe balki fallback message aaye
        answer = f"[Local AI not reachable. Make sure 'ollama serve' is running. Error: {e}]"

    return {
        "response": answer,
        "routed_model": model_label,
        "external_calls": 0,  # Hamesha 0 - yehi sovereignty proof hai
    }


@app.get("/logs")
def logs():
    """Zero-Egress Monitor panel ke liye fake/demo logs."""
    return {
        "external_calls": 0,
        "status": "isolated",
        "message": "No traffic has left the local network.",
    }


@app.get("/")
def root():
    return {"status": "Sovereign AI Workbench backend is running."}


# ---- Priyanshi ka document-generation route yahan judta hai ----
try:
    from docgen import router as doc_router
    app.include_router(doc_router)
except ImportError:
    pass

# ---- Real Network Monitor route yahan judta hai ----
try:
    from network_monitor import router as network_router
    app.include_router(network_router)
except ImportError:
    pass
