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
    
def generate_url(page: int, division: str, gender: str, season: int, event_id: str):
    return (
        f"https://hyrox.r.mikatiming.com/season-{season}/?page={page}&event={division}" \
        f"_{event_id}&num_results=100&pid=list&pidp=start&ranking=time_finish_netto&search" \
        f"%5Bsex%5D={gender}&search%5Bage_class%5D=%25&search%5Bnation%5D=%25"
    )

def removeprefix(x: str, prefix: str):
    if x.startswith(prefix):
        return x[len(prefix):]
    return x
