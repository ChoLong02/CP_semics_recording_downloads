from fastapi import FastAPI
from routes.files import file_router

import uvicorn

app = FastAPI()
app.include_router(file_router, prefix="/file")


@app.get("/")
async def welcome() -> str:
    return "녹화영상 다운로드"

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9999, reload=True)