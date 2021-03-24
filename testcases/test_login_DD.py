import pytest
from selenium import webdriver
from Pageobject.LoginPage import Login
from utilities.repositries import Readconfig
from utilities.customLogger import LogGen
import time
from testcases.confitest import setup
from utilities import XLutility
class Test_002_Login_DDT:
    baseurl=Readconfig.ApplicationUrl()
    path="TestData/Logindata.xlsx"
    logger=LogGen.loggen()

    def test_Login(self,setup):

        self.logger.info("********************Test_002_Login_DDT*************")
        self.logger.info("********************verifying login DDT test*************")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=Login(self.driver)
        self.row=XLutility.getrowcount(self.path,'Sheet1')
        print("number of row is:", self.row)
        lst_status=[]
        for r in range(2,self.row+1):
            self.user=XLutility.readdata(self.path,'Sheet1',r,1)
            self.password = XLutility.readdata(self.path, 'Sheet1', r,2)
            self.exp = XLutility.readdata(self.path, 'Sheet1', r,3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"
            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("************Passed*******")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("**********Failed**********")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title!=exp_title:
                if self.exp=="Pass":
                    self.logger.info("**********Failed*************")
                    lst_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("**********Passed**********")
                    lst_status.append("Pass")
                    time.sleep(5)
        if "Fail" not in lst_status:
            self.logger.info("************testloginDDT is Passesd*************")
            self.driver.close()
            assert True
        else:
             self.logger.info("************testloginDDT is Failed*************")
             self.driver.close()
             assert False





















