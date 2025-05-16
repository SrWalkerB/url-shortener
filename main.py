import dotenv
import os
import uvicorn

from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from url_reference.generate_link_dto import GenerateLinkDto 
from url_reference.url_reference_service import UrlReferenceService
from database.database_init import Database


dotenv.load_dotenv()
app = FastAPI()

HOST_SERVER = os.getenv('HOST')
PORT_SERVER = os.getenv('PORT')

templates = Jinja2Templates(directory='templates')

@app.on_event('startup')
def on_startup():
    database = Database()


@app.get('/redirect_link_by_code/{code}')
def redirect_link_by_code(code: str, req: Request):
    return templates.TemplateResponse(request=req, name='redirect.html', context={"url_to_redirect": 'https://www.google.com/'})

@app.post("/generate-link")
def generate_link(props: GenerateLinkDto, req: Request):
    props.url_target = props.url_target.strip()
    urlReferenceService = UrlReferenceService()
    response = urlReferenceService.insert(props.url_target)

    return { 'response': response }

if __name__ == '__main__':
    uvicorn.run(app, host=HOST_SERVER, port=int(PORT_SERVER))
