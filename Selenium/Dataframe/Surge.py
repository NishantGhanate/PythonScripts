from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import logging as logger
import os
import csv
import pandas as pd
import urllib.request as urllib
import sys
import time 
import json


class Surge:

    def __init__(self):
        self.fields = ['Date','Calories','Steps','Distance','floors','Minutes_sitting']
        self.fields += ['Minutes_of_slow_activity','Minutes_of_moderate_activity','Minutes_of_intense_activity']
        self.fields += ['Calories_Burned','Protein_Source','Protein_Intake']
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.filePathCsv = self.scriptDir + os.sep + 'Dataframe.csv'
        self.array = []
        self.myDict = {}

    def startBrowser(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--enable-automation")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")
        if sys.platform == 'win32':
            self.driver = webdriver.Chrome(ChromeDriverManager().install() , options=chrome_options )
        elif sys.platform == 'linux' or sys.platform == 'linux2' :
            self.driver = webdriver.Chrome(options=chrome_options )
        try:
            if self.driver is None:
                logger.error("Please provide an url")
                quit()
            self.driver.maximize_window()
            self.driver.get('http://unwritten-string.surge.sh/')
        except Exception as e:
            logger.error( str(e))   

     # Helps to scroll down
    def scrollEnd(self):
        SCROLL_PAUSE_TIME = 5
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            # print("Scrolling..............",flush=True)        
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll down to bottom 
            time.sleep(SCROLL_PAUSE_TIME) # Wait to load page
            # Calculate new scroll height and compare with last scroll 
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            # print(last_height ,new_height ,flush=True )
            if new_height == last_height :   
                break 
            last_height = new_height 
     
    def scrap(self):
        html = self.driver.page_source
        soup = BeautifulSoup(html,'html5lib')
        table = soup.find_all('div',attrs={'class':'row'})
        # print(table)
        for t in table:
            self.myDict['Date'] = t.select('div > p')[0].get_text(strip=True).split(':')[1]
            self.myDict['Calories'] = t.select('div > p')[1].get_text(strip=True).split(':')[1]
            self.myDict['Steps'] = t.select('div > p')[2].get_text(strip=True).split(':')[1]

            self.myDict['Distance'] = t.select('div >  p')[3].get_text(strip=True).split(':')[1]
            self.myDict['floors'] = t.select('div > p')[4].get_text(strip=True).split(':')[1]
            self.myDict['Minutes_sitting'] = t.select('div > p')[5].get_text(strip=True).split(':')[1]

            self.myDict['Minutes_of_slow_activity'] = t.select('div > p')[6].get_text(strip=True).split(':')[1]
            self.myDict['Minutes_of_moderate_activity'] = t.select('div > p')[7].get_text(strip=True).split(':')[1]
            self.myDict['Minutes_of_intense_activity'] = t.select('div > p')[8].get_text(strip=True).split(':')[1]

            self.myDict['Calories_Burned'] = t.select('div > p')[9].get_text(strip=True).split(':')[1]
            self.myDict['Protein_Source'] = t.select('div > p')[10].get_text(strip=True).split(':')[1]
            self.myDict['Protein_Intake'] = t.select('div > p')[11].get_text(strip=True).split(':')[1]

            print(self.myDict)
            self.array.append(self.myDict)
            self.myDict ={}

    def writeCsv(self):
        with open(self.filePathCsv, 'w', encoding='utf-8') as csvfile: 
            # creating a csv dict writer object 
            writer = csv.DictWriter(csvfile, fieldnames = self.fields)
            writer.writeheader() 
            writer.writerows(self.array)


    def closeDriver(self):
        self.driver.quit()

if __name__ == '__main__':
    url = 'http://unwritten-string.surge.sh/'
    surge = Surge()
    surge.startBrowser()
    surge.scrollEnd()
    surge.scrap()
    surge.writeCsv()
    surge.closeDriver()