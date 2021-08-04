from core.result_base import ResultBase
from api.user_kuai import user
from common.logger import logger


def login_user(phone, verificationCode):
    """
    登录用户
    :param username: 用户名
    :param password: 密码
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    payload = {
        "phone": phone,
        "verificationCode": verificationCode
    }
    header = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    res = user.login(json=payload, headers=header)
    result.success = False
    if res.json()["code"] == 200:
        result.success = True
        result.token = res.json()["data"]["token"]
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    logger.info("登录用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result
