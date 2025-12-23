from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from champions_data import CHAMPIONS, CURRENT_PATCH

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

ROLE_ICON = {
    "Baron": "/static/roles/baron.png",
    "Jungle": "/static/roles/jungle.png",
    "Mid": "/static/roles/mid.png",
    "Dragon": "/static/roles/dragon.png",
    "Support": "/static/roles/support.png",
}

@app.get("/")
def champions_page(request: Request):
    return templates.TemplateResponse(
        "champions.html",
        {
            "request": request,
            "champions": CHAMPIONS,
            "role_icon": ROLE_ICON,
            "current_patch": CURRENT_PATCH
        }
    )
