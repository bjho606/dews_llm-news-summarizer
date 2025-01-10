from html.parser import HTMLParser
from typing import List, Dict, Tuple

class HeadlineParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_item = False
        self.in_url = False
        self.current_url = ""
        self.current_title = ""
        self.items = []

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, str]]) -> None:
        attrs = dict(attrs)
        if tag == "li" and "class" in attrs and "sa_item" in attrs["class"]:
            self.in_item = True
        if self.in_item and tag == "a" and "class" in attrs and "sa_text_title" in attrs["class"]:
            self.in_url = True
            self.current_url = attrs.get("href", "")

    def handle_endtag(self, tag: str) -> None:
        if tag == "li" and self.in_item:
            self.in_item = False
            if self.current_title and self.current_url:
                self.items.append({"title": self.current_title, "url": self.current_url})
            self.current_title = ""
            self.current_url = ""
        if tag == "a" and self.in_url:
            self.in_url = False

    def handle_data(self, data: str) -> None:
        if self.in_url:
            self.current_title += data.strip()


class ContentParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_article = False
        self.article_content = []

    def handle_starttag(self, tag, attrs):
        if tag == "article":
            attrs = dict(attrs)
            if attrs.get("id") == "dic_area":
                self.in_article = True

    def handle_endtag(self, tag):
        if tag == "article" and self.in_article:
            self.in_article = False

    def handle_data(self, data):
        if self.in_article:
            sentence = data.strip()
            if sentence and not sentence.isspace():
                self.article_content.append(data.strip())