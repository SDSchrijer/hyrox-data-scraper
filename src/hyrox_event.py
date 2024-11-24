# Built-in Python packages
import itertools

# Internal packages
from constants import Division, Gender

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


    def generate_url(
            self,
            page: int,
            division: Division,
            gender: Gender
            ):
        
        return f"https://hyrox.r.mikatiming.com/season-{self.season}/?page={page}&event=
        {division.value}_{self.event_id}&num_results=100&pid=list&pidp=start&ranking=time_finish_
        netto&search%5Bsex%5D={gender.value}&search%5Bage_class%5D=%25&search%5Bnation%5D=%25"


    def get_info(self):

        