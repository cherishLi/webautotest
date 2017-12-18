import time
import pymysql
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
browser = webdriver.Chrome()
browser.get("http://127.0.0.1:8080/itsm")  # 打开网页
# #填写用户名
browser.find_element_by_id('accountNameId').send_keys('nima')
# #填写密码
browser.find_element_by_id('passwordId').send_keys('1')
# time.sleep(10)
browser.find_element_by_id('verifyCodeId').send_keys('4123')
# #手动
# #点击【登录】
browser.find_element_by_id('loginBtn').click()
time.sleep(2)
# 点击【基础功能】
browser.find_element_by_xpath(
    "//div[@id='main-container']/div[1]/div[@id='sidebar']/div[@id='sidebar-shortcuts']/div[@id='sidebar-shortcuts-large']/button[2]").click()
time.sleep(1)
# 点击【服务质量管理】
browser.find_element_by_id('menu_li_id').find_element_by_xpath('li[2]/a[1]').click()
time.sleep(1)
oldFrameCut = len(
    browser.find_element_by_id('maincontent').find_element_by_xpath('div[1]/div[1]').find_element_by_class_name(
        'main').find_elements_by_tag_name('iframe'))
# 点击【运营级别管理】
browser.find_element_by_id('menu_li_id').find_element_by_xpath('li[2]/ul[1]/li[2]/a[1]').click()
time.sleep(2)
# iframe切换
iframe = browser.find_element_by_id('maincontent').find_element_by_xpath('div[1]/div[1]').find_element_by_class_name(
    'main').find_elements_by_tag_name('iframe')[oldFrameCut]
browser.switch_to_frame(iframe)
time.sleep(1)
#新增运营级别
def addOperationLevel(ola_name,ola_name_description):
    browser.find_element_by_class_name('iconsh-plus').click()
    time.sleep(1)
    browser.find_element_by_id('servicelevel_div').find_element_by_xpath('table[1]/tbody[1]/tr[2]/td[2]/div[1]/input[2]').send_keys(ola_name)
    browser.find_element_by_id('servicelevel_div').find_element_by_xpath('table[1]/tbody[1]/tr[3]/td[2]/div[1]').click()
    browser.find_element_by_id('itemsD').find_element_by_xpath('li[2]').click()
    browser.find_element_by_id('description').send_keys(ola_name_description)
    browser.find_element_by_id('btn_submit').click()
    time.sleep(1)
olaName='运营级别测试'
olaNameDescription='运营级别测试描述'
addOperationLevel(olaName,olaNameDescription)
#判断是否新增成功
def isSucessful():
    result=browser.find_element_by_id('baseTable').find_elements_by_xpath('tbody[1]/tr/td[3]')
    flag = -1
    for i in result:
        if i.text==olaName:
            flag = 1
            break
    if flag == 1:
        print('运营级别添加成功')
    else:
        print('运营级别添加失败')
isSucessful()
#模糊查询运营级别
def selectOperationLevel(ola_name):
    browser.find_element_by_id('keyWord').clear()
    browser.find_element_by_id('keyWord').send_keys(ola_name)
    browser.find_element_by_class_name('iconsh-search1').click()
    time.sleep(2)
#修改运营级别
def editOperationLevel(ola_name,ola_name_description):
    selectOperationLevel(olaName)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]/label[1]/input[1]').click()
    browser.find_element_by_class_name('iconsh-edit').click()
    time.sleep(1)
    browser.find_element_by_id('servicelevel_div').find_element_by_xpath('table[1]/tbody[1]/tr[2]/td[2]/div[1]/input[2]').clear()
    browser.find_element_by_id('servicelevel_div').find_element_by_xpath('table[1]/tbody[1]/tr[2]/td[2]/div[1]/input[2]').send_keys(ola_name)
    browser.find_element_by_id('servicelevel_div').find_element_by_xpath('table[1]/tbody[1]/tr[3]/td[2]/div[1]').click()
    browser.find_element_by_id('itemsD').find_element_by_xpath('li[3]').click()
    browser.find_element_by_id('description').clear()
    browser.find_element_by_id('description').send_keys(ola_name_description)
    browser.find_element_by_id('btn_submit').click()
    time.sleep(2)
    result=browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[3]').text
    if result == ola_name:
        print('运营级别修改成功')
    else:
        print('运营级别修改失败')
editOlaName='编辑运营级别测试'
editOlaNameDescription='编辑运营级别测试描述'
editOperationLevel(editOlaName,editOlaNameDescription)
#新增运营级别配置
def addOperationLevelSetting(target_time):
    selectOperationLevel(olaName)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]/label[1]/input[1]').click()
    browser.find_element_by_class_name('iconsh-setting').click()
    iframe= browser.find_element_by_class_name('layui-layer-content').find_element_by_xpath('iframe[1]')
    browser.switch_to_frame(iframe)
    browser.find_element_by_id('accordion').find_element_by_xpath('div[1]/div[1]/h4[1]/a[1]').click()
    browser.find_element_by_id('usertask2').find_element_by_xpath('div[1]/table[1]/tbody[1]/tr[1]/td[4]/div[2]/span[1]').click()
    browser.find_element_by_id('process_div').find_element_by_xpath('table[1]/tbody[1]/tr[1]/td[2]/input[1]').send_keys(target_time)
    browser.find_element_by_id('process_div').find_element_by_xpath('table[1]/tbody[1]/tr[2]/td[2]/div[1]/label[1]').click()
    classify=browser.find_element_by_id('process_div').find_element_by_xpath('table[1]/tbody[1]/tr[2]/td[2]/div[1]/label[1]/span[1]').text
    browser.find_element_by_id('process_div').find_element_by_xpath('table[1]/tbody[1]/tr[3]/td[2]/select[1]').click()
    browser.find_element_by_id('process_div').find_element_by_xpath('table[1]/tbody[1]/tr[3]/td[2]/select[1]/option[2]').click()
    browser.find_element_by_id('process_div').find_element_by_xpath('table[1]/tbody[1]/tr[4]/td[2]/textarea[1]').send_keys(target_time)
    browser.find_element_by_id('btn_submit').click()
    time.sleep(1)
    alert = browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[2]').text
    browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
    time.sleep(2)
    result=browser.find_element_by_id('usertask2').find_element_by_xpath('div[1]/table[1]/tbody[1]/tr[1]/td[4]/div[1]/ul[1]/li[1]/span[1]').text
    joint=classify+str(target_time)+'分钟'
    if result==joint and alert=='保存成功!':
        print('告警策略配置成功')
    else:
        print('告警策略配置失败')
targetTime=2
addOperationLevelSetting(targetTime)
#修改运营级别配置
def editOperationLevelSetting(target_time):
    #browser.find_element_by_id('accordion').find_element_by_xpath('div[1]/div[1]/h4[1]/a[1]').click()
    time.sleep(1)
    browser.find_element_by_id('usertask2').find_element_by_xpath('div[1]/table[1]/tbody[1]/tr[1]/td[4]/div[1]/ul[1]/li[1]').click()
    time.sleep(1)
    browser.find_element_by_id('process_div').find_element_by_xpath('table[1]/tbody[1]/tr[1]/td[2]/input[1]').clear()
    browser.find_element_by_id('process_div').find_element_by_xpath('table[1]/tbody[1]/tr[1]/td[2]/input[1]').send_keys(target_time)
    browser.find_element_by_id('process_div').find_element_by_xpath('table[1]/tbody[1]/tr[4]/td[2]/textarea[1]').clear()
    browser.find_element_by_id('process_div').find_element_by_xpath('table[1]/tbody[1]/tr[4]/td[2]/textarea[1]').send_keys(target_time)
    classify = browser.find_element_by_id('process_div').find_element_by_xpath('table[1]/tbody[1]/tr[2]/td[2]/div[1]/label[1]/span[1]').text
    browser.find_element_by_id('btn_submit').click()
    time.sleep(1)
    alert = browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[2]').text
    browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
    time.sleep(2)
    result = browser.find_element_by_id('usertask2').find_element_by_xpath(
        'div[1]/table[1]/tbody[1]/tr[1]/td[4]/div[1]/ul[1]/li[1]/span[1]').text
    joint = classify + str(target_time) + '分钟'
    if result == joint and alert == '保存成功!':
        print('告警策略修改成功')
    else:
        print('告警策略修改失败')
editOperationLevelSetting(3)
#计时策略设置
def cumulativeTiming():
    browser.find_element_by_id('usertask2').find_element_by_xpath('div[1]/table[1]/tbody[1]/tr[1]/td[2]/label[1]/input[1]').click()
    time.sleep(1)
    browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
    time.sleep(1)
    result = browser.find_element_by_class_name('layui-layer-hui').find_element_by_xpath('div[1]').text
    if result == '修改计时策略成功！':
        print('计时策略配置成功')
    else:
        print('计时策略配置失败')
cumulativeTiming()
#删除运营级别配置
def deleteOperationLevelSetting():
    browser.find_element_by_id('usertask2').find_element_by_xpath('div[1]/table[1]/tbody[1]/tr[1]/td[4]/div[1]/ul[1]/li[1]/a[1]').click()
    time.sleep(1)
    browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
    time.sleep(1)
    result = browser.find_element_by_class_name('layui-layer-hui').find_element_by_xpath('div[1]').text
    if result == '删除成功！':
        print('告警策略删除成功')
    else:
        print('告警策略删除成功')
    time.sleep(1)
    browser.switch_to.parent_frame()
    #browser.switch_to.default_content()
    #browser.switch_to.frame(0)
    #browser.find_element_by_id('servicelevel_div')
    browser.find_element_by_class_name('layui-layer-close1').click()
deleteOperationLevelSetting()
#删除运营级别
def deleteOperationLevel():
    selectOperationLevel(olaName)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]/label[1]/input[1]').click()
    browser.find_element_by_class_name('iconsh-delete').click()
    time.sleep(1)
    result=browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[2]').text
    if result == '确认删除选中的数据吗？':
        browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
        time.sleep(1)
        result2 = browser.find_element_by_class_name('layui-layer-hui').find_element_by_xpath('div[1]').text
        if result2 == '数据删除成功！':
            print('运营级别删除成功')
        else:
            print('运营级别删除成功')
deleteOperationLevel()
browser.close()
