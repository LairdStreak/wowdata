'''
Module Docstring
'''
import pprint as pp
from selenium import webdriver
from bs4 import BeautifulSoup


def main_function():
    '''Function Doc String
    '''
    url = "http://www.wowhead.com/world-quests/na"
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=0x0')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    content_data = driver.page_source
    driver.close()
    driver.quit()
    soup = BeautifulSoup(content_data, "html.parser")
    div = soup.find(id="articlebody")
    listdiv = soup.find(id='list')
    table_item = soup.select('#lv-lv-world-quests > div.listview-scroller > table > tbody')

    rows = table_item.find("tbody").find_all("tr")

    for row in rows:
        cells = row.find_all("td")
        rn = cells[0].get_text()

    pp.pprint(listdiv)
    pp.pprint(listdiv)


if __name__ == '__main__':
    main_function()
