# importing module
import sqlite3
import os

scriptDir = os.path.dirname(os.path.realpath(__file__))
# connecting to the database 
connection = sqlite3.connect(scriptDir + os.path.sep + "myTable.db")

# cursor 
crsr = connection.cursor()

sql = "Select DISTINCT Age FROM Student "
ans = crsr.execute(sql) 
print( list(ans) )

sql = "Select COUNT(DISTINCT Age) FROM Student "
ans = crsr.execute(sql) 
print( list(ans) )

sql = "Select * FROM Student WHERE Address = 'Byculla' "
ans = crsr.execute(sql) 
print( list(ans) )

sql = "Select * FROM Student WHERE Address = 'Byculla' AND Age = 20"
ans = crsr.execute(sql) 
print( list(ans) )

sql = "Select * FROM Student WHERE NOT Address = 'Byculla' AND Age = 20"
ans = crsr.execute(sql) 
print( list(ans) )

