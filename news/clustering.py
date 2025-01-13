import utils.converter as converter
from sentence_transformers import SentenceTransformer
from sklearn.cluster import DBSCAN
from pymongo import MongoClient
from datetime import datetime

# from sklearn.preprocessing import normalize
# from sklearn.neighbors import NearestNeighbors
# import matplotlib.pyplot as plt
# import numpy as np


# [1. Clustering]
# 1. Prepare news data
news_data = converter.load_news_from_csv("example.tsv")
# print(news_data)

# 2. Combine title+content for Calculation
texts = [f"{item['title']} {item['content']}" for item in news_data]
# print(texts)

# 3. Load Sentence-BERT model & Create embedding
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(texts)
# embeddings = normalize(embeddings)
print(embeddings)

# 4. Perform Clustering - with DBSCAN
dbscan = DBSCAN(eps=0.1, min_samples=2, metric="cosine")
clusters = dbscan.fit_predict(embeddings)
print(clusters)

# 5. Collect news data by Each Clusters
clustered_news = {}
for i, cluster in enumerate(clusters):
    if cluster != -1:  # -1은 노이즈로 제외
        if cluster not in clustered_news:
            clustered_news[cluster] = []
        clustered_news[cluster].append(news_data[i])

# [check news datas for each clusters]
for cluster, news_list in clustered_news.items():
    print(f"Cluster {cluster}:")
    for news in news_list:
        print(f"  - {news['title']}")

# 6. Sort by Cluster-size
sorted_clusters = sorted(clustered_news.items(), key=lambda x: len(x[1]), reverse=True)
# print(sorted_clusters)

# ---
# [2. Make Summary & Store to MongoDB]
# 1. Connect MongoDB Client
client = MongoClient("mongodb://localhost:27017/")
db = client["dews-news-data"]
collection = db["summary"]

# TODO
# priority = 1
# for cluster_id, news_list in sorted_clusters:
#     cluster_news = "\n".join([f"{news['title']}: {news['content']}" for news in news_list])
#
#     # 2. Create Summarization - with ___ model
#     summary = generate_summary(cluster_news)
#
#     # 3. Store summarization for each clusters
#     collection.insert_one({
#         "title": f"Cluster {cluster_id} Summary",
#         "priority": priority,
#         "date": date_today,
#         "summary": summary
#     })
#
#     priority += 1  # 우선순위 업데이트