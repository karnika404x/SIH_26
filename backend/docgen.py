# backend/docgen.py
from docx import Document
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class DocRequest(BaseModel):
    title: str
    content: str

@router.post("/generate-doc")
def generate_doc(req: DocRequest):
    doc = Document()
    doc.add_heading(req.title, 0)
    doc.add_paragraph(req.content)
    path = f"./demo-files/{req.title}.docx"
    doc.save(path)
    return {"file_path": path}