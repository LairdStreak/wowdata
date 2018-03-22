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
    pp.pprint(soup.prettify)


if __name__ == '__main__':
    main_function()
