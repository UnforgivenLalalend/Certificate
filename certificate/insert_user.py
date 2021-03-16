import config
import db_query
import mysql.connector
from mysql.connector import Error


def insert_user_column(db, user_fio, user_tel, user_mail, user_teacher):
    using = "USE SM_APP"
    insert_user_query = f"""
    INSERT INTO 
        users (fio, tel, mail, teacher)
    VALUES
        (%s, %s, %s, %s)
    """
    args = (user_fio, user_mail, user_tel, user_teacher)
    try:
        crsr = db.cursor()
        crsr.execute(using)
        crsr.execute(insert_user_query, args)
        print("User insertion successful")
    except Error as e:
        print(f"The error {e} occured")

    return db
