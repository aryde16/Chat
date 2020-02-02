import requests as rq


def get_post():
    resp = rq.get('localhost:8080')
    if resp.status_code == 200:
        return resp.text()

    raise Exception
