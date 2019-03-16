import json


OFSSET = 4


RESPONSE = {}

RESPONSE['OpenSession'] = """{"result": 0,
 "description": "Успешно завершено",
 "sessionKey": "CAC1A797-6A48-474A-A08E-72A8CD3AEFE2",
 "protocolVer": "1.0"}"""

RESPONSE['CloseSession'] = """{"result": 0,
 "description": "Успешно завершено"}"""

RESPONSE['GetCommonInfo'] = """{"result": 0,
 "description": "Успешно завершено",
 "model": "Название модели ККТ",
 "kktNum": "123456789012",
 "fnNum": "9908176526",
 "ffdFnVer": "1.0.5",
 "ffdKktVer": "1.0",
 "mac": "45:F2:0D:73:37:00",
 "programVer": "3.1",
 "programDate": "2016-09-04",
 "protocolVer": "3.0",
 "dateTime": "2016-10-01T09:15:43",
 "crc": "C5AD",
 "cpl": [21, 10],
 "dpl": 240,
 "maxGoodsSum": 999999999,
 "maxCheckSum": 999999999,
 "maxGoodsQty": 99}"""

RESPONSE['GetRegistrationInfo'] = """{"isRegistered": true,
 "registrationInfo": {
 "dateTime": "2016-10-03T12:35:27",
 "owner": {
 "inn": "3890473625"
 },
 "kkt": {
 "regNum": "123456789012",
 "mode": {
 "encryptData": true,
 "offline": false,
 "forService": true,
 "ASBSO": false
 }
 },
 "ofd": {
 "inn": "4029017981",
 "url": "ofd.astralnalog.ru",
 "port": 7779
 },
 "taxSystem": [0, 1, 3],
 "reason": 2}}"""

RESPONSE['GetDateTime'] = """{"result": 0,
 "description": "Успешно завершено",
 "dateTime": "2016-10-01T09:15:43"}"""

RESPONSE['GetStatus'] = """{"result": 0,
 "description": "Успешно завершено",
 "dateTime": "2016-10-01T09:15:43",
 "shiftInfo": {
 "isOpen": true,
 "is24Expired": false,
 "num": 17,
 "lastOpen": "2016-09-30T08:10:15",
 "cash": 500680,
 "check0": {
 "qty": 15,
 "sum": 500680
 },
 "check1": {
 "qty": 0,
 "sum": 0
 },
 "check2": {
 "qty": 0,
 "sum": 0
 },
 "check3": {
 "qty": 0,
 "sum": 0
 },
 "check4": {
 "qty": 0,
 "sum": 0
 },
 "check5": {
 "qty": 0,
 "sum": 0
 },
 "bring": {
 "qty": 0,
 "sum": 0
 },
 "withdraw": {
 "qty": 0,
 "sum": 0
 }
 },
 "checkInfo": {
 "isOpen": true,
 "num": 4,
 "goodsQty": 8,
 "sum": 12534
 },
 "fnInfo": {
 "status": 1,
 "lastDoc": {
 "num": 60,
 "dateTime": "2016-10-01T09:10:24"
 },
 "unsignedDocs": {
 "qty": 1,
 "firstNum": 61,
 "firstDateTime": "2016-10-01T09:13:37"}}}"""

RESPONSE['OpenShift'] = """{"result": 0,
 "description": "Успешно завершено",
 "shiftNum": 125,
 "fiscalDocNum": 1153,
 "fiscalSign": "1189046352"}"""

RESPONSE['CloseShift'] = """{"result": 0,
 "description": "Успешно завершено",
 "shiftNum": 125,
 "fiscalDocNum": 1153,
 "fiscalSign": "1189046352"}"""

RESPONSE['OpenCheck'] = """{"result": 0,
 "description": "Успешно завершено",
 "shiftNum": 125,
 "checkNum": 18}"""

RESPONSE['CloseCheck'] = """{"result": 0,
 "description": "Успешно завершено",
 "shiftNum": 125,
 "checkNum": 18,
 "fiscalDocNum": 1173,
 "fiscalSign": "1189046352",
 "checkUrl": "nalog.ru",
 "changeSum": 4000}"""

RESPONSE['AddGoods'] = """{"result": 0,
 "description": "Успешно завершено",
 "shiftNum": 235,
 "checkNum": 18,
 "goodsNum": 2,
 "taxSum": 0,
 "extraSum": -116,
 "goodsSum": 3134,
 "checkSum": 5392}"""

RESPONSE['PrintReport'] = """{"result": 0,
 "description": "Успешно завершено"}"""

RESPONSE['ResetCheck'] = """{"result": 0,
 "description": "Успешно завершено"}"""


def do_command(data):
    data = data[OFSSET:].decode('utf-8')
    
    data = data.rstrip('\x00')

    res = json.loads(data)

    print('->')
            
    print(res)

    if res.get('command') is None:
        return b''

    message = RESPONSE.get(res['command'])

    if message is None:
        return b''
     
    print('<-') 
    
    print(message)

    message = message.encode('utf-8')
    
    len_message = len(message)
    
    len_message = len_message.to_bytes(OFSSET, byteorder='big', signed=True)

    return len_message + bytes(message)


