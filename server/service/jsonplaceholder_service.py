import requests as r
import json
from flask import Response


def get_by_n_registros(n=None):
    get = r.get('https://jsonplaceholder.typicode.com/todos')

    if get.status_code != 200:
        return Response(json.dumps({
            "error": {
                "reason": "Request error: https://jsonplaceholder.typicode.com/todos (GET)"
            }
        }), status=500)

    dados = get.json()
    if n:
        dados = dados[:n]

    return list(map(lambda x: {
        "id": x['id'],
        "title": x['title']
    }, dados))
