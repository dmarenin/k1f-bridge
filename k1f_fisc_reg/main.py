from fisc_reg_exchange import *
from b_tszh_payment import *
from conf import *
import json


def reg_fisc_doc(**data):
    sock = init_oper()

    if sock is None:
        return None

    res = do_oper('OpenSession', sock, session_key=None)

    if res.get('sessionKey') is None:
        print('session_key is None')
        return None
    
    session_key = res['sessionKey']

    res = do_oper('GetCommonInfo', sock, session_key=session_key)

    res = do_oper('GetRegistrationInfo', sock, session_key=session_key)

    res = do_oper('GetStatus', sock, session_key=session_key)

    #if res['is24Expired'] != True:
    #    res = do_oper('CloseShift', sock, session_key=session_key)
    #    if res['result'] != 0:
    #        print('CloseShift error')
    
    #if res['isOpen'] != True:
    #    res = do_oper('OpenShift', sock, session_key=session_key)
    #    if res['result'] != 0:
    #        print('OpenShift error')

    #ниже закомментировано
    #res = do_oper('OpenCheck', sock, session_key=session_key)
    #if res['result'] != 0:
    #    print('OpenCheck error')

    for x in data['goods']: 
        code = x['code']
        id = x['id']
        name = x['name']

        qty = x['qty']
        price = x['price']

        extra_type = 0
        extra_value = 0

        section = 1
        tax_code = 1
        payment_form_code = 4

        #res = do_oper('AddGoods', sock, session_key=session_key, code=code, id=id, name=name, qty=qty, section=section, tax_code=tax_code, payment_form_code=payment_form_code, price=price, extra_type=extra_type, extra_value=extra_value)
        #if res['result'] != 0:
        #    print('CloseCheck error')

    client = data['client']
    add_info = data['add_info']
    cash = data['cash']
    ecash = data['ecash']
    prepayment = data['prepayment']
    credit = data['credit']
    consideration = data['consideration']

    #res = do_oper('CloseCheck', sock, session_key=session_key, client=client, add_info=add_info, cash=cash, ecash=ecash, prepayment=prepayment, credit=credit, consideration=consideration)
    #if res['result'] != 0:
    #    print('CloseCheck error')
    # fiscalDocNum = res['fiscalDocNum']
    # checkUrl = res['checkUrl']
    # check_num = res['checkNum']
    # shiftNum = res['shiftNum']

    res = do_oper('CloseSession', sock, session_key=session_key)

    check_num = 0

    return check_num

def do_loop():
    result = get_data()

    if result is None:
        return None

    for x in result:
        
        print(x)
        
        client = 'test@mail.ru'
        add_info = 'test'
        cash = '100'
        ecash = 0
        prepayment = 0
        credit = 0
        consideration = 0

        goods = []

        goods.append({'code': '', 'id': '', 'name': 'тест', 'qty':1, 'price':1})

        res_fisc = reg_fisc_doc(goods=goods, client=client, add_info=add_info, cash=cash, ecash=ecash, prepayment=prepayment, credit=credit, consideration=consideration)
        
        x['res_fisc'] = res_fisc

        #if not res_fisc is None:
        #    res_set = set_result(x)

            #if res_set is None:
                #res_str = json.dumps(x)
                
                #with open('error.txt', 'a') as file:
                    #file.write(res_str)

    return None


if __name__ == "__main__":
    import time
    
    while True:
        do_loop()

        time.sleep(T_SLEEP)

