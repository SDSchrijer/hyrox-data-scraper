# Internal modules
from src.utils.utils import fetch_html
from src.models.season import Season
from src.models.event import Event

# External packages
from bs4 import BeautifulSoup

def scrape_seasons(base_url):
    
    season_nr = 1
    seasons = {}
    seasons = []

    while True: 

        # Extend url to access events
        season_url = base_url + f'events?tab=all&s={season_nr}'

        # Extract website content
        html_content = fetch_html(season_url)
        soup = BeautifulSoup(html_content, "html.parser")

        # Extract season year
        span = soup.find("span", class_="rt-SelectTriggerInner")
        season_year = span.text
        season_year = season_year.replace(" ","")

        # Stop if there are no more seasons
        if season_year == "":
            break
        
        # Create season name
        season_name = f's{season_nr}'

        # Create season class
        season = Season(name=season_name, year=season_year)

        # Find all events for this season
        h3_elements = soup.find_all("h3")

        # Store events in Season class
        for h3 in h3_elements:
            event_name = h3.text
            event_name = event_name.replace("HYROX ","")

            season.add_event(event_name)
        
        # Add Season to list of seasons
        seasons.append(season)        

        season_nr += 1

    return seasons