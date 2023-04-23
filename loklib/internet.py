import requests

def check():
    url = 'https://www.google.com/'
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            res = "connected"
        else:
            res = "Failed to connect to the internet"
    except requests.ConnectionError or Exception as e:
        # status = f"exception occurred : {e} "
        res = "Failed to connect to the internet"
    return res

