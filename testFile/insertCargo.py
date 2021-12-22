import json
import common.re_token
import requests
import testFile.getToken
import time
import testFile
import testFile.getConfig

hosts = testFile.getConfig.read_ini("API", "host")


class Cargo():
    def number(self):
        self.token = common.re_token.read_token()
        url = hosts + '/web/request/number/1'
        headers = {"content-type": 'application/json; charset=utf-8', "authorization": self.token}
        rep = requests.get(url, headers=headers)
        requestNo = rep.json()['data']
        if requestNo is None:
            return 0
        reqno = requestNo[0]
        return reqno

    def insert_Cargo(self):
        reqno = self.number()
        token = self.token
        url = hosts + '/web/request/cargo'
        data = [{"cargoRequestNo": reqno, "cargoOwner": "霍山洪峰石斛种植专业合作社", "paymentType": 30,
                 "cargoBusinessType": None, "senderAddressName": None, "pickUpTime": None, "receiverAddressName": None,
                 "receivedTime": None, "urgentType": "2", "remark": None, "ext10": None, "ext11": None, "ext12": None,
                 "ext13": None, "ext14": None, "ext15": None, "ext16": None, "cargoRequestTagList": [
                {"cargoRequestId": "50360576", "tagId": "R40", "tagName": "已配载", "id": "23472",
                 "creatorId": "202117000032", "creator": "1111深圳市杰思邦灯饰科技有限公司", "createTime": "2021-11-12T20:57:39",
                 "updaterId": "202117000032", "updater": "1111深圳市杰思邦灯饰科技有限公司", "updateTime": "2021-11-12T20:57:39",
                 "enabledFlag": 1, "traceId": "90327e1cbf5c6e3f"},
                {"cargoRequestId": "50360576", "tagId": "R10", "tagName": "已卸货", "id": "23475", "creatorId": "0",
                 "creator": "admin", "createTime": "2021-11-12T21:01:02", "updaterId": "0", "updater": "admin",
                 "updateTime": "2021-11-12T21:01:02", "enabledFlag": 1, "traceId": "2021-11-12T21:01:01.509"}],
                 "consignorType": None, "consignorId": None, "consignorName": "霍山洪峰石斛种植专业合作社", "consignorPhone": None,
                 "cargoPriceType": "0", "cargoTotalCost": 1000, "creatorId": "202117000032",
                 "creator": "1111深圳市杰思邦灯饰科技有限公司", "createTime": "2021-11-12T20:57:38", "updaterId": "202117000032",
                 "updater": "1111深圳市杰思邦灯饰科技有限公司", "updateTime": "2021-11-12T21:01:02", "enabledFlag": 1,
                 "traceId": "2021-11-12T21:01:01.509", "isIn": 'true', "cargoGoodsDtoList": [
                {"goodsCode": None, "cargoRequestId": "50360576", "descriptionOfGoods": "13r55",
                 "cargoTypeClassificationCode": "0800", "goodsItemGrossWeight": 1000, "goodsItemCube": 1000000,
                 "totalNumberOfPackages": 1, "priceMode": "0", "unitPrice": 1000, "accountReceivable": 1000,
                 "creatorId": "202117000032", "creator": "1111深圳市杰思邦灯饰科技有限公司", "createTime": "2021-11-12T20:57:38",
                 "updaterId": "202117000032", "updater": "1111深圳市杰思邦灯饰科技有限公司", "updateTime": "2021-11-12T20:57:38",
                 "enabledFlag": 1, "traceId": "90327e1cbf5c6e3f", "tempId": "1mb1m6zem0v"}], "cargoPointDtoList": [
                {"cargoRequestId": "50360576", "pointType": 10, "pointAddress": "北京市朝阳区双井街道双花园商业街", "pointCode": 110105,
                 "pointSort": 0, "pointLongitude": "116.452189", "pointLatitude": "39.90213", "contacts": "ffgg11",
                 "contactsPhone": "15854565441", "arriveTime": "2021-11-14T19:36:00", "sendTime": None,
                 "actualArriveTime": None, "actualSendTime": None, "operationType": 1, "creatorId": "202117000032",
                 "creator": "1111深圳市杰思邦灯饰科技有限公司", "createTime": "2021-11-12T20:57:38", "updaterId": "202117000032",
                 "updater": "1111深圳市杰思邦灯饰科技有限公司", "updateTime": "2021-11-12T20:57:38", "enabledFlag": 1,
                 "traceId": "90327e1cbf5c6e3f"}, {"cargoRequestId": "50360576", "pointType": 20,
                                                  "pointAddress": "河北省廊坊市安次区光明西道街道廊坊市城轨交通技工学校北京城轨交通学校廊坊校区",
                                                  "pointCode": 131002, "pointSort": 1, "pointLongitude": "116.68239",
                                                  "pointLatitude": "39.521757", "contacts": "nnn",
                                                  "contactsPhone": "18645444545", "arriveTime": "2021-11-19T19:36:00",
                                                  "sendTime": None, "actualArriveTime": None, "actualSendTime": None,
                                                  "operationType": 2, "creatorId": "202117000032",
                                                  "creator": "1111深圳市杰思邦灯饰科技有限公司", "createTime": "2021-11-12T20:57:38",
                                                  "updaterId": "202117000032", "updater": "1111深圳市杰思邦灯饰科技有限公司",
                                                  "updateTime": "2021-11-12T20:57:38", "enabledFlag": 1,
                                                  "traceId": "90327e1cbf5c6e3f"}],
                 "receiptDto": {"receiptCode": None, "receiptAddress": None, "receipter": None, "receipterPhone": None,
                                "mailBack": 0, "uploadPhoto": 1}, "estimateArriveTime": "2021-11-14T19:36:00",
                 "estimateCompleteTime": "2021-11-19T19:36:00"}]

        headers = {"content-type": 'application/json; charset=utf-8', "authorization": token}
        rep = requests.post(url, data=json.dumps(data), headers=headers)
        print(rep.json())
        return rep.json()['code']

    def get_token(self):
        code = Cargo().insert_Cargo()
        print(code)
        if code == 401:
            testFile.getToken.Token().write_token()
            for _ in range(10):
                Cargo().number()
                Cargo().insert_Cargo()
                time.sleep(1)
        else:
            for _ in range(10):
                Cargo().number()
                Cargo().insert_Cargo()
                time.sleep(1)


if __name__ == '__main__':
    Cargo().get_token()
