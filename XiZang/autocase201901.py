# -*-coding:utf-8 -*-
'''
Created on 2019年1月19日

@author:Taozhan
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from autocase11 import autocase11yue
import autocase11
import HTMLTestRunnerA

class autocase0901(autocase11.autocase11yue):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_VmGroupADD(self):
        u"""虚拟组新增"""
        driver = self.driver
        autocase11yue.load(self)
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        time.sleep(1)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='个人查询'])[1]/following::div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='操作员上岗'])[1]/following::li[1]").click()
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        driver.find_element_by_id("addButton").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='虚拟组类型'])[4]/following::span[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='话务班组'])[2]/following::div[1]").click()
        driver.find_element_by_id("condition_GROUP_NAME").click()
        driver.find_element_by_id("condition_GROUP_NAME").clear()
        driver.find_element_by_id("condition_GROUP_NAME").send_keys(u"虚拟一组")
        driver.find_element_by_id("confirmButton").click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div[2]/button[1]').click()
        time.sleep(3)
        RET=driver.find_element_by_xpath('//*[@id="wade_messagebox-7d67d44b138069da347b912e05066846_title"]').text
        print RET
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='新增成功'])[1]/following::button[1]").click()
        
    def test_VmGroupQuery(self):
        u"""虚拟组信息查询"""
        driver = self.driver
        autocase11yue.load(self)
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        time.sleep(3)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='个人查询'])[1]/following::div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='操作员上岗'])[1]/following::li[1]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='删除'])[1]/following::button[1]").click()
        driver.find_element_by_id("GROUP_NAME").click()
        driver.find_element_by_id("GROUP_NAME").clear()
        driver.find_element_by_id("GROUP_NAME").send_keys(u"虚拟一组")
        driver.find_element_by_id("qryButton").click()
        time.sleep(3)
        Message=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div/table/tbody').text
        print Message
    
    def test_VmGroupEdit(self):
        u"""虚拟组信息修改"""
        driver = self.driver
        autocase11yue.load(self)
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        time.sleep(3)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='个人查询'])[1]/following::div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='操作员上岗'])[1]/following::li[1]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='删除'])[1]/following::button[1]").click()
        driver.find_element_by_id("GROUP_NAME").click()
        driver.find_element_by_id("GROUP_NAME").clear()
        driver.find_element_by_id("GROUP_NAME").send_keys(u"虚拟一组")
        driver.find_element_by_id("qryButton").click()
        time.sleep(3)
        driver.find_element_by_id("ROLE_MGT").click()
        driver.find_element_by_id("editButton").click()
        driver.find_element_by_id("cond_GROUP_NAME").click()
        driver.find_element_by_id("cond_GROUP_NAME").clear()
        driver.find_element_by_id("cond_GROUP_NAME").send_keys(u"虚拟二组")
        driver.find_element_by_id("modifyButton").click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div[2]/button[1]').click()
        time.sleep(3)
        RET01=driver.find_element_by_xpath('//*[@id="wade_messagebox-0a844469c0371a6a292f672f522081c2_title"]').text
        print RET01
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='修改成功'])[1]/following::button[1]").click()

    def test_VmGroupDelete(self):
        u"""虚拟组删除"""
        driver = self.driver
        autocase11yue.load(self)
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        time.sleep(3)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='个人查询'])[1]/following::div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='操作员上岗'])[1]/following::li[1]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='删除'])[1]/following::button[1]").click()
        driver.find_element_by_id("GROUP_NAME").click()
        driver.find_element_by_id("GROUP_NAME").clear()
        driver.find_element_by_id("GROUP_NAME").send_keys(u"虚拟二组")
        driver.find_element_by_id("qryButton").click()
        time.sleep(3)
        driver.find_element_by_id("ROLE_MGT").click()
        driver.find_element_by_id("deleteButton").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='确认要删除吗？'])[1]/following::button[1]").click()
        time.sleep(3)
        RET02=driver.find_element_by_xpath('//*[@id="wade_messagebox-ff0ae50b712f71e54cd568c372cf3f44_title"]').text
        print RET02
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='业务受理成功！'])[1]/following::button[1]").click()
    
    def test_VmGroupManAdd(self):
        u"""虚拟组成员新增"""
        driver = self.driver
        autocase11yue.load(self)
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        time.sleep(3)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='个人查询'])[1]/following::div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='虚拟组管理'])[1]/following::li[1]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='虚拟组'])[1]/following::span[2]").click()
        driver.find_element_by_id("GROUP_NAME").click()
        driver.find_element_by_id("GROUP_NAME").clear()
        driver.find_element_by_id("GROUP_NAME").send_keys(u"米琪")
        driver.find_element_by_id("qryButton").click()
        time.sleep(3)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='组名称：'])[1]/following::span[1]").click()
        driver.find_element_by_id("addButton").click()
        time.sleep(3) 
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div[2]/div/div[1]/ul/li[2]/div[2]/span/span').click()
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="frame_editPopup_group2_item849def3a05e939183749adfcf260522b"]'))
        driver.find_element_by_xpath('//*[@class="e_select"]').click
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="mySelect_float"]/div[2]/div/div/ul/li[3]/div').click() 
        time.sleep(3)
        driver.find_element_by_id("OPERATOR_ID").click()
        driver.find_element_by_id("OPERATOR_ID").clear()
        driver.find_element_by_id("OPERATOR_ID").send_keys("91110020")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='员工姓名'])[1]/following::button[1]").click()
        driver.find_element_by_name("operator").click()
        driver.find_element_by_id("confirmButton").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='确认要新增虚拟组成员91110020吗？'])[1]/following::button[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='操作成功！'])[1]/following::button[1]").click()
    
    def test_GNJAdd(self):
        u"""功能集新增"""
        driver = self.driver
        autocase11yue.load(self)
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        time.sleep(3)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='个人查询'])[1]/following::div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='系统权限行为维护'])[1]/following::li[1]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        driver.find_element_by_id("addButton").click()
        driver.find_element_by_id("condition_ROLE_NAME").click()
        driver.find_element_by_id("condition_ROLE_NAME").clear()
        driver.find_element_by_id("condition_ROLE_NAME").send_keys(u"虚拟功能集")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='功能集类型'])[5]/following::span[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='资源类'])[3]/following::div[1]").click()
        driver.find_element_by_id("condition_REGION_CODE_span").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='--请选择--'])[16]/following::div[1]").click()
        driver.find_element_by_id("condition_DOMAIN_ID_span").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='--请选择--'])[16]/following::div[1]").click()
        driver.find_element_by_id("confirmButton").click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[14]/div/div[2]/div[2]/button[1]').click()
        time.sleep(3)
        messageee=driver.find_element_by_xpath('//*[@id="wade_messagebox-7d67d44b138069da347b912e05066846_title"]').text
        print messageee
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='新增成功'])[1]/following::button[1]").click()
    
    def test_GNJQuery(self):
        u"""功能集查询"""
        driver = self.driver
        autocase11yue.load(self)
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        time.sleep(3)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='个人查询'])[1]/following::div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='系统权限行为维护'])[1]/following::li[1]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        time.sleep(5)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='删除'])[1]/following::button[1]").click()
        driver.find_element_by_id("ROLE_NAME").click()
        driver.find_element_by_id("ROLE_NAME").clear()
        driver.find_element_by_id("ROLE_NAME").send_keys(u"虚拟功能集")
        driver.find_element_by_id("qryButton").click()
        time.sleep(5)
        RES=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div/table/tbody').text
        print RES
        
    def test_GNJEdit(self):
        u"""功能集修改"""
        driver = self.driver
        autocase11yue.load(self)
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        time.sleep(3)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='个人查询'])[1]/following::div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='系统权限行为维护'])[1]/following::li[1]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        time.sleep(5)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='删除'])[1]/following::button[1]").click()
        driver.find_element_by_id("ROLE_NAME").click()
        driver.find_element_by_id("ROLE_NAME").clear()
        driver.find_element_by_id("ROLE_NAME").send_keys(u"虚拟功能集")
        driver.find_element_by_id("qryButton").click()
        time.sleep(3)
        driver.find_element_by_id("ROLE_MGT").click()
        driver.find_element_by_id("editButton").click()
        driver.find_element_by_id("cond_ROLE_NAME").click()
        driver.find_element_by_id("cond_ROLE_NAME").clear()
        driver.find_element_by_id("cond_ROLE_NAME").send_keys(u"虚拟功能集一")
        driver.find_element_by_id("modifyButton").click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[14]/div/div[2]/div[2]/button[1]').click()
        time.sleep(3)
        RES01=driver.find_element_by_xpath('//*[@id="wade_messagebox-0a844469c0371a6a292f672f522081c2_title"]').text
        print RES01
    
    def test_GNJDelete(self):
        u"""功能集删除"""
        driver = self.driver
        autocase11yue.load(self)
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        time.sleep(3)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='个人查询'])[1]/following::div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='系统权限行为维护'])[1]/following::li[1]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        time.sleep(5)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='删除'])[1]/following::button[1]").click()
        driver.find_element_by_id("ROLE_NAME").click()
        driver.find_element_by_id("ROLE_NAME").clear()
        driver.find_element_by_id("ROLE_NAME").send_keys(u"虚拟功能集一")
        driver.find_element_by_id("qryButton").click()
        driver.find_element_by_id("ROLE_MGT").click()
        driver.find_element_by_id("deleteButton").click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[14]/div/div[2]/div[2]/button[1]').click()
        time.sleep(3)
        RES02=driver.find_element_by_xpath('//*[@id="wade_messagebox-ff0ae50b712f71e54cd568c372cf3f44_title"]').text
        print RES02
    
    def test_GNJCdAdd(self):
        u"""功能集系统菜单分配权限"""
        driver = self.driver
        autocase11yue.load(self)
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        time.sleep(3)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='个人查询'])[1]/following::div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='功能集关系管理'])[1]/following::li[1]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        time.sleep(5)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='功能集'])[1]/following::span[2]").click()
        driver.find_element_by_id("ROLE_NAME").click()
        driver.find_element_by_id("ROLE_NAME").clear()
        driver.find_element_by_id("ROLE_NAME").send_keys(u"卢")
        driver.find_element_by_id("qryButton").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='功能集编号：'])[1]/following::span[1]").click()
        driver.find_element_by_id("grantRightButton").click()
        driver.find_element_by_id("queryButton").click()
        driver.find_element_by_id("FUNCTION").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='失效日期：'])[1]/following::button[1]").click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[18]/div/div[2]/div[2]/button[1]').click()
        time.sleep(3)
        RES03=driver.find_element_by_xpath('//*[@id="wade_messagebox-41a09a6eba201eaa9bee6bb98ca43849_title"]').text
        print RES03
    
        
    def test_VmGroupManDlete(self):
        u"""虚拟组成员删除"""
        driver = self.driver
        autocase11yue.load(self)
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        time.sleep(3)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='个人查询'])[1]/following::div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='虚拟组管理'])[1]/following::li[1]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='虚拟组'])[1]/following::span[2]").click()
        time.sleep(3)
        driver.find_element_by_id("GROUP_NAME").click()
        driver.find_element_by_id("GROUP_NAME").clear()
        driver.find_element_by_id("GROUP_NAME").send_keys(u"虚拟三组")
        driver.find_element_by_id("qryButton").click()
        time.sleep(3)
        #//*[@id="scroller32"]/div[1]/div[1]/ul/li/div
        driver.find_element_by_xpath('//*[@id="scroller32"]/div[1]/div[1]/ul/li/div').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="PackageRightPart"]/div/div/div/div/div/table/tbody/tr[2]/td').click()
        driver.find_element_by_id("deleteButton").click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[11]/div/div[2]/div[2]/button[1]').click()
        time.sleep(3)
        messagee=driver.find_element_by_xpath('//*[@id="wade_messagebox-9209358670f30487059ce524c5999b73_title"]').text
        print messagee
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='操作成功！'])[1]/following::button[1]").click()
    
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    #unittest.main()#运行所有test开头的测试用例
    testunit=unittest.TestSuite()
    #将测试用例加入到测试容器中
    testunit.addTest(autocase0901("test_VmGroupADD"))
    testunit.addTest(autocase0901("test_VmGroupQuery"))
    testunit.addTest(autocase0901("test_VmGroupEdit"))
    testunit.addTest(autocase0901("test_VmGroupDelete"))   
    #testunit.addTest(autocase0901("test_VmGroupManAdd"))  
    testunit.addTest(autocase0901("test_VmGroupManDlete"))   
    testunit.addTest(autocase0901("test_GNJAdd"))
    testunit.addTest(autocase0901("test_GNJQuery")) 
    testunit.addTest(autocase0901("test_GNJEdit"))  
    testunit.addTest(autocase0901("test_GNJDelete"))  
    testunit.addTest(autocase0901("test_GNJCdAdd"))
    #获取当前时间，这样便于下面的使用。
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
    #打开一个文件，将result写入此file中
    fp=open("result"+now+".html",'wb')
    runner=HTMLTestRunnerA.HTMLTestRunner(stream=fp,title='Test Report',description=u'南基五期新CRM个人业务自动化测试,test by taozhan')
    runner.run(testunit) 
    fp.close()
