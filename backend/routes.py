from fastapi import APIRouter, HTTPException, File, UploadFile
from database import upload_csv

routerCsv = APIRouter()


@routerCsv.post("/upload-csv/{filename}/")
async def upload_csv(filename: str):
    try:
        upload_csv(filename)
        return {"message": "Data uploaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@routerCsv.post("/upload-file/")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        return {"filename": file.filename, "contents": contents}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))