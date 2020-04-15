
import os 
import csv
import requests
from bs4 import BeautifulSoup

fieldnames = ['IP Address','Port','Code', 'Country','Anonymity','Google','Https','Last Checked']

def getProxies():
    r = requests.get("https://free-proxy-list.net/")
    soup = BeautifulSoup(r.content, 'html5lib') 
    proxyAddress = soup.find('table',attrs={'id':'proxylisttable'}).tbody
    proxies = []
    dictn = {}
    for proxy in proxyAddress:
        for name , p in zip(fieldnames,proxy):
            dictn[name] = p.get_text()
        proxies.append(dictn)
        # print(proxies)
    return proxies
        
def writeCsv(proxyList):
    with open('ProxyIp.csv', mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(proxyList)

proxyList = getProxies()
writeCsv(proxyList)
