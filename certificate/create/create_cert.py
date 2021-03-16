import config
import db_query
import mysql.connector
from mysql.connector import Error


def create_cert_table(db):
    using = "USE SM_APP"
    query = "DROP TABLE IF EXISTS `cert`"
    create_cert_table = """
    CREATE TABLE `cert` (
        `reg_no` text NOT NULL,
        `cert_user_id` int(11) NOT NULL,
        `cert_type_id` int(11) NOT NULL,
        `cert_comp_id` int(11) NOT NULL,
        `cert_exam_id` int(11) NOT NULL,
        `result` int(11) NOT NULL,
        `cert_id` int(11) NOT NULL AUTO_INCREMENT,
        PRIMARY KEY (`cert_id`),
        FOREIGN KEY (cert_user_id) REFERENCES users(user_id) ON DELETE RESTRICT,
        FOREIGN KEY (cert_comp_id) REFERENCES company(comp_id) ON DELETE RESTRICT,
        FOREIGN KEY (cert_exam_id) REFERENCES exams(exam_id) ON DELETE RESTRICT,
        FOREIGN KEY (cert_type_id) REFERENCES user_type(type_id) ON DELETE RESTRICT
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    """
    crsr = db.cursor()
    try:
        crsr.execute(using)
        crsr.execute(query)
        crsr.execute(create_cert_table)
        db.commit()
        print("Cert_query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

    return db
