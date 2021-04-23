from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request as urllib
import os 
import logging as logger
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup
import csv
import time
import sys

# os.environ["PATH"] += os.pathsep + 'G:\msedgedriver.exe'

class Tiktok:

    def __init__(self,username,profileUrl):
        self.username = username
        self.url = profileUrl
    
    def start(self):
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--private")
        # self.driver = webdriver.Firefox(executable_path = GeckoDriverManager().install() , options=firefox_options)
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = webdriver.Ie(IEDriverManager().install())
        
        try:
            if self.driver is None or self.url is None:
                logger.error("Please provide an url")
                quit()
            self.driver.get(self.url)
            self.driver.maximize_window()
            # print(self.driver.get_log('driver'))
        except Exception as e:
            logger.error(str(e))

    # 9417 , goal = 125617
    def scollEnd(self):
        # Get scroll height
        self.driver.execute_script("window.scrollTo(0,arguments[0]);",150) # Scroll down
            # # self.driver.execute_script("window.scrollTo(0,0);")
            # # self.driver.execute_script("window.scrollTo(0,0);") # Scroll Up

            # last_height = self.driver.execute_script("return document.body.scrollWidth")
            # print(last_height)
            # time.sleep(5)
        self.driver.execute_script("window.scrollTo(arguments[0],0);",150)
    

    def getPost(self):
        html = self.driver.page_source
        soup = BeautifulSoup(html,'html5lib') 
        links = soup.find_all('a',attrs = {'class':'jsx-1792501825'})
        print('\n Extracting post')
        for index,link in enumerate(links):
            print('Index = {} , link = {}'.format(index,link.get('href')))
            try:
                self.driver.get(link.get('href'))
                time.sleep(2)
                video = self.driver.find_element_by_class_name('jsx-3382097194')
                if video != []:
                    videoDownload = video.get_attribute('src')
                    print('\nVideo download link = {}'.format(videoDownload))
                    fileName =  self.username + '_' + str(index) + '.mp4'
                    urllib.urlretrieve(videoDownload,fileName)
                    print("\nVideo Saved image = "+str(fileName))
            except Exception as e:
                print(e)
                print('No video')
        # self.driver.close()
        print('done')

if __name__ == "__main__":
    # Copy paste profile url and usename 
    username = ''
    profileUrl = ''
    print('\n Welcome to Tiktok scaper ')
    print('\n Use Python Tiktok.py url username \n For now This can scrap of max 30 posts')
    print('\n Examaple 1 : Python Tiktok.py https://www.tiktok.com/@nasjaq nasboi')

    arguments = len(sys.argv) - 1
    if arguments == 2:
        # print(arguments)
        profileUrl = sys.argv[1]
        username = sys.argv[2]
        tiktok = Tiktok(profileUrl = profileUrl , username = username )
        tiktok.start()
        # tiktok.scollEnd()
        tiktok.getPost()
    else:
        print('\n Please enter an tiktok url\n')
        quit()

   
    
   

    