import time
import pymysql
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
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
time.sleep(2)
# 点击【基础功能】
browser.find_element_by_xpath(
    "//div[@id='main-container']/div[1]/div[@id='sidebar']/div[@id='sidebar-shortcuts']/div[@id='sidebar-shortcuts-large']/button[2]").click()
time.sleep(1)
# 点击【业务信息管理】
browser.find_element_by_id('menu_li_id').find_element_by_xpath('li[5]/a[1]').click()
time.sleep(1)
oldFrameCut = len(
    browser.find_element_by_id('maincontent').find_element_by_xpath('div[1]/div[1]').find_element_by_class_name(
        'main').find_elements_by_tag_name('iframe'))
# 点击【事件优先级定义】
browser.find_element_by_id('menu_li_id').find_element_by_xpath('li[5]/ul[1]/li[3]/a[1]').click()
time.sleep(2)
# iframe切换
iframe = browser.find_element_by_id('maincontent').find_element_by_xpath('div[1]/div[1]').find_element_by_class_name(
    'main').find_elements_by_tag_name('iframe')[oldFrameCut]
browser.switch_to_frame(iframe)
time.sleep(3)
#优先级计算公式界面，修改优先级维度表
def editPriority():
    browser.find_element_by_id('formulaTable').find_element_by_xpath('tbody[1]/tr[1]/td[3]/select[1]').click()
    browser.find_element_by_id('formulaTable').find_element_by_xpath('tbody[1]/tr[1]/td[3]/select[1]/option[3]').click()
    browser.find_element_by_id('formulaTable').find_element_by_xpath('tbody[1]/tr[1]/td[3]/select[1]').click()
    time.sleep(1)
    result=browser.find_element_by_class_name('layui-layer-hui').find_element_by_xpath('div[1]').text
    if result == '保存成功':
        print('事件优先级修改成功')
        browser.find_element_by_id('formulaTable').find_element_by_xpath('tbody[1]/tr[1]/td[3]/select[1]/option[2]').click()
        browser.find_element_by_id('formulaTable').find_element_by_xpath('tbody[1]/tr[1]/td[3]/select[1]').click()
        time.sleep(2)
    else:
        print('事件优先级修改失败')
editPriority()
#切换到影响程度界面
browser.find_element_by_id('myTab').find_element_by_xpath('li[2]').click()
#修改影响程度优先级
def editInfluencePriority():
    browser.find_element_by_id('table').find_element_by_xpath('tbody[1]/tr[1]/td[1]/input[2]').clear()
    time.sleep(3)
    browser.find_element_by_id('table').find_element_by_xpath('tbody[1]/tr[1]/td[1]/input[2]').send_keys('29')
    browser.find_element_by_id('table').find_element_by_xpath('tbody[1]/tr[1]/td[1]').click()
    time.sleep(2)
    result=browser.find_element_by_class_name('layui-layer-hui').find_element_by_xpath('div[1]').text
    if result == '保存成功':
        print('影响程度优先级修改成功')
        browser.find_element_by_id('table').find_element_by_xpath('tbody[1]/tr[1]/td[1]/input[2]').clear()
        browser.find_element_by_id('table').find_element_by_xpath('tbody[1]/tr[1]/td[1]/input[2]').send_keys('30')
        browser.find_element_by_id('table').find_element_by_xpath('tbody[1]/tr[1]/td[1]').click()
        time.sleep(2)
    else:
        print('影响程度优先级修改失败')
editInfluencePriority()
#新增影响程度
def addInfluence(attr,value,description):
    browser.find_element_by_class_name('iconsh-plus').click()
    browser.find_element_by_id('attr').send_keys(attr)
    time.sleep(1)
    browser.find_element_by_id('value').send_keys(value)
    browser.find_element_by_id('description').send_keys(description)
    time.sleep(2)
    browser.find_element_by_id('btn_submit').click()
    time.sleep(2)
    result = browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[2]').text
    if result == '保存成功':
        print('影响程度添加成功')
        browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
        time.sleep(2)
    else:
        print('影响程度添加失败')
influenceAttr='测试'
influenceValue='33'
influenceDescription='测试描述'
addInfluence(influenceAttr,influenceValue,influenceDescription)
#模糊查询影响程度
def selectInfluence(attr):
    browser.find_element_by_id('keyWord').clear()
    browser.find_element_by_id('keyWord').send_keys(attr)
    browser.find_element_by_id('searchBtn').click()
    time.sleep(2)
#修改影响程度
def editInfluence(attr,description):
    selectInfluence(influenceAttr)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]/label[1]/input[1]').click()
    browser.find_element_by_class_name('iconsh-edit').click()
    browser.find_element_by_id('attr').clear()
    browser.find_element_by_id('attr').send_keys(attr)
    browser.find_element_by_id('description').clear()
    browser.find_element_by_id('description').send_keys(description)
    browser.find_element_by_id('btn_submit').click()
    time.sleep(1)
    result = browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[2]').text
    if result == '保存成功':
        print('影响程度修改成功')
        browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
        time.sleep(2)
    else:
        print('影响程度修改失败')
editAttr='编辑测试'
editDescription='编辑测试描述'
editInfluence(editAttr,editDescription)
#删除影响程度
def deleteInfluence():
    selectInfluence(influenceAttr)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]/label[1]/input[1]').click()
    browser.find_element_by_class_name('btn-danger').click()
    time.sleep(2)
    browser.find_element_by_class_name('ui-dialog-buttons').find_element_by_xpath('div[3]/div[1]/button[1]').click()
    time.sleep(2)
    result = browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]').text
    if result == '没有相关数据':
        print('影响程度删除成功')
        time.sleep(2)
    else:
        print('影响程度删除失败')
deleteInfluence()
#切换到紧急程度界面
browser.find_element_by_id('myTab').find_element_by_xpath('li[3]').click()
time.sleep(1)
#新增紧急程度
def addUrgency(attr,value,description):
    browser.find_element_by_class_name('iconsh-plus').click()
    browser.find_element_by_id('attr').send_keys(attr)
    time.sleep(1)
    browser.find_element_by_id('value').send_keys(value)
    browser.find_element_by_id('description').send_keys(description)
    browser.find_element_by_id('btn_submit').click()
    time.sleep(1)
    result = browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[2]').text
    if result == '保存成功':
        print('紧急程度添加成功')
        browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
        time.sleep(2)
    else:
        print('紧急程度添加失败')
urgencyAttr='测试'
urgencyValue='33'
urgencyDescription='测试描述'
addUrgency(urgencyAttr,urgencyValue,urgencyDescription)
#模糊查询紧急程度
def selectUrgency(attr):
    browser.find_element_by_id('keyWord').clear()
    browser.find_element_by_id('keyWord').send_keys(attr)
    browser.find_element_by_id('searchBtn').click()
    time.sleep(2)
#修改紧急程度
def editUrgency(attr,description):
    selectUrgency(urgencyAttr)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]/label[1]/input[1]').click()
    browser.find_element_by_class_name('iconsh-edit').click()
    browser.find_element_by_id('attr').clear()
    browser.find_element_by_id('attr').send_keys(attr)
    browser.find_element_by_id('description').clear()
    browser.find_element_by_id('description').send_keys(description)
    browser.find_element_by_id('btn_submit').click()
    time.sleep(1)
    result = browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[2]').text
    if result == '保存成功':
        print('紧急程度修改成功')
        browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
        time.sleep(2)
    else:
        print('紧急程度修改失败')
editUrgency(editAttr,editDescription)
#删除紧急程度
def deleteUrgency():
    selectUrgency(urgencyAttr)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]/label[1]/input[1]').click()
    browser.find_element_by_class_name('btn-danger').click()
    time.sleep(2)
    browser.find_element_by_class_name('ui-dialog-buttons').find_element_by_xpath('div[3]/div[1]/button[1]').click()
    time.sleep(2)
    result = browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]').text
    if result == '没有相关数据':
        print('紧急程度删除成功')
        time.sleep(2)
    else:
        print('紧急程度删除失败')
deleteUrgency()
browser.switch_to.parent_frame()
browser.find_element_by_id('navbar-container').find_element_by_xpath('div[2]/ul[1]/li[3]/a[1]').click()
browser.find_element_by_id('user-menu').find_element_by_xpath('li[5]/a[1]').click()
time.sleep(1)
browser.find_element_by_class_name('ui-dialog-buttons').find_element_by_xpath('div[3]/div[1]/button[1]').click()
browser.close()