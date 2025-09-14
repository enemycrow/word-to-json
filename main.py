from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
from docx import Document

app = FastAPI()

@app.post("/convert")
async def convert_docx(file: UploadFile):
    contents = await file.read()

    with open("temp.docx", "wb") as f:
        f.write(contents)

    doc = Document("temp.docx")
    data = {"title": file.filename, "chapters": []}

    current_chapter = None

    for para in doc.paragraphs:
        style = para.style.name
        text = para.text.strip()
        if not text:
            continue

        # Detectamos un capítulo (Heading 1)
        if "Heading 1" in style:
            current_chapter = {"title": text, "content": ""}
            data["chapters"].append(current_chapter)
        else:
            # El texto normal va directo al contenido del capítulo actual
            if current_chapter:
                current_chapter["content"] += text + "\n"

    return JSONResponse(content=data, media_type="application/json")
