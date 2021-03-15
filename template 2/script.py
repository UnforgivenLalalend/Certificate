import config
import mysql.connector 
from mysql.connector import Error
from connect import create_and_connect
from create_user import create_user_table

db = create_and_connect()

line = input()
if (line == "create_user"):
    print("Let's create some users")
    db = create_user_table(db)

else:
    print("No")

