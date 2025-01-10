from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime, timedelta
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

# All news should exist in this format
class NewsItem(BaseModel):
    title: str
    category: str
    priority: int
    date: datetime
    summary: str


# News GET API
@app.get("/news", response_model=List[NewsItem])
async def get_news(category: Optional[str] = None, limit: Optional[int] = 5):
    news_collection = db.news

    today_start = datetime.combine(datetime.today(), datetime.min.time())
    today_end = today_start + timedelta(days=1)

    query = {
        "date": {
            "$gte": today_start.isoformat(),
            "$lt": today_end.isoformat()
        }
    }
    if category:
        query["category"] = category

    logger.info(f"Querying with parameter: {query}")

    cursor = news_collection.find(query).sort("priority", 1).limit(limit)
    news_list = await cursor.to_list(length=limit)
    logger.info(f"Queried {len(news_list)} news")

    cursor_test = news_collection.find({})
    news_list_test = await cursor_test.to_list()
    logger.info(f"Total {len(news_list_test)} news in DB")
    logger.info(news_list_test[0])

    if not news_list:
        raise HTTPException(status_code=404, detail="No news found")

    return news_list


# Root endpoint
@app.get("/")
def read_root():
    logger.info("Root accessed")
    return {"server status: OK"}
