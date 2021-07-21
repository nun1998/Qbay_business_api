# 导包
import app
import unittest
from api.login import LoginApi
from tools.dbunit import DBUnit
from tools.md5 import generate_md5
from parameterized import parameterized


# 构造数据
def build_data():
    # 查询用例数据语句
    sql = "select * from login"
    # 获取数据
    db_data = DBUnit.exe_sql(sql)
    # 处理数据
    test_data = []
    for case_data in db_data:
        email = case_data[2]
        password = case_data[3]
        status_code = case_data[4]
        test_data.append((email, password, status_code))
    # 返回数据
    return test_data


# 创建测试类
class TestLogin(unittest.TestCase):

    # 前置处理
    def setUp(self):
        self.login_api = LoginApi()

    # 后置处理
    def tearDown(self):
        pass

    @parameterized.expand(build_data())
    def test01(self, email, password, status_code):
        # 处理密码
        password = generate_md5(password + app.pepper)
        response = self.login_api.login({
            "email": email,
            "password": password,
            "grant_type": "password"
        })
        # 断言
        self.assertEqual(status_code, response.status_code)

        if response.status_code == 200:
            app.TOKEN = "Bearer" + response.json().get("access_token")
            app.header_data["Authorization"] = app.TOKEN
