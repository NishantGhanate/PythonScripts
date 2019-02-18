# Json to Database for app api

import json
import os
import sqlite3
import mysql.connector

folderPath = r'H:\Github\PythonScripts\SQL\Channels\json'
scriptDir = os.path.dirname(os.path.realpath(__file__))
# connecting to the database 
connection = sqlite3.connect(scriptDir + os.path.sep + "packages.db")
crsr = connection.cursor()

def putMemoryDb(path):
    with open(path) as f:
        channels_json = json.loads(f.read())
        fileName =  path.split('.')
        fileName = fileName[0].split('\\')
        fileName = fileName[-1]
        print(fileName)

    # SQL command to create a table in the database
    sql_command = """ CREATE TABLE """+fileName+""" (
        ID INTEGER PRIMARY KEY  AUTOINCREMENT, 
        channel_name varchar(255) ,
        channel_genre varchar(255),
        channel_language varchar(255),
        channel_price varchar(255),
        channel_quality varchar(255)
    ); """
    
    # execute the statement
    crsr.execute(sql_command)
    sql = "INSERT INTO "+ fileName +" (channel_name,channel_genre) VALUES (?,?)"
    for c in channels_json:
        crsr.execute(sql, (c['channel_name'] , c['channel_genre']))   
    connection.commit()


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="channels_packages"
)

mycursor = mydb.cursor()

def putLocalHostDb(path):
    with open(path) as f:
        channels_json = json.loads(f.read())
        fileName =  path.split('.')
        fileName = fileName[0].split('\\')
        fileName = fileName[-1]
        print(fileName)
    mycursor.execute("CREATE TABLE "+fileName+" (id INT AUTO_INCREMENT PRIMARY KEY, channel_name VARCHAR(255), channel_genre VARCHAR(255) ,  channel_language VARCHAR(255) ,  channel_quality VARCHAR(255) , channel_price VARCHAR(255))")
    sql = "INSERT INTO "+fileName+" (channel_name, channel_genre) VALUES (%s, %s)"
    for c in channels_json:
        val = (c['channel_name'] , c['channel_genre'])
        mycursor.execute(sql, val)
        mydb.commit()


for f in os.scandir(folderPath):
    # print(f.path)
    # putMemoryDb(f.path)
    putLocalHostDb(f.path)

# close the connection
connection.close()