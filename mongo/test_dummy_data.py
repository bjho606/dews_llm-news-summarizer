from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")
db = client["news_database"]
news_collection = db["news"]

with open("test_dummy_news.json", "r") as file:
    dummy_data = json.load(file)

news_collection.delete_many({})
news_collection.insert_many(dummy_data)
print("sample data inserted")
