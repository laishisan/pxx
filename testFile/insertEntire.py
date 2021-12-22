import json
import common.re_token
import requests
import testFile.getToken
import testFile.getConfig

hosts = testFile.getConfig.read_ini("API", "host")
import time


class Entire():
    def insert_Entire(self):
        token = common.re_token.read_token()
        Url = hosts + '/web/request/entire'
        data = {"isMatchPrice": 0, "paymentType": 20, "estimateArriveTime": "2021-12-11T23:00:00",
                "estimateCompleteTime": "2021-12-13T06:00:00", "pointList": [
                {"pointAddress": "广东省深圳市南山区学府路前海凯御(深圳市南山区)", "pointCode": 440305, "pointLongitude": "113.911543",
                 "pointLatitude": "22.527911", "contacts": "那看看", "contactsPhone": "13896321234", "addressName": None,
                 "arriveTime": "2021-12-11T23:00:00", "sendTime": "2021-12-12T17:00:00", "pointSort": 0,
                 "pointType": 10},
                {"pointAddress": "广东省广州市黄埔区广州统一企业有限公司(康南路)", "pointCode": 440112, "pointLongitude": "113.556389",
                 "pointLatitude": "23.093617", "contacts": "刘大夫", "contactsPhone": "15123566547", "addressName": None,
                 "arriveTime": "2021-12-13T06:00:00", "pointSort": 1, "pointType": 20}], "cargoRequestList": [
                {"cargoGoodsList": [], "cargoPointList": [
                    {"pointAddress": "广东省深圳市南山区学府路前海凯御(深圳市南山区)", "pointCode": 440305, "pointLongitude": "113.911543",
                     "pointLatitude": "22.527911", "contacts": "那看看", "contactsPhone": "13896321234",
                     "addressName": None, "arriveTime": "2021-12-11T23:00:00", "sendTime": "2021-12-12T17:00:00",
                     "pointSort": 0, "pointType": 10, "operationType": 1},
                    {"pointAddress": "广东省广州市黄埔区广州统一企业有限公司(康南路)", "pointCode": 440112, "pointLongitude": "113.556389",
                     "pointLatitude": "23.093617", "contacts": "刘大夫", "contactsPhone": "15123566547",
                     "addressName": None, "arriveTime": "2021-12-13T06:00:00", "pointSort": 1, "pointType": 20,
                     "operationType": 2}]}],
                "pointOperationList": [{"pointSort": 0, "operationType": 1}, {"pointSort": 1, "operationType": 2}],
                "costCent": 1200, "priceMode": "4", "priceValue": 1200,
                "attachList": [{"attachCatalog": "20", "attachGroup": "20", "attachKey": None, "attachValue": None}],
                "receipt": {"receiptCode": None, "receiptAddress": None, "receipter": None, "receipterPhone": None,
                            "mailBack": 0, "uploadPhoto": 0}, "assignList": [
                {"assignType": 1, "platformUndertakeDuty": 0, "driverPhone": "13537700044", "driverName": "张冬冬2",
                 "driverId": "202130011014", "carrierDriverId": "2357957", "vehicleId": None,
                 "carrierVehicleId": "6358896", "vehicleNumber": "桂M2D001", "vehiclePlateColorCode": "1"}],
                "isInvite": 0, "operateType": 1}
        headers = {"content-type": 'application/json; charset=utf-8', "authorization": token}
        rep = requests.post(Url, data=json.dumps(data), headers=headers)
        print(rep.json())
        return rep.json()['code']

    def get_token(self):
        code = Entire().insert_Entire()
        print(code)
        if code == 401:
            testFile.getToken.Token().write_token()
            for _ in range(3000):
                Entire().insert_Entire()
                time.sleep(3)
        else:
            for _ in range(3000):
                Entire().insert_Entire()
                time.sleep(3)


if __name__ == '__main__':
    Entire().get_token()
