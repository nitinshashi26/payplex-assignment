from fastapi import APIRouter, UploadFile, File
from .aipipeline import process_document

router = APIRouter(tags=["IDP"])

@router.post("/process")
async def process_doc(file: UploadFile = File(...)):
    contents = await file.read()
    with open("temp_upload.pdf", "wb") as f:
        f.write(contents)
    result = process_document("temp_upload.pdf")
    return {"filename": file.filename, **result}
