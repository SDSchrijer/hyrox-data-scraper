# Python built-in packages
import os
from enum import Enum

# External packages
from requests import request

def get_html(url: str):
    cookie_retrieval = request("GET", url)
    cookie = cookie_retrieval.request.headers.get("Cookie")
    response = request("GET", url, headers={"Cookie": cookie})
    return response.text
    
def remove_prefix(x: str, prefix: str):
    if x.startswith(prefix):
        return x[len(prefix):]
    return x
