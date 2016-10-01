import config
import requests
import console


def get_ip_address():
    url = config.get_value("url")
    try:
        raw_source = requests.get(url).text.strip('\n')
        return raw_source
    except requests.exceptions.ConnectionError:
        console.log("No internet connection: "+url)
        return "CONNFAIL"
