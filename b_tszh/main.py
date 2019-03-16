import pymysql.cursors
import time
import requests
import json
import sqlite3
from sqlite3 import Error
from datetime import datetime, date

from secret import *


T_SLEEP = 60

API_SERVER = '192.168.1.99'
API_PORT = 8081
API_MAKE_PAYMENT = 'make_payment'

DB_LOCAL = 'operations.db'


def get_data_source(last_id):
    try:
        connection = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DB, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    except Exception as e:
        print(e)
        return None

    cursor = connection.cursor()
    
    query_text = f"SELECT b_tszh_payment.*, b_user.* FROM b_tszh_payment LEFT JOIN b_user ON b_tszh_payment.USER_ID = b_user.ID WHERE b_tszh_payment.ID > {last_id}"
    
    try:
        res = cursor.execute(query_text, )
    except Exception as e:
        print(e)
        return None

    result = cursor.fetchall()

    cursor = None

    connection.close()

    return result

def get_last_id():
    try:
        connection = sqlite3.connect(DB_LOCAL)
    except Error as e:
        print(e)
        return None

    cursor = connection.cursor()
    
    query_text = f"SELECT last_id FROM operations ORDER BY last_id DESC LIMIT 1"
    
    try:
        res = cursor.execute(query_text, )
    except Exception as e:
        print(e)
        return None

    result = cursor.fetchall()

    cursor = None

    connection.close()

    if len(result) == 0:
        return 0
    
    return result[0][0]

def set_result(res, x):
    try:
        connection = sqlite3.connect(DB_LOCAL)
    except Error as e:
        print(e)
        return None

    source_data = json.dumps(res, default=json_serial)
    fisc_reg_data = json.dumps(x, default=json_serial)
    last_id = x['ID']
    fisc_reg_doc = res['fiscalDocNum']

    cursor = connection.cursor()
    
    rows = [(source_data, fisc_reg_data, last_id, fisc_reg_doc)]

    cursor.executemany('INSERT INTO operations values (?,?,?,?)', rows)
   
    connection.commit()

    cursor = None

    connection.close()

    return None

def make_payment(client, summ, add_info):
    data = {}
    
    data['client'] = client
    data['add_info'] = add_info
    data['cash'] = 0
    data['ecash'] = summ
    data['prepayment'] = 0
    data['credit'] = 0
    data['consideration'] = 0
    
    data['goods'] = []
    
    row_goods = {}
    
    row_goods['code'] = '001'
    row_goods['id'] = '001'
    row_goods['name'] = add_info
    row_goods['qty'] = 1
    row_goods['price'] = summ
    row_goods['extra_type'] = 0
    row_goods['extra_value'] = 0
    row_goods['section'] = 1
    row_goods['tax_code'] = 1
    row_goods['payment_form_code'] = 0
    
    data['goods'].append(row_goods)
    
    data = json.dumps(data, default=json_serial)
    
    r = requests.post(f"""http://{API_SERVER}:{API_PORT}/{API_MAKE_PAYMENT}""", data=data)
    
    print('API_SERVER response:')
    print(r)
    print(r.text)

    if r.status_code == 200:
        res = json.loads(r.text)
        return res

    return None

def do_loop():
    print('')
    print(datetime.now())
    
    last_id = get_last_id()

    if last_id is None:
        return None

    result = get_data_source(last_id)

    if result is None:
        return None
        
    print('new records ' + str(len(result)))
    
    if len(result) == 0:
        return None

    for x in result:
        print(x)
        res = make_payment(x['EMAIL'], x['SUMM_PAYED'], x['C_ADDRESS'])
        
        if not res is None:
            set_result(res, x)

    pass

def json_serial(obj):
    from datetime import datetime, date
    import decimal
    if isinstance(obj, (datetime, date)):
       return obj.isoformat()

    if isinstance(obj, decimal.Decimal):
       return float(obj)
    pass 


while True:
    do_loop()

    time.sleep(T_SLEEP)

