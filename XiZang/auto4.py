# -*- coding: utf-8 -*-
'''
Created on 2019年4月26日

@author: Taozhan
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import HTMLTestRunnerA
import cx_Oracle
import os
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class HKautocase04(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def test_AccessLoad(self,access_num):
        #供后续复用
        u"""服务号码登录"""
        driver = self.driver
        driver.get("http://172.17.24.75:8080/web-ngboss?")
        driver.find_element_by_id("STAFF_ID").click()
        driver.find_element_by_id("STAFF_ID").clear()
        driver.find_element_by_id("STAFF_ID").send_keys("91110029")
        driver.find_element_by_id("PASSWORD").click()
        driver.find_element_by_id("PASSWORD").clear()
        driver.find_element_by_id("PASSWORD").send_keys("123456")
        driver.find_element_by_id("loginBtn").click()
        time.sleep(2)
        #去掉系统提示弹窗
        driver.find_element_by_xpath('/html/body/div[9]/div[1]/div[2]/div/div/div[2]/button[1]').click()
        driver.find_element_by_id("NO_PASSWORD_LOGIN_CHECKBOX").click()
        driver.find_element_by_id("LOGIN_NUM").click()
        driver.find_element_by_id("LOGIN_NUM").clear()
        driver.find_element_by_id("LOGIN_NUM").send_keys(access_num)
        driver.find_element_by_id("LOGIN_BTN").click()
        time.sleep(3)
    
    def test_(self):
        u'''Mymobile信息查询'''
        #页面功能未完善，暂仅测试页面进入
        driver=self.driver
        HKautocase04.test_AccessLoad(self,'93157018')
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_148"]'))
        #点击Mymobile元素
        driver.find_element_by_xpath('//*[@id="Mymobile"]').click()
        time.sleep(3)
        
        
    def test_VasReset(self):
        u'''VAS服务重置'''
        driver=self.driver
        HKautocase04.test_AccessLoad(self,'93157018')
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        time.sleep(5)
        driver.find_element_by_id("menus_tab_li_2").click()
        time.sleep(5)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='宽带业务'])[1]/following::div[3]").click()
        driver.find_element_by_id("10000219").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_148"]'))
        #点击【reset】
        driver.find_element_by_xpath('//*[@id="310021_insLi"]').click()
        time.sleep(3)
        #提交订单
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/button').click()
        time.sleep(3)
        #二次确认页面确认提交
        driver.find_element_by_xpath('//*[@id="myDialog"]/div/div[3]/div[1]/button[2]').click()
        time.sleep(5)
        SBwadeKuangJIA="wade_messagebox-(.*?)_ct"
        resB=driver.find_element_by_xpath('//*[starts-with(@id,SBwadeKuangJIA)]').text
        order_idB = re.search( r'\d{15}', resB).group(0)
        print order_idB
        
    
    def test_QueryBaseVas(self):
        u'''BASE VAS查询'''
        driver = self.driver
        HKautocase04.test_load(self)
        driver.find_element_by_id("NO_PASSWORD_LOGIN_CHECKBOX").click()
        driver.find_element_by_id("LOGIN_NUM").click()
        driver.find_element_by_id("LOGIN_NUM").clear()
        driver.find_element_by_id("LOGIN_NUM").send_keys("51068332")
        driver.find_element_by_id("LOGIN_BTN").click()
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='停开机'])[1]/following::div[2]").click()
        driver.find_element_by_id("101502").click()
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_128"]'))
        for i in range(1,60):
            XpathA='/html/body/div[1]/div/div[5]/ul/li[]'.format([int(i)])
            Jy005=driver.find_element_by_xpath(XpathA).text
            print Jy005 
        
    def test_QueryExitOffer(self):
        u'''已订购列表数据查询'''
        driver = self.driver
        HKautocase04.test_load(self)
        driver.find_element_by_id("NO_PASSWORD_LOGIN_CHECKBOX").click()
        driver.find_element_by_id("LOGIN_NUM").click()
        driver.find_element_by_id("LOGIN_NUM").clear()
        driver.find_element_by_id("LOGIN_NUM").send_keys("51068332")
        driver.find_element_by_id("LOGIN_BTN").click()
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='停开机'])[1]/following::div[3]").click()
        driver.find_element_by_id("101502").click()
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_128"]'))
        for i in range(1,45):
            XpathA='/html/body/div[1]/div/div[6]/ul/li[]'.format([int(i)])
            Jy005=driver.find_element_by_xpath(XpathA).text
            print Jy005 
        
    def test_QueryOffer(self):
        u'''初始化页面查询组件功能校验'''
        driver = self.driver
        HKautocase04.test_load(self)
        driver.find_element_by_id("NO_PASSWORD_LOGIN_CHECKBOX").click()
        driver.find_element_by_id("LOGIN_NUM").click()
        driver.find_element_by_id("LOGIN_NUM").clear()
        driver.find_element_by_id("LOGIN_NUM").send_keys("96630663")
        driver.find_element_by_id("LOGIN_BTN").click()
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='停开机'])[1]/following::div[3]").click()
        driver.find_element_by_id("101502").click()
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_128"]'))
        driver.find_element_by_xpath('//*[@id="insSearch"]').click()
        driver.find_element_by_xpath('//*[@id="insSearch"]').clear()
        driver.find_element_by_xpath('//*[@id="insSearch"]').send_keys('#SMS Package Intra 8')
        driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[2]/span/button').click()
        time.sleep(5)
        Jy006=driver.find_element_by_xpath('/html/body/div[1]/div/div[6]/ul/li[1]').text
        if Jy006[0:20]=='#SMS Package Intra 8':
            print u"""查询组件功能校验成功"""
        else:
            print u"""查询组件功能校验失败"""
    
    def test_AddButtonClick(self):
        u'''ADD订购主页登录'''
        tns=cx_Oracle.makedsn('172.17.24.68',1522,'hkcrmtst') 
        conn=cx_Oracle.connect('aitest','aitest_1234',tns)
        c=conn.cursor()
        sql="select access_num from (select access_num from ins1.um_subscriber_852 where subscriber_type=1 and subscriber_status=1 and rownum<1000 order by dbms_random.value)  where rownum< 2"
        c.execute(sql)
        rs=c.fetchall() 
        #print rs
        c.close()
        conn.close()    
        driver=self.driver
        y=rs[0]
        HKautocase04.test_AccessLoad(self,y)
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        time.sleep(2)
        driver.find_element_by_id("menus_tab_li_2").click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div/ul/li[6]/div[1]')
        time.sleep(2)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='宽带业务'])[1]/following::div[2]").click()
        driver.find_element_by_id("10000219").click()
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_148"]'))
        if self.isElementPresent('id','insSearch'):
            print u"ADD组件功能正常！"
        else:
            print u"ADD组件功能异常"
        
        
    def test_OfferCataQuery(self):
        u'''OFFER目录查询组件功能校验'''
        driver = self.driver
        HKautocase04.test_AddButtonClick(self)
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="searchOfferkeyWord"]').click()
        driver.find_element_by_xpath('//*[@id="searchOfferkeyWord"]').clear()
        driver.find_element_by_xpath('//*[@id="searchOfferkeyWord"]').send_keys('4G Handset Rebate Contract Upgrade')
        time.sleep(3)
        Jy008=driver.find_element_by_xpath('//*[@id="offerId_311234"]').text
        if Jy008=='4G Handset Rebate Contract Upgrade9':
            print 'Query Success'
        else:
            print 'Query Default'
        
    def test_ADDoffer(self):
        u"""OFFER订购"""
        tns=cx_Oracle.makedsn('172.17.24.68',1522,'hkcrmtst') 
        conn=cx_Oracle.connect('aitest','aitest_1234',tns)
        c=conn.cursor()
        sql="select access_num from (select access_num from ins1.um_subscriber_852 where subscriber_type=1 and subscriber_status=1 and rownum<1000 order by dbms_random.value)  where rownum< 2"
        c.execute(sql)
        rs=c.fetchall() 
        c.close()
        conn.close()    
        driver=self.driver
        y=rs[0]
        HKautocase04.test_AccessLoad(self,y)
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        time.sleep(2)
        driver.find_element_by_id("menus_tab_li_2").click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div/ul/li[6]/div[1]')
        time.sleep(2)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='宽带业务'])[1]/following::div[3]").click()
        driver.find_element_by_id("10000219").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_148"]'))
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/button").click()
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="offerFrame"]'))
        driver.find_element_by_id("offerName_200234").click()
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="iframe1"]'))
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/ul[3]/li[2]/div[2]/span/span/span[1]/span').click()
        driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div[7]/button[3]').click()
        time.sleep(3)
        driver.find_element_by_id("OFFER_BUTTON_SUBMIT").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_148"]'))
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/button').click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div[1]/button[2]').click()
        time.sleep(5)
        SBwadeKuangJIA="wade_messagebox-(.*?)_ct"
        resA=driver.find_element_by_xpath('//*[starts-with(@id,SBwadeKuangJIA)]').text
        order_idA = re.search( r'\d{15}', resA).group(0)
        driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div[2]/button').click()
        print order_idA 
        
    def test_ChangeOfferCha(self):
        u'''OFFER特征值变更'''
        driver=self.driver
        HKautocase04.test_AccessLoad(self,'93163518')
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        time.sleep(5)
        driver.find_element_by_id("menus_tab_li_2").click()
        time.sleep(5)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='宽带业务'])[1]/following::div[3]").click()
        driver.find_element_by_id("10000219").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_148"]'))
        driver.find_element_by_xpath('//*[@id="200021_insLi"]').click()
        time.sleep(5) 
        driver.find_element_by_xpath('//*[@id="chaSpec_152852000032"]').send_keys("333")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="OFFER_BUTTON_CHANGE"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/button').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="myDialog"]/div/div[3]/div[1]/button[2]').click()
        time.sleep(10)
        SBwadeKuangJIA="wade_messagebox-(.*?)_ct"
        resB=driver.find_element_by_xpath('//*[starts-with(@id,SBwadeKuangJIA)]').text
        order_idB = re.search( r'\d{15}', resB).group(0)
        print order_idB 
        
    def test_DeleteOffer(self):
        u'''OFFER退订'''
        tns=cx_Oracle.makedsn('172.17.24.68',1522,'hkcrmtst') 
        conn=cx_Oracle.connect('aitest','aitest_1234',tns)
        c=conn.cursor()
        sql='''select access_num from (select access_num from ins1.um_subscriber_852 where subscriber_type=1 
        and subscriber_status=1 and rownum<1000 order by dbms_random.value)  where rownum< 2'''
        c.execute(sql)
        rs=c.fetchall() 
        #print rs
        c.close()
        conn.close()    
        driver=self.driver
        y=rs[0]
        HKautocase04.test_AccessLoad(self,y)
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        time.sleep(2)
        driver.find_element_by_id("menus_tab_li_2").click()
        time.sleep(2)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='宽带业务'])[1]/following::div[3]").click()
        driver.find_element_by_id("10000219").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_148"]'))
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[6]/ul/li[1]/div[4]").click()#删除
        time.sleep(3) 
        if self.isElementPresent('id','EDIT_EXP_DATE'):#手动录入时间场景
            driver.find_element_by_xpath('//*[@id="EDIT_EXP_DATE"]').click()
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="_Wade_DropDownCalendar_float"]/div[2]/div/div[7]/button[3]').click()
            time.sleep(5)
            driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/div[3]/div/button').click()
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/div[2]/div[1]/button').click()
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div[1]/button[2]').click()
            time.sleep(10)
            SBwadeKuangJIA="wade_messagebox-(.*?)_ct"
            resB=driver.find_element_by_xpath('//*[starts-with(@id,SBwadeKuangJIA)]').text
            order_idB = re.search( r'\d{15}', resB).group(0)
            print order_idB  
        else:#默认生效时间场景
            driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/div[3]/div/button').click()
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/div[2]/div[1]/button').click()
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div[1]/button[2]').click()
            time.sleep(10)
            SBwadeKuangJIA="wade_messagebox-(.*?)_ct"
            resB=driver.find_element_by_xpath('//*[starts-with(@id,SBwadeKuangJIA)]').text
            order_idB = re.search( r'\d{15}', resB).group(0)
            print order_idB

    
    def test_DryNUM(self):
        u'''OFFER受理-销户用户校验'''
        tns=cx_Oracle.makedsn('172.17.24.68',1522,'hkcrmtst') 
        conn=cx_Oracle.connect('aitest','aitest_1234',tns)
        c=conn.cursor()
        sql='select access_num from ins1.UM_SUBSCRIBER_852 where SUBSCRIBER_TYPE=1 and subscriber_status=4' 
        c.execute(sql)
        rs=c.fetchall() 
        #print rs
        c.close()
        conn.close()    
        driver=self.driver
        y=rs[0]
        HKautocase04.test_AccessLoad(self,y)
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        time.sleep(5)
        driver.find_element_by_id("menus_tab_li_2").click()
        time.sleep(5)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='宽带业务'])[1]/following::div[3]").click()
        driver.find_element_by_id("10000219").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_129"]'))
        err1=driver.find_element_by_xpath('/html/body/div/div/div[2]').text
        print err1
        
        
    def test_SuspendNUM(self):
        u'''OFFER受理-停机用户校验'''
        tns=cx_Oracle.makedsn('172.17.24.68',1522,'hkcrmtst') 
        conn=cx_Oracle.connect('aitest','aitest_1234',tns)
        c=conn.cursor()
        sql='''select t.access_num from ins1.um_subscriber_852 t, ins1.um_prod_sta_852 m
            where t.subscriber_ins_id = m.subscriber_ins_id
            and t.data_status = '1'
            and t.subscriber_status = '1'
            and t.subscriber_type = '1'
            and m.prod_status = '2'
            '''
        c.execute(sql)
        rs=c.fetchall() 
        #print rs
        c.close()
        conn.close()   
        driver=self.driver
        y=rs[0]
        HKautocase04.test_AccessLoad(self,y)
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        time.sleep(5)
        driver.find_element_by_id("menus_tab_li_2").click()
        time.sleep(5)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='宽带业务'])[1]/following::div[3]").click()
        driver.find_element_by_id("10000219").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_148"]'))
        err2=driver.find_element_by_xpath('/html/body/div/div/div[2]').text
        print err2
        
    def test_IngOrdNUM(self):
        u'''商品变更在途工单客户OFFER受理'''
        tns=cx_Oracle.makedsn('172.17.24.68',1522,'hkcrmtst') 
        conn=cx_Oracle.connect('aitest','aitest_1234',tns)
        c=conn.cursor()
        sql='''select access_num from ord.om_line where order_id in
         (select order_id from ord.om_order t where t.busi_code ='500140000002')
            '''
        c.execute(sql)
        rs=c.fetchall() 
        #print rs
        c.close()
        conn.close()   
        driver=self.driver
        y=rs[0]
        HKautocase04.test_AccessLoad(self,y)
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        time.sleep(5)
        driver.find_element_by_id("menus_tab_li_2").click()
        time.sleep(5)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='宽带业务'])[1]/following::div[3]").click()
        driver.find_element_by_id("10000219").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_148"]'))
        err3=driver.find_element_by_xpath('/html/body/div/div/div[2]').text
        print err3
        
        
    def test_IngCusNUM(self):
        u'''客户资料在途工单客户OFFER受理'''
        tns=cx_Oracle.makedsn('172.17.24.68',1522,'hkcrmtst') 
        conn=cx_Oracle.connect('aitest','aitest_1234',tns)
        c=conn.cursor()
        sql='''select access_num from ord.om_line where order_id in
         (select order_id from ord.om_order t where t.busi_code ='500220000005')
            '''
        c.execute(sql)
        rs=c.fetchall() 
        #print rs
        c.close()
        conn.close()   
        driver=self.driver
        y=rs[2]
        HKautocase04.test_AccessLoad(self,y)
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        time.sleep(5)
        driver.find_element_by_id("menus_tab_li_2").click()
        time.sleep(5)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='宽带业务'])[1]/following::div[3]").click()
        driver.find_element_by_id("10000219").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_148"]'))
        time.sleep(5)
        #//*[@id="insSearch"]
        if self.isElementPresent('id','insSearch'):
            print u"校验成功！"
        else:
            print u"校验失败"
        
    def test_UnActiveNUM(self):
        u'''开户未激活客户OFFER订购校验'''
        tns=cx_Oracle.makedsn('172.17.24.68',1522,'hkcrmtst') 
        conn=cx_Oracle.connect('aitest','aitest_1234',tns)
        c=conn.cursor()
        sql="select access_num from ins1.UM_SUBSCRIBER_852 where SUBSCRIBER_TYPE=1 and subscriber_status=10"
        c.execute(sql)
        rs=c.fetchall() 
        #print rs
        c.close()
        conn.close()   
        driver=self.driver
        y=rs[0]
        time.sleep(5)
        HKautocase04.test_AccessLoad(self,y)
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        time.sleep(5)
        driver.find_element_by_id("menus_tab_li_2").click()
        time.sleep(5)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='宽带业务'])[1]/following::div[3]").click()
        driver.find_element_by_id("10000219").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_128"]'))
        time.sleep(5)
        #//*[@id="insSearch"]
        if self.isElementPresent('id','insSearch'):
            print u"校验成功！"
        else:
            print u"校验失败"
        
    def test_OfferHC(self):
        u'''OFFER订购互斥校验'''
        driver=self.driver
        HKautocase04.test_AccessLoad(self,"50033104")
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_def"]'))
        driver.find_element_by_id("welTab_tab_li_1").click()
        time.sleep(5)
        driver.find_element_by_id("menus_tab_li_2").click()
        time.sleep(5)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='宽带业务'])[1]/following::div[3]").click()
        driver.find_element_by_id("10000219").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_148"]'))
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/button').click()
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="offerFrame"]'))
        time.sleep(3)
        driver.find_element_by_id("searchOfferkeyWord").click()
        driver.find_element_by_id("searchOfferkeyWord").click()
        driver.find_element_by_id("searchOfferkeyWord").clear()
        driver.find_element_by_id("searchOfferkeyWord").send_keys("300307")
        driver.find_element_by_xpath('//*[@id="searchOffersearchButton"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="offerId_200792"]').click()
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="iframe1"]'))
        driver.find_element_by_xpath('//*[@id="OFFER_BUTTON_SUBMIT"]').click()
        time.sleep(2)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_148"]'))
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/button').click()
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="offerFrame"]'))
        time.sleep(3)
        driver.find_element_by_id("searchOfferkeyWord").click()
        driver.find_element_by_id("searchOfferkeyWord").click()
        driver.find_element_by_id("searchOfferkeyWord").clear()  
        driver.find_element_by_id("searchOfferkeyWord").send_keys("300308")
        driver.find_element_by_xpath('//*[@id="searchOffersearchButton"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="offerId_200348"]').click()
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="iframe2"]'))
        driver.find_element_by_xpath('//*[@id="chaSpec_52223104_152852000017"]').send_keys('888')
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/ul[3]/li[2]/div[2]/span/span/span[1]').click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div[7]/button[3]').click()
        driver.find_element_by_xpath('//*[@id="OFFER_BUTTON_SUBMIT"]').click()
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="navframe_148"]'))
        driver.find_element_by_xpath('/html/body/div[2]/div[1]').click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div[1]/button[2]').click()
        time.sleep(5)
        HC=driver.find_element_by_xpath('html/body/div[8]/div/div[2]/div/div[2]').text
        print HC
        
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
    testunit.addTest(HKautocase04('test_Mymobile'))
    testunit.addTest(HKautocase04('test_VasReset'))
    testunit.addTest(HKautocase04('test_QueryBaseVas'))
    testunit.addTest(HKautocase04('test_QueryExitOffer'))  
    testunit.addTest(HKautocase04('test_QueryOffer'))
    testunit.addTest(HKautocase04('test_AddButtonClick'))
    testunit.addTest(HKautocase04('test_OfferCataQuery'))
    testunit.addTest(HKautocase04('test_ADDoffer'))
    testunit.addTest(HKautocase04('test_ChangeOfferCha'))
    testunit.addTest(HKautocase04('test_DeleteOffer'))
    testunit.addTest(HKautocase04('test_DryNUM'))
    testunit.addTest(HKautocase04('test_SuspendNUM'))
    testunit.addTest(HKautocase04('test_IngOrdNUM'))
    testunit.addTest(HKautocase04('test_IngCusNUM'))
    testunit.addTest(HKautocase04('test_UnActiveNUM'))
    testunit.addTest(HKautocase04('test_OfferHC'))
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))  
    #打开一个文件，将result写入此file中
    fp=open("result"+now+".html",'wb')
    runner=HTMLTestRunnerA.HTMLTestRunner(stream=fp,title='Test Report',description=u'南基五期香港新CRM自动化测试,test by taozhan')
    runner.run(testunit)
    fp.close()