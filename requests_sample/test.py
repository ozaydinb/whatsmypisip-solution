import requests


def get_ip_address():
    url = "http://myexternalip.com/raw"
    raw_source = requests.get(url).text
    return raw_source


print(get_ip_address())