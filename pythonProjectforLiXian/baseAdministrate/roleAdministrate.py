# coding = utf-8
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
#time.sleep(10)
browser.find_element_by_id('verifyCodeId').send_keys('8888')

# #手动
# #点击【登录】
browser.find_element_by_id('loginBtn').click()
time.sleep(2)
# 点击【系统功能】
browser.find_element_by_xpath(
    "//div[@id='main-container']/div[1]/div[@id='sidebar']/div[@id='sidebar-shortcuts']/div[@id='sidebar-shortcuts-large']/button[3]").click()
time.sleep(1)
# 点击【基础管理】
browser.find_element_by_id('menu1').find_element_by_xpath('a[1]').click()
time.sleep(1)
oldFrameCut = len(
    browser.find_element_by_id('maincontent').find_element_by_xpath('div[1]/div[1]').find_element_by_class_name(
        'main').find_elements_by_tag_name('iframe'))
# 点击【角色管理】
browser.find_element_by_id('menu1').find_element_by_xpath('ul[1]/li[3]/a[1]').click()
time.sleep(2)
# iframe切换
iframe = browser.find_element_by_id('maincontent').find_element_by_xpath('div[1]/div[1]').find_element_by_class_name(
    'main').find_elements_by_tag_name('iframe')[oldFrameCut]
browser.switch_to_frame(iframe)
time.sleep(1)
#新增角色
def addRole(new_role,new_role_description):
    browser.find_element_by_id('addBtn').click()
    browser.find_element_by_id('auForm').find_element_by_xpath('table[1]/tbody[1]/tr[3]/td[2]/input[1]').send_keys(new_role)
    browser.find_element_by_id('auForm').find_element_by_xpath('table[1]/tbody[1]/tr[4]/td[2]/textarea[1]').send_keys(new_role_description)
    browser.find_element_by_id('addRole').click()
    time.sleep(2)
    td = browser.find_element_by_id('baseTable').find_element_by_xpath('tbody').text
    if new_role in td:
        print('角色添加成功')
    else:
        print('角色添加失败')
new_role='领导'
new_role_description='领导描述'
addRole(new_role,new_role_description)
#判断是否添加成功
def isSucessful(new_role):
    td=browser.find_element_by_id('baseTable').find_elements_by_xpath('tbody/tr/td[3]')
    flag=-1
    for i in td:
        if i.text==new_role:
            flag=1
            break
    if flag==1:
        print('角色添加成功')
    else:
        print('角色添加失败')

#模糊查询角色
def selectRole(new_role):
    time.sleep(1)
    browser.find_element_by_class_name('widget-main').find_element_by_xpath('input').clear()
    browser.find_element_by_class_name('widget-main').find_element_by_xpath('input').send_keys(new_role)
    browser.find_element_by_id('searchBtn').click()
    time.sleep(2)
selectRole(new_role)
#查看角色
def checkRole():
    selectRole(new_role)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[6]/div[1]/a[2]').click()
    time.sleep(1)
    browser.find_element_by_id('auDiv').find_element_by_xpath('div[1]/button[2]').click()
    print('角色查看成功')
checkRole()
#编辑角色
def editRole(edit_role,edit_role_description):
    selectRole(new_role)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[6]/div[1]/a[3]').click()
    time.sleep(1)
    browser.find_element_by_id('auForm').find_element_by_xpath('table[1]/tbody[1]/tr[3]/td[2]/input[1]').clear()
    browser.find_element_by_id('auForm').find_element_by_xpath('table[1]/tbody[1]/tr[3]/td[2]/input[1]').send_keys(edit_role)
    browser.find_element_by_id('auForm').find_element_by_xpath('table[1]/tbody[1]/tr[4]/td[2]/textarea[1]').clear()
    browser.find_element_by_id('auForm').find_element_by_xpath('table[1]/tbody[1]/tr[4]/td[2]/textarea[1]').send_keys(edit_role_description)
    browser.find_element_by_id('addRole').click()
    time.sleep(1)
    edit_result=browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[3]').text
    edit_result_description=browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[5]').text
    if edit_result == edit_role and edit_result_description == edit_role_description:
        print('角色修改成功')
    else:
        print('角色修改失败')
edit_role='编辑后的领导'
edit_role_description='编辑后的领导描述'
editRole(edit_role,edit_role_description)
#角色授权菜单
#此处默认勾选所有菜单，如果不是，请修改循环条件
def grantMenu():
    selectRole(new_role)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[6]/div[1]/a[1]').click()
    time.sleep(1)
    li=browser.find_element_by_id('authorityTree').find_elements_by_xpath('li')
    for j in li:
        if j is not None:
            j.find_element_by_xpath('span[2]').click()
        else:
            continue
    browser.find_element_by_id('roleImpower').click()
    time.sleep(2)
    liAfter=browser.find_element_by_id('authorityTree').find_elements_by_xpath('li')
    flag=1
    for j in liAfter:
        if j is not None :
            try:
                u=j.find_element_by_class_name('checkbox_true_full')
                flag=1
            except selenium.common.exceptions.NoSuchElementException:
                flag=-1
        else:
            break
    if flag==1:
        print('菜单授权成功')
    else:
        print('菜单授权失败')
grantMenu()
#删除角色
def deleteRole():
    selectRole(new_role)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[6]/div[1]/a[4]').click()
    time.sleep(1)
    browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
    time.sleep(2)
    afterDelete=browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]').text
    deleteinLaw='没有相关数据'
    if afterDelete == deleteinLaw:
        print('角色删除成功')
    else:
        print('角色删除失败')
deleteRole()
#批量删除角色
def batchDelete():
    print('批量删除角色部分:')
    addRole(new_role,new_role_description)
    selectRole(new_role)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]/label[1]/input[1]').click()
    browser.find_element_by_id('delBatchBtn').click()
    browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
    time.sleep(1)
    afterDelete=browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]').text
    deleteinLaw='没有相关数据'
    if afterDelete == deleteinLaw:
        print('角色批量删除成功')
    else:
        print('角色批量删除失败')
batchDelete()
browser.switch_to.parent_frame()
browser.find_element_by_id('navbar-container').find_element_by_xpath('div[2]/ul[1]/li[3]/a[1]').click()
browser.find_element_by_id('user-menu').find_element_by_xpath('li[5]/a[1]').click()
time.sleep(1)
browser.find_element_by_class_name('ui-dialog-buttons').find_element_by_xpath('div[3]/div[1]/button[1]').click()
browser.close()