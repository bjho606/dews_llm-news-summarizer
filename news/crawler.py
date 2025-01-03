from typing import Optional
import requests

class PortalNews:

    def __init__(self, base_url: str, *args: str) -> None:
        if len(args) % 2 == 1:
            raise Exception("# of args must be even.")
        self.base_url = base_url
        self.category_to_path: dict[str, str] = {}
        for i in range(0, len(args), 2):
            self.category_to_path[args[i]] = args[i + 1]


news_dict: dict[str, PortalNews] = {
    "naver": PortalNews(
        "https://news.naver.com/section",
        "politics", "/100",
        "economy", "/101",
        "society", "/102",
        "culture", "/103",
        "scitech", "/105"
    )
}


def get_headline_news(category: str, portal: PortalNews) -> Optional[list]:
    base_url: str = portal.base_url
    path_dict: dict[str, str] = portal.category_to_path
    if category not in path_dict:
        return None
    result = []
    url = base_url + path_dict[category]
    response = requests.get(url)
    if response.status_code != 200:
        print(f"failed to retrieve the page from url={url}")
        return None
    # parse headline articles from response.text and append (article_title, article_url) to result for each article
    return result


def crawl(portal_name: str, *categories: str) -> dict[str, list]:
    if portal_name not in news_dict:
        raise Exception("no such portal_name: {}".format(portal_name))
    portal: PortalNews = news_dict[portal_name]
    result: dict[str, list] = {}
    for category in categories:
        print(category)
        headline_news = get_headline_news(category, portal)
        if headline_news is None:
            continue
        # from article_url, get article_body and append to result
    return result


def main():
    portal_name = "naver"
    categories = ["politics", "scitech"]
    crawl(portal_name, *categories)


if __name__ == "__main__":
    main()