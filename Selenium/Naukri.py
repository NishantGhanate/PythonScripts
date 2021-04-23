from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 

import urllib.request as urllib
import os 
import time
import re
import logging as logger

from bs4 import BeautifulSoup 
from lxml.html import fromstring

class Naukri:

    def __init__(self,driverPath,id,pwd,url):
        self._driverPath = driverPath
        self._id = id
        self._pwd = pwd
        self._url = url

    def loadDriver(self):
        try:
            if self._driverPath is None:
                logger.error(" Please provide a driver path")
                return
            if self._url is None:
                logger.error(" Please provide a website url ")
            # open crome options pass --incognito add_argument 
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")
            self.driver = webdriver.Chrome(executable_path = self._driverPath , options=chrome_options)
            # self.driver = webdriver.Firefox(executable_path = self._driverPath )
            self.driver.get(self._url)
        except Exception as e:
            logger.error(str(e))
            return   

    def login(self):
        try: 
            if self._id  and self._pwd  == None :
                logger.error(" Please provide your email and password")
                return 
            search = self.driver.find_element_by_id('usernameField')
            search.send_keys(self._id)
            search = self.driver.find_element_by_id('passwordField')
            search.send_keys(self._pwd)
            search.send_keys(Keys.RETURN)

        except Exception as e:
            logger.error( str(e) )
            return 

    # def applyFilter(self,skill,location,exp,salary):
    #     # Note : Selenium does not know when new page is loaded . So wait till it find element from next page
    #     element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "qsb-location-sugg")))
    #     print(self.driver.current_url)
        # search = self.driver.find_element_by_id('qsb-location-sugg')
        # search.click()
        # search.send_keys(skill)
        # search = self.driver.find_element_by_id('qsb-location-sugg')
        # search.send_keys(location)
        # search = self.driver.find_element_by_id('hid_expDroope-experience')
        # search.send_keys(exp)
        # search = self.driver.find_element_by_id('hid_salaryDroope-salary')
        # search.send_keys(salary)
        # search.send_keys(Keys.RETURN)

        # search = self.driver.find_element_by_class_name('view-all right-align')
        # search.click()
        
        # h = self.driver.find_element_by_xpath("//div[@class=view-all.right-align']//a/@href")
        # print(h)

        # self.driver.find_element_by_class_name('view-all.right-align').click()

    def applyJobs(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "qsb-location-sugg")))
        s = self.driver.current_url 
        s = s.replace('homepage' , 'recommendedjobs')
        self.driver.get(s)
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "jobTuple  ")))
        print(self.driver.current_url)
        html = self.driver.page_source
        parser = fromstring(html)
        urls = parser.xpath("//a[@class='tupleLink']//@href")
        for u in urls :
            print(u)
            if "ambitionbox" not in u :
                self.driver.execute_script("window.open('"+u+"', '_self')")
                self.driver.implicitly_wait(5)
                
                element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "trig1")))
                if element != None:
                    print('Applied to this : {} '.format(u))
                    element.click()
                else :
                    continue
          
            
if __name__ == '__main__':
    driverPath = 'G:/Github/PythonScripts/Selenium/Driver/chromedriver.exe'
    # driverPath = 'G:/Github/PythonScripts/Selenium/Driver/geckodriver.exe'
    id = 'eamil@gmail.com'
    pwd = 'passqord^'
    url ='https://www.naukri.com/nlogin/logout'

    naukri = Naukri(driverPath,id,pwd,url)
    naukri.loadDriver()
    naukri.login()

    # skill = 'python'
    # location = 'mumbai'
    # exp = 1
    # salary = 5
    # naukri.applyFilter(skill,location,exp,salary)
    
    naukri.applyJobs()


    


 # Input fileds : driver.clear()
    # id : qsb-keyskill-sugg
    # id : qsb-location-sugg
    # id : expDroope-experienceFor , hid_expDroope-experience 0 - 30  years
    # id : salaryDroope-salaryFor , hid_salaryDroope-salary 0 - 100 LPA
    # driver.find_element_by_xpath("//input[contains(@class,'view-all right-align')]").get_attribute('value')
    # by_xpath("//a[@class='tupleLink']//@href")
# $x("//a[@class='tupleLink']")


   # print(html)
        # soup = BeautifulSoup(html, 'html5lib') 
        # table = soup.findAll('a', attrs = {'class':'tupleLink'})
        # print(table) 
        # for t in table:
        #     url = t['href']
        #     print(url)
     # jobLinks = self.driver.find_element_by_xpath("//a[@class='tupleLink']")