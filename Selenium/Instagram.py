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

    def loadDriver(self):
        try:
            if self.driverPath is None:
                logger.error(" Please provide a driver path")
                return
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


    def scollEnd(self):
        SCROLL_PAUSE_TIME = 2
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            print("Scrolling..............")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll down to bottom 
            time.sleep(SCROLL_PAUSE_TIME) # Wait to load page

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            # print(new_height)
            if new_height == last_height:
                self.getImages()
                break
            last_height = new_height

    def getImages(self):
        print("\nRetriving images xpath.......")
        # instagram image class <image class="FFVAD" srcset="url">
        imagesXpath = self.driver.find_elements_by_xpath("//*[@class='FFVAD']")
        for image in imagesXpath:
            img = image.get_attribute("srcset")
            # in @srcset there's about 3-4 resolution images url sep by ,
            img = img.split(",")
            # last one being highest res image -4 to escpae resoluton X*X in url
            self.images.append(img[-1][:-4])

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
        if self.count > imgLen:
            self.count = imgLen

        try:
            for  i in range(self.count):
                fileName = self.savePhotosDir + os.sep + userName + str(i)+".png"
                urllib.urlretrieve(self.images[i],fileName)
                print("\nSaving image = "str(fileName))

        except Exception as e:
            logger.error(str(e))

        print("Excution completed .....")
        self.driver.close()

if __name__ == "__main__":

    driverPath = r"H:\Github\PythonScripts\Selenium\Driver\chromedriver.exe"
    savePhotosDir = r"D:\Instagram\SundarPichai"
    url = "https://www.instagram.com/sundarpichai/?hl=en"
    count = 500
    
    instagram = Instagram(
        driverPath = driverPath,
        savePhotosDir = savePhotosDir,
        url = url,
        count = count
        )
    instagram.loadDriver()