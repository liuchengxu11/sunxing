import pytest
from utils import shell_tool
from utils.dingding import dingding


if __name__ == '__main__':
    # 修改成要执行的测试用例
    # test_case = 'TestSuite/CcsMerchantController/test_merchat_addorupdate.py'
    test_case="TestSuite/CcsMerchantController/test_merchat_addorupdate/test_merchat_addorupdate.py"
    # 叮叮报告
    # test_ding="utils/dingding.py"
    xml_allure = './allure/xml/'
    html_allure = './allure/html/'
    pytest.main([ "-v","-s",'--alluredir',xml_allure,html_allure,
                 test_case])

    pytest.main(dingding("执行成功"))
    cmd1 = 'allure generate %s -o %s --clean' % (
        xml_allure, html_allure)
    cmd2 = 'allure serve %s' % (xml_allure)


    shell_tool.invoke(cmd1)
    shell_tool.invoke(cmd2)