import config
import db_query
import mysql.connector 
from mysql.connector import Error

def create_and_connect():
    data = config.data

    db = mysql.connector.connect(host = data['host_name'], user = data['user_name'], passwd = data['password'])

    def create_database(db):
        try:
            crsr = db.cursor()  
            crsr.execute(db_query.query)
            print("Database created successfully")
        except Error as e:
            print(f"The error '{e}' occured")

    create_database(db)

    return db