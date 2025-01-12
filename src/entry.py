# Internal modules
from src.utils.utils import fetch_html
from src.scraping.seasons import scrape_seasons


def main():

    url = 'https://www.hyresult.com/'

    seasons = scrape_seasons(base_url=url)

    print(seasons)