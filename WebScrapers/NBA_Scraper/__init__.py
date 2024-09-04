base_url = "https://www.espn.com/"
delay_time = 5

class TEAM:
    def __init__ (self, conf:str, team:str, url: str):
        self._name = team
        self._conf = conf
        self._url = url
    
    @property
    def team_name(self):
        return self._name
    
    @property
    def team_conf(self):
        return self._conf
    
    @property
    def stats_url(self):
        return self._url
    
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