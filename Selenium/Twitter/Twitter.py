####################################
# Author: Nisahnt.k.Ghanate                     
# File name: Twitter.py                
# Date created : 9/1/2020                    
# Python Version: Python 3.7.4  
# Status : Incomplete           
####################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request as urllib
import os 
import time
import logging as logger
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



class Twitter:
    def __init__(self,url=None,savePhotosDir=None):
        self.url = url 
        self.savePhotosDir = savePhotosDir 
        self.images = []
        self.videos = []
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))  # current working Folder/Directory 
        self.postsUrls = []

    def yeet(self):
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
            self.getUrl()
        except Exception as e:
            logger.error(str(e))

    def getUrl(self):
        try:
            if self.driver is None:
                logger.error("Please provide an url")
                return
            self.driver.get(self.url)
            # print(driver.get_log('driver'))
            self.scollEnd()
        except Exception as e:
            logger.error( str(e))

    def scollEnd(self):
        SCROLL_PAUSE_TIME = 3.5
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        i = 0
        while True:
            print("Scrolling..............")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll down to bottom 
            time.sleep(SCROLL_PAUSE_TIME) # Wait to load page
            # Calculate new scroll height and compare with last scroll 
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            # print(last_height ,new_height )
            # i = i + 1
            # if i == 12 :
            #     self.getPost()    
            #     break

            if new_height == last_height :
                self.getPost()    
                return 
            last_height = new_height

    def getPost(self):
        # path = self.driver.find_element_by_css_selector('div.AdaptiveMedia-photoContainer.js-adaptive-photo')
        # print(path)
        # path = path.get_attribute('data-image-url')
        # print(path)

        # path = self.driver.find_element_by_xpath('//div[@data-image-url]')
        # print(path)
        
        path = self.driver.find_element_by_class_name('content')
        print(path)

if __name__ == "__main__":

    savePhotosDir = r"D:\Twitter\Elon"
    url = "https://twitter.com/elonmusk/media"
    twitter = Twitter(
        savePhotosDir = savePhotosDir,
        url = url,
        )
    twitter.yeet()


