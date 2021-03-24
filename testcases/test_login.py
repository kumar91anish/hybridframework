import pytest
from selenium import webdriver
from Pageobject.LoginPage import Login
from utilities.repositries import Readconfig
from utilities.customLogger import LogGen
#from testcases.confitest import pytest_configure
#from testcases.confitest import pytest_metadata
from testcases.confitest import setup

class Test_001_Login:
    baseurl=Readconfig.ApplicationUrl()
    usermail=Readconfig.UserName()
    password=Readconfig.Password()
    logger=LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("**************** Test_001_Login ****************")
        self.logger.info("*************verifying home page title*********")
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("****************home page title test case passed********************")
        else:
            self.driver.save_screenshot(".\\Screeshots\\"+ "test_homePageTitle.png")
            self.driver.close()
            self.logger.warning("****************home page title test case Failed********************")
            assert False


    def test_Login(self,setup):
        self.logger.info("********************verifying login test*************")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=Login(self.driver)
        self.driver.maximize_window()
        self.lp.setUserName(self.usermail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin(self)
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("******************** login test case is passed ***************")
        else:
            self.driver.save_screenshot(".\\Screeshots\\" + "test_Login.png")
            self.driver.close()
            self.logger.info("************************* login test case is Failed *****************")
            assert False







