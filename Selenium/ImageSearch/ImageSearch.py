####################################
# Author: Nisahnt.k.Ghanate                     
# File name: ImageSearch.py                
# Date created : 17/2/2020                    
# Python Version: Python 3.7.4  
# Status : --           
####################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request as urllib
import os 
import logging as logger
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import csv
import time
import sys
import pandas as pd

class ImageSearch:

    def __init__(self):
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.images = []
        self.links = []

    def getImages(self,folder):
        savePhotosDir =  self.scriptDir + os.sep + folder
        if os.path.exists(savePhotosDir):
            files = os.listdir(savePhotosDir)
            if len(files) == 0 : 
                print('no images ')
                quit()
            for f in files:
                path = savePhotosDir +  os.sep + f
                self.images.append(path)
        else:
            print('Folder does not exists , keep .py and folder in same parent folder')

    def getCsv(self,file):
        file = self.scriptDir + os.sep + file
        if not os.path.exists(file):
            print('File does not exists')
            quit()
        try :
            csvFile = pd.read_csv(file)
            for links in csvFile.values:
                if links[0] != None or links[0] != "":
                    # Select 1st column in csv file containing links 
                    self.links.append(links[0])
        except Exception as e:
            print(e)      

    def loadDriver(self,url):
        try :
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
            self.driver.maximize_window()
            self.driver.get(url)
        except Exception as e:
            print(e)

    def search(self):
        button = self.driver.find_element_by_xpath("//*[@class='LM8x9c']")
        if button != None:
            button.click()
            upload = self.driver.find_elements_by_xpath("//*[@class='qbwr']")[0]
            if upload != None:
                upload.click()
                linkBar = self.driver.find_element_by_xpath("//*[@id='qbui']")
                linkBar.send_keys(self.links[0])
                webdriver.ActionChains(self.driver).send_keys(Keys.ENTER).perform()

if __name__ == '__main__':
    url = 'https://images.google.com/'
    arguments = len(sys.argv) - 1
    if arguments:
        filePath = sys.argv[1]
        imageSearch = ImageSearch()
        # imageSearch.getImages(folder = filePath)
        imageSearch.getCsv(file = filePath)
        imageSearch.loadDriver(url)
        imageSearch.search()
    else:
        print('folder name not given given')
        quit()


