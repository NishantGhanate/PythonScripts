
import requests
from bs4 import BeautifulSoup 
import json

class BlinkList:

    def __init__(self):
        self.DATA = {}

    def getUrl(self,url):
        r = requests.get(url)
        print(r.status_code)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'html5lib') 
            siteMapGroups = soup.find_all('div', attrs = {'class':'sitemap-group'}) 
            totalFound  = len(siteMapGroups)
            print('Total found = {}'.format(totalFound))
            if totalFound :
                for siteMap in siteMapGroups:
                    # print(siteMap)
                    links = siteMap.find_all('a' , attrs= {'class':'sitemap-links__link'})
                    # print(links)
                    for link in links:
                        print('Name = {} , Link = {} '.format( link.get_text(),link.get('href')) )
                        header =  link.get_text()
                        url = link.get('href')
                        self.extractInfo(header,url)
                        break
                    break

    def extractInfo(self,header,url):
        book = {}
        # title : h2.book-sample-info__title
        # subtitle : h4.book-sample-info__subtitle
        # author : div.book-sample-info__author
        # synopis : div.book-sample-info__about-text
        # abstract : div.book-sample-reader__text reader-text>h2
        # summary : div.book-sample-reader__text reader-text.p
        # key_ideas : span.book-sample-reader__chapters-label [] 
        r = requests.get(url)
        # print(r.status_code)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'html5lib')
            title = soup.find('h2',attrs={'class':'book-sample-info__title'}).get_text()
            subtitle = soup.find('h4',attrs={'class':'book-sample-info__subtitle'}).get_text()
            author = soup.find('div',attrs={'class':'book-sample-info__author'}).get_text()
            synopis = soup.find('div',attrs={'class':'book-sample-info__about-text'}).get_text()
            abstract = soup.find('div',attrs={'class':'book-sample-reader__text reader-text'}).h2.get_text()
            summary = soup.find('div',attrs={'class':'book-sample-reader__text reader-text'}).p.get_text()
            keyIdeas = soup.find_all('span',attrs={'class':'book-sample-reader__chapters-label'})
            keyIdeas = [k.get_text() for k in keyIdeas]

            # print(title ,  subtitle , author , synopis)
            # print(abstract,summary)
            # print(keyIdeas)

            book['title'] = title
            book['subtitle'] = subtitle
            book['author'] = author
            book['synopis'] = synopis
            book['abstract'] = abstract
            book['summary'] = summary
            book['keyIdeas'] = keyIdeas

            print(book)
            self.DATA[header] = book

    def writeJson(self):
        with open('data.json', 'a+', encoding='UTF-8') as outfile:
            json.dump(self.DATA, outfile , indent=4 , ensure_ascii=False)

if __name__ == "__main__":
    url = 'https://www.blinkist.com/en/sitemap'
    blinkList = BlinkList()
    blinkList.getUrl(url)
    blinkList.writeJson()
    