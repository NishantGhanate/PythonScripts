# importing module
import sqlite3
import os

scriptDir = os.path.dirname(os.path.realpath(__file__))
# connecting to the database 
connection = sqlite3.connect(scriptDir + os.path.sep + "myTable.db")

# cursor 
crsr = connection.cursor()

# execute the command to fetch all the data from the table emp
crsr.execute("SELECT * FROM Student") 
 
# store all the fetched data in the ans variable
ans = crsr.fetchall() 
 
# loop to print all the data
for i in ans:
    print(i)


# sql = "Update Student SET Address = 'Agripada' WHERE ID = 8"
# ans = crsr.execute(sql) 
# connection.commit()
# print(ans)

