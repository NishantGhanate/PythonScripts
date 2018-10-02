from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# driver = webdriver.Chrome(executable_path=r'H:\Github\PythonScripts\PyQtDesigner\WebScrapper\chromedriver.exe')
driver = webdriver.Firefox(executable_path=r'H:\Github\PythonScripts\PyQtDesigner\WebScrapper\geckodriver.exe')
driver.implicitly_wait(10)
driver.get("https://www.reddit.com/r/ProgrammerHumor/")

# elems = driver.find_elements_by_xpath("//a[@href]")
# for elem in elems:
#     print (elem.get_attribute("href"))


elems = driver.find_element_by_tag_name('h2')
print(elems.text)


elems = driver.find_element_by_class_name('FHCV02u6Cp2zYL0fhQPsO')
print(elems.text)


driver.close()

#elems = driver.find_elements_by_css_selector('div.individual_internship_details')