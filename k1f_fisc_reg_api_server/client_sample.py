import requests
import json


server = '10.0.0.55'
port = 8081

method = 'get_common_info'
r = requests.get(f"""http://{server}:{port}/{method}""")
print(r)
print(r.text)

method = 'get_registration_info'
r = requests.get(f"""http://{server}:{port}/{method}""")
print(r)
print(r.text)

method = 'get_status'
r = requests.get(f"""http://{server}:{port}/{method}""")
print(r)
print(r.text)

#method = 'open_shift'
#r = requests.get(f"""http://{server}:{port}/{method}""")  
#print(r)
#print(r.text)

#method = 'close_shift'
#r = requests.get(f"""http://{server}:{port}/{method}""")
#print(r)
#print(r.text)

#data = {}

#data['client'] = 'test@mail.ru'
#data['add_info'] = 'оплата по заказу номер 100'
#data['cash'] = 0
#data['ecash'] = 100
#data['prepayment'] = 0
#data['credit'] = 0
#data['consideration'] = 0

#data['goods'] = []

#row_goods = {}

#row_goods['code'] = '001'
#row_goods['id'] = '001'
#row_goods['name'] = 'услуги'
#row_goods['qty'] = 1
#row_goods['price'] = 100

#row_goods['extra_type'] = 0
#row_goods['extra_value'] = 0

#row_goods['section'] = 1
#row_goods['tax_code'] = 1
#row_goods['payment_form_code'] = 0

#data['goods'].append(row_goods)

#data = json.dumps(data)
#method = 'make_payment'
#r = requests.post(f"""http://{server}:{port}/{method}""", data=data)
#print(r)
#print(r.text)

p = input()

