from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox(executable_path=r'H:\Github\PythonScripts\PyQtDesigner\WebScrapper\geckodriver.exe')
driver.get("https://www.tatacliq.com/global-desi-navy-embroidered-kurta/p-mp000000000876745")
driver.set_page_load_timeout(45)
driver.maximize_window()
driver.implicitly_wait(2)
driver.get_screenshot_as_file("D:\\Tatacliq.png")
print ("Executed Succesfull")
# driver.find_element_by_xpath("//div[@class='pdp-promo-title pdp-title']").click()`enter code here`
# SpecialPrice =driver.find_element_by_xpath("//div[@class='pdp-promo-title pdp-title']").text
# print(SpecialPrice)
driver.close()
