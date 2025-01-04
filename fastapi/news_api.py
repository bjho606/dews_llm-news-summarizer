from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel


# App instance
app = FastAPI()

# Sample in-memory news data
news_data = [
    {"title": "Sports News 1", "summary": "Summary of Sports News 1", "priority": 5, "category": "sports"},
    {"title": "Sports News 2", "summary": "Summary of Sports News 2", "priority": 10, "category": "sports"},
    {"title": "Tech News 1", "summary": "Summary of Tech News 1", "priority": 8, "category": "tech"},
    {"title": "Business News 1", "summary": "Summary of Business News 1", "priority": 7, "category": "business"},
    {"title": "Entertainment News 1", "summary": "Summary of Entertainment News 1", "priority": 3, "category": "entertainment"},
    {"title": "Health News 1", "summary": "Summary of Health News 1", "priority": 6, "category": "health"},
    # Add more news items as needed
]


# All news should exist in this format
class NewsItem(BaseModel):
    title: str
    summary: str
    priority: int
    category: str


# News GET API
@app.get("/news", response_model=List[NewsItem])
def get_news(category: Optional[str] = None, limit: Optional[int] = 5):
    if category:
        filtered_news = [news for news in news_data if news["category"] == category.lower()]
        if not filtered_news:
            raise HTTPException(status_code=404)

    else:
        categories = {news["category"] for news in news_data}
        filtered_news = [next(news for news in news_data if news["category"] == cat) for cat in categories]

    sorted_news = sorted(filtered_news, key=lambda x: x["priority"], reverse=True)
    return sorted_news[:limit]


# Root endpoint
@app.get("/")
def read_root():
    return {"server status: OK"}
