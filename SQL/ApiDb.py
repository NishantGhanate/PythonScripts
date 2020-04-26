import requests 
import sqlite3 
import json 
import csv 
import sys
import os 
import random 

scriptDir = os.path.dirname(os.path.realpath(__file__))  # current working Folder/Directory 
dbFilepAth = scriptDir + os.path.sep + "api.db"

connection = sqlite3.connect(dbFilepAth)
crsr = connection.cursor()
sql_command = """ CREATE TABLE IF NOT EXISTS apitest (
                id INTEGER PRIMARY KEY  AUTOINCREMENT, 
                userId varchar(255),
                title varchar(255) ,
                completed varchar(255)
                ); """
                # execute the statement
crsr.execute(sql_command)
connection.commit()


n = random.randint(1, 50)
url = "https://jsonplaceholder.typicode.com/todos/{}".format(n)
x = requests.get(url)
if x.status_code == 200 :
    data = json.loads(x.text)
    print(data)
    del data['id']
    columns = ', '.join(data.keys())
    placeholders = ', '.join('?' * len(data))
    sql = 'INSERT INTO apitest ({}) VALUES ({})'.format(columns, placeholders)
    print(sql)
    values = tuple(data.values())
    crsr.execute(sql,values)
    connection.commit()
