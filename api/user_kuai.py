import os
from core.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_kuai_url = data.load_ini(data_file_path)["host"]["api_kuai_url"]


class User(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(User, self).__init__(api_kuai_url, **kwargs)

    def list_all_users(self, **kwargs):
        return self.get("/user/getLoginUserInfo", **kwargs)

    def list_one_user(self, **kwargs):
        return self.get("/user/getLoginUserInfo", **kwargs)

    # def register(self, **kwargs):
    #     return self.post("/register", **kwargs)

    def login(self, **kwargs):
        return self.post("/user/login", **kwargs)

    # def update(self, user_id, **kwargs):
    #     return self.put("/update/user/{}".format(user_id), **kwargs)
    #
    # def delete(self, name, **kwargs):
    #     return self.post("/delete/user/{}".format(name), **kwargs)
    #

user = User(api_kuai_url)