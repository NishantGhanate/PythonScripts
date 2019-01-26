####################################
# Author: Nisahnt.k.Ghanate                     
# File name: Instagram.py                
# Date created : 24/1/2019                     
# Python Version: 3.6   
# Crome driver url : http://chromedriver.chromium.org/downloads              
####################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request as urllib
import os 
import time
import logging as logger


class Instagram:
    def __init__(self,driverPath=None,url=None,savePhotosDir=None,count=None):
        self.driverPath = driverPath 
        self.url = url # instagram open Account URL 
        self.savePhotosDir = savePhotosDir # photos saving DIR
        self.count = count # images count
        self.images = []
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))  # current working Folder/Directory 
        self.postsUrls = []
    def loadDriver(self):
        try:
            if self.driverPath is None:
                logger.error(" Please provide a driver path")
                return
            # open crome options pass --incognito add_argument
            # open crome options pass --incognito add_argument 
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")
            self.driver = webdriver.Chrome(executable_path = self.driverPath , options=chrome_options)
            self.getUrl()
        except Exception as e:
            logger.error(str(e))

    def getUrl(self):
        try:
            if self.driver is None:
                logger.error(" Please provide an url")
                return
            self.driver.get(self.url)
            # print(driver.get_log('driver'))
            self.scollEnd()
        except Exception as e:
            logger.error( str(e))

    # Helps to scroll down
    def scollEnd(self):
        SCROLL_PAUSE_TIME = 2
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            print("Scrolling..............")
            path = self.driver.find_elements_by_xpath("//*[@class='v1Nh3 kIKUG  _bz0w']//a")        
            self.getImages(path)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll down to bottom 
            time.sleep(SCROLL_PAUSE_TIME) # Wait to load page
            # Calculate new scroll height and compare with last scroll 
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            # print(last_height ,new_height )
            if new_height == last_height:
                self.getPost()    
                return 
            last_height = new_height 

    def getImages(self,path):
        print("\nRetriving posts url .......")  
        for p in path:
            url = p.get_attribute("href")
            print(url)
            if url not in self.postsUrls:
                self.postsUrls.append(url)

        # print(len(self.postsUrls))
        # print(self.postsUrls)
        

    def getPost(self):

        for url in self.postsUrls:
            self.driver.execute_script("window.open('"+url+"', '_self')")
            self.driver.implicitly_wait(2)
            imagesXpath = self.driver.find_elements_by_xpath("//*[@class='FFVAD']")
            for x in imagesXpath:
                img = x.get_attribute("srcset")
                # in @srcset there's about 3-4 resolution images url seperated by ,
                img = img.split(",")
                img = img[-1][:-6]
                print(img)
                if img not in self.images:
                    # last one being highest res image -4 to escpae resoluton X*X in url
                    self.images.append(str(img[-1][:-6]))

        print(len(self.images))
        print(self.images)
        self.saveImages()
   
    def saveImages(self):
        # get the username to save phots name accordingly 
        userName = self.url.split("/")
        userName = userName[-2]
        
        # saving into working folder as default 
        if self.savePhotosDir is None :      
            self.savePhotosDir = self.savePhotosDir = self.scriptDir + os.path.sep + 'Instagram'

        if not os.path.exists(self.savePhotosDir):
            os.makedirs(self.savePhotosDir)
        logger.info('\nFile saving into : ' + str(self.savePhotosDir))
    
        imgLen = len(self.images)
        print("Images found = "+str(imgLen))
        if self.count > imgLen or imgLen is None:
            self.count = imgLen

        try:
            for  i in range(self.count):
                fileName = self.savePhotosDir + os.sep + userName + str(i)+".jpeg"
                urllib.urlretrieve(self.images[i],fileName)
                print("\nSaving image = "+str(fileName))

        except Exception as e:
            logger.error(str(e))

        print("Excution completed .....")
        self.driver.close()

if __name__ == "__main__":

    driverPath = r"H:\Github\PythonScripts\Selenium\Driver\chromedriver.exe"
    savePhotosDir = r"D:\Instagram\SundarPichai1"
    url = "https://www.instagram.com/sundarpichai/?hl=en"
    count = 500
    
    instagram = Instagram(
        driverPath = driverPath,
        savePhotosDir = savePhotosDir,
        url = url,
        count = count
        )
    instagram.loadDriver()

