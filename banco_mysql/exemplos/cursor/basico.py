import mysql.connector
from mysql.connector.cursor import MySQLCursor

db = mysql.connector.connect(user='root',
                             password='xs9d2m!13N@1p',
                             host='127.0.0.1',
                             database='udemy_neri')

cursor1 = db.cursor()  # 1st method
cursor2 = MySQLCursor(db)   # 2nd method

print(db)

print("cursor1: ", cursor1)
print("cursor2: ", cursor2)

cursor1.close()
cursor2.close()

db.close()
