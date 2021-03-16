import config
import db_query
import mysql.connector
from mysql.connector import Error


def create_exams_table(db):
    using = "USE SM_APP"
    query = "DROP TABLE IF EXISTS `exams`"
    create_exams_table = """
    CREATE TABLE `exams` (
        `exam_id` int(11) NOT NULL AUTO_INCREMENT,
        `date` text NOT NULL,
        `name` text NOT NULL,
        `type` text NOT NULL,
        PRIMARY KEY (`exam_id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    """
    crsr = db.cursor()
    try:
        crsr.execute(using)
        crsr.execute(query)
        crsr.execute(create_exams_table)
        db.commit()
        print("Exams_query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

    return db
