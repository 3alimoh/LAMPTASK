#!/usr/bin/python3
import os
import pymysql

# Database connection parameters - update as needed
DB_USER='azureuser'
DB_PSWD='11223344'
DB_HOST='localhost'

db = pymysql.connect(host=DB_HOST, 
										 user=DB_USER, 
										 password=DB_PSWD, 
										 database='mysql', 
										 cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()
cursor.execute("SHOW DATABASES")

print("Content-type: text/html\n")
print("Setup Successful")
