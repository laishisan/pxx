
import requests
from ruamel import yaml
import testFile.getConfig
hosts = testFile.getConfig.read_ini("API", "host")

class Token():
    def __init__(self):
        self.Url = hosts + "/oauth/pass"
        self.Data = {'username': "13537700044",'password': "e9bc0e13a8a16cbb07b175d92a113126",'client':"web"}
        self.Headers = {'Content_type': "application/x-www-form-urlencoded"}

    def get_token(self):
       Url = self.Url
       data = self.Data
       headers = self.Headers
       rep = requests.post(Url, data, headers)
       return rep.json()['data']['accessToken']

    def write_token(self):
        tonken = self.get_token()
        yamlpath = r'D:\pxx\common\Token.yaml'
        with open(yamlpath, "w", encoding="utf-8") as f:
            yaml.dump(tonken, f, Dumper=yaml.RoundTripDumper)

if __name__=='__main__':
    Token().write_token()



