
import requests
import pandas as pd
from config import API_KEY

BASE_URL = "https://api.harvardartmuseums.org/object"

def fetch_objects(classification, target=2500):
    page, records = 1, []
    while len(records) < target:
        params = {
            "apikey": API_KEY,
            "classification": classification,
            "size": 100,
            "page": page
        }
        response = requests.get(BASE_URL, params=params).json()
        records.extend(response.get("records", []))
        if page >= response["info"]["pages"]:
            break
        page += 1
    return records[:target]

def transform(records):
    meta, media, colors = [], [], []
    for r in records:
        meta.append({
            "id": r.get("id"),
            "title": r.get("title"),
            "culture": r.get("culture"),
            "period": r.get("period"),
            "century": r.get("century"),
            "medium": r.get("medium"),
            "dimensions": r.get("dimensions"),
            "description": r.get("description"),
            "department": r.get("department"),
            "classification": r.get("classification"),
            "accessionyear": r.get("accessionyear"),
            "accessionmethod": r.get("accessionmethod")
        })

        media.append({
            "objectid": r.get("id"),
            "imagecount": r.get("imagecount"),
            "mediacount": r.get("mediacount"),
            "colorcount": r.get("colorcount"),
            "rank": r.get("rank"),
            "datebegin": r.get("datebegin"),
            "dateend": r.get("dateend")
        })

        for c in r.get("colors", []):
            colors.append({
                "objectid": r.get("id"),
                "color": c.get("color"),
                "spectrum": c.get("spectrum"),
                "hue": c.get("hue"),
                "percent": c.get("percent"),
                "css3": c.get("css3")
            })
    return pd.DataFrame(meta), pd.DataFrame(media), pd.DataFrame(colors)
