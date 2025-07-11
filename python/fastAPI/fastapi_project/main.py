from fastapi import FastAPI

app = FastAPI(title="KwantaBit CodeLabs FastAPI Tuto",)

@app.get('/')
async def index():
    return {"message" : "Hello World!"}