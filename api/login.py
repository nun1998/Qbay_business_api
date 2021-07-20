# 导包
import requests
import app

# 创建登录接口类
class LoginApi:
    def __init__(self):
        self.url = app.url + "/sign_in/v2"

    def login(self, login_data):
        return requests.post(url=self.url, json=login_data)