from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class GenerateLinkDto(BaseModel):
    url_target: str

@app.get("/")
def read():
    return { 'message': 'hello world' }

@app.post("/generate-link")
def generate_link(props: GenerateLinkDto):
    props.url_target = props.url_target.strip()

    return { 'message': props }