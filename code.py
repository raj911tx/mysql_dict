import mysql.connector
from mysql.connector import Error

 
cnt=None
try:
    cnt=mysql.connector.connect(user='root',password="password",
    host="localhost",database="Dictionary")
    if cnt.is_connected():
        print("Connected to the database")
        cursor=cnt.cursor()
        word=input("Enter word: ")
        
        
        query=("SELECT * from Dictionary WHERE Expression='%s'"%word)
        
        cursor.execute(query)
        result=cursor.fetchall()
        if result:
            for data in range(len(result)):
                print(result[data][1])
        else:
            print("Word not Found")
        
    else:
        print("Connection Failed")
except Error as e:
    print(e)
finally:
    if cnt is not None and cnt.is_connected():
        cnt.close()
        print("Connection Closed")








    