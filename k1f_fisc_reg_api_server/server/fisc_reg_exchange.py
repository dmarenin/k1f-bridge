import json
from server.conf import *


def message_to_byte(message):
    message = json.dumps(message)
    message = message.encode('utf-8')
    
    len_message = len(message)
    
    len_message = len_message.to_bytes(OFSSET, byteorder='big', signed=True)

    return len_message + bytes(message)

def send_data(message, sock):
    mes = message_to_byte(message)
    
    sock.send(mes)
    
    data = sock.recv(BUF_SIZE)
    data = data[OFSSET:].decode('utf-8')
    
    res = json.loads(data)
    
    print(res)
    print('')

    return res

def init_oper():
    import socket

    sock = None
    try:
        sock = socket.socket()
        sock.connect(SERVER)
    except Exception as e:
        raise Exception('Socket error ' + str(e))
        
        return None

    return sock

def do_oper(oper, sock, **data):
    res = None

    if not oper in OPER_LIST:
        raise Exception('Operation is not defined' + str(oper))

    session_key = data['session_key']

    d = {'sessionKey': session_key, 'command': oper}

    if oper == 'OpenSession':        
        d['connectionPassword'] = CON_PASSWORD
        d['login'] = LOGIN
        d['password'] = PASSWORD

    elif oper == 'OpenCheck':
        d['checkType'] = CHECK_TYPE
        d['taxSystem'] = TAX_SYSTEM
        d['printDoc'] = PRINT_DOC

    elif oper == 'CloseCheck':
        d['sendCheckTo'] = data['client']
        d['addInfo'] = data['add_info']

        payment = {'cash':data['cash'], 'ecash':data['ecash'], 'prepayment':data['prepayment'], 'credit':data['credit'], 'consideration':data['consideration']}

        d['payment'] = payment        

    elif oper == 'AddGoods':
        d['nomenclatureCode'] = data['code']
        d['productID'] = data['id']
        d['productName'] = data['name']
        d['qty'] = data['qty']
        d['section'] = data['section']
        d['taxCode'] = data['tax_code']
        d['paymentFormCode'] = data['payment_form_code']
        d['price'] = data['price']
        
        extra = {'type': data['extra_type'], 'value': data['extra_value']}

        d['extra'] = extra

    res = send_data(d, sock)

    return res

