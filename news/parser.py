from html.parser import HTMLParser
from typing import List, Dict, Tuple

class HeadlineParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_headline_item = False
        self.in_url = False
        self.current_url = ""
        self.current_title = ""
        self.headlines = []

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, str]]) -> None:
        attrs = dict(attrs)
        if tag == "li" and "class" in attrs and "sa_item _SECTION_HEADLINE" in attrs["class"]:
            self.in_headline_item = True
        if self.in_headline_item and tag == "a" and "class" in attrs and "sa_text_title" in attrs["class"]:
            self.in_url = True
            self.current_url = attrs.get("href", "")

    def handle_endtag(self, tag: str) -> None:
        if tag == "li" and self.in_headline_item:
            self.in_headline_item = False
            if self.current_title and self.current_url:
                self.headlines.append({"title": self.current_title, "url": self.current_url})
            self.current_title = ""
            self.current_url = ""
        if tag == "a" and self.in_url:
            self.in_url = False

    def handle_data(self, data: str) -> None:
        if self.in_url:
            self.current_title += data.strip()
