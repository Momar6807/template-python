from fastapi import FastAPI
from api.modules.chat import chat_request
from pydantic import BaseModel

app = FastAPI()




@app.get("/api/")
def hello_world():
    return {"message": "Hello World"}


class Item(BaseModel):
    message: str
    
@app.post('/api/message')
def chat(item: Item):
    print(item)
    response = chat_request(item.message)    
    return response
