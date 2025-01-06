from typing import List, Dict, Optional
import requests
from parser import HeadlineParser, ContentParser

class PortalNews:
    def __init__(self, base_url: str, *args: str) -> None:
        if len(args) % 2 == 1:
            raise Exception("# of args must be even.")
        self.base_url = base_url
        self.category_to_path: Dict[str, str] = {}
        for i in range(0, len(args), 2):
            self.category_to_path[args[i]] = args[i + 1]


news_dict: Dict[str, PortalNews] = {
    "naver": PortalNews(
        "https://news.naver.com/section",
        "politics", "/100",
        "economy", "/101",
        "society", "/102",
        "culture", "/103",
        "scitech", "/105"
    )
}


def get_headline_news(category: str, portal: PortalNews) -> List[Dict[str, str]]:
    base_url: str = portal.base_url
    path_dict: dict[str, str] = portal.category_to_path
    if category not in path_dict:
        return []
    url = base_url + path_dict[category]
    response = requests.get(url)
    if response.status_code != 200:
        print(f"failed to retrieve the page from url={url}")
        return []
    parser = HeadlineParser()
    parser.feed(response.text)
    return parser.headlines[:]


def get_content(url: str) -> Optional[List[str]]:
    response = requests.get(url)
    if response.status_code != 200:
        print(f"failed to retrieve the page from url={url}")
        return None
    parser = ContentParser()
    parser.feed(response.text)
    return parser.article_content[:]


def crawl(portal_name: str, *categories: str) -> Dict[str, Dict[str, str | List[str]]]:
    if portal_name not in news_dict:
        raise Exception("no such portal_name: {}".format(portal_name))
    portal: PortalNews = news_dict[portal_name]
    result = {}
    for category in categories:
        headline_news = get_headline_news(category, portal)
        if headline_news is None:
            continue
        for article in headline_news:
            if "url" not in article:
                raise Exception("headline news parse error")
            content = get_content(article["url"])
            article["content"] = content
        result[category] = headline_news
    return result


def main():
    portal_name = "naver"
    categories = ["politics", "economy"]
    crawl(portal_name, *categories)


if __name__ == "__main__":
    main()