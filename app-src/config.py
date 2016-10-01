def get_value(key):
    in_memory = dict(
            url="http://myexternalip.com/raw",
            interval="5", # seconds
            oaserver_get="http://127.0.0.1:5000/api/get",
            oaserver_post="http://127.0.0.1:5000/api/add")
    return in_memory[key]
