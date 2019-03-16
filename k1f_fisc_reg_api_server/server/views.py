from flask import render_template, request, jsonify
import server.fisc_reg_exchange as fisc_reg
from server.conf import *
from server import app
import json


HEADERS = {"Content-type": "application/json",
           "Access-Control-Allow-Origin": "*", 
           "Access-Control-Expose-Headers": "Access-Control-Allow-Origin",
           "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept"}

@app.route('/')
@app.route('/index')
def index():
    return """it's k1-f server api""", 200, HEADERS


@app.errorhandler(Exception)
def handle_invalid_usage(error):
    str_error = "Exception: %s" % error

    print(str_error)

    response = jsonify(str_error)
    response.status_code = 500
    response.content_type = 'text/plain; charset=utf-8'
    
    return response

   
@app.route('/get_common_info', methods=['GET'])
def get_common_info():
    sock = fisc_reg.init_oper()

    if sock is None:
        raise Exception('Нет связи')

    res = fisc_reg.do_oper('OpenSession', sock, session_key=None)

    if res.get('sessionKey') is None:
        raise Exception('session_key is None')
    
    session_key = res['sessionKey']

    res = fisc_reg.do_oper('GetCommonInfo', sock, session_key=session_key)

    res = json.dumps(res, default=json_serial)

    fisc_reg.do_oper('CloseSession', sock, session_key=session_key)

    return res, 200, HEADERS

@app.route('/get_registration_info', methods=['GET'])
def get_registration_info():
    sock = fisc_reg.init_oper()

    if sock is None:
        raise Exception('Нет связи')

    res = fisc_reg.do_oper('OpenSession', sock, session_key=None)

    if res.get('sessionKey') is None:
        raise Exception('session_key is None')
    
    session_key = res['sessionKey']

    res = fisc_reg.do_oper('GetRegistrationInfo', sock, session_key=session_key)

    res = json.dumps(res, default=json_serial)
        
    fisc_reg.do_oper('CloseSession', sock, session_key=session_key)

    return res, 200, HEADERS

@app.route('/get_status', methods=['GET'])
def get_status():
    sock = fisc_reg.init_oper()

    if sock is None:
        raise Exception('Нет связи')

    res = fisc_reg.do_oper('OpenSession', sock, session_key=None)

    if res.get('sessionKey') is None:
        raise Exception('session_key is None')
    
    session_key = res['sessionKey']

    res = fisc_reg.do_oper('GetStatus', sock, session_key=session_key)

    res = json.dumps(res, default=json_serial)
        
    fisc_reg.do_oper('CloseSession', sock, session_key=session_key)
    
    return res, 200, HEADERS

@app.route('/open_shift', methods=['GET'])
def open_shift():
    sock = fisc_reg.init_oper()

    if sock is None:
        raise Exception('Нет связи')

    res = fisc_reg.do_oper('OpenSession', sock, session_key=None)

    if res.get('sessionKey') is None:
        raise Exception('session_key is None')
    
    session_key = res['sessionKey']

    res = fisc_reg.do_oper('OpenShift', sock, session_key=session_key)

    res = json.dumps(res, default=json_serial)
        
    fisc_reg.do_oper('CloseSession', sock, session_key=session_key)

    return res, 200, HEADERS

@app.route('/close_shift', methods=['GET'])
def close_shift():
    sock = fisc_reg.init_oper()

    if sock is None:
        raise Exception('Нет связи')

    res = fisc_reg.do_oper('OpenSession', sock, session_key=None)

    if res.get('sessionKey') is None:
        raise Exception('session_key is None')
    
    session_key = res['sessionKey']

    res = fisc_reg.do_oper('CloseShift', sock, session_key=session_key)

    res = json.dumps(res, default=json_serial)
        
    fisc_reg.do_oper('CloseSession', sock, session_key=session_key)
    
    return res, 200, HEADERS

@app.route('/make_payment', methods=['POST'])
def make_payment():
    body = request.data.decode('utf-8-sig')
    
    data = json.loads(body)

    sock = fisc_reg.init_oper()

    if sock is None:
        raise Exception('Нет связи')

    res = fisc_reg.do_oper('OpenSession', sock, session_key=None)

    if res.get('sessionKey') is None:
        raise Exception('session_key is None')
    
    session_key = res['sessionKey']

    res_status = fisc_reg.do_oper('GetStatus', sock, session_key=session_key)

    if res_status['shiftInfo']['is24Expired'] == True:
        res = fisc_reg.do_oper('CloseShift', sock, session_key=session_key)
        if res['result'] != 0:
            raise Exception('CloseShift error: ' + str(res))
    
    if res_status['shiftInfo']['isOpen'] != True:
        res = fisc_reg.do_oper('OpenShift', sock, session_key=session_key)
        if res['result'] != 0:
            raise Exception('OpenShift error: ' + str(res))

    res = fisc_reg.do_oper('OpenCheck', sock, session_key=session_key)
    if res['result'] != 0:
        raise Exception('OpenCheck error: ' + str(res))

    for x in data['goods']: 
        code = x['code']
        id = x['id']
        name = x['name']

        qty = x['qty']
        price = x['price']

        extra_type = x['extra_type']
        extra_value = x['extra_value']

        section = x['section']
        tax_code = x['tax_code']
        payment_form_code = x['payment_form_code']

        res = fisc_reg.do_oper('AddGoods', sock, session_key=session_key, code=code, id=id, name=name, qty=qty, section=section, tax_code=tax_code, payment_form_code=payment_form_code, price=price, extra_type=extra_type, extra_value=extra_value)
        
        if res['result'] != 0:
            raise Exception('AddGoods error: ' + str(res))

    client = data['client']
    add_info = data['add_info']
    cash = data['cash']
    ecash = data['ecash']
    prepayment = data['prepayment']
    credit = data['credit']
    consideration = data['consideration']

    res = fisc_reg.do_oper('CloseCheck', sock, session_key=session_key, client=client, add_info=add_info, cash=cash, ecash=ecash, prepayment=prepayment, credit=credit, consideration=consideration)

    if res['result'] != 0:
        raise Exception('CloseCheck error: ' + str(res))

    res = json.dumps(res, default=json_serial)
        
    fisc_reg.do_oper('CloseSession', sock, session_key=session_key)

    return res, 200, HEADERS


def json_serial(obj):
    from datetime import datetime, date
    import decimal
    if isinstance(obj, (datetime, date)):
       return obj.isoformat()

    if isinstance(obj, decimal.Decimal):
       return float(obj)
    pass

