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