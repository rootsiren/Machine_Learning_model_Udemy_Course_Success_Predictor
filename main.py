import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/scrape")
def scrape(url: str):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }
        res = requests.get(url, headers=headers)

        if res.status_code != 200:
            return {"error": "Failed to fetch page", "status": res.status_code}

        soup = BeautifulSoup(res.text, "html.parser")

        # 🧪 Example: scrape title and price
        title = soup.find("h1")
        price = soup.find("span", class_="price-text")  # May need updating

        return {
            "title": title.text.strip() if title else "N/A",
            "price": price.text.strip() if price else "N/A"
        }

    except Exception as e:
        return {"error": str(e)}
