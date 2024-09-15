# the base url to use for espn scraping
base_url = "https://www.espn.com/"
# delay for selenium scraping, to avoid timing conflicts
delay_time = 5

class TEAM:
    """
    TEAM object to store historic player stats data
    """
    def __init__ (self, conf:str, team:str, url: str):
        """
        Constructor for the TEAM object

        @param conf : the nba conference that the team belongs to
        @type conf : str
        @param team : the team name
        @type team : str
        @param url : url for the team stats
        @type url : str
        """
        self._name = team
        self._conf = conf
        self._url = url
    
    @property
    def team_name(self):
        """
        returns the team's name
        """
        return self._name
    
    @property
    def team_conf(self):
        """
        returns the team's conference
        """
        return self._conf
    
    @property
    def stats_url(self):
        """
        returns the team's stats url
        """
        return self._url
"""
Stat categories to collect for each player
"""   
STATS_KEY = {
    "GP": "Games Played",
    "GS": "Games Started",
    "MIN": "Minutes Per Game",
    "PTS": "Points Per Game",
    "OR": "Offensive Rebounds Per Game",
    "DR": "Defensive Rebounds Per Game",
    "REB": "Rebounds Per Game",
    "AST": "Assists Per Game",
    "STL": "Steals Per Game",
    "BLK": "Blocks Per Game",
    "TO": "Turnovers Per Game",
    "PF": "Fouls Per Game",
    "AST/TO": "Assist to Turnovers Per Game",
    "FGM": "Average Field Goals Made",
    "FGA": "Average Field Goals Attempted",
    "FG%": "Field Goal Percentage",
    "3PM": "Average 3-Point Field Goals Made",
    "3PA": "Average 3-Point Field Goals Attempted",
    "3P%": "3-Point Field Goal Percentage",
    "FTM": "Average Free Throws Made",
    "FTA": "Average Free Throws Attempted",
    "FT%": "Free Throw Percentage",
    "2PM": "Average 2-Point Field Goals Made",
    "2PA": "Average 2-Point Field Goals Attempted",
    "2P%": "2-Point Field Goal Percentage",
    "SC-EFF": "Scoring Efficiency",
    "SH-EFF": "Shooting Efficiency"
}

# import to run the scraper
from NBA_Scraper import espn_scraper