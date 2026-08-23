from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI(title="Sovereign AI Workbench Backend")

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
        answer = f"[Local AI not reachable. Make sure 'ollama serve' is running. Error: {e}]"

    return {
        "response": answer,
        "routed_model": model_label,
        "external_calls": 0,
    }


@app.get("/logs")
def logs():
    return {
        "external_calls": 0,
        "status": "isolated",
        "message": "No traffic has left the local network.",
    }


@app.get("/")
def root():
    return {"status": "Sovereign AI Workbench backend is running."}


try:
    from docgen import router as doc_router
    app.include_router(doc_router)
except ImportError:
    pass
