'''
Module Docstring
'''
import pprint as pp
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import urllib
import os.path
import matplotlib.pyplot as plt


FILE_NAME = 'wowaucdata.csv'

def main_function():
    '''Function Doc String
    '''
    #   Name Rewards Faction Ends at... Zone
    #records = fetch_wowhead_dailies()

    #pddata = pd.DataFrame(records)
    # list of aray from list of lists 
    # name   = [i[0] for i in records]
    # something  = [i[1] for i in records]

    # pp.pprint(pddata.head)
    result = fetch_wowaucdata()
    # result = True
    if result:
        pandaFrame = build_panda_dataframe()
        # Realm_Name = pandaFrame['Realm Name'].unique()
        # Item_Name = pandaFrame['Item Name'].unique()
        glyphRows = pandaFrame.loc[pandaFrame['Item Name'].str.contains('Glyph of')]
        profitItems = glyphRows[glyphRows['PMktPrice StdDev'] > 0]
        profitItems = profitItems.head(5)

        dfItemList = profitItems['Item Name'].tolist()
        dfValueList = profitItems['PMktPrice StdDev'].tolist()
        
        plt.xticks(rotation=90)
        plt.bar(dfItemList, dfValueList,color=['black', 'red', 'green', 'blue', 'cyan'])
        plt.show()

def build_panda_dataframe():
    '''docstr'''
    df = pd.read_csv(FILE_NAME,sep='\t', error_bad_lines=False)
    return df

def fetch_wowaucdata():
    '''docstr
    '''
    # if(os.path.isfile('wowaucdata.csv')):
    url = 'http://www.wowuction.com/us/khazgoroth/alliance/Tools/RealmDataExportGetFileStatic?token=wVQ31OiPJkUSpa1tbirwyA2'
    fetch_save_from_url(url, FILE_NAME)
    return True

def fetch_save_from_url(url, filename):
    csvfileOpener = urllib.URLopener()
    csvfileOpener.retrieve(url, filename)


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
