# main.py (your backend)
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from playwright.sync_api import sync_playwright

app = FastAPI()

# Allow CORS so frontend can call this
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:8501"] for dev
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/scrape")
def scrape_course(url: str = Query(...)):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        title = page.locator('h1.clp-lead__title').inner_text()
        rating = page.locator('span[data-purpose="rating-number"]').inner_text()
        price = page.locator('div[data-purpose="course-price-text"]').inner_text()
        
        browser.close()

        return {
            "course_title": title,
            "rating": rating,
            "price": price
        }
