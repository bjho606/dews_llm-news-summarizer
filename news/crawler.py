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


def crawl(portal_name: str, *categories: str) -> None:
    if portal_name not in news_dict:
        raise Exception("no such portal_name: {}".format(portal_name))
    path_dict: dict[str, str] = news_dict[portal_name]
    result = []

def main():
    portal_name = "naver"
    categories = ["politics", "scitech"]
    crawl(portal_name, *categories)


if __name__ == "__main__":
    main()