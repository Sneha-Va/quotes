import requests
import json
import mysql.connector
try:

    mydb = mysql.connector.connect(host = 'localhost', user = 'root',password = '',database='quotesdb')

except mysql.connector.Error as e:

    print("Connector error ",e)

mycursor = mydb.cursor()

data = requests.get("https://dummyjson.com/quotes").text

data_info = json.loads(data)

for i in data_info["quotes"]:

   sql = "INSERT INTO `quotes`(`quote`, `author`) VALUES ('"+i['quote']+"','"+i['author']+"')"

mycursor.execute(sql)

mydb.commit()

print('Inserted the value succesfully')