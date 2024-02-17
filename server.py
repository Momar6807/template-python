from fastapi import FastAPI, WebSocket
from pydantic import BaseModel
import uvicorn
from modules.chat import *
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "https://fast-gpt-gamma.vercel.app",
    "https://*.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)

class Item(BaseModel):
    message: str
    keywords: list
    
    
@app.get("/api")
def hello():
    return {"message": "Hello"}

@app.websocket("/api/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        message = data.get("message")
        keywords = data.get("keywords")
        async for chunk in chat_request_chunks(message, keywords):
            if(type(chunk) == str):
                await websocket.send_text(chunk)

if __name__ == "__main__":
    uvicorn.run() 