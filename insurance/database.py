import sqlite3
# create database
connection = sqlite3.connect('insurance.db')

query ="""create table project (age integer ,gender integer ,bmi integer , children integer , region varchar(5),smoker integer , health integer,prediction varchar(10))"""

cur=connection.cursor()

cur.execute(query)

print("your databse created")
cur.close()
connection.close()