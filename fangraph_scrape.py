#fangraph_scrape.py
import requests
import os
import re
import pandas
import numpy
from bs4 import BeautifulSoup, Comment
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Fangraph_scrape:
    """
    fangraph_scrape class uses selenium and beautiful soup to scrape
    mlb data from fangraph.com
    """
    def __init__(self):
        
        #get the chrome web driver
        self.driver = self._get_driver() 


    def _get_driver(self):
        """
        Install the chrome webdriver and load options
        """
        options = Options()

        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')
        options.add_argument("--enable-javascript")
        
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    
    def get_soup_page(self, url):
        """
        Use the webdriver and requests to get the beautiful soup page.
        """
        self.driver.get(url)
        page = requests.get(url)

        return BeautifulSoup(page.content, "html.parser")


    def team(self, soup_page):
        """
        Scrape the mlb teams dataset.
        """
        table_class_name = 'depth-charts-aspx_table'
        col_list = []
        regex = r'teamid=(\d+)'

        teams_table = soup_page.find_all(class_ = table_class_name)
        team_df = pandas.read_html(teams_table[0].prettify())[0]
        for col in team_df.columns:
            if col[1] != 'Team':
                col_list.append(col[1] + ' ' + col[0])
            
            else:
                col_list.append(col[1])

        team_df.columns = col_list
        
        href_col = self.get_href(teams_table, regex)
        
        team_df.insert(0, 'Team Id', href_col)
        
        return team_df


    def roster(self):
        """
        Scrape the roster for each mlb team.
        """
        pass


    def get_href(self, href_soup,  regex):
        """
        Scrape hrefs from page.
        """
        href_list = []
        for href in href_soup:

            a_tags = href.find_all('a', href=True)

            for tag in a_tags:
                ids = re.findall(regex , str(tag))
                if len(ids):
                    href_list.append(ids[0])

        return pandas.Series(href_list).drop_duplicates()


    def __del__(self):
        self.driver.quit()


