#-*- coding:utf-8 -*-
'''
Created on 2018年11月21日

@author: taozhan
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import HTMLTestRunnerA
import sys
# from asn1crypto._ffi import null
# from twisted.python.test.deprecatedattributes import message
import os
reload(sys)
sys.setdefaultencoding( "utf-8" )
class autocase11yue(unittest.TestCase):   
    def setUp(self):#初始化部分
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    #登录CRM主页
    def load(self):    
        driver = self.driver
        driver.get("http://172.16.79.15:8826/crmweb/?service=page/Login")
        driver.find_element_by_id("OPER_CODE").click()
        driver.find_element_by_id("OPER_CODE").clear()
        driver.find_element_by_id("OPER_CODE").send_keys("91110029")
        driver.find_element_by_id("PASSWORD").click()
        driver.find_element_by_id("PASSWORD").clear()
        driver.find_element_by_id("PASSWORD").send_keys("123456")
        driver.find_element_by_id("login_btn").click()        
    #服务号码登录
    def test_FuWoHaoMaLoad(self,number):
        u"""服务号码登录"""
        driver = self.driver
        autocase11yue.load(self)
        time.sleep(5)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='营业员 / 91110029'])[1]/following::li[2]").click()
        driver.find_element_by_id("NO_PASSWORD_LOGIN_CHECKBOX").click()
        driver.find_element_by_id("LOGIN_NUM").click()
        driver.find_element_by_id("LOGIN_NUM").clear()
        driver.find_element_by_id("LOGIN_NUM").send_keys(number)
        driver.find_element_by_id("LOGIN_BTN").click()
    #异常订单信息查询
    def test_GetOrderErrPrint(self):
        u"""订单异常信息查询"""
        driver = self.driver
        autocase11yue.load(self)
        time.sleep(5)
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_xpath('//*[@id="menu_ct"]')
        #进入个人业务
        driver.find_element_by_xpath('//*[@id="menu_l1_ul"]/li[2]').click()
        #进入订单查询页面
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='一号双终端副卡开户'])[1]/following::li[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        time.sleep(5)
        #查询页面
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        #driver.find_element_by_css_selector('css=input[type="text"]')
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='导出'])[1]/following::input[2]").click()
        time.sleep(5)
        driver.find_element_by_id("cond_ORDER_ID").click()
        driver.find_element_by_id("cond_ORDER_ID").clear()
        driver.find_element_by_id("cond_ORDER_ID").send_keys("181111000594445")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='结束日期'])[1]/following::button[1]").click()
        time.sleep(3)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='竣工订单查询'])[1]/following::input[1]").click()
        driver.find_element_by_id("showDetailButton").click()
        time.sleep(5)
        #driver.close()
    #黑名单校验
    def test_IdentifityHMD(self):
        u"""黑名单验证"""
        driver =self.driver
        autocase11yue.load(self)
        time.sleep(5)
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_xpath('//*[@id="menu_ct"]')
        #进入个人业务
        driver.find_element_by_xpath('//*[@id="menu_l1_ul"]/li[2]').click() 
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_xpath('//*[@id="menu_l2_2"]/div/div[4]/ul/li[3]').click()
        #driver.find_element_by_xpath('//*[@id="menu_l2_2"]/div/div[4]/ul/li[3]').click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        driver.find_element_by_id("CUST_INFO_DIV").click()
        driver.find_element_by_id("editInfoButton").click()
        time.sleep(5)
        driver.find_element_by_id("PARTY_NAME").click()
        driver.find_element_by_id("PARTY_NAME").clear()
        driver.find_element_by_id("PARTY_NAME").send_keys(u"多诺万")
        driver.find_element_by_id("IDEN_NR").click()
        driver.find_element_by_id("IDEN_NR").clear()
        driver.find_element_by_id("IDEN_NR").send_keys("440103199003070539")
        driver.find_element_by_id("IDEN_NR_BUTTON").click()
        time.sleep(5)
        #---------------------------------------------
        #这里加一个判断是否达到测试要求
        objeee=driver.find_element_by_xpath('//*[@id="wade_messagebox-bf13ceff87ff389ac56a906e76ed36de_ct"]').text
        #attribute =obj.text
        print objeee
        if objeee== u"该证件号码是特殊名单！":
            print "Successful verification of special list"
        else:
            print "Special list check failure"
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="wade_messagebox-bf13ceff87ff389ac56a906e76ed36de_ct"]').click()
        #driver.close()
    #一证五号校验
    def test_YiZhengWuHao(self):
        u"""一证五号校验"""
        driver =self.driver
        autocase11yue.load(self)
        time.sleep(5)
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_xpath('//*[@id="menu_ct"]')
        #进入个人业务
        driver.find_element_by_xpath('//*[@id="menu_l1_ul"]/li[2]').click() 
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_xpath('//*[@id="menu_l2_2"]/div/div[4]/ul/li[3]').click()
        #driver.find_element_by_xpath('//*[@id="menu_l2_2"]/div/div[4]/ul/li[3]').click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        driver.find_element_by_id("CUST_INFO_DIV").click()
        driver.find_element_by_id("editInfoButton").click()
        time.sleep(5)
        driver.find_element_by_id("PARTY_NAME").click()
        driver.find_element_by_id("PARTY_NAME").clear()
        driver.find_element_by_id("PARTY_NAME").send_keys(u"陶展")
        driver.find_element_by_id("IDEN_NR").click()
        driver.find_element_by_id("IDEN_NR").clear()
        driver.find_element_by_id("IDEN_NR").send_keys("430124199304118372")
        driver.find_element_by_id("IDEN_NR_BUTTON").click()
        time.sleep(5)
        #---------------------------------------------
        #加校验，弹出框的提示对的上即返回成功
        a=driver.find_element_by_xpath('//*[@id="wade_tipbox-1_content"]').text
        print a
        if a ==u'省内一证多号验证：该证件号码只能使用[2]次,现在已经达到了最大数!':
            print 'One card multi-number check is normal'
        else:
            print 'A multi-number check anomaly'
    #欠费校验
    def test_QianFei(self):
        u"""欠费校验"""
        driver =self.driver
        autocase11yue.load(self)
        time.sleep(5)
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_xpath('//*[@id="menu_ct"]')
        #进入个人业务
        driver.find_element_by_xpath('//*[@id="menu_l1_ul"]/li[2]').click() 
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_xpath('//*[@id="menu_l2_2"]/div/div[4]/ul/li[3]').click()
        #driver.find_element_by_xpath('//*[@id="menu_l2_2"]/div/div[4]/ul/li[3]').click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        driver.find_element_by_id("CUST_INFO_DIV").click()
        driver.find_element_by_id("editInfoButton").click()
        time.sleep(5)
        driver.find_element_by_id("PARTY_NAME").click()
        driver.find_element_by_id("PARTY_NAME").clear()
        driver.find_element_by_id("PARTY_NAME").send_keys(u"多玩")
        driver.find_element_by_id("IDEN_NR").click()
        driver.find_element_by_id("IDEN_NR").clear()
        driver.find_element_by_id("IDEN_NR").send_keys("110101197811075620")
        driver.find_element_by_id("IDEN_NR_BUTTON").click()
        time.sleep(5)
        #-----------------------------------------------------
        #这里截取欠费的字符就好
        qf=driver.find_element_by_xpath('//*[@id="wade_messagebox-c5c33bf56d85d24c78640100df197c4c_ct"]').text
        #attribute =obj.text
        qfpanduan=qf[0:4]
        #print (type(qf))
        if qfpanduan== u".客户欠费":
            print "Customer arrears are judged to be normal"
        else:
            print "Customer default judgment anomaly"
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[46]/div/div[2]/div[2]/button').click()
    #一证多名校验    
    def test_YiZhengDuoMing(self):
        u"""一证多名校验"""
        driver =self.driver
        autocase11yue.load(self)
        time.sleep(5)
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_xpath('//*[@id="menu_ct"]')
        #进入个人业务
        driver.find_element_by_xpath('//*[@id="menu_l1_ul"]/li[2]').click() 
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_xpath('//*[@id="menu_l2_2"]/div/div[4]/ul/li[3]').click()
        #driver.find_element_by_xpath('//*[@id="menu_l2_2"]/div/div[4]/ul/li[3]').click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        driver.find_element_by_id("CUST_INFO_DIV").click()
        driver.find_element_by_id("editInfoButton").click()
        time.sleep(5)
        driver.find_element_by_id("PARTY_NAME").click()
        driver.find_element_by_id("PARTY_NAME").clear()
        driver.find_element_by_id("PARTY_NAME").send_keys(u"陶曦阳")
        driver.find_element_by_id("IDEN_NR").click()
        driver.find_element_by_id("IDEN_NR").clear()
        driver.find_element_by_id("IDEN_NR").send_keys("430124199304118372")
        driver.find_element_by_id("IDEN_NR_BUTTON").click()
        time.sleep(5)
        bid=driver.find_element_by_xpath('//*[@id="wade_messagebox-6ac7754849cedcbeffb201c1de26b456_ct"]').text
        #print bid
        ff=re.findall("PARTY_NAME",bid)
        #这里截取一下字符串，取开头几个字符就好/正则表达是抓取出字符
        print ff
        if ff[0] == 'PARTY_NAME':
            print 'One success of multiple verification'
        else:
            print 'One multiple checkout anomaly'
    #HLR信息管理-新增
    def test_HLR_ADD(self):
        u"""HLR新增"""
        driver = self.driver
        autocase11yue.load(self)
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_xpath('//*[@id="menu_ct"]')
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='客户管理'])[1]/following::div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='资源价格管理'])[1]/following::li[1]").click()
        time.sleep(2)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        driver.find_element_by_id("addButton").click()
        driver.find_element_by_id("add_NUM_SEG").click()
        driver.find_element_by_id("add_NUM_SEG").clear()
        driver.find_element_by_id("add_NUM_SEG").send_keys("1880094")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='重置'])[2]/following::button[1]").click()
        time.sleep(10)
        SBwadeKuangJIA="wade_messagebox-(.*?)_ct"
        hlrJYneiron=driver.find_element_by_xpath('//*[starts-with(@id,SBwadeKuangJIA)]').text
        #hlrll=driver.find_elements_by_css_selector('#wade_messagebox-4aa8d22d38aa3a1a036048e5162f24e9_ct').text
        print hlrJYneiron
        order_id=re.findall('\d{14}', hlrJYneiron)
        print order_id
        if order_id=='' or len(order_id)==0:
            print (u'HLR 入库失败')
        else:
            print (u'HLRr入库成功')
    #IMSI与HLR信息管理                
    def test_IMS_HLR_ADD(self):
        u"""IMS_HLR新增"""
        driver = self.driver
        autocase11yue.load(self)
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_xpath('//*[@id="menu_ct"]')
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='客户管理'])[1]/following::div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='HLR信息管理'])[1]/following::li[1]").click()
        time.sleep(2)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_58"]'))
        driver.find_element_by_id("addButton").click()
        driver.find_element_by_id("add_START_IMSI").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=add_START_IMSI | ]
        driver.find_element_by_id("add_START_IMSI").clear()
        driver.find_element_by_id("add_START_IMSI").send_keys("460066660000000")
        driver.find_element_by_id("add_END_IMSI").click()
        driver.find_element_by_id("add_END_IMSI").clear()
        driver.find_element_by_id("add_END_IMSI").send_keys("460066660000010")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='重置'])[2]/following::button[1]").click()
        time.sleep(10)
        SBwadeKuangJIA="wade_messagebox-(.*?)_ct"
        IMSJYneiron=driver.find_element_by_xpath('//*[starts-with(@id,SBwadeKuangJIA)]').text
        #hlrll=driver.find_elements_by_css_selector('#wade_messagebox-4aa8d22d38aa3a1a036048e5162f24e9_ct').text
        print IMSJYneiron
        order_id=re.findall('\d{14}', IMSJYneiron)
        print order_id
        if order_id=='' or len(order_id)==0:
            print (u'IMS 新增业务办理失败')
        else:
            print (u'IMS 新增业务办理成功')
    
    #受理撤单
    def test_ShouLiCheDan(self):
        u"""受理撤单"""
        driver = self.driver
        autocase11yue.test_FuWoHaoMaLoad(self,'18798907431')
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='业务示例'])[1]/following::div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='改号关联关系取消'])[1]/following::li[1]").click()
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_69"]'))
        driver.find_element_by_id("qryBox").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='开始时间'])[1]/following::span[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='分期支付'])[1]/following::div[9]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='分期支付'])[1]/following::div[7]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='六'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='结束时间'])[1]/following::span[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='六'])[1]/following::span[28]").click()
        driver.find_element_by_id("queryButton").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='受理区县'])[1]/following::td[1]").click()
        driver.find_element_by_id("CSSUBMIT_BUTTON").click()
        time.sleep(3)
        driver.find_element_by_id("sofeeconfirmButton").click()
        messageA=driver.find_element_by_xpath('//*[@id="wade_messagebox-8a125e7591b006eb0ef5b279bed54fab_title"]').text
        print messageA
        if messageA==u'错误提示':
            print u"受理撤单失败"
        else:
            print u"受理撤单成功"
    
    def test_HuanHao(self):
        u"""换号"""
        driver = self.driver
        autocase11yue.test_FuWoHaoMaLoad(self, '13518972376')
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='业务示例'])[1]/following::div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='跨省补换卡'])[2]/following::li[1]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_69"]'))
        time.sleep(2)
        piupiupiu=driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div[2]').text
        #/html/body/div/div/div[2]/div[1]/div[2]
        #/html/body/div[starts-with(@class,content)]
        print piupiupiu
        #time.sleep(30)
    def test_FufeiGuanXiQuery(self):
        u"""付费关系查询"""
        driver = self.driver
        autocase11yue.test_FuWoHaoMaLoad(self, "13518972376")
        time.sleep(2)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='业务示例'])[1]/following::div[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='交换机'])[1]/following::li[1]").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_69"]'))
        driver.find_element_by_id("queryByTel").click()
        time.sleep(3)
        driver.find_element_by_id("myQryTab_tab_li_5").click()
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="consumeRelationship"]'))
        aaa=driver.find_element_by_xpath('//*[starts-with(@id,table2)]').text
        print aaa
#         forFUfri=driver.find_element_by_xpath('//*[@id="table2"]/div/div/table/tbody/tr/td[1]').text
#         res_tr = r'<td>(.*?)</td>'
#         m_tr = re.findall(res_tr,aaa)
#         print m_tr
                
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
        
#     def getFile(self,test_dir):
#         u"""获取报告路径"""
#         #列举test_dir目录下的所有文件，结果以列表形式返回。
#         lists=os.listdir(test_dir)
#         #sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
#         #最后对lists元素，按文件修改时间大小从小到大排序。
#         lists.sort(key=lambda fn:os.path.getmtime(test_dir+'\\'+fn))
#         #获取最新文件的绝对路径
#         file_path=os.path.join(test_dir,lists[-1])
#     #    L=file_path.split('\\')
#     #    file_path='\\\\'.join(L)
#         return file_path
#         print file_path
    
    

if __name__ == "__main__":
    #unittest.main()#运行所有test开头的测试用例
    testunit=unittest.TestSuite()
    #将测试用例加入到测试容器中
#     testunit.addTest(autocase11yue("test_GetOrderErrPrint"))
    testunit.addTest(autocase11yue("test_IdentifityHMD"))
#     testunit.addTest(autocase11yue("test_YiZhengWuHao"))
#     testunit.addTest(autocase11yue("test_QianFei"))
#     testunit.addTest(autocase11yue("test_YiZhengDuoMing"))
#     testunit.addTest(autocase11yue("test_HLR_ADD"))
#     testunit.addTest(autocase11yue("test_IMS_HLR_ADD"))
#     testunit.addTest(autocase11yue("test_ShouLiCheDan"))
#     testunit.addTest(autocase11yue("test_HuanHao"))
#     testunit.addTest(autocase11yue("test_FufeiGuanXiQuery"))
    #获取当前时间，这样便于下面的使用。
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
    #打开一个文件，将result写入此file中
    fp=open("result"+now+".html",'wb')
    runner=HTMLTestRunnerA.HTMLTestRunner(stream=fp,title='Test Report',description=u'南基五期新CRM个人业务自动化测试,test by taozhan')
    runner.run(testunit) 
    fp.close()
    #瞎JB写，调用getFile方法输出报告路径
#     test_report_dir='D:\pythontest\testresult'
#     new_report=autocase11yue.getFile(test_report_dir)
    
    
