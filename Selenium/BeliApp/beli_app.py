
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time
import random
import pandas as pd
from bs4 import BeautifulSoup
from datetime import timedelta, datetime

class BeliApp:

    URL = "https://app.beliapp.com/lists/northeatsbias"
    RUN_TIME =  timedelta(minutes=1) 

    def __init__(self, save_file) -> None:
        self.save_file = save_file
    
    def load_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options= options)
        self.driver.get(self.URL)

    def scoll_end(self):
        start_time = datetime.now()
        time.sleep(5)
        body = self.driver.find_element(By.TAG_NAME, 'body')
        body.click()
        while True:
            time.sleep(random.randint(1, 3))
            body.send_keys(Keys.PAGE_DOWN)
            end_time = datetime.now() - start_time
            if end_time.seconds >= self.RUN_TIME.seconds:
                break

    def extract(self):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
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
            # print(mapped, end= '\n\n')

        df = pd.DataFrame(restraunt_list)
        df.to_csv('beli_file.csv', encoding='utf-8', index=False, doublequote=True)

    def close(self):
        self.driver.close()

if __name__ == '__main__':
    beli_app = BeliApp(save_file = '')
    beli_app.load_driver()
    beli_app.scoll_end()
    beli_app.extract()
    beli_app.close()