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
browser.find_element_by_id('menu_li_id').find_element_by_xpath('li[2]/a[1]').click()
time.sleep(1)
oldFrameCut = len(
    browser.find_element_by_id('maincontent').find_element_by_xpath('div[1]/div[1]').find_element_by_class_name(
        'main').find_elements_by_tag_name('iframe'))
# 点击【员工组管理】
browser.find_element_by_id('menu_li_id').find_element_by_xpath('li[2]/ul[1]/li[5]/a[1]').click()
time.sleep(2)
# iframe切换
iframe = browser.find_element_by_id('maincontent').find_element_by_xpath('div[1]/div[1]').find_element_by_class_name(
    'main').find_elements_by_tag_name('iframe')[oldFrameCut]
browser.switch_to_frame(iframe)
time.sleep(1)
#新增员工组
def addGroup(new_group,new_group_description):
    browser.find_element_by_id('addPosBtn').click()
    browser.find_element_by_id('auPosForm').find_element_by_xpath('table[1]/tbody[1]/tr[3]/td[2]/input[1]').send_keys(new_group)
    browser.find_element_by_id('auPosForm').find_element_by_xpath('table[1]/tbody[1]/tr[4]/td[2]/textarea[1]').send_keys(new_group_description)
    browser.find_element_by_id('addUserGroup').click()
#判断是否新增成功
def isSucessful(new_group,new_group_description):
    groupResult=browser.find_element_by_id('baseOrgTable').find_elements_by_xpath('tbody/tr/td[2]')
    descriptionResult=browser.find_element_by_id('baseOrgTable').find_elements_by_xpath('tbody/tr/td[3]')
    flag=-1
    for i in groupResult:
        if i.text==new_group:
            flag=1
            break
    for j in descriptionResult:
        if j.text==new_group_description:
            flag=1
            break
    if flag==1:
        print('员工组添加成功')
    else:
        print('员工组添加失败')
newGroup='用户组'
newGroupDescription='用户组描述'
addGroup(newGroup,newGroupDescription)
time.sleep(1)
isSucessful(newGroup,newGroupDescription)
#模糊查询员工组
def selectGroup(new_group):
    time.sleep(1)
    browser.find_element_by_id('baseOrgForm').find_element_by_xpath('div[1]/input[1]').clear()
    browser.find_element_by_id('baseOrgForm').find_element_by_xpath('div[1]/input[1]').send_keys(new_group)
    time.sleep(1)
    browser.find_element_by_id('baseOrgForm').find_element_by_xpath('div[1]/button[1]').click()
    time.sleep(2)
#查看员工组
def checkGroup():
    selectGroup(newGroup)
    browser.find_element_by_id('baseOrgTable').find_element_by_xpath('tbody[1]/tr[1]/td[5]/div[1]/a[1]').click()
    time.sleep(1)
    browser.find_element_by_id('auPosDiv').find_element_by_xpath('div[1]/button[2]').click()
    print('员工组查看成功')
checkGroup()
#查看员工组名称和描述
def editGroup(edit_group,edit_group_description):
    selectGroup(newGroup)
    browser.find_element_by_id('baseOrgTable').find_element_by_xpath('tbody[1]/tr[1]/td[5]/div[1]/a[2]').click()
    time.sleep(1)
    browser.find_element_by_id('auPosForm').find_element_by_xpath('table[1]/tbody[1]/tr[3]/td[2]/input[1]').clear()
    browser.find_element_by_id('auPosForm').find_element_by_xpath('table[1]/tbody[1]/tr[3]/td[2]/input[1]').send_keys(edit_group)
    browser.find_element_by_id('auPosForm').find_element_by_xpath('table[1]/tbody[1]/tr[4]/td[2]/textarea[1]').clear()
    browser.find_element_by_id('auPosForm').find_element_by_xpath('table[1]/tbody[1]/tr[4]/td[2]/textarea[1]').send_keys(edit_group_description)
    browser.find_element_by_id('addUserGroup').click()
    time.sleep(1)
    edit_result=browser.find_element_by_id('baseOrgTable').find_element_by_xpath('tbody[1]/tr[1]/td[2]').text
    edit_result_description = browser.find_element_by_id('baseOrgTable').find_element_by_xpath('tbody[1]/tr[1]/td[3]').text
    if edit_result == edit_group and edit_result_description==edit_group_description:
        print('员工组修改成功')
    else:
        print('员工组修改失败')
editgroup='编辑后的用户组'
editGroupDescriptionp='编辑后的用户组描述'
editGroup(editgroup,editGroupDescriptionp)
def traversal(li,selected):
    for i in li:
        try:
            if i.find_element_by_xpath('a[1]').text == selected:
                return i
        except selenium.common.exceptions.NoSuchElementException:
            break
browser.find_element_by_id('orgTree_1').find_element_by_xpath('span[1]').click()
groupLi=browser.find_element_by_id('orgTree').find_elements_by_xpath('li[1]/ul[1]/li')
traversal(groupLi,editgroup).find_element_by_xpath('a[1]').click()
#为员工组添加用户
def addUsertoGroup(user_name):
    time.sleep(1)
    browser.find_element_by_id('arrangeAccBtn').click()
    time.sleep(1)
    browser.find_element_by_id('arrangeAccForm').find_element_by_xpath('div[1]/input[1]').send_keys(user_name)
    browser.find_element_by_id('arrangeAccForm').find_element_by_xpath('div[1]/button[1]').click()
    time.sleep(1)
    browser.find_element_by_id('accs_all').click()
    browser.find_element_by_id('arrangeAccDiv').find_element_by_xpath('div[2]/button[1]').click()
    browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
    time.sleep(1)
    user_result = browser.find_element_by_id('basePosTable').find_element_by_xpath( 'tbody[1]/tr[1]/td[4]').text
    if user_result==user_name:
        print('员工组添加成员成功')
    else:
        print('员工组添加成员失败')
userName='经理'
addUsertoGroup(userName)
#组内成员设置
def userSetting():
    time.sleep(1)
    browser.find_element_by_id('basePosTable').find_element_by_xpath('tbody[1]/tr[1]/td[8]/div[1]/a[1]').click()
    time.sleep(2)
    browser.find_element_by_id('basePosTable').find_element_by_xpath('tbody[1]/tr[1]/td[8]/div[1]/a[2]').click()
    time.sleep(2)
    browser.find_element_by_id('basePosTable').find_element_by_xpath('tbody[1]/tr[1]/td[8]/div[1]/a[3]').click()
    time.sleep(2)
    a=browser.find_element_by_id('basePosTable').find_element_by_xpath('tbody[1]/tr[1]/td[5]/span[1]').text
    b = browser.find_element_by_id('basePosTable').find_element_by_xpath('tbody[1]/tr[1]/td[6]/span[1]').text
    c= browser.find_element_by_id('basePosTable').find_element_by_xpath('tbody[1]/tr[1]/td[7]/span[1]').text
    if a==b==c=='是':
        print('成员设置成功')
    else:
        print('成员设置失败')
userSetting()
#员工组移除成员
def deleteUserfromGroup():
    time.sleep(1)
    browser.find_element_by_id('basePosTable').find_element_by_xpath('tbody[1]/tr[1]/td[8]/div[1]/a[4]').click()
    time.sleep(1)
    browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
    time.sleep(2)
    deleteResult=browser.find_element_by_id('basePosTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]').text
    if deleteResult=='没有相关数据':
        print('员工组移除成员成功')
    else:
        print('员工组移除成员失败')



deleteUserfromGroup()

#删除员工组
def deleteGroup():
    browser.find_element_by_id('orgTree').find_element_by_xpath('li[1]/a[1]/span[2]').click()
    selectGroup(newGroup)
    browser.find_element_by_id('baseOrgTable').find_element_by_xpath('tbody[1]/tr[1]/td[5]/div[1]/a[3]').click()
    browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
    time.sleep(2)
    deleteResult=browser.find_element_by_id('baseOrgTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]').text
    if deleteResult=='没有相关数据':
        print('员工组删除成功')
    else:
        print('员工组删除失败')
deleteGroup()
browser.switch_to.parent_frame()
browser.find_element_by_id('navbar-container').find_element_by_xpath('div[2]/ul[1]/li[3]/a[1]').click()
browser.find_element_by_id('user-menu').find_element_by_xpath('li[5]/a[1]').click()
time.sleep(1)
browser.find_element_by_class_name('ui-dialog-buttons').find_element_by_xpath('div[3]/div[1]/button[1]').click()
browser.close()