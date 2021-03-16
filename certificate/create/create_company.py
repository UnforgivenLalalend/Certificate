import config
import db_query
import mysql.connector
from mysql.connector import Error


def create_company_table(db):
    using = "USE SM_APP"
    query = "DROP TABLE IF EXISTS `company`"
    create_company_table = """
    CREATE TABLE `company` (
        `comp_id` int(11) NOT NULL AUTO_INCREMENT,
        `name` text NOT NULL,
        PRIMARY KEY (`comp_id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    """

    crsr = db.cursor()
    try:
        crsr.execute(using)
        crsr.execute(query)
        crsr.execute(create_company_table)
        db.commit()
        print("Company_query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

    return db
