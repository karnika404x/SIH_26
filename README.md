# Sovereign AI Workbench — Hackathon Prototype

Ye ek local, offline-chalne wala AI assistant demo hai. Niche har cheez step-by-step
di gayi hai — bilkul beginner ke liye.

## Project Structure

```
sovereign-ai-workbench/
├── frontend/
│   ├── dashboard.html      ← Main landing screen
│   ├── chat.html           ← Chat screen (AI se baat karne wala)
│   └── documents.html      ← Document upload screen
├── backend/
│   ├── main.py             ← Server (chat + routing)
│   ├── docgen.py           ← Word document generator
│   └── requirements.txt    ← Python libraries list
├── demo-files/             ← Generated/sample documents yahan save honge
└── README.md               ← Ye file
```

## Setup — Pehli Baar (ek hi baar karna hai)

### 1. Ollama install karo aur AI model download karo
```
ollama pull llama3.2
```

### 2. Python libraries install karo
Terminal me `backend` folder ke andar jaake:
```
cd backend
py -m pip install -r requirements.txt
```

## Roz Chalane Ka Tarika (Demo/Testing ke liye)

Teen cheezein chalani hain — do terminal windows aur ek browser.

### Terminal 1 — Ollama (agar already chal nahi raha)
```
ollama serve
```
*(Agar "address already in use" error aaye, iska matlab already chal raha hai — chhod do, aage badho)*

### Terminal 2 — Backend Server
```
cd backend
py -m uvicorn main:app --reload --port 8000
```
Ye chalne pe dikhega: `Uvicorn running on http://127.0.0.1:8000`

### Browser — Frontend kholo
`frontend` folder ke andar `dashboard.html` file pe **double-click** karo — seedha browser me khul jayega.

(Koi npm/React install karne ki zarurat nahi — ye plain HTML files hain.)

## Test Karo

1. `dashboard.html` khulne ke baad, sidebar me "Chat" pe click karo
2. Neeche box me kuch type karo, jaise: `Hello, how are you?`
3. Send button dabao
4. Kuch second baad AI ka jawab aana chahiye, saath me "Routed to: ReasoningModel-14B" ka badge

Agar coding se related sawaal poocho (jaise "write a python function"), to badge
"CodeModel-7B" dikhayega — ye router demo ke liye hai.

## Kisne Kya Banaya

| File | Kisne banaya |
|---|---|
| `backend/main.py` | Yashika |
| `backend/docgen.py` | Priyanshi |
| `demo-files/` sample documents | Priyanshi |
| `frontend/*.html` polish/fixes | Rupal |
| Integration + is README | Tum (leader) |

## Common Problems

**"uvicorn not recognized" error aaye**
→ `uvicorn` ki jagah `py -m uvicorn` likho.

**Chat me "Local AI not reachable" error aaye**
→ Check karo Ollama chal raha hai ya nahi (Terminal 1).

**Chat me kuch response hi na aaye / stuck rahe**
→ Browser ka Console kholo (F12 dabao → Console tab) aur error dekho, ya backend
wali terminal window me error check karo.

**Backend band karna ho to**
→ Terminal me jaha uvicorn chal raha hai, wahan `Ctrl + C` dabao.

## Demo Day Tips

- Demo se pehle ek baar poora flow khud test kar lo (chat + document upload)
- Agar Ollama slow ho ya hang ho jaye, ek chhota/simple sawaal hi live demo me poochna
- Internet band karke bhi dikha sakte ho ki system offline kaam karta hai — yehi
  sabse bada selling point hai
