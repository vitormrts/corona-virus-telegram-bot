import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import simplejson

top = {}
rankings = {
    'totcases': {'aria-label': 'TotalCases'},
    'newcases': {'aria-label': 'NewCases', },
    'totdeaths': {'aria-label': 'TotalDeaths'},
    'newdeaths': {'aria-label': 'NewDeaths'},
    'totrecovered': {'aria-label': 'TotalRecovered'},
    'activecases': {'aria-label': 'ActiveCases'},
}


def create_rank(type):
    arialabel = rankings[type]['aria-label']

    if arialabel != 'TotalCases':
        browse.find_element_by_xpath(
            f"//table[@id='main_table_countries_today']//thead//tr//th[@aria-label='{arialabel}: activate to sort column descending']").click()

    element = browse.find_element_by_xpath(
        "//table[@id='main_table_countries_today']")
    html_content = element.get_attribute('outerHTML')

    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find(name='table')

    df_full = pd.read_html(str(table))[0].head(11)
    df = df_full[['#', 'Country,Other', f'{arialabel}']]
    df.columns = ['pos', 'country', 'total']
    df.dropna(axis='columns')

    print(df)

    return df.to_dict('records')


url = "https://www.worldometers.info/coronavirus/#countries"

option = Options()
option.headless = True  # firefox invisibel to us (action in background)
browse = webdriver.Firefox(options=option)

browse.get(url)
browse.maximize_window()
time.sleep(10)

for rank in rankings:
    top[rank] = create_rank(rank)

browse.quit()

with open('./src/ranking.json', 'w', encoding='utf8') as jp:
    #js = json.dumps(top, indent=4)
    js = simplejson.dumps(top, ignore_nan=True, indent=4)

    jp.write(js)
