# NBA Scraper 

_This is a webscraper built using selenium, a python library for webscraping. It collects every NBA team's historical player stats that are available on espn's website._

### Requirements
* Python 3.8 or newer
* Google Chrome installed
    > NOTE : Selenium can work with other browsers
* Active Internet connection

### How-To-Use
1. Install all of the required libraries \
 `python -m pip install -r requirements.txt`
2. Run the NBA_Scraper module
 `python -m NBA_Scraper.__main__`

Once the scraper has completed, it will produce the found data in 3 different formats: json, csv, and excel files.

> NOTE: Excel has a row count limit of 1,048,576; if the data found exceeds this limit, the excel results cannot be generated.