from html.parser import HTMLParser
from typing import TypedDict

class findreq_type(TypedDict):
    classname: str|None
    dataformat: str|None
    attrs_need: list|None
    values_need: list|None


class SiteParser(HTMLParser):
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        return super().handle_starttag(tag, attrs)
    
    def handle_endtag(self, tag: str) -> None:
        return super().handle_endtag(tag)
    
    def handle_data(self, data: str) -> None:
        return super().handle_data(data)
    
    def presetting_find(self, findreq: findreq_type):
        pass