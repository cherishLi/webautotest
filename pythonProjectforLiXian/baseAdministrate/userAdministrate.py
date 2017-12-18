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
# time.sleep(10)
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
# 点击【用户管理】
browser.find_element_by_id('menu1').find_element_by_xpath('ul[1]/li[2]/a[1]').click()
time.sleep(2)
# iframe切换
iframe = browser.find_element_by_id('maincontent').find_element_by_xpath('div[1]/div[1]').find_element_by_class_name(
    'main').find_elements_by_tag_name('iframe')[oldFrameCut]
browser.switch_to_frame(iframe)
time.sleep(1)
def addUser(new_user,new_name):
    browser.find_element_by_id('addBtn').click()
    browser.find_element_by_id('loginName').send_keys(new_user)
    browser.find_element_by_id('orgName').click()
    time.sleep(1)
    browser.find_element_by_id('orgTree').find_element_by_xpath('li[1]/span[1]').click()
    time.sleep(1)
    browser.find_element_by_id('orgTree').find_element_by_xpath('li[1]/ul[1]/li[2]/a[1]').click()
    browser.find_element_by_id('auForm').find_element_by_xpath('table[1]/tbody[1]/tr[3]/td[2]/input[1]').send_keys(new_name)
    head_sculpture = browser.find_element_by_id('picker').find_element_by_xpath('div[2]/input[1]')
    head_sculpture.send_keys('d:\\nima.jpg')
    time.sleep(5)
    #print('上传头像'+head_sculpture.get_attribute('value')+'成功')
    browser.find_element_by_id('addUser').click()
def isSucessful(newUserName):
    td=browser.find_element_by_id('baseTable').find_elements_by_xpath('tbody/tr/td[4]')
    flag=-1
    for i in td:
        if i.text==newUserName:
            flag=1
            break
    if flag==1:
        print('用户添加成功')
    else:
        print('用户添加失败')

newUserLoginName='user#jingyu'
newUserName='用户'
addUser(newUserLoginName,newUserName)
time.sleep(2)
isSucessful(newUserName)
#模糊查询用户
def selectUser(newUserName):
    browser.find_element_by_id('baseForm').find_element_by_xpath('div[1]/div[1]/input[1]').clear()
    browser.find_element_by_id('baseForm').find_element_by_xpath('div[1]/div[1]/input[1]').send_keys(newUserName)
    time.sleep(1)
    browser.find_element_by_id('baseForm').find_element_by_xpath('div[1]/div[1]/button[1]').click()
    time.sleep(2)
selectUser(newUserName)
#查看角色
def checkUser():
    selectUser(newUserName)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[9]/div[1]/a[2]').click()
    time.sleep(2)
    browser.find_element_by_id('auDiv').find_element_by_xpath('div[1]/button[2]').click()
    print('角色查看成功')
checkUser()
#编辑用户
def editUser(edit_user):
    selectUser(newUserName)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[9]/div[1]/a[3]').click()
    time.sleep(1)
    browser.find_element_by_id('auForm').find_element_by_xpath('table[1]/tbody[1]/tr[3]/td[2]/input[1]').clear()
    browser.find_element_by_id('auForm').find_element_by_xpath('table[1]/tbody[1]/tr[3]/td[2]/input[1]').send_keys(edit_user)
    browser.find_element_by_id('addUser').click()
    time.sleep(1)
    edit_result=browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[4]').text
    if edit_result == edit_role:
        print('用户修改成功')
    else:
        print('用户修改失败')
edit_role='编辑后的用户'
editUser(edit_role)
#重置用户密码
def resetPassword(newPassword):
    selectUser(newUserName)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[9]/div[1]/a[1]').click()
    browser.find_element_by_id('resetPwdFrom').find_element_by_xpath('table[1]/tbody[1]/tr[2]/td[2]/input[1]').send_keys(newPassword)
    browser.find_element_by_id('btn_bc').click()
    time.sleep(1)
    print('用户密码重置成功')
newPassword='1'
resetPassword(newPassword)



#为用户授权角色，是否授权成功是根据class变化判断的


def grantRole(role,selectedCheckBox):
    selectUser(newUserName)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[9]/div[1]/a[5]').click()
    time.sleep(1)
    li = browser.find_element_by_id('authorityTree').find_elements_by_xpath('li[1]/ul[1]/li')
    for j in li:
        i=j.find_element_by_xpath('a[1]').get_attribute('title')
        if j is not None and i==role:
            j.find_element_by_xpath('span[2]').click()
        else:
            continue
    browser.find_element_by_id('authorityDiv').find_element_by_xpath('div[1]/div[2]/button[1]').click()
    time.sleep(1)
    liAfter = browser.find_element_by_id('authorityTree').find_elements_by_xpath('li[1]/ul[1]/li')
    flag = 1
    for j in liAfter:
        i = j.find_element_by_xpath('a[1]').get_attribute('title')
        if j is not None and i==role:
            u=j.find_element_by_xpath('span[2]').get_attribute('class')
            if selectedCheckBox in u:
                flag=1
            else:
                flag=-1
        else:
            continue
    if flag==1:
        print('角色授权成功')
    else:
         print('角色授权失败')
role='经理'
selectedCheckBox='checkbox_true_full'
grantRole(role,selectedCheckBox)
#删除用户
def deleteUser():
    selectUser(newUserName)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[9]/div[1]/a[4]').click()
    time.sleep(1)
    browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
    time.sleep(2)
    afterDelete = browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]').text
    deleteinLaw = '没有相关数据'
    if afterDelete == deleteinLaw:
        print('用户删除成功')
    else:
        print('用户删除失败')
deleteUser()
#批量删除用户，为保证测试数据完整性，方法里首先添加了用户
def batchDelete():
    print('批量删除用户部分:')
    addUser(newUserLoginName, newUserName)
    selectUser(newUserName)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]/label[1]/input[1]').click()
    browser.find_element_by_id('delBatchBtn').click()
    browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
    time.sleep(1)
    afterDelete=browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]').text
    deleteinLaw='没有相关数据'
    if afterDelete == deleteinLaw:
        print('用户批量删除成功')
    else:
        print('用户批量删除失败')
batchDelete()
browser.switch_to.parent_frame()
browser.find_element_by_id('navbar-container').find_element_by_xpath('div[2]/ul[1]/li[3]/a[1]').click()
browser.find_element_by_id('user-menu').find_element_by_xpath('li[5]/a[1]').click()
time.sleep(1)
browser.find_element_by_class_name('ui-dialog-buttons').find_element_by_xpath('div[3]/div[1]/button[1]').click()
browser.close()