import configparser
import os

"""
    读取配置文件
"""

# 创建对象
read_ini = configparser.ConfigParser()
# 获取当前文件路径
current_file_path = os.path.dirname(os.path.abspath(__file__))
# 读取配置文件内容
read_ini.read(current_file_path + "/config.ini")


# 接口拼接
def url_join(api):
    url = get_host() + api
    return url


# IP地址
def get_host():
    return read_ini['API']['host']


# 登录接口
def get_hotMarkList():
    return url_join(read_ini['API']['hotMarkList'])


if __name__ == '__main__':
    print(get_hotMarkList())
