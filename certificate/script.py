import config
import mysql.connector
from mysql.connector import Error
from connect import create_and_connect
# """""""""""""""""""""""""""""""""""""""""""""""

from create.create_user import create_user_table
from create.create_exams import create_exams_table
from create.create_company import create_company_table
from create.create_user_type import create_user_type_table
from create.create_cert import create_cert_table

# """""""""""""""""""""""""""""""""""""""""""""""
from insert_user import insert_user_column

db = create_and_connect()

db = create_user_table(db)
db = create_exams_table(db)
db = create_company_table(db)
db = create_user_type_table(db)
db = create_cert_table(db)


line = input()

if (line == "Insert user"):
    user_fio, user_tel, user_mail, user_teacher = input().split()
    insert_user_column(db, user_fio, user_tel, user_mail, user_teacher)
else:
    print("NO")
