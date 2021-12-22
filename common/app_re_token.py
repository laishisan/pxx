import yaml


def read_token():
    file = open(r'D:\pxx\common\appToken.yaml', 'r')
    data = yaml.load(file, Loader=yaml.FullLoader)
    print(data)
    return data


if __name__ == "__main__":
    read_token()
