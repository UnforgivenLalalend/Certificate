import config
import db_query
import mysql.connector 
from mysql.connector import Error

def create_user_table(db):
    using = "USE SM_APP"
    query = "DROP TABLE IF EXISTS `users`"
    create_users_table = """
    CREATE TABLE `users` (
        `user_id` int(11) NOT NULL AUTO_INCREMENT,
        `fio` text NOT NULL,
        `tel` text NOT NULL,
        `mail` text NOT NULL,
        `teacher` text NOT NULL,
        PRIMARY KEY (`user_id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    """
    crsr = db.cursor()
    try:
        crsr.execute(using)
        crsr.execute(query)
        crsr.execute(create_users_table)
        db.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    
    return db