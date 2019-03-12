import pymysql.cursors
from conf import *

def get_cursor():
    try:
        connection = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DB, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    except Exception as e:
        print(e)
        return None

    cursor = connection.cursor()

    return cursor

def get_data():
    cursor = get_cursor()
    if cursor is None :
        return None

    sql = "SELECT * FROM b_tszh_payment" #WHERE TODO

    res = cursor.execute(sql, )

    result = cursor.fetchall()

    cursor = None

    return result

def set_result(res, ):
    cursor = get_cursor()
    if cursor is None :
        return None

    cursor = connection.cursor()

    sql += """INSERT INTO `op` (`email`, `password`) VALUES (%s, %s)""" #TODO

    res = cursor.execute(sql, )

    result = cursor.fetchall()

    cursor = None

    return result

