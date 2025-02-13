from urllib.request import Request, urlopen


def get(url: str):
    req = Request(url,method='GET')
    data = urlopen(req)
    return data