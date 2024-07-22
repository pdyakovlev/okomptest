from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='static/templates')
router = APIRouter()


@router.get('/', response_class=HTMLResponse)
async def read_city(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@router.post('/get_forecast', response_class=HTMLResponse)
async def return_forecast(request: Request):
    forecast = {'now': 'sunny',
                'after': 'rainy',
                'then': 'sunny again'}
    return templates.TemplateResponse(
        'index.html',
        {'request': request, 'forecast': forecast})
