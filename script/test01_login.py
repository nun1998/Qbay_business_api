# 导包
import unittest
from api.login import LoginApi
import app


# 创建测试类
class TestLogin(unittest.TestCase):

    # 前置处理
    def setUp(self):
        self.login_api = LoginApi()

    # 后置处理
    def tearDown(self):
        pass

    def test01_case001(self):
        # 登录接口
        response = self.login_api.login({
            "email": "test3@bay.com",
            "password": "3db33c55b160c7c8108dd2b4f0cc472e",
            "grant_type": "password"
        })

        # 断言
        self.assertEqual(200, response.status_code)

        if response.status_code == 200:
            app.TOKEN = "Bearer" + response.json().get("access_token")
            app.header_data["Authorization"] = app.TOKEN
