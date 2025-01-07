from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
import logging

# app instance
app = FastAPI()

# set logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Sample in-memory news data
MONGO_URL = "mongodb://mongodb:27017"
client = AsyncIOMotorClient(MONGO_URL)
db = client.news_database
news_collection = db.news

# All news should exist in this format
class NewsItem(BaseModel):
    title: str
    summary: str
    priority: int
    category: str


# News GET API
@app.get("/news", response_model=List[NewsItem])
async def get_news(category: Optional[str] = None, limit: Optional[int] = 5):
    logger.info(f"Querying {limit} news")

    query = {}
    if category:
        query = {"category": category}

    cursor = news_collection.find(query).sort("priority", -1).limit(limit)
    news_list = await cursor.to_list(length=limit)
    logger.info(f"Queried {len(news_list)} news")

    if not news_list:
        raise HTTPException(status_code=404, detail="No news found")

    return news_list


# Root endpoint
@app.get("/")
def read_root():
    logger.info("Root accessed")
    return {"server status: OK"}
