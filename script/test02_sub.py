# 导包
import app
import unittest
from api.sub import SubApi
from tools.dbunit import DBUnit
from parameterized import parameterized


def build_data():

    # 查询用例数据
    sql = "select * from sub_account"
    # 获取数据
    db_data  = DBUnit.exe_sql(sql)
    # 处理数据
    test_data = []
    for case_data in db_data:
        username = case_data[2]
        password = case_data[3]
        fire = case_data[4]
        status_code = case_data[5]
        test_data.append((username, password, fire, status_code))
    return test_data


class TestSub(unittest.TestCase):

    sub_name = None

    # 前置处理
    def setUp(self):
        self.sub_api = SubApi()

    # 后置处理
    def tearDown(self):
        pass

    @parameterized.expand(build_data())
    def test01_create(self, username, password, fire, status_code):
        sub_data = {
            "username": username,
            "password": password
        }
        print(sub_data)
        response = self.sub_api.sub_create(sub_data)
        self.assertEqual(status_code, response.status_code)

    def test02_search(self):
        params = {
            "offset": 0,
            "limit": 2
        }
        response = self.sub_api.sub_search(params)
        TestSub.sub_name = response.json().get('list')[0]["username"]

    def test03_update(self):
        params = {
            "username": TestSub.sub_name
        }
        sub_data = {
            "username": 'nun123',
            "password": "12345"
        }
        response = self.sub_api.sub_update(sub_data,params=params)
        self.assertEqual(200, response.status_code)
        print(response)

    def test04_delete(self):
        username_data = {
            "username": 'nun123'
        }
        print(username_data)
        response = self.sub_api.sub_delete(username_data)
        self.assertEqual(200, response.status_code)
