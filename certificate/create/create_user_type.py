import config
import db_query
import mysql.connector
from mysql.connector import Error


def create_user_type_table(db):
    using = "USE SM_APP"
    query = "DROP TABLE IF EXISTS `user_type`"
    create_user_type_table = """
    CREATE TABLE `user_type` (
        `type_id` int(11) NOT NULL AUTO_INCREMENT,
        `name` text NOT NULL,
        PRIMARY KEY (`type_id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    """

    crsr = db.cursor()
    try:
        crsr.execute(using)
        crsr.execute(query)
        crsr.execute(create_user_type_table)
        db.commit()
        print("User_type_query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

    return db
