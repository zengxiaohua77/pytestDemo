import pytest
import allure
from operation.user_kuai import login_user, get_one_user_info
from common.logger import logger
from testcases.conftest import scenario_kuai_data


# @allure.step("步骤1 ==>> 注册用户")
# def step_1(username, password, telephone, sex, address):
#     logger.info("步骤1 ==>> 注册用户 ==>> {}, {}, {}, {}, {}".format(username, password, telephone, sex, address))


@allure.step("步骤2 ==>> 登录用户")
def step_2(phone):
    logger.info("步骤2 ==>> 登录用户：{}".format(phone))


@allure.step("步骤3 ==>> 获取某个用户信息")
def step_3(username):
    logger.info("步骤3 ==>> 获取某个用户信息：{}".format(username))


@allure.severity(allure.severity_level.CRITICAL)
@allure.epic("针对业务场景的测试")
@allure.feature("场景：用户注册-用户登录-查看用户")
class TestRegLogList():

    @allure.story("用例--注册/登录/查看--预期成功")
    @allure.description("该用例是针对 注册-登录-查看 场景的测试")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("用户注册登录查看-预期成功")
    @pytest.mark.multiple
    # @pytest.mark.usefixtures("delete_register_user")#如果一个方法或者一个class用例想要同时调用多个fixture，可以使用@pytest.mark.usefixture()进行叠加。注意叠加顺序，先执行的放底层，后执行的放上层。
    def test_user_register_login_update_success(self, testcase_data_kuai):
        username = testcase_data_kuai["login"]["username"]
        verificationCode = testcase_data_kuai["login"]["verificationCode"]
        phone = testcase_data_kuai["login"]["phone"]

        except_result = testcase_data_kuai["except_result"]
        except_code = testcase_data_kuai["except_code"]
        except_msg = testcase_data_kuai["except_msg"]

        logger.info("*************** 开始执行用例 ***************")
        result = login_user(phone, verificationCode)
        step_2(phone)
        token = result.token
        logger.info("-------------{}".format(token))
        assert result.success is True, result.error

        result = get_one_user_info(token)
        step_3(username)

        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_01_register_login_list.py"])