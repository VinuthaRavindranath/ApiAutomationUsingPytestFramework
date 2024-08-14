# Help you to make the POST, GET, PATCH, PUT and Delete.

import json
import requests


def get_request(url, params, headers):
    response = requests.get(url=url, params=params, headers=headers)
    return response.json()