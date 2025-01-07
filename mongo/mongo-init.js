db = db.getSiblingDB('news_database');

db.createCollection("news");

news_collection.insert_many([
  {
    "title": "Politics News 1",
    "summary": "Summary of Politics News 1",
    "priority": 5,
    "category": "politics"
  },
  {
    "title": "Politics News 2",
    "summary": "Summary of Politics News 2",
    "priority": 8,
    "category": "politics"
  },
  {
    "title": "Politics News 3",
    "summary": "Summary of Politics News 3",
    "priority": 7,
    "category": "politics"
  },
  {
    "title": "Politics News 4",
    "summary": "Summary of Politics News 4",
    "priority": 6,
    "category": "politics"
  },
  {
    "title": "Economy News 1",
    "summary": "Summary of Economy News 1",
    "priority": 8,
    "category": "economy"
  },
  {
    "title": "Economy News 2",
    "summary": "Summary of Economy News 2",
    "priority": 7,
    "category": "economy"
  },
  {
    "title": "Economy News 3",
    "summary": "Summary of Economy News 3",
    "priority": 6,
    "category": "economy"
  },
  {
    "title": "Economy News 4",
    "summary": "Summary of Economy News 4",
    "priority": 9,
    "category": "economy"
  },
  {
    "title": "Society News 1",
    "summary": "Summary of Society News 1",
    "priority": 6,
    "category": "society"
  },
  {
    "title": "Society News 2",
    "summary": "Summary of Society News 2",
    "priority": 5,
    "category": "society"
  },
  {
    "title": "Society News 3",
    "summary": "Summary of Society News 3",
    "priority": 7,
    "category": "society"
  },
  {
    "title": "Society News 4",
    "summary": "Summary of Society News 4",
    "priority": 8,
    "category": "society"
  },
  {
    "title": "Society News 5",
    "summary": "Summary of Society News 5",
    "priority": 4,
    "category": "society"
  },
  {
    "title": "Life/Culture News 1",
    "summary": "Summary of Life/Culture News 1",
    "priority": 9,
    "category": "life/culture"
  },
  {
    "title": "Life/Culture News 2",
    "summary": "Summary of Life/Culture News 2",
    "priority": 8,
    "category": "life/culture"
  },
  {
    "title": "Life/Culture News 3",
    "summary": "Summary of Life/Culture News 3",
    "priority": 7,
    "category": "life/culture"
  },
  {
    "title": "Tech News 1",
    "summary": "Summary of Tech News 1",
    "priority": 7,
    "category": "tech"
  },
  {
    "title": "Tech News 2",
    "summary": "Summary of Tech News 2",
    "priority": 8,
    "category": "tech"
  },
  {
    "title": "Tech News 3",
    "summary": "Summary of Tech News 3",
    "priority": 9,
    "category": "tech"
  },
  {
    "title": "Tech News 4",
    "summary": "Summary of Tech News 4",
    "priority": 10,
    "category": "tech"
  },
  {
    "title": "Tech News 5",
    "summary": "Summary of Tech News 5",
    "priority": 6,
    "category": "tech"
  },
  {
    "title": "Tech News 6",
    "summary": "Summary of Tech News 6",
    "priority": 5,
    "category": "tech"
  },
  {
    "title": "Tech News 7",
    "summary": "Summary of Tech News 7",
    "priority": 8,
    "category": "tech"
  },
  {
    "title": "Tech News 8",
    "summary": "Summary of Tech News 8",
    "priority": 7,
    "category": "tech"
  },
  {
    "title": "Tech News 9",
    "summary": "Summary of Tech News 9",
    "priority": 6,
    "category": "tech"
  },
  {
    "title": "Tech News 10",
    "summary": "Summary of Tech News 10",
    "priority": 4,
    "category": "tech"
  }
])