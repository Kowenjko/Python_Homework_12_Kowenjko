import psycopg2
from psycopg2 import Error
from settings import *

try:
    connection = psycopg2.connect(user=USER,
                                  password=PASSWORD,
                                  host=HOST,
                                  port=PORT,
                                  database='shop_db')
    cursor = connection.cursor()
# -----------------Таблиці------------------------------------
    # login = """CREATE TABLE login
    #                       (ID SERIAL  PRIMARY KEY,
    #                        login      varchar(50)    NOT NULL,
    #                        password   varchar(50)    NOT NULL
    #                        ); """
    # cursor.execute(login)
    # connection.commit()
# ----------------------------------------------------------------
    insert_login = """ INSERT INTO  login (ID, login, password)
                                     VALUES
                                     (1, 'admin','admin'),
                                     (2, 'roman','1234'),
                                     (3, 'logo','2564'),
                                     (4, 'kolis','457'),
                                     (5, 'lims','1236')                                    

                    """
    cursor.execute(insert_login)
    connection.commit()
# ----------------------------------------------------------------

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
