import requests
import requests.exceptions
import sys
import console

import config


def get_last_ip_address():
    get_url = config.get_value("oaserver_get")
    try:
        get_result = requests.get(get_url)
        response = get_result.json()
        ipaddress = response["last_ip_address"]
        console.log("Last: {}".format(ipaddress))
        return ipaddress
    except requests.exceptions.ConnectionError:
        console.log("Connection failed: "+ get_url)
        return "CONNFAIL"
    except:
       console.log("An exeption occured: "+sys.exc_info()[0])


def save_current_ip_address(current_ip):
    post_url = config.get_value("oaserver_post")
    request_data = {"ipaddress": current_ip}
    response = requests.post(post_url, json=request_data)
    if response.status_code != 200:
        raise requests.exceptions.HTTPError(response.reason)
    console.log("Changed: {}".format(current_ip))
