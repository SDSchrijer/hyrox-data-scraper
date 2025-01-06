# Built-in Python packages
import itertools

# External packages
from tqdm import tqdm
from bs4 import BeautifulSoup

# Internal packages
from constants import Division, Gender
from utils import get_html, remove_prefix

class HyroxEvent:
    def __init__(
            self,
            event_id: str,
            season: int
            ):
        
        self.event_id = event_id
        self.season = season
        self.event_name = ""
        self.event_participants = dict((x, dict((y, []) for y in Gender)) for x in Division)
        self.num_event_participants = dict((x, dict((y, 0) for y in Gender)) for x in Division)


    def get_info(self):
        
        # Define all combinations of division and gender
        combinations = list(itertools.product(Division, Gender))
        pbar = tqdm(combinations, desc="Retrieving participants")

        for division, gender in pbar:
            page = 1

            while True:

                # Track process of retrieving data
                pbar.set_postfix({
                    "Division": division.name,
                    "Gender": gender.name,
                    "Page": page
                })

                # Generate URL for page, division, gender combination
                url = self.generate_url(
                    page=page, 
                    division=division, 
                    gender=gender)

                # Retrieve html code of selected page
                html = get_html(url)

                # Change to structured object using Beautifulsoup
                soup = BeautifulSoup(html, 'html.parser')

                # Get subheading of page
                h2_title: str = soup.h2.text.strip()
                h2_title = remove_prefix(h2_title, "Results: ").split(" / HYROX")[0]
                if h2_title == "General Ranking / All":
                    break


        pass

    def generate_url(
        self,
        page: int,
        division: Division,
        gender: Gender
        ):

        return f"https://hyrox.r.mikatiming.com/season-{self.season}/?page={page}&event=
        {division.value}_{self.event_id}&num_results=100&pid=list&pidp=start&ranking=time_finish_
        netto&search%5Bsex%5D={gender.value}&search%5Bage_class%5D=%25&search%5Bnation%5D=%25"