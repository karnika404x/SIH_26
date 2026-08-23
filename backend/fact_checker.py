"""
Sovereign AI Workbench - Offline Fact Checker
================================================
Ye "SachAI" jaisa hi idea hai (AI ke jawab me claims verify karna),
lekin poori tarah OFFLINE - koi Wikipedia ya internet call nahi.

Original SachAI extension Wikipedia API use karta hai, jo hamare
"Zero-Egress" pitch ko todta hai. Isliye yahan hum sirf apni
organization ki apni local knowledge_base.txt file se claims
verify karte hain - kabhi bhi internet nahi jata.
"""

import re
import os
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

KB_PATH = os.path.join(os.path.dirname(__file__), "knowledge_base.txt")


def load_knowledge_base() -> str:
    if not os.path.exists(KB_PATH):
        return ""
    with open(KB_PATH, "r", encoding="utf-8") as f:
        return f.read()


CLAIM_PATTERNS = [
    r"[A-Z][^.!?]*\b\d{4}\b[^.!?]*[.!?]",
    r"[A-Z][^.!?]*\b\d+(?:\.\d+)?\s*(?:million|billion|thousand|%|percent)[^.!?]*[.!?]",
    r"[A-Z][^.!?]*\b(?:was|is|were|are)\s+\w+[^.!?]*[.!?]",
]


def extract_claims(text: str):
    claims = set()
    for pattern in CLAIM_PATTERNS:
        for m in re.finditer(pattern, text):
            sentence = m.group(0).strip()
            if 20 < len(sentence) < 300:
                claims.add(sentence)
    # Fallback: split into sentences directly if regex found nothing
    if not claims:
        for s in re.split(r"(?<=[.!?])\s+", text):
            if 20 < len(s.strip()) < 250:
                claims.add(s.strip())
    return list(claims)[:6]


def score_claim(sentence: str, kb_text: str):
    s_words = set(w.lower() for w in re.findall(r"\w{4,}", sentence))
    kb_words = set(w.lower() for w in re.findall(r"\w{4,}", kb_text))

    if not s_words:
        return "unverified", 10, "No checkable content found"

    overlap = len(s_words & kb_words)
    ratio = overlap / len(s_words)

    if ratio > 0.35:
        return "verified", min(95, round(ratio * 150 + 30)), "Matches local knowledge base"
    elif ratio > 0.15:
        return "flagged", round(ratio * 200 + 15), "Partial match - manual review recommended"
    else:
        return "unverified", 15, "Not found in local knowledge base"


class VerifyRequest(BaseModel):
    text: str


@router.post("/verify-claims")
def verify_claims(req: VerifyRequest):
    kb_text = load_knowledge_base()
    claims = extract_claims(req.text)

    results = []
    for sentence in claims:
        verdict, confidence, reason = score_claim(sentence, kb_text)
        results.append({
            "sentence": sentence,
            "verdict": verdict,
            "confidence": confidence,
            "reason": reason,
        })

    return {
        "claims_checked": len(results),
        "results": results,
        "source": "local_knowledge_base",
        "external_calls_made": 0,
    }
