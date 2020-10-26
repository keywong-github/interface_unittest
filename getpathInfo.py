#!/usr/bin/env python
#获取项目绝对路径
import os


def get_Path():
    path = os.path.split(os.path.realpath(__file__))[0]  #切割后，0是当前文件的上一级，1是当前文件1
    #path =os.path.dirname(os.path.abspath(__file__))  这个和上面的效果一样的
    #print(os.path.realpath(__file__))
    return path


if __name__ == '__main__':  # 执行该文件，测试下是否OK
    print('测试路径是否OK,路径为：', get_Path())