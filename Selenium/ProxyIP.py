####################################
# Author: Nisahnt.k.Ghanate                     
# File name: ProxyIp.py                
# Date created : 26/12/2018                     
# Python Version: 3.6                 
####################################

from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.keys import Keys
import os 

scriptDir = os.path.dirname(os.path.realpath(__file__))
foxDriver = scriptDir + os.path.sep + 'Driver' + os.path.sep + 'foxdriver.exe'
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
        # print(p.find_elements_by_xpath('.//td[4]')[0].text) 
        # print(p.find_elements_by_xpath('.//td[7]')[0].text)
        proxies.append(ip+":"+port+","+https)
        # print(proxies)
    driver.close() 
    return proxies



def changeHostFirefox(proxy):

    ip, port = proxy.split(':')
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.privatebrowsing.autostart", True)
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", ip)
    profile.set_preference("network.proxy.http_port", port)
    # set user_agent
    # profile.set_preference("general.useragent.override", generate_user_agent())
    profile.update_preferences()
    driver = webdriver.Firefox(executable_path = foxDriver,firefox_profile=profile)
    driver.get("http://www.google.com")
    search = driver.find_element_by_name('q')
    search.send_keys("my ip")
    search.send_keys(Keys.RETURN)

def changeHostFirefox1():
    # myProxy = proxies[0]
    PROXY = "115.178.25.130:51056"
    print(PROXY)
    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': PROXY,
        'ftpProxy': PROXY,
        'sslProxy': PROXY,
        'noProxy': '' # set this value as desired
        })
    driver = webdriver.Firefox(executable_path = foxDriver,proxy=proxy)
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
# proxies = getProxies()
# print(proxies)

# if proxies:
#     changeHostCrome(proxies[0])


proxy = '66.98.56.237:8080'
changeHostCrome(proxy)
# # proxy = "115.178.25.130:51056"

