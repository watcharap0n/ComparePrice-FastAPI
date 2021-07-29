from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes import receive
import logging
import os
import uvicorn

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
template = Jinja2Templates(directory="templates")

origins = [
    "https://service.mangoanywhere.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    receive.route,
    tags=['API'],
    responses={418: {'description': "I'm a teapot"}}
)


@app.get('/check_userId', tags=['Page'])
async def check_userId(request: Request):
    return template.TemplateResponse('public/check_userId.html', context={'request': request})


@app.get('/index', tags=['Page'])
async def index(request: Request):
    return template.TemplateResponse('src/index.html', context={'request': request})


@app.get('/register', tags=['Page'])
async def root_register(request: Request):
    return template.TemplateResponse('src/register.html', context={'request': request})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8008))
    uvicorn.run('app:app', debug=True, port=port)
