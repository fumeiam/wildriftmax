from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# ---- ROLE ICON MAP (static images) ----
ROLE_ICON = {
    "Baron": "/static/roles/baron.png",
    "Jungle": "/static/roles/jungle.png",
    "Mid": "/static/roles/mid.png",
    "Dragon": "/static/roles/dragon.png",
    "Support": "/static/roles/support.png",
}

# ---- SAMPLE DATA (5 champs, role-specific stats) ----
champions = [
    {
        "name": "Ahri",
        "roles": ["Mid"],
        "icon": "/static/champions/placeholder.png",
        "stats": {
            "Mid": {
                "SEA": {"wr": 53.2, "rank1": "FoxQueen", "points": 18740},
                "EU":  {"wr": 50.6, "rank1": "OrbMage",  "points": 16210},
                "NA":  {"wr": 49.9, "rank1": "CharmFox", "points": 15400},
            }
        }
    },
    {
        "name": "Kha'Zix",
        "roles": ["Jungle"],
        "icon": "/static/champions/placeholder.png",
        "stats": {
            "Jungle": {
                "SEA": {"wr": 54.1, "rank1": "VoidHunter", "points": 20100},
                "EU":  {"wr": 51.9, "rank1": "ClawEdge",   "points": 17650},
                "NA":  {"wr": 50.3, "rank1": "ShadowBug",  "points": 16820},
            }
        }
    },
    {
        "name": "Garen",
        "roles": ["Baron"],
        "icon": "/static/champions/placeholder.png",
        "stats": {
            "Baron": {
                "SEA": {"wr": 50.1, "rank1": "DemaciaX", "points": 14300},
                "EU":  {"wr": 49.2, "rank1": "SpinLord", "points": 13820},
                "NA":  {"wr": 48.7, "rank1": "JusticeMan","points": 13210},
            }
        }
    },
    {
        "name": "Lucian",
        "roles": ["Dragon", "Mid"],  # primary = Dragon
        "icon": "/static/champions/placeholder.png",
        "stats": {
            "Dragon": {
                "SEA": {"wr": 51.7, "rank1": "DualShot",  "points": 16980},
                "EU":  {"wr": 50.1, "rank1": "Relentless","points": 15800},
                "NA":  {"wr": 49.6, "rank1": "TwinPistol","points": 14950},
            },
            "Mid": {
                "SEA": {"wr": 50.2, "rank1": "LaneKing",  "points": 16010},
                "EU":  {"wr": 49.4, "rank1": "SideStep",  "points": 15030},
                "NA":  {"wr": 48.9, "rank1": "QuickDraw","points": 14420},
            }
        }
    },
    {
        "name": "Blitzcrank",
        "roles": ["Support"],
        "icon": "/static/champions/placeholder.png",
        "stats": {
            "Support": {
                "SEA": {"wr": 49.4, "rank1": "HookGod",  "points": 13210},
                "EU":  {"wr": 47.8, "rank1": "IronFist","points": 12400},
                "NA":  {"wr": 47.2, "rank1": "GrabBot","points": 11980},
            }
        }
    },
]

@app.get("/")
def champions_page(request: Request):
    return templates.TemplateResponse(
        "champions.html",
        {
            "request": request,
            "champions": champions,
            "role_icon": ROLE_ICON
        }
    )
