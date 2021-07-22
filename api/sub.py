# 导包
import requests
import app


# 创建子账户类
class SubApi:
    def __init__(self):
        # 创建子账户
        self.url_create = app.url + "/create_sub_shop/v2"
        # 修改子账户
        self.url_update = app.url + "/update_sub_shop/v2"
        # 查询所有子账户
        self.url_search = app.url + "/search_sub_shop_list/v2"
        # 删除子账户
        self.url_delete = app.url + "/delete_sub_shop/v2"

    def sub_create(self, sub_data):
        return requests.post(url=self.url_create, json=sub_data, headers=app.header_data)

    def sub_update(self, sub_data, params):
        return requests.post(url=self.url_update, json=sub_data,params=params ,headers=app.header_data)

    def sub_search(self, params):
        return requests.get(url=self.url_search, params=params, headers=app.header_data)

    def sub_delete(self, username_data):
        print(self.url_delete)
        return requests.post(url=self.url_delete, json=username_data, headers=app.header_data)