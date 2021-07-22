# 导包
import app
import unittest
from api.sub import SubApi
from tools.dbunit import DBUnit
from parameterized import parameterized


class TestSub(unittest.TestCase):

    # 前置处理
    def setUp(self):
        self.sub_api = SubApi()

    # 后置处理
    def tearDown(self):
        pass

    def test01_create(self):
        sub_data = {
            "username": "nun",
            "password": "12345"
        }
        response = self.sub_api.sub_create(sub_data)
        self.assertEqual(200, response.status_code)

    @unittest.skip("程序有bug")
    def test02_update(self):
        sub_data = {
            "username": 'nun123',
            "password": "12345"
        }
        response = self.sub_api.sub_update(sub_data)
        self.assertEqual(200, response.status_code)
        print(response)
