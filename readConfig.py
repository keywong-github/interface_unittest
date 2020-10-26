#!/usr/bin/env python
#读取配置文件的方法，并返回文件中内容

import os
import configparser
import getpathInfo  # 引入我们自己的写的获取路径的类
#from getpathInfo import *

path = getpathInfo.get_Path()  # 调用实例化，还记得这个类返回的路径为F:\pycharm\1211\接口自动化
#https://blog.csdn.net/hao930826/article/details/52232324 这里getpathInfo 里面没有定义class，所以不用括号
config_path = os.path.join(path,'config.ini')
# 这句话是在path路径下再加一级，最后变成F:\pycharm\1211\接口自动化\config.ini
config = configparser.ConfigParser()  # 调用外部的读取配置文件的方法
config.read(config_path, encoding='utf-8')


class ReadConfig():

    def get_http(self, name):
        value = config.get('HTTP', name)
        return value

    def get_email(self, name):
        value = config.get('EMAIL', name)
        return value

    def get_mysql(self, name):  # 写好，留以后备用。但是因为我们没有对数据库的操作，所以这个可以屏蔽掉
        value = config.get('DATABASE', name)
        return value


if __name__ == '__main__':  # 测试一下，我们读取配置文件的方法是否可用
    print('HTTP中的baseurl值为：', ReadConfig().get_http('baseurl'))
    print('EMAIL中的开关on_off值为：', ReadConfig().get_email('on_off'))
