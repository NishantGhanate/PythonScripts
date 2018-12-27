####################################
# Author: Nisahnt.k.Ghanate                     
# File name: ProxyIp.py                
# Date created : 26/12/2018                     
# Python Version: 3.6                 
####################################

from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import os 

scriptDir = os.path.dirname(os.path.realpath(__file__))
foxDriver = scriptDir + os.path.sep + 'Driver' + os.path.sep + 'geckodriver.exe'
chromeDriver = scriptDir + os.path.sep + 'Driver' + os.path.sep + 'chromedriver.exe' 

def getProxies():
    driver = webdriver.Firefox(executable_path = foxDriver)
    driver.get("https://free-proxy-list.net/")
    proxyAddress = driver.find_elements_by_xpath("//*[@id='proxylisttable']/tbody/tr")
    # IP Address,Port,Code,Country,Anonymity,Google,Https,Last Checked
    proxies = list()
    for p in proxyAddress:
        # Note if you are using selenium-driver xpath use .text 
        ip = p.find_elements_by_xpath('.//td[1]')[0].text
        port = p.find_elements_by_xpath('.//td[2]')[0].text
        https = p.find_elements_by_xpath('.//td[7]')[0].text
        if https =='yes':
            proxies.append(ip+":"+port)

        # print(proxies)
    driver.close() 
    return proxies



def changeHostFirefox(proxy):

    ip, port = proxy.split(':')
    port = int(port)
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
    firefox_profile.set_preference("network.proxy.type", 1)
    firefox_profile.set_preference("network.proxy.http", ip)
    firefox_profile.set_preference("network.proxy.http_port", port)
    firefox_profile.set_preference("network.proxy.ssl", ip )
    firefox_profile.set_preference("network.proxy.ssl_port", port)
    # set user_agent
    # firefox_profile.set_preference("general.useragent.override", generate_user_agent())
    firefox_profile.update_preferences()
    driver = webdriver.Firefox(executable_path = foxDriver,firefox_profile=firefox_profile)
    driver.get("http://whatismyipaddress.com")
    driver.implicitly_wait(2)
    # driver.execute_script('''window.open("https://www.youtube.com/watch?v=Z5VdGcOWGHY&t=3s","_self");''')
    driver.get("https://www.youtube.com/watch?v=IKZ2Zbmoccw")
    elementTime = driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[3]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[20]/div[2]/div[1]/div/span[3]')
    print(elementTime.text)


def changeHostFirefox1(proxy):
    print(proxy)
    PROXY = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': proxy,
        'ftpProxy': proxy,
        'sslProxy': proxy
        })
    driver = webdriver.Firefox(executable_path = foxDriver,proxy=PROXY)
    driver.get("http://www.google.com")
    search = driver.find_element_by_name('q')
    search.send_keys("my ip")
    search.send_keys(Keys.RETURN)


def changeHostCrome(proxy):
    chrome_options = webdriver.ChromeOptions()
    print(proxy)
    chrome_options.add_argument('--proxy-server=http://%s' % proxy )
    chrome_options.add_argument("--incognito")
    chrome = webdriver.Chrome(executable_path=chromeDriver , options=chrome_options)
    chrome.get("http://whatismyipaddress.com")
    # chrome.get("http://www.google.com")
    # search = chrome.find_element_by_name('q')
    # search.send_keys("my ip")
    # search.send_keys(Keys.RETURN)
    print(chrome.get_log('driver'))

# get proxies
proxies = getProxies()
print(proxies)

if proxies:
    changeHostFirefox(proxies[0])
    # changeHostCrome(proxies[0])

# changeHostFirefox("212.211.185.27:3128")

