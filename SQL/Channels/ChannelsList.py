import json
import os
import mysql.connector

channelsList = r"H:\Github\PythonScripts\SQL\Channels\channels.json"
packagesList = r"H:\Github\PythonScripts\SQL\Channels\packages.json"

# Go to your local pho admin create a local Database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="packages"
    )

with open(channelsList) as f:
    channels_json = json.loads(f.read())
    
    # mycursor = mydb.cursor()
    # mycursor.execute("CREATE TABLE channels_list (id INT AUTO_INCREMENT PRIMARY KEY, channel_icon  VARCHAR(255), channel_name VARCHAR(255),  channel_price VARCHAR(255, channel_broadcaster VARCHAR(255), channel_genre VARCHAR(255) ,  channel_language VARCHAR(255) , channel_quality  VARCHAR(255) )")
    # sql = "INSERT INTO channels_list (channel_icon , channel_name, channel_price , channel_broadcaster,channel_genre,channel_language ,channel_quality) VALUES (%s, %s,%s, %s,%s, %s,%s)"
    # for c in channels_json:
    #     val = (c['channel_icon'],c['channel_name'] , c['channel_price'],c['channel_broadcaster'],c['channel_genre'],c['channel_language'],c['channel_quality'])
    #     mycursor.execute(sql, val)
    #     mydb.commit()

# with open(packagesList) as f:
#     packagesList_json = json.loads(f.read())
#     mycursor = mydb.cursor()

#     mycursor.execute("CREATE TABLE packages_list (id INT AUTO_INCREMENT PRIMARY KEY, package_name VARCHAR(255), channel_count VARCHAR(255), package_price VARCHAR(255) ) ");
#     sql = "INSERT INTO packages_list (package_name , channel_count, package_price) VALUES (%s, %s,%s)"
#     for p in packagesList_json:
#         val = (p['package_name'],p['channel_count'] , p['package_price'])
#         mycursor.execute(sql, val)
#         mydb.commit()