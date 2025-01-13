import csv
from typing import List, Dict

def save_news_to_csv(news_data: List[Dict[str, str]], filename: str) -> None:
    """
    Save crawled news data to a CSV file.

    :param news_data: The result of the crawl() function.
    :param filename: The name of the output CSV file.
    """
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["category", "title", "content", "url"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # Write the header
        # writer.writerow(["Category", "Title", "Content", "URL"])
        writer.writeheader()

        # for category, articles in news_data.items():
        #     for article in articles:
        #         writer.writerow([
        #             category,
        #             article.get("title", ""),
        #             article.get("url", ""),
        #             article.get("content", "")
        #         ])
        writer.writerows(news_data)


def load_news_from_csv(filename: str) -> List[Dict[str, str]]:
    """
    Load news data from a CSV file and extract title and content.

    :param filename: The name of the CSV file.
    :return: A list of dictionaries with 'title' and 'content'.
    """
    news_data = []
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            news_data.append({
                "title": row.get("title", ""),
                "content": row.get("content", "")
            })
    return news_data
