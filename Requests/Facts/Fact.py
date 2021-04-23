import requests
import json
import random 
from bs4 import BeautifulSoup 




def randomIntresting():
    page = random.randint(1, 5) 
    r = requests.get("https://www.thefactsite.com/1000-interesting-facts/page/"+str(page) )
    print(r.status_code)

    soup = BeautifulSoup(r.content, 'html5lib') 
    
    table = soup.findAll('p', attrs = {'class':'list'}) 

    fact = table[ random.randint(0, len(table) )  ]

    fact = fact.text

    print(fact) 


def wierd():
    r = requests.get("https://www.thefactsite.com/50-weird-facts/")
    soup = BeautifulSoup(r.content, 'html5lib') 
    table = soup.findAll('p', attrs = {'class':'list'}) 
    fact = table[ random.randint(0, len(table) ) ]
    fact = fact.text
    print(fact) 


def strange():
    r = requests.get("https://www.thefactsite.com/100-strange-but-true-facts/")
    soup = BeautifulSoup(r.content, 'html5lib') 
    table = soup.findAll('p', attrs = {'class':'list'}) 
    fact = table[ random.randint(0, len(table) ) ]
    fact = fact.text
    print(fact) 


def mindblown():
    r = requests.get("https://www.thefactsite.com/100-mind-blowing-facts/")
    soup = BeautifulSoup(r.content, 'html5lib') 
    table = soup.findAll('p', attrs = {'class':'list'}) 
    fact = table[ random.randint(0, len(table) ) ]
    fact = fact.text
    print(fact) 

def amaze():
    r = requests.get("https://www.thefactsite.com/100-amazing-facts-you-never-knew/")
    soup = BeautifulSoup(r.content, 'html5lib') 
    table = soup.findAll('p', attrs = {'class':'list'}) 
    fact = table[ random.randint(0, len(table) ) ]
    fact = fact.text
    print(fact) 


def omg():
    r = requests.get("https://www.thefactsite.com/200-omg-facts-you-didnt-know/")
    soup = BeautifulSoup(r.content, 'html5lib') 
    table = soup.findAll('p', attrs = {'class':'list'}) 
    index = random.randint(0, len(table) )
    fact = table[ index ]
    fact = fact.text
    print(fact) 

def tech():
    r = requests.get("https://www.thefactsite.com/200-omg-facts-you-didnt-know/")
    soup = BeautifulSoup(r.content, 'html5lib') 
    table = soup.findAll('p', attrs = {'class':'list'}) 
    index = random.randint(0, len(table) )
    fact = table[ index ]
    fact = fact.text
    print(fact) 


def getFact(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib') 
    table = soup.findAll('p', attrs = {'class':'list'}) 
    index = random.randint(0, len(table) )
    fact = table[ index ]
    fact = fact.text
    return index , fact

urls = ["https://www.thefactsite.com/200-omg-facts-you-didnt-know/" ,
        "https://www.thefactsite.com/100-amazing-facts-you-never-knew/",
        "https://www.thefactsite.com/100-mind-blowing-facts/",
        "https://www.thefactsite.com/100-strange-but-true-facts/",
        "https://www.thefactsite.com/50-weird-facts/"
        ]
msg = getFact(urls[4])
print(msg)