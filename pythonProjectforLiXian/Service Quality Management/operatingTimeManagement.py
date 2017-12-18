# coding = utf-8
import time

import selenium
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("http://118.178.253.144:8080/itsm")  # 打开网页
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
browser.find_element_by_id('menu_li_id').find_element_by_xpath('li[2]/a[1]').click()
time.sleep(1)
oldFrameCut = len(
    browser.find_element_by_id('maincontent').find_element_by_xpath('div[1]/div[1]').find_element_by_class_name(
        'main').find_elements_by_tag_name('iframe'))
# 点击【运营时间管理】
browser.find_element_by_id('menu_li_id').find_element_by_xpath('li[2]/ul[1]/li[5]/a[1]').click()
time.sleep(2)
# iframe切换
iframe = browser.find_element_by_id('maincontent').find_element_by_xpath('div[1]/div[1]').find_element_by_class_name(
    'main').find_elements_by_tag_name('iframe')[oldFrameCut]
browser.switch_to_frame(iframe)
time.sleep(1)
#新增运营时间，判断是否新增成功
def addOperatingTime(operating_time_name):
    browser.find_element_by_class_name('iconsh-plus').click()
    time.sleep(1)
    browser.find_element_by_id('optime_div').find_element_by_xpath('table[1]/tbody[1]/tr[1]/td[2]/div[1]/input[2]').send_keys(operating_time_name)
    time.sleep(1)
    browser.find_element_by_id('optime_div').find_element_by_xpath('table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[1]/div[1]/i[1]').click()
    workingTime_o=browser.find_element_by_id('optime_div').find_element_by_xpath('table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[1]/div[2]/ul[1]/li[2]')
    workingTime=workingTime_o.text
    workingTime_o.click()
    browser.find_element_by_id('optime_div').find_element_by_xpath('table[1]/tbody[1]/tr[3]/td[2]/div[1]/div[1]/div[1]/i[1]').click()
    holiday_o=browser.find_element_by_id('optime_div').find_element_by_xpath('table[1]/tbody[1]/tr[3]/td[2]/div[1]/div[1]/div[2]/ul[1]/li[2]')
    holiday=holiday_o.text
    holiday_o.click()
    browser.find_element_by_id('btn_submit').click()
    time.sleep(2)
    operatingTimeResult=browser.find_element_by_id('baseTable').find_elements_by_xpath('tbody[1]/tr')
    operatingTimeNameResult=[]
    workingTimeNameResult=[]
    holidayTimeNameResult=[]
    for i in operatingTimeResult:
        operatingTimeNameResult.append(i.find_element_by_xpath('td[3]').text)
        workingTimeNameResult.append(i.find_element_by_xpath('td[5]/a[1]').text)
        holidayTimeNameResult.append(i.find_element_by_xpath('td[6]/a[1]').text)
    if operating_time_name in operatingTimeNameResult and workingTime in workingTimeNameResult and holiday in holidayTimeNameResult:
        print('运营时间新增成功')
    else:
        print('运营时间新增失败')
operatingTimeName='测试运营时间'
addOperatingTime(operatingTimeName)
#模糊查询运营时间
def selectOperatingTime(operating_time_name):
    time.sleep(1)
    browser.find_element_by_id('keyWord').clear()
    time.sleep(1)
    browser.find_element_by_id('keyWord').send_keys(operating_time_name)
    browser.find_element_by_class_name('iconsh-search1').click()
    time.sleep(2)
#修改运营时间
def editOperatingTime(edit_operating_time_name):
    selectOperatingTime(operatingTimeName)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]/label[1]/input[1]').click()
    browser.find_element_by_class_name('iconsh-edit').click()
    time.sleep(1)
    browser.find_element_by_id('optime_div').find_element_by_xpath('table[1]/tbody[1]/tr[1]/td[2]/div[1]/input[2]').clear()
    time.sleep(1)
    browser.find_element_by_id('optime_div').find_element_by_xpath('table[1]/tbody[1]/tr[1]/td[2]/div[1]/input[2]').send_keys(edit_operating_time_name)  # 通过第一个节点找平级的第二个节点
    browser.find_element_by_id('btn_submit').click()
    time.sleep(2)
    editOperatingTimeResult=browser.find_element_by_id('baseTable').find_elements_by_xpath('tbody[1]/tr/td[3]')
    editOperatingTimeResults=[]
    for i in editOperatingTimeResult:
        editOperatingTimeResults.append(i.text)
    if edit_operating_time_name in editOperatingTimeResults:
        print('运营时间修改成功')
    else:
        print('运营时间修改失败')
editOperatingTimeName='编辑测试运营时间'
editOperatingTime(editOperatingTimeName)
#默认时间设置
def defaultTimeSetting():
    selectOperatingTime(operatingTimeName)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[7]/div[1]/a[1]').click()
    browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
    time.sleep(2)
    defaultTimeSettingResult=browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[4]/span[1]').text
    if defaultTimeSettingResult =='是':
        print('默认运营时间设置成功')
    else:
        print('默认运营时间设置失败')
defaultTimeSetting()
#删除运营时间
def deleteOperatingTime(edit_operating_time_name):
    selectOperatingTime(operatingTimeName)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]/label[1]/input[1]').click()
    browser.find_element_by_class_name('iconsh-delete').click()
    time.sleep(2)
    editOperatingTimeResult=browser.find_element_by_id('baseTable').find_elements_by_xpath('tbody[1]/tr/td[3]')
    editOperatingTimeResults=[]
    for i in editOperatingTimeResult:
        editOperatingTimeResults.append(i.text)
    if edit_operating_time_name in editOperatingTimeResults:
        print('运营时间修改失败')
    else:
        print('运营时间修改成功')
deleteOperatingTime(editOperatingTimeName)