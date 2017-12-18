import time

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
# 点击【业务信息管理】
browser.find_element_by_id('menu_li_id').find_element_by_xpath('li[3]/a[1]').click()
time.sleep(1)
oldFrameCut = len(
    browser.find_element_by_id('maincontent').find_element_by_xpath('div[1]/div[1]').find_element_by_class_name(
        'main').find_elements_by_tag_name('iframe'))
# 点击【技术分类管理】
browser.find_element_by_id('menu_li_id').find_element_by_xpath('li[3]/ul[1]/li[2]/a[1]').click()
time.sleep(2)
# iframe切换
iframe = browser.find_element_by_id('maincontent').find_element_by_xpath('div[1]/div[1]').find_element_by_class_name(
    'main').find_elements_by_tag_name('iframe')[oldFrameCut]
browser.switch_to_frame(iframe)
time.sleep(3)
#树递归
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
#新增技术分类，技术分类编辑框都要切换iframe，之后再切回原来的。不知道开发什么脑洞
def addTechnicalAnalysis(new_tech_code,new_tech_name,new_tech_description):
    browser.find_element_by_id('addBtn').click()
    iframe = browser.find_element_by_class_name('layui-layer-iframe').find_element_by_xpath('div[2]/iframe[1]')
    browser.switch_to_frame(iframe)
    time.sleep(1)
    browser.find_element_by_id('Form').find_element_by_xpath('table[1]/tbody[1]/tr[1]/td[2]/div[1]/input[4]').send_keys(new_tech_code)
    browser.find_element_by_id('Form').find_element_by_xpath('table[1]/tbody[1]/tr[2]/td[2]/div[1]/input[1]').send_keys(new_tech_name)
    browser.find_element_by_id('Form').find_element_by_xpath('table[1]/tbody[1]/tr[3]/td[2]/div[1]/label[1]/input[1]').click()
    browser.find_element_by_id('Form').find_element_by_xpath('table[1]/tbody[1]/tr[4]/td[2]/div[1]/textarea[1]').send_keys(new_tech_description)
    browser.find_element_by_id('btn_submit').click()
    time.sleep(1)
    result = browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[2]').text
    if result=='保存成功':
        print('技术分析添加成功')
        browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
        time.sleep(2)
    else:
        print('技术分析添加失败')
newTechCode=99
newTechName='测试'
newTechDescription='测试的描述'
addTechnicalAnalysis(newTechCode,newTechName,newTechDescription)
iframe = browser.find_element_by_id('maincontent').find_element_by_xpath('div[1]/div[1]').find_element_by_class_name('main').find_elements_by_tag_name('iframe')[oldFrameCut]
browser.switch_to_frame(iframe)
#修改技术分类
def editTechnicalAnalysis(edit_root_name,edit_root_description):
    rootLi = browser.find_element_by_id('Tree_1')
    traversal(rootLi, newTechName).find_element_by_xpath('a[1]').click()
    time.sleep(1)
    browser.find_element_by_id('editBtn').click()
    iframe = browser.find_element_by_class_name('layui-layer-iframe').find_element_by_xpath('div[2]/iframe[1]')
    browser.switch_to_frame(iframe)
    time.sleep(1)
    browser.find_element_by_id('name').clear()
    browser.find_element_by_id('name').send_keys(edit_root_name)
    browser.find_element_by_id('description').clear()
    browser.find_element_by_id('description').send_keys(edit_root_description)
    browser.find_element_by_id('btn_submit').click()
    time.sleep(1)
    result = browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[2]').text
    if result=='修改成功':
        print('技术分析修改成功')
        browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
        time.sleep(2)
    else:
        print('技术分析修改失败')
editTechName='编辑测试'
editTechDescription='编辑测试的描述'
editTechnicalAnalysis(editTechName,editTechDescription)
#模糊查询技术分类
def selectTechnicalAnalysis(new_root_name):
    browser.find_element_by_id('baseForm').find_element_by_xpath('div[1]/div[1]/input[1]').clear()
    browser.find_element_by_id('baseForm').find_element_by_xpath('div[1]/div[1]/input[1]').send_keys(new_root_name)
    browser.find_element_by_id('searchBtn').click()
    time.sleep(1)
iframe = browser.find_element_by_id('maincontent').find_element_by_xpath('div[1]/div[1]').find_element_by_class_name('main').find_elements_by_tag_name('iframe')[oldFrameCut]
browser.switch_to_frame(iframe)
#模块配置
def moduleconfiguration():
    browser.find_element_by_id('Tree_1').find_element_by_xpath('a[1]').click()
    time.sleep(1)
    selectTechnicalAnalysis(editTechName)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]/label[1]/input[1]').click()
    label=browser.find_element_by_id('module').find_elements_by_xpath('label')
    for j in label:
        if j is not None:
            j.find_element_by_xpath('input[1]').click()
        else:
            continue
    browser.find_element_by_id('baseForm').find_element_by_xpath('div[1]/div[1]/button[2]').click()
    time.sleep(2)
    labelAfter = browser.find_element_by_id('module').find_elements_by_xpath('label')
    flag = 1
    for j in labelAfter:
        if j is not None:
            try:
                j.find_element_by_xpath('input[1]').get_attribute('checked')
                flag = 1
            except selenium.common.exceptions.NoSuchElementException:
                flag = -1
        else:
            break
    if flag == 1:
        print('模块配置成功')
    else:
        print('模块配置失败')
    label=browser.find_element_by_id('module').find_elements_by_xpath('label')
    for j in label:
        if j is not None:
            j.find_element_by_xpath('input[1]').click()
        else:
            continue
    browser.find_element_by_id('baseForm').find_element_by_xpath('div[1]/div[1]/button[2]').click()
    time.sleep(2)
moduleconfiguration()
#删除技术分类
def deleteTechnicalAnalysis():
    rootLi = browser.find_element_by_id('Tree_1')
    traversal(rootLi, editTechName).find_element_by_xpath('a[1]').click()
    time.sleep(1)
    browser.find_element_by_id('delBtn').click()
    browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
    time.sleep(2)
    rootLi = browser.find_element_by_id('Tree_1')
    result = traversal(rootLi, editTechName)
    if result == None:
        print('技术分析删除成功')
    else:
        print('技术分析删除失败')
deleteTechnicalAnalysis()
browser.close()

