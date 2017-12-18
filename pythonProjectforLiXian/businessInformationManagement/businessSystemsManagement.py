import time

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
# 点击【业务系统管理】
browser.find_element_by_id('menu_li_id').find_element_by_xpath('li[5]/ul[1]/li[4]/a[1]').click()
time.sleep(2)
# iframe切换
iframe = browser.find_element_by_id('maincontent').find_element_by_xpath('div[1]/div[1]').find_element_by_class_name(
    'main').find_elements_by_tag_name('iframe')[oldFrameCut]
browser.switch_to_frame(iframe)
time.sleep(3)
#新增业务系统
def addBusinessSystemsAnalysis(new_busi_code,new_busi_name,new_busi_description):
    browser.find_element_by_id('addBtn').click()
    browser.find_element_by_id('causeForm').find_element_by_xpath('table[1]/tbody[1]/tr[1]/td[2]/input[1]').send_keys(new_busi_code)
    browser.find_element_by_id('causeForm').find_element_by_xpath('table[1]/tbody[1]/tr[2]/td[2]/input[1]').send_keys(new_busi_code)
    browser.find_element_by_id('causeForm').find_element_by_xpath('table[1]/tbody[1]/tr[3]/td[2]/input[1]').send_keys(new_busi_name)
    browser.find_element_by_id('causeForm').find_element_by_xpath('table[1]/tbody[1]/tr[5]/td[2]/textarea[1]').send_keys(new_busi_description)
    browser.find_element_by_id('addSysDict').click()
    time.sleep(2)
newBusiCode=33
newBusiName='测试系统'
newBusiDescription='测试系统的描述'
addBusinessSystemsAnalysis(newBusiCode,newBusiName,newBusiDescription)
def traversal(li,selected):
    if li.find_element_by_xpath('a[1]').get_attribute('title')== selected:
        return li
    try:
        childItems = li.find_elements_by_xpath('ul/li')
        for i in childItems:
            i = traversal(i,selected)
            if (i is not None):
                return i
        return None
    except selenium.common.exceptions.NoSuchElementException:
        return None
#判断是否添加成功
def isSusscessful():
    rootLi = browser.find_element_by_id('Tree_1')
    result=traversal(rootLi,newBusiName).find_element_by_xpath('a[1]').get_attribute('title')
    if result==newBusiName:
        print('业务系统添加成功')
    else:
        print('业务系统添加失败')
isSusscessful()
def selectBusinessSystemsAnalysis(new_busi_name):
    browser.find_element_by_id('baseForm').find_element_by_xpath('div[1]/div[1]/input[1]').clear()
    browser.find_element_by_id('baseForm').find_element_by_xpath('div[1]/div[1]/input[1]').send_keys(new_busi_name)
    browser.find_element_by_id('searchBtn').click()
    time.sleep(1)
#修改业务系统
def editBusinessSystemsAnalysis(edit_busi_name,edit_busi_description):
    rootLi = browser.find_element_by_id('Tree_1')
    traversal(rootLi, newBusiName).find_element_by_xpath('a[1]').click()
    browser.find_element_by_id('editBtn').click()
    time.sleep(1)
    browser.find_element_by_id('causeForm').find_element_by_xpath('table[1]/tbody[1]/tr[3]/td[2]/input[1]').clear()
    browser.find_element_by_id('causeForm').find_element_by_xpath('table[1]/tbody[1]/tr[3]/td[2]/input[1]').send_keys(edit_busi_name)
    browser.find_element_by_id('causeForm').find_element_by_xpath('table[1]/tbody[1]/tr[5]/td[2]/textarea[1]').clear()
    browser.find_element_by_id('causeForm').find_element_by_xpath('table[1]/tbody[1]/tr[5]/td[2]/textarea[1]').send_keys(edit_busi_description)
    browser.find_element_by_id('addSysDict').click()
    time.sleep(2)
    browser.find_element_by_id('Tree_1').find_element_by_xpath('a[1]').click()
    time.sleep(1)
    selectBusinessSystemsAnalysis(newBusiName)
    editResult=browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[4]').text
    editResultDescription = browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[5]').text
    if editResult==edit_busi_name and editResultDescription==edit_busi_description:
        print('业务系统修改成功')
    else:
        print('业务系统修改失败')
editBusiName='编辑测试系统'
editBusiDescription='编辑测试系统的描述'
editBusinessSystemsAnalysis(editBusiName,editBusiDescription)
#添加业务系统管理员（已下线）
def addBusinessAdministrator(business_name):
    rootLi = browser.find_element_by_id('Tree_1')
    traversal(rootLi, editBusiName).find_element_by_xpath('a[1]').click()
    selectBusinessSystemsAnalysis(editBusiName)
    browser.find_element_by_id('addDepManager').click()
    browser.find_element_by_id('depUsersForm').find_element_by_xpath('div[1]/input[1]').send_keys(business_name)
    browser.find_element_by_id('depUsersForm').find_element_by_xpath('div[1]/button[1]').click()
    time.sleep(1)
    browser.find_element_by_link_text('添加').click()
    time.sleep(2)
    browser.find_element_by_class_name('layui-layer-close1').click()
    time.sleep(2)
    result=browser.find_element_by_id('depManagerTb').find_element_by_xpath('tbody[1]/tr[1]/td[2]').text
    if result==business_name:
        print('业务管理员添加成功')
    else:
        print('业务管理员添加失败')
businessName='用户'
#addBusinessAdministrator(businessName)
#删除业务系统管理员（已下线）
def deleteBusinessAdministrator():
    browser.find_element_by_id('depManagerTb').find_element_by_xpath('tbody[1]/tr[1]/td[3]/a[1]').click()
    time.sleep(3)
    result = browser.find_element_by_id('depManagerTb').find_element_by_xpath('tbody[1]/tr[1]/td[1]').text
    if result=='没有相关数据':
        print('业务管理员删除成功')
    else:
        print('业务管理员删除失败')
#deleteBusinessAdministrator()
#删除业务系统
def deleteBusinessSystemsAnalysis():
    rootLi = browser.find_element_by_id('Tree_1')
    traversal(rootLi, editBusiName).find_element_by_xpath('a[1]').click()
    time.sleep(1)
    browser.find_element_by_id('delBtn').click()
    browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
    time.sleep(2)
    rootLi = browser.find_element_by_id('Tree_1')
    result=traversal(rootLi, editBusiName)
    if result==None:
        print('业务系统删除成功')
    else:
        print('业务系统删除失败')
deleteBusinessSystemsAnalysis()
browser.switch_to.parent_frame()
browser.find_element_by_id('navbar-container').find_element_by_xpath('div[2]/ul[1]/li[3]/a[1]').click()
browser.find_element_by_id('user-menu').find_element_by_xpath('li[5]/a[1]').click()
time.sleep(1)
browser.find_element_by_class_name('ui-dialog-buttons').find_element_by_xpath('div[3]/div[1]/button[1]').click()
browser.close()