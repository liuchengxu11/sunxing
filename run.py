import pytest
from utils import shell_tool



if __name__ == '__main__':
    # 修改成要执行的测试用例
    # test_case = 'TestSuite/CcsMerchantController/test_merchat_addorupdate.py'
    test_case="TestSuite/CcsMerchantController/test_merchat_addorupdate/test_merchat_addorupdate.py"
    xml_allure = './allure/xml/'
    html_allure = './allure/html/'
    pytest.main([ "-v","-s",'--alluredir',xml_allure,html_allure,test_case])

    cmd1 = 'allure generate %s -o %s --clean' % (
        xml_allure, html_allure)
    cmd2 = 'allure serve %s' % (xml_allure)

    shell_tool.invoke(cmd1)
    shell_tool.invoke(cmd2)
