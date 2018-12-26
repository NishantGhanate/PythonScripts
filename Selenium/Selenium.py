from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os 

scriptDir = os.path.dirname(os.path.realpath(__file__))
cromeDriver = scriptDir + os.path.sep + 'Driver' + os.path.sep + 'cromedriver.exe' 
foxDriver = scriptDir + os.path.sep + 'Driver' + os.path.sep + 'foxdriver.exe' 


# driver = webdriver.Chrome(executable_path=)
driver = webdriver.Firefox(executable_path = foxDriver)
driver.implicitly_wait(10)
driver.get("https://www.reddit.com/r/ProgrammerHumor/")

elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    print (elem.get_attribute("href"))

driver.close()
