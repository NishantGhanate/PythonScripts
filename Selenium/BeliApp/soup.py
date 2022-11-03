import pandas as pd
from bs4 import BeautifulSoup

with open("Beli.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

restraunt_list = []
rows = soup.find_all('ion-grid')
for row in rows:
    mapped = {
        'restaurant_name' : '',
        'dollar_sign' : '',
        'neighborhood' : '',
        'city' : '',
        'rating' : ''
    }
    paras = row.findAll('p')
    mapped['restaurant_name'] = paras[0].get_text()[5:].strip()
    categories =  paras[1].get_text()
    if '|' in categories:
        categories = categories.split('|')
        mapped['dollar_sign'] = categories[0].strip()
        mapped['categories'] = categories[1]
    elif '$' in categories:
        mapped['dollar_sign'] = categories.strip()
    else:
        mapped['categories'] = categories
    
    address = paras[2].get_text().split(',')
    if len(address) == 1:
        mapped['neighborhood'] = address[0]
    else:
        mapped['neighborhood'] = address[0]
        mapped['city'] = address[1]

    mapped['rating'] = row.strong.get_text()
    restraunt_list.append(mapped)
    print(mapped, end= '\n\n')


df = pd.DataFrame(restraunt_list)
df.to_csv('beli_file.csv', encoding='utf-8', index=False, doublequote=True)

