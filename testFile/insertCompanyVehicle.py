import json
import common.re_token
import requests
from random import randint
import testFile.getToken
import testFile.getConfig

hosts = testFile.getConfig.read_ini("API", "host")


class Vehicle():
    def insert_Company_Vehicle(self):
        token = common.re_token.read_token()
        Url = hosts + '/web/companyVehicle/insertCompanyVehicle'
        data = [{"vehicleNumber": f"粤B8{randint(1111, 9999)}", "drivers": [], "vehiclePlateColorCode": "1",
                 "vehicleType": "1002", "vehicleLength": "35"}]
        headers = {"content-type": 'application/json', "authorization": token}
        rep = requests.post(Url, data=json.dumps(data), headers=headers)
        print(rep.json())
        print(data)

    def get_token(self):
        code = Vehicle().insert_Driver()
        print(code)
        if code == 401:
            testFile.getToken.Token().write_token()
            for _ in range(4):
                Vehicle().insert_Driver()
        else:
            for _ in range(4):
                Vehicle().insert_Driver()


if __name__ == '__main__':
    Vehicle().get_token()
