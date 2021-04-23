import os 
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging as logger

# https://github.com/mozilla/geckodriver/releases


SCROLL_PAUSE_TIME = 2

class Youtube():
    
    def __init__(self,driverPath,url):
        self.driverPath = driverPath
        self.url = url
        
    def loadDriver(self):
        try:
            if self.driverPath is None:
                logger.error(" Please provide a driver path")
                return
            # open crome options pass --incognito add_argument
            # chrome_options = webdriver.ChromeOptions()
            # # chrome_options.add_argument("--incognito")
            # chrome_options.add_argument('--disable_infobars')
            # self.driver = webdriver.Chrome(executable_path = self.driverPath , options=chrome_options)
            
            self.driver = webdriver.Firefox(executable_path = self.driverPath )
            return True
        except Exception as e:
            logger.error(str(e))
            return False
        
    def login_gmail(self,email,password):
        self.driver.find_element_by_name('identifier').send_keys(email+Keys.ENTER)
        time.sleep(2)
        self.driver.find_element_by_name('password').send_keys(password+Keys.ENTER)
               
    def loadUrl(self):
        try:
            if self.url is not None:
                self.driver.get(self.url)
                return True
            else:
                print('Please enter an url ')
                return False
        except Exception as e:
             logger.error(str(e))
             return False
                              
    def start(self,):
        driver.implicitly_wait(10)
        self.driver.get(self.url)
        # Had to write like because document.body.scrollHeight was returning 0 on youtube
        previous = 0
        difference = 0
        while True:
            # Scroll down to bottom
            current = self.driver.execute_script("return document.documentElement.scrollHeight")
            print(current)
            self.driver.execute_script("window.scrollTo(0, " + str(current)+")") 
            # Wait to load page
            difference = current - previous
            if difference == 0:
                break
            previous = current
            time.sleep(SCROLL_PAUSE_TIME)
            
        self.driver.close() 
 
if __name__ == "__main__":
    scriptDir = os.path.dirname(os.path.realpath(__file__)) 
    # loadd the crome driver
    # driverPath = scriptDir + os.path.sep + 'Driver' + os.path.sep + 'chromedriver.exe'
    driverPath = scriptDir + os.path.sep + 'Driver' + os.path.sep + 'foxdriver.exe'
    
    youttubeUrl = 'https://www.youtube.com/user/PewDiePie/videos'
    googlLogin ='https://accounts.google.com/signin/v2/identifier?service=CPanel&flowName=GlifWebSignIn&flowEntry=ServiceLogin' 
    youtube = Youtube(driverPath = driverPath, url = youttubeUrl)
    opened = youtube.loadDriver()
    link = youtube.loadUrl() 
    
    email = '*******@gmail.com'
    password ='********'
    if opened and link:
        # youtube.login_gmail(email,password)
        youtube.start()
              
              
