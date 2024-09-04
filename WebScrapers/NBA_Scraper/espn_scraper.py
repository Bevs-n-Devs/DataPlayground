import json
from NBA_Scraper import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


def get_team_stats(team: TEAM)->dict:
    """
    Collects an NBA team stat history for Post & Pre Season

    @param conf: team to collect data for
    @type conf: Team
    """
    global webdriver
    webdriver.get(team.stats_url)
    sleep(delay_time)
    print("Team:",team.team_name)
    dropdown = webdriver.find_element(By.XPATH, "//*[@class='dropdown dropdown--md mr2 filters__seasonDropdown']")
    season_opts = dropdown.find_elements(By.TAG_NAME, "option")
    # season_opts = [s.text for s in season_opts]
    season_opts = [opt.get_attribute("value").split("|") for opt in season_opts[:-1] ]
    # season_opts = [a.split("|") + [b.split(" ")[-1]] for a,b in season_opts[:-1]]
    data = {}
    for a,b in season_opts:
        # print(a, webdriver.current_url)
        szn_url = webdriver.current_url.split("/")
        if "season" in szn_url:
            szn_url = "/".join(szn_url[:-4])
        else:
            szn_url = "/".join(szn_url[:-1])

        szn_url = szn_url + "/season/" + str(a) + "/seasontype/" + b 
        print(szn_url)
        webdriver.get(szn_url)
        sleep(delay_time/2)

        k = str(a)
        if int(b) == 2: k+="_reg"
        else: k+="_pos"

        data[k] = {"players" : {}}
        tbls = webdriver.find_elements(By.XPATH, "//*[@class='ResponsiveTable ResponsiveTable--fixed-left mt5 remove_capitalize']")
        plyr_data = data[k]
        for tbl in tbls:
            tmp = tbl.find_element(By.CLASS_NAME, "flex").find_elements(By.TAG_NAME, "th")
            tmp = [h.text.strip() for h in tmp]
            headers = tmp[1:]
            tbodies = tbl.find_elements(By.TAG_NAME, "tbody")
            name_body = tbodies[0]
            stat_body = tbodies[1]
            name_body_rows = name_body.find_elements(By.TAG_NAME, "tr")[:-1]
            stat_body_rows = stat_body.find_elements(By.TAG_NAME, "tr")[:-1]

            rec = {}
            for r in range(0,len(name_body_rows)):
                name = name_body_rows[r].find_element(By.TAG_NAME, "a").text.strip()
                if name not in plyr_data["players"].keys(): 
                    plyr_data["players"][name] = {}
                    pos = name_body_rows[r].find_element(By.CLASS_NAME, "font10").text.strip()
                    plyr_data["players"][name]["pos"] = pos
                    print("player:",name,", postition:",pos)
                
                rec = plyr_data["players"][name]
                cols = stat_body_rows[r].find_elements(By.TAG_NAME, "td")
                for c in range(0, len(cols)):
                    rec[headers[c]] = cols[c].text
                    # print("\t\t*", headers[c], cols[c].text)
                # if len(rec.keys()) > len(cols):
                #     print(json.dumps(rec,indent=2))
    
    data["conference"] = team.team_conf
    return data

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

data = {}
for t in teams:
    data[t.team_name] = get_team_stats(team=t)

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

# Close the browser session
webdriver.close()