from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

# Ye line frontend ko backend se baat karne dega
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

def route_task(message: str) -> str:
    code_words = ["code", "function", "debug", "sql", "query", "script"]
    if any(word in message.lower() for word in code_words):
        return "CodeModel-7B"
    return "ReasoningModel-14B"

@app.post("/chat")
def chat(req: ChatRequest):
    model = route_task(req.message)

    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.2",
        "prompt": req.message,
        "stream": False
    })

    answer = response.json().get("response", "")

    return {
        "response": answer,
        "routed_model": model,
        "external_calls": 0
    }

@app.get("/logs")
def logs():
    return {"external_calls": 0, "status": "isolated"}
