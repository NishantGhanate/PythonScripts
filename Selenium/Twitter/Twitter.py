####################################
# Author: Nisahnt.k.Ghanate                     
# File name: Twitter.py                
# Date created : 9/1/2020                    
# Python Version: Python 3.7.4  
# Status : Complete           
####################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request as urllib
import os 
import logging as logger
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import csv
import time

class Twitter:
    def __init__(self,url=None,saveFile=None):
        self.url = url 
        self.saveFile = saveFile 
        self.images = []
        self.videos = []
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))  # current working Folder/Directory 
        self.postsUrls = []

    def yeet(self):
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
            self.getUrl()
        except Exception as e:
            logger.error(str(e))

    def getUrl(self):
        try:
            if self.driver is None:
                logger.error("Please provide an url")
                return
            self.driver.get(self.url)
            # print(driver.get_log('driver'))
            self.scollEnd()
            # self.getPost()
        except Exception as e:
            logger.error( str(e))

    def scollEnd(self):
        SCROLL_PAUSE_TIME = 3.5
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            print("Scrolling..............")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll down to bottom 
            time.sleep(SCROLL_PAUSE_TIME) # Wait to load page
            # Calculate new scroll height and compare with last scroll 
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            # print(last_height ,new_height )

            if new_height == last_height :
                self.getPost()    
                return 
            last_height = new_height

    def getPost(self):
        mydict = {}
        filePath = self.scriptDir + os.sep + self.saveFile
        html = self.driver.page_source
        soup = BeautifulSoup(html,'html5lib')
        li = soup.findAll('li',attrs={'data-item-type':'tweet'})
        print("Total found = {}".format(len(li)))
        self.fields = ['Time', 'Tweet', 'Comment','Retweet','Like' ,'ImageLink'] 
        titels = ['Comment','Retweet','Like']
        with open(filePath, 'a') as csvfile: 
            # creating a csv dict writer object 
            writer = csv.DictWriter(csvfile, fieldnames = self.fields) 
            # writing headers (field names) 
            writer.writeheader() 
            i = 0
            for l in li:
                # print('\n\n')
                time = l.small.a.get('title')
                # print('Time {}'.format(time))
                mydict['Time'] = time

                tweet = l.find('div', attrs = {'class':'js-tweet-text-container'})
                tweet = tweet.find('p').getText()
                # print('Tweet {}'.format(tweet))
                mydict['Tweet'] = tweet.encode(encoding='UTF-8',errors='replace')

                stats = l.find_all('span', attrs = {'class':'ProfileTweet-actionCount'})[0:3]
                for s , t in zip(stats,titels):
                    # print(s.get('data-tweet-stat-count')) # comment , retweet like
                    mydict[t] = s.get('data-tweet-stat-count')

                imageLink = l.find('div', attrs = {'class':'PlayableMedia-player'})
                # print(imageLink)
                if imageLink != None:
                    imageLink = imageLink.get('style')
                    imageLink = imageLink.split('url')
                    imageLink = imageLink[1]
                    # fileName = self.scriptDir + os.sep + 'Media' +  os.sep  + str(i)+".jpg"
                    # urllib.urlretrieve(imageLink,fileName)
                mydict['ImageLink'] = imageLink
                i = i+1

                # print('\n\n')
                # writing data rows 
                writer.writerow(mydict)
                mydict = {}
        
            
if __name__ == "__main__":
    savefile = 'ElonBoi.csv'
    url = "https://twitter.com/elonmusk"
    twitter = Twitter(url = url , saveFile= savefile)
    twitter.yeet()


