import json
import common.app_re_token
import requests
import testFile.getAppToken
import testFile.getConfig

hosts = testFile.getConfig.read_ini("API", "host")


class Shipment():
    def app_Shipment_Ltl(self):
        token = common.app_re_token.read_token()
        url = hosts + '/app/shipment/ltl'
        data = [{
            "inQuery": {
                "shipmentStatus": ["0", "10"]
            },
            "query": {},
            "pageSize": "2",
            "page": "0"
        }]
        headers = {"content-type": 'application/json', "authorization": token}
        rep = requests.post(url, data=json.dumps(data), headers=headers)
        print(rep.json())
        print(data)

    def get_token(self):
        code = Shipment.app_Shipment_Ltl()
        print(code)
        if code == 401:
            testFile.getToken.Token().write_token()
            for _ in range(4):
                Shipment.app_Shipment_Ltl()
        else:
            for _ in range(4):
                Shipment.app_Shipment_Ltl()


if __name__ == '__main__':
    Shipment.get_token()
