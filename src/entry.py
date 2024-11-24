# Python built-in packages
import itertools

# Internal modules
from constants import Division, Gender
from src.utils.utils import (
    generate_url,
    get_html,
    removeprefix
)

# External modules
from bs4 import BeautifulSoup

def main():

    # Test loading results for Leipzig 2021
    page = 1
    season = 5
    division = "H"
    event_id = "2EFMS4JI2BF"
    gender = "M"

    url = generate_url(
        page=page,
        division=division,
        gender=gender,
        season=season,
        event_id=event_id
        )
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')

    # Get event name
    h2_title: str = soup.h2.text.strip()
    h2_title = removeprefix(h2_title, "Results: ").split(" / HYROX")[0]

    list_headers = soup.select(".list-group-header .list-field")
    if len(list_headers) > 0 and list_headers[0].text.strip() == "Race":
        print("exit loop")

    # try:
    #     splits = soup.find(class_="detail-box box-splits")
    # except AttributeError:
    #     self.ignore = True
    #     return



    pass
