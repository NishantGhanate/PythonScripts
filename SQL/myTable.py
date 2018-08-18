# importing module
import sqlite3
import os

scriptDir = os.path.dirname(os.path.realpath(__file__))
# connecting to the database 
connection = sqlite3.connect(scriptDir + os.path.sep + "myTable.db")

# cursor 
crsr = connection.cursor()

# SQL command to create a table in the database
sql_command = """ CREATE TABLE Student (
    ID INTEGER PRIMARY KEY  AUTOINCREMENT, 
    FirstName varchar(255) NOT NULL,
    LastName varchar(255),
    Age int,
    Roll_no int,
    Address varchar(255)
    
); """
 
# execute the statement
crsr.execute(sql_command)
 
# SQL command to insert the data in the table
 
sql_command = """INSERT INTO Student VALUES (NULL,"Nishant", "Ghanate", 22, 71, "Byculla");"""
crsr.execute(sql_command)

# another SQL command to insert the data in the table
sql_command = """INSERT INTO Student VALUES (NULL,"Rinisha", "Burriwar",20, 13,"Byculla");"""
crsr.execute(sql_command)

sql_command = """INSERT INTO Student VALUES (NULL,"Vikas", "Rajbhar", 21, 40,"Byculla");"""
crsr.execute(sql_command)

sql_command = """INSERT INTO Student VALUES (NULL,"Pankaj", "Chaurasia",21, 65,"Chowpatty");"""
crsr.execute(sql_command)

sql_command = """INSERT INTO Student VALUES (NULL,"Rishabh", "Sutravey",23, 70,"Mumbai central");"""
crsr.execute(sql_command)

sql_command = """INSERT INTO Student VALUES (NULL,"Sourabh", "Sutravey",20, 53,"Mumbai central");"""
crsr.execute(sql_command)

sql_command = """INSERT INTO Student VALUES (NULL,"Abhishek", "Gupta",21, 18,"Chinchpokli");"""
crsr.execute(sql_command)

sql_command = """INSERT INTO Student VALUES (NULL,"Shubham", "Bonkar",21, 47,"Chinchpokli");"""
crsr.execute(sql_command)

# To save the changes in the files. Never skip this. 
# If we skip this, nothing will be saved in the database.
connection.commit()
 
# close the connection
connection.close()