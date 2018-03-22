'''
Module Docstring
'''
import pprint as pp
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


def main_function():
    '''Function Doc String
    '''
    #   Name Rewards Faction Ends at... Zone
    records = fetch_wowhead_dailies()
    pddata = pd.DataFrame(records)

    
    # name   = [i[0] for i in records]
    # something  = [i[1] for i in records]

    pp.pprint(pddata.head)

def fetch_wowhead_dailies():
    '''docstr
    '''
    url = "http://www.wowhead.com/world-quests/na"
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=0x0')
    driver = webdriver.Chrome(chrome_options=options, executable_path=r"chromedriver.exe")
    driver.get(url)
    content_data = driver.page_source
    driver.close()
    driver.quit()
    soup = BeautifulSoup(content_data, "html.parser")
    div = soup.find(id="articlebody")
    listdiv = soup.find(id='list')
    table_item = soup.select('#lv-lv-world-quests > div.listview-scroller > table > tbody > tr')
    arrMain = []
    for record in table_item:
        arrSub = []
        for index, itemCell in enumerate(record.children):
            arrSub.insert(index, itemCell.text)
        arrMain.append(arrSub)
    
    return arrMain

if __name__ == '__main__':
    main_function()
