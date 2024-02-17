import os

from fastapi import APIRouter, HTTPException, status
from pathlib import Path
from fastapi.responses import FileResponse

file_router = APIRouter(
    tags=["File"],
)
dir_path = "D:/test"

@file_router.get("/list")
async def list_files():
    try:
        files = os.listdir(dir_path)
        return {"files": files}
    except Exception as e:
        return {"error": str(e)}
    
@file_router.get("/download")
async def download_file(file_name):
    print(file_name)
    file_path = Path(dir_path + "/" + file_name)
    if not file_path.is_file():
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path)