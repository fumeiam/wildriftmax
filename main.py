from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# ---------- SAMPLE DATA ----------
champions = [
    {
        "id": 1,
        "name": "Ahri",
        "role": "Mid",
        "global_wr": 51.8,
        "tier": "S",
        "servers": {
            "SEA": {"wr": 53.2, "rank1": "FoxQueen", "points": 18740},
            "EUW": {"wr": 50.6, "rank1": "OrbMage", "points": 16210},
        }
    },
    {
        "id": 2,
        "name": "Kha'Zix",
        "role": "Jungle",
        "global_wr": 52.4,
        "tier": "S",
        "servers": {
            "SEA": {"wr": 54.1, "rank1": "VoidHunter", "points": 20100},
            "EUW": {"wr": 51.9, "rank1": "ClawEdge", "points": 17650},
        }
    },
    {
        "id": 3,
        "name": "Garen",
        "role": "Baron",
        "global_wr": 49.7,
        "tier": "B",
        "servers": {
            "SEA": {"wr": 50.1, "rank1": "DemaciaX", "points": 14300},
            "EUW": {"wr": 49.2, "rank1": "SpinLord", "points": 13820},
        }
    },
    {
        "id": 4,
        "name": "Lucian",
        "role": "Dragon",
        "global_wr": 50.9,
        "tier": "A",
        "servers": {
            "SEA": {"wr": 51.7, "rank1": "DualShot", "points": 16980},
            "EUW": {"wr": 50.1, "rank1": "Relentless", "points": 15800},
        }
    },
    {
        "id": 5,
        "name": "Blitzcrank",
        "role": "Support",
        "global_wr": 48.6,
        "tier": "C",
        "servers": {
            "SEA": {"wr": 49.4, "rank1": "HookGod", "points": 13210},
            "EUW": {"wr": 47.8, "rank1": "IronFist", "points": 12400},
        }
    }
]

@app.get("/")
def champions_page(request: Request):
    return templates.TemplateResponse(
        "champions.html",
        {"request": request, "champions": champions}
    )

@app.get("/tierlist")
def tierlist_page(request: Request):
    return templates.TemplateResponse(
        "tierlist.html",
        {"request": request, "champions": champions}
    )
