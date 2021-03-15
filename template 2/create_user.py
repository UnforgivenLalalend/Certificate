import config
import db_query
import mysql.connector 
from mysql.connector import Error

def create_user_table(db):
    using = "USE SM_APP"

    create_users_table = """
    CREATE TABLE IF NOT EXISTS `users` (
    `id` INT AUTO_INCREMENT, 
    `name` VARCHAR(100), 
    `age` INT, 
    `gender` VARCHAR(100), 
    `nationality` VARCHAR(100), 
    PRIMARY KEY (id)
    ) ENGINE = InnoDB;
    """
    crsr = db.cursor()
    try:
        crsr.execute(using)
        crsr.execute(create_users_table)
        db.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    
    return db