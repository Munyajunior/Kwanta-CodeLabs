from fastapi import FastAPI
import uvicorn

app = FastAPI(title="KwantaBit CodeLabs FastAPI Tuto",)

@app.get('/')
async def index():
    return {"message" : "Hello World!"}





if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)