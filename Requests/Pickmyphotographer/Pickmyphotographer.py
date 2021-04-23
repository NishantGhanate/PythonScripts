from requests_html import HTMLSession
import requests.exceptions 
import time
import csv

# ToDo collect email , address ,contactnumber, name , city name. https://www.pickmyphotographer.com/mumbai

# class Pick:

#     def __init__(self,initURl):


def getUrl(url):
    # session = HTMLSession()
    global session
    b = session.get(url)
    address = b.html.xpath("//p[@itemprop='address']//text()") # get address of company 
    print(address)
    cUrls = b.html.xpath("//a[@target='_blank']/@href") # get urls of company 
    print(cUrls)
    price = b.html.xpath("//div[@class='price-value']//text()") # get prices 
    print(price)
    row = [address,cUrls,price]
    with open('Pick.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)


url = 'https://www.pickmyphotographer.com/mumbai'
# session = HTMLSession()
# r = session.get(url)
# print(r.html.absolute_links)

# xpathSrc = "//h2[@class='profile-title']/a/@href"
# src = r.html.xpath(xpathSrc)

with open('Pick.csv', 'w') as csvfile:
    fieldnames = ['Address', 'Url' , 'Price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()



session = HTMLSession()

for i in range(15):
    url = url + "#all/page-" + str(i)
    r = session.get(url)
    xpathSrc = "//h2[@class='profile-title']/a/@href"
    src = r.html.xpath(xpathSrc)
    for s in src:
        s = 'https:'+s
        print(s)
        getUrl(s)
        time.sleep(5)


# for s in src:
#     s = 'https:'+s
#     print(s)
#     getUrl(s)
   

# ---------------------------  Testting work   -----------------------------------
#
# https://www.pickmyphotographer.com/mumbai /* Main url */
# //h2[@class='profile-title']/a/@href   /* Posts url hit link  */
# //p[@itemprop='address']//text()       /* Address remove /n /t */
# //a[@target='_blank']/@href            /* Related Urls */
# main url + '#all/page-' + i            /* pagination jugad  10 page limit */
# //div[@class='price-value']//text()    /* price */
# //p[@class='price-info']//text()       /* header page of Ad */

