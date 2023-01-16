from fastapi import FastAPI, Request, Response, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
from fastapi.staticfiles import StaticFiles
from fastapi import Depends
import numpy as np


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/index/")
async def index(request: Request):
    r = 5
    c = 3
    random_data = get_data(r,c)
    n_rows = list(range(0, r))
    n_cols = list(range(0, c))
    col_mix = get_mix(random_data)
    col_colors = ['bg-red-900', 'bg-green-900', 'bg-purple-900']
    context = {'request': request, 'n_cols': n_cols, 'n_rows': n_rows, 'col_colors': col_colors, 'random_data': random_data, 'col_mix': col_mix}
    return templates.TemplateResponse("index.html", context)

@app.get("/edit_data/")
def edit_data(request: Request ):
    current_value = list(request.query_params.values())[1]
    cId = list(request.query_params.values())[0]
    context = {'request': request, 'current_value': current_value, 'cId': cId}
    return templates.TemplateResponse("partials/edit_data.html", context)

@app.get("/edited_data/")
def edited_data(request: Request ):
    changed_value = list(request.query_params.values())[0]
    CId = list(request.query_params.values())[1]    
    context = {'request': request, 'changed_value': changed_value, 'CId': CId}
    return templates.TemplateResponse("partials/edited_data.html", context)


def get_data(r,c):
    random_data = np.random.randint(100, size=(r, c))
    return random_data

def get_mix(data):
    col_mix = 100* data / np.sum(data, axis=0) 
    return col_mix
