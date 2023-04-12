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

class fangraph_scrape:
    """
    fangraph_scrape class uses selenium and beautiful soup to scrape
    mlb data from fangraph.com
    """
    def __init__(self):

        self.TEAMS_URL = 'https://www.fangraphs.com/depthcharts.aspx?position=Standings'
        self.ROSTER_URL = 'https://www.fangraphs.com/teams/mets'
        
        #get the chrome web driver
        self.driver = self.get_driver() 


    def get_driver(self):
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
        pass

    def team(self):
        """
        Scrape the mlb teams dataset.
        """
        pass


    def roster(self):
        """
        Scrape the roster for each mlb team.
        """
        pass


    def get_href(self):
        """
        Scrape h_refs from page.
        """
        pass


