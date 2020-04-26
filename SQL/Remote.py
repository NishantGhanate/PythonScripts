from mysql.connector import connection
import mysql.connector


def getDb():
    try:
        cnx = connection.MySQLConnection(user='root', password='toot',
                                host='127.0.0.1',
                                database='dummby')
        cursor = cnx.cursor()   
        cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'dummy'")
        colnames = cursor.fetchall()
        colnames = [c[0] for c in colnames]
        cursor.execute("SELECT * from dummy")
        result = cursor.fetchall()
        print(result) 
        print('\nData type = {}'.format(type(result))) 
        print('\nLength = {}\n'.format(len(result)))
        cnx.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("\nSomething is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("\nDatabase does not exist")
        else:
            print(err)


getDb()
