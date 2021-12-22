import json
import common.re_token
import requests
import testFile.getToken
from random import randint
import testFile.getConfig
host = testFile.getConfig.read_ini("API", "host")

class Driver():
    def insert_Driver(self):
        token = common.re_token.read_token()
        Url = host + '/web/companyDriver/insertBatch'
        data = [{"driverName": '蓝精灵', "driverPhone": f"135{randint(11111111, 99999999)}"}]
        headers = {"content-type": 'application/json', "authorization": token}
        rep = requests.post(Url, data=json.dumps(data), headers=headers)
        print(rep.json())
        return rep.json()['code']
    def get_token(self):
        code = Driver().insert_Driver()
        print(code)
        if code == 401:
           testFile.getToken.Token().write_token()
           for _ in range(4):
               Driver().insert_Driver()
        else:
            for _ in range(4):
                Driver().insert_Driver()
if __name__=='__main__':
    Driver().get_token()




