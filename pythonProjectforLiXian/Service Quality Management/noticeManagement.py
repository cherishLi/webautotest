# coding = utf-8
import time

import selenium
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("http://127.0.0.1:8080/itsm")  # 打开网页
browser.maximize_window()
# #填写用户名
browser.find_element_by_id('accountNameId').send_keys('admin#jingyu')
# #填写密码
browser.find_element_by_id('passwordId').send_keys('1')
# time.sleep(10)
browser.find_element_by_id('verifyCodeId').send_keys('8888')
# #手动
# #点击【登录】
browser.find_element_by_id('loginBtn').click()
time.sleep(5)
# 点击【基础功能】
browser.find_element_by_xpath(
    "//div[@id='main-container']/div[1]/div[@id='sidebar']/div[@id='sidebar-shortcuts']/div[@id='sidebar-shortcuts-large']/button[2]").click()
time.sleep(2)
# 点击【服务质量管理】
browser.find_element_by_id('menu_li_id').find_element_by_xpath('li[3]/a[1]').click()
time.sleep(1)
oldFrameCut = len(
    browser.find_element_by_id('maincontent').find_element_by_xpath('div[1]/div[1]').find_element_by_class_name(
        'main').find_elements_by_tag_name('iframe'))
# 点击【通知管理】
browser.find_element_by_id('menu_li_id').find_element_by_xpath('li[3]/ul[1]/li[6]/a[1]').click()
time.sleep(2)
# iframe切换
iframe = browser.find_element_by_id('maincontent').find_element_by_xpath('div[1]/div[1]').find_element_by_class_name(
    'main').find_elements_by_tag_name('iframe')[oldFrameCut]
browser.switch_to_frame(iframe)
time.sleep(1)

#新增通知
def addNotice(notice_title,notice_theme,mail_content,sms_content,user_be_noticed):
    browser.find_element_by_class_name('iconsh-plus').click()
    time.sleep(1)
    browser.find_element_by_id('alarmDiv').find_element_by_xpath('table[1]/tbody[1]/tr[1]/td[2]/div[1]/input[1]').send_keys(notice_title)
    browser.find_element_by_id('alarmDiv').find_element_by_xpath('table[1]/tbody[1]/tr[2]/td[2]/div[1]/label[1]/input[1]').click()
    browser.find_element_by_id('alarmDiv').find_element_by_xpath('table[1]/tbody[1]/tr[2]/td[4]/div[1]/label[1]/input[1]').click()
    browser.find_element_by_id('alarmTheme').send_keys(notice_theme)
    browser.find_element_by_id('mailContent').send_keys(mail_content)
    browser.find_element_by_id('smsContent').send_keys(sms_content)
    browser.find_element_by_id('addAccount').click()
    time.sleep(2)
    browser.find_element_by_id('accountForm').find_element_by_xpath('div[1]/input[1]').send_keys(user_be_noticed)
    browser.find_element_by_id('searchAccount').click()
    time.sleep(1)
    browser.find_element_by_id('accountTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]/label[1]/input[1]').click()
    browser.find_element_by_id('saveAccount').click()
    time.sleep(1)
    browser.find_element_by_id('btn_submit').click()
    time.sleep(3)
    result=browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[2]').text
    if result =='提交成功!':
        browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
        print('通知添加成功')
    else:
        print('通知添加失败')
noticeTitle='测试通知标题'
noticeTheme='测试通知主题'
mailContent='测试通知邮件内容'
smsContent='测试通知短信内容'
userbeNoticed='经理'
addNotice(noticeTitle,noticeTheme,mailContent,smsContent,userbeNoticed)
time.sleep(2)

#模糊查询通知
def selectNotice(notice_title):
    browser.find_element_by_id('keyWord').clear()
    time.sleep(1)
    browser.find_element_by_id('keyWord').send_keys(notice_title)
    time.sleep(1)
    browser.find_element_by_id('searchBtn').click()
    time.sleep(2)
#修改查询通知
def editNotice(edit_notice_title):
    selectNotice(noticeTitle)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]/label[1]/input[1]').click()
    browser.find_element_by_class_name('iconsh-edit').click()
    browser.find_element_by_id('alarmDiv').find_element_by_xpath('table[1]/tbody[1]/tr[1]/td[2]/div[1]/input[1]').clear()
    time.sleep(2)
    browser.find_element_by_id('alarmDiv').find_element_by_xpath('table[1]/tbody[1]/tr[1]/td[2]/div[1]/input[1]').send_keys(edit_notice_title)
    time.sleep(1)
    browser.find_element_by_id('btn_submit').click()
    time.sleep(3)
    result=browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[2]').text
    if result =='提交成功!':
        browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
        print('通知修改成功')
    else:
        print('通知修改失败')
editNoticeTitle='编辑测试通知标题'
editNotice(editNoticeTitle)

#删除通知
def deleteNotice():
    selectNotice(editNoticeTitle)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]/label[1]/input[1]').click()
    browser.find_element_by_class_name('iconsh-delete').click()
    time.sleep(1)
    browser.find_element_by_id('jyConfirm').find_element_by_xpath('//parent::div/div[3]/div[1]/button[1]').click()
    time.sleep(2)
    result=browser.find_element_by_id('jyInfo').find_element_by_xpath('div[1]/h5[1]/span[1]').text
    if result =='删除成功！':
        time.sleep(1)
        #browser.find_element_by_id('jyInfo').find_element_by_xpath('//parent::div/div[3]/div[1]/button[1]').click()
        browser.find_element_by_xpath("//div[@id='jyInfo']/../div[3]/div[1]/button[1]").click()
        print('通知删除成功')
    else:
        print('通知删除失败')
deleteNotice()
browser.switch_to.parent_frame()
browser.find_element_by_id('navbar-container').find_element_by_xpath('div[2]/ul[1]/li[3]/a[1]').click()
browser.find_element_by_id('user-menu').find_element_by_xpath('li[5]/a[1]').click()
time.sleep(1)
browser.find_element_by_class_name('ui-dialog-buttons').find_element_by_xpath('div[3]/div[1]/button[1]').click()
browser.close()