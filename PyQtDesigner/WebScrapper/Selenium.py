from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path=r'H:\Github\PythonScripts\PyQtDesigner\WebScrapper\geckodriver.exe')
# driver.implicitly_wait(10)
driver.get("https://internshala.com/internships/computer%20science-internship-in-mumbai")

# elems = driver.find_elements_by_xpath("//a[@href]")
# for elem in elems:
#     print (elem.get_attribute("href"))

#elems = driver.find_elements_by_css_selector('div.individual_internship_details')

# print(elems)

for e in elems:
    print(e.text)

driver.close()

