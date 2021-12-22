import json
import common.app_re_token
import requests
import testFile.getAppToken
import testFile.getConfig

hosts = testFile.getConfig.read_ini("API", "host")


class Point():
    def transit_Ponit(self):
        token = common.app_re_token.read_token()
        url = hosts + '/app/transitPointOperation'
        data = [{
            "operationType": "0",
            "taskId": "117517",
            "childId": "",
            "id": "",
            "shipmentId": "44403968",
            "amapServiceId": "227878",
            "lon": "113.9114786783854",
            "amapTrackId": "164740",
            "lat": "22.52794379340278",
            "amapTerminalId": "361761730"
        }]
        headers = {"content-type": 'application/json', "authorization": token}
        rep = requests.put(url, data=json.dumps(data), headers=headers)
        print(rep.json())
        return rep.json()['code']

    def get_token(self):
        code = Point().transit_Ponit()
        print(code)
        if code == 401:
            testFile.getAppToken.AppToken().write_token()
            for _ in range(1):
                Point().transit_Ponit()
        else:
            Point().transit_Ponit()


if __name__ == '__main__':
    Point().get_token()
