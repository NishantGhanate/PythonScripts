
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request as urllib
import os 
import time
                     

url = "https://www.instagram.com/realbarbarapalvin/?hl=en"


scriptDir = os.path.dirname(os.path.realpath(__file__)) 
# laod the crome driver
chromeDriver = scriptDir + os.path.sep + 'Driver' + os.path.sep + 'chromedriver.exe' 

savePhotosDir = scriptDir + os.path.sep + 'Instagram'
if not os.path.exists(savePhotosDir):
    os.makedirs(savePhotosDir)


# open crome options pass --incognito add_argument 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path=chromeDriver , options=chrome_options)

driver.get(url)



SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
print(last_height)

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    # time.sleep(SCROLL_PAUSE_TIME)

    print(new_height)
    if new_height == last_height:
        break
    last_height = new_height






i = 0
images = driver.find_elements_by_xpath("//*[@class='FFVAD']")
for image in images:
    img = image.get_attribute("srcset")
    img = img.split(",")
    img = img[-1][:-4]
    print(img)
    print("\n")
    # download the image
    filename = savePhotosDir + os.sep + "Barbara"+str(i)+".png"
    urllib.urlretrieve(img,filename )
    i = i + 1

driver.close() 