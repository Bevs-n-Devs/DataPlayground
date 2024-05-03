from NBA_Scraper import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


def get_team_stats(team: TEAM)->None:
    """
    Collects an NBA team stat history for Post & Pre Season

    @param conf: team conference
    @type conf: str
    @param team: team name
    @type team: str
    @param url: team stats url
    @type url: str
    """
    global webdriver
    webdriver.get(team.stats_url)
    sleep(delay_time)
    dropdown = webdriver.find_element(By.XPATH, "//*[@class='dropdown dropdown--md mr2 filters__seasonDropdown']")
    season_opts = dropdown.find_elements(By.TAG_NAME, "option")
    season_opts = [s.text for s in season_opts]
    for s in season_opts: print("\t\t-", s)

# Specify browser options
options = Options()
options.add_argument("--start-maximized")

# Instantiate a Chrome Browser instance
webdriver = webdriver.Chrome(options=options)

# Gets the website in the browser
webdriver.get(base_url)

# Allow time to wait for the browser to load the website
sleep(delay_time)

# Find a html element by its partial linke text
nba_btn = webdriver.find_element(By.PARTIAL_LINK_TEXT, "NBA")

# Action Chains is an object to perform mouse actions to interact
# with the browser programmatically
actionChains = ActionChains(driver=webdriver)
actionChains.move_to_element(nba_btn)
actionChains.perform()
sleep(1)

# click on the Teams button that gets displayed
webdriver.find_element(By.PARTIAL_LINK_TEXT, "Teams").click()
sleep(delay_time/2)

teams = []
conferences = webdriver.find_elements(By.CLASS_NAME, "mt7")
for el in conferences:
    divs = el.find_elements(By.TAG_NAME, "div")
    conf = divs[0].text
    print("-", conf)
    elBlock = divs[1]
    # print(elBlock.text)
    for t in elBlock.find_elements(By.CLASS_NAME, "pl3"):
        team_name = t.find_element(By.CLASS_NAME, "AnchorLink").text
        sec = t.find_element(By.CLASS_NAME, "TeamLinks__Links")
        stats = sec.find_element(By.TAG_NAME, "a")
        team_stat_url = stats.get_attribute("href")
        print("\t-", team_name, team_stat_url)
        teams.append(TEAM(conf=conf,team=team_name,url=team_stat_url))


for t in teams:
    get_team_stats(team=t)

# Close the browser session
webdriver.close()