#!/usr/bin/env python
#读取userCase.xlsx中的用例，使用unittest来进行断言校验
import json
import unittest
import sys
from os.path import abspath,dirname
sys.path.insert(0,dirname(dirname(abspath(__file__))))
from common.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
# import pythoncom
import readExcel

# pythoncom.CoInitialize()

url = geturlParams.geturlParams().get_Url()  # 调用我们的geturlParams获取我们拼接的URL
login_xls = readExcel.readExcel().get_xls('userCase.xlsx', 'login')


@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
    def setParameters(self, case_name, path, query, method):
        """
        set params
        :param case_name:
        :param path
        :param query
        :param method
        :return:
        """
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)

    def description(self):
        """
        test report description
        :return:
        """
        self.case_name

    def setUp(self):
        """
        :return:
        """
        print(self.case_name + "测试开始前准备")

    def test01case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):  # 断言
        """
        check test result
        :return:
        """
        url1 = "http://127.0.0.1:8888/login?"  #http://www.xxx.com/login?
        new_url = url1 + self.query
        data1 = dict(urllib.parse.parse_qsl(
            urllib.parse.urlsplit(new_url).query))  # 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
        #https://www.cnblogs.com/fanjc/p/9910292.html   u'.p.u.(url).query切割url并拿query那块  
        info = RunMain().run_main(self.method, url, data1)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = json.loads(info)  # 将响应转换为字典格式
        if self.case_name == 'login':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], 200)
        if self.case_name == 'login_error':  # 同上
            self.assertEqual(ss['code'], -1)
        if self.case_name == 'login_null':  # 同上
            self.assertEqual(ss['code'], 10001)

if __name__=='__main__':
    unittest.main()
