import requests
import json
import random 
from bs4 import BeautifulSoup
import re




r = requests.get("https://twitter.com/elonmusk")
print(r.status_code)
soup = BeautifulSoup(r.content, 'html5lib')

def test1(soup)
    print(soup)  
    table = soup.findAll('ol', attrs = {'id':'stream-items-id'}) 
    print(table) 


    Images download from Tweet : https://twitter.com/elonmusk/media
    table = soup.findAll('div', attrs = {'class':'AdaptiveMedia-photoContainer js-adaptive-photo'}) 
    for t in table:
        print(t['data-image-url']) 

    table = soup.findAll('p', attrs= {'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text'}) 
    for t in table:
        print(t.getText()) 

    table = soup.findAll('span', attrs= {'class':'ProfileTweet-actionCount'}) 
    for t in table:
        print(t.get('data-tweet-stat-count')) # comments , retweets , likes 

    table = soup.findAll('div', attrs= {'class':'stream'}) 
    for t in table:
        print(t) 

def test2(soup):
    table = soup.findAll('div', attrs= {'class':'content'})
    for t in table:
        print('\n\n')
        time = t.small.a.get('title')
        print('Time {}'.format(time))

        tweet = t.find('div', attrs = {'class':'js-tweet-text-container'})
        tweet = tweet.find('p').getText()
        print('Tweet {}'.format(tweet))

        imageLink = t.find('div', attrs = {'class':'PlayableMedia-player'})
        print(imageLink)
             
        # if 'data-image-url' in t:
        #     print(t['data-image-url']) 
        stats = t.find_all('span', attrs = {'class':'ProfileTweet-actionCount'})[0:3]
        for s in stats:
            print(s.get('data-tweet-stat-count'))
        print('\n\n')




# Time = div.content>small.time>a.data-original-title
# Text = div.content>js-tweet-text-container>p
# Data = div.content>div.stream-item-footer>span.data-tweet-stat-count
# Image = div.content>div.AdaptiveMediaOuterContainer>div.AdaptiveMedia-container>div>div.data-image-url
# stream>ol>li>
# div.content>div.ProfileTweet-actionCountList u-hiddenVisually>span.ProfileTweet-actionCountForAria
