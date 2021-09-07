import mysql.connector

__cnx = None

def sql_connection():
    global __cnx
    if not __cnx:
        __cnx = mysql.connector.connect(user='root', password='root',
                                    host='127.0.0.1',
                                    database='blog')
    return __cnx