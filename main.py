from fastapi import FastAPI
from sqlmodel import Field, SQLModel

app = FastAPI()

@app.get("/") # path sobre el que desplegar el get
async def root():
    return {"message": "Hello World"}

@app.get("/url") # path sobre el que desplegar el get
async def predict():
    return {"url_curso": "https://mouredev.com/python"}


# Start the server: uvicorn main:app --reload / python -m uvicorn main:app --reload
# Documentation with Swagger: http://127.0.0.1:8000/docs#/
# Documentation with Redocly http://127.0.0.1:8000/redoc/
# https://mintlify.com/ is also a very nice documentation