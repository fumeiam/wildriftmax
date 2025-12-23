import random
from champions_roles import CHAMPION_ROLES

CURRENT_PATCH = "5.2"
SERVERS = ["SEA", "EU", "NA"]

def generate_placeholder():
    return {
        server: {
            "wr": round(random.uniform(45, 55), 1),
            "rank1": "PlayerX",
            "points": random.randint(12000, 22000)
        } for server in SERVERS
    }

CHAMPIONS = []

for name, roles in CHAMPION_ROLES.items():
    stats = {}
    for role in roles:
        stats[role] = {
            CURRENT_PATCH: generate_placeholder()
        }
    CHAMPIONS.append({
        "name": name,
        "roles": roles,
        "icon": "/static/champions/placeholder.png",
        "stats": stats
    })
