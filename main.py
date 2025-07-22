from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests
from bs4 import BeautifulSoup

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Let any frontend call it
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/scrape")
def scrape(url: str):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            return {"error": "Failed to fetch page", "status": r.status_code}
        soup = BeautifulSoup(r.text, "html.parser")
        title = soup.title.string if soup.title else "No Title Found"
        return {"title": title}
    except Exception as e:
        return {"error": str(e)}
