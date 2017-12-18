# coding = utf-8
import time

import selenium
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://127.0.0.1:8080/itsm")  # 打开网页
browser.maximize_window()#最大化窗口
# 添加cookie
# browser.add_cookie({'name':'JSESSIONID', 'value':'DD3000388A638CA362403F13A19A17BE'})
# browser.add_cookie({'domain':'139.196.212.3:8081/itsm', 'name':'Hm_lvt_a23643b4e99bbca4fd9c03a9c8258ae5', 'value':'1498918891,1499003404,1499044656', 'path':'/'})
# browser.add_cookie({'domain':'139.196.212.3:8081/itsm', 'name':'Hm_lpvt_a23643b4e99bbca4fd9c03a9c8258ae5', 'value':'1499044656', 'path':'/'})
# browser.add_cookie({ 'name':'rememberMe', 'value':'yCJO5A5x7i/CxHgVh7KgMKfQX47V8FtUUwM5aOuTRp2BSSrK9OghhOA2dwaYsK+gTUsSSVv5QktK/86+X5pi82dVUfcVq4szaNtt65t3PS8sNSQ2XYWbKWWZA8GHcaYwaiLNnx0tLliYx2wW7Qe+Q9DIwWaIPuWt1mFAP8ADgCVA1Mbj5vZXHs+Pl15P9WKIWKuTKJYmmY8UjRmbKAVcvCcrTzPHhnFL6N/wnD40Fu/eBE3A6sUBudMjSNSY8NLufYEF2iEmPW3Nvi+mYzTDohAF7GlcIIt6tgg0yzUqyrh4KKKPDEtd+mopUurBtzPH0E6R/aRcQQdNTf0DcHcncJ5y19O17XNOq5Ga0m6a3ausC3rKhm/mytrIwL2ms/SFUMvkGzoxRV4Gr3RNzhCQRhP/fvuSFc9pqsXyeZ9Gnx6zFf8zQGJnSGzKaA4qjsBCJfO/Q/JJ0GyVDjgEP8Gkh6w4CUYUNlr1e8RiMWMrUJXK/6k7CxwXJOAFDEdMm+HzCkIbteNiqpGzQ57qx8aWAOGdcF4yRtsCpj8yODMMZXg='})

#browser.add_cookie( {'domain': '139.196.212.3', 'path': '/itsm', 'name': 'JSESSIONID', 'value': '7165E43DAF100D661AF6F13AFE0D919D'})
# browser.add_cookie({'domain':'139.196.212.3', 'name':'Hm_lvt_a23643b4e99bbca4fd9c03a9c8258ae5', 'value':'1498918891,1499003404,1499044656'})
# browser.add_cookie({'domain':'139.196.212.3', 'path':'/itsm', 'name':'Hm_lpvt_a23643b4e99bbca4fd9c03a9c8258ae5', 'value':'1499044656'})
#browser.add_cookie({'domain': '139.196.212.3', 'path': '/itsm', 'name': 'rememberMe',
                   # 'value': 'Q2fhGDYJ7ZT0k1sxiFVDZwjiXvHOcgqvDsGro11FdDDkLEOXF7bSp47p31oRlxuIMnUN1Kh6/D+O3LW0PqAHO9zLrRt9jRz3VzbOqN1CX1LecBP0XqwA2+ZvuYK1PBJ3hrPfaOaTleCG8c5RUdhJrY2LMG0/ao8e79N4rAYLGY+u9odMivzlL9rQh3vk3OLUTkrDYlg9sStrMx5TcGceJpBwpjKM3n1cBw+41+aShpPsy9RnHuVA5ukOohQp7vZvkt/QKpkvEm4XB2bElwvYRB7/MiiPAy4Cue5bhTEi0cF9u1uAM5E4iovZLL7NSIqMRRNRDzScX8nUVH271fSeEVtCGOttqcfFfAb5y98HfyNksPs1cVpd8zvUPxmq7xJUiuuQEWiUlSiplCndSHotcneVcxSoH238f5q5L1Yge8lFJAKM+iuSVbkuH1oyMQOdrin2xJEMC1zXBv9LXRM0OMggXXV/AQpetWED5obhl00qrwZFFz1fP+2oExAbDtSw8bCZPi1y+PWgxCWqJGHrrmomswLHs4reH0IXo/6k+60='})
## 刷新直接进入主界面


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
# 点击【机构管理】
browser.find_element_by_id('menu_li_id').find_element_by_xpath('li[2]/ul[1]/li[1]/a[1]').click()
time.sleep(2)
# iframe切换，元素获取范围在机构管理
iframe = browser.find_element_by_id('maincontent').find_element_by_xpath('div[1]/div[1]').find_element_by_class_name(
    'main').find_elements_by_tag_name('iframe')[oldFrameCut]
browser.switch_to_frame(iframe)
# 根目录选择
time.sleep(2)
#树递归，传入整棵树（li）和需要的节点(selected)；返回所需节点
def traversal(li,selected):
    if li.find_element_by_xpath('a').text == selected:
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

#browser.find_element_by_id('orgTree_1_span').click()
# 点击【新增】
#新增机构，选择一个父节点，添加机构后判断是否添加成功
def addOrg(new_org,new_org_description,parent):
    items = browser.find_element_by_id('orgTree').find_element_by_xpath('li')
    it = traversal(items, parent).find_element_by_xpath('a[1]').click()
    time.sleep(3)
    browser.find_element_by_id('addOrgBtn').click()
    browser.find_element_by_id('auOrgForm').find_element_by_xpath('table[1]/tbody[1]/tr[3]/td[2]/input[1]').send_keys(
        new_org)
    browser.find_element_by_id('auOrgForm').find_element_by_xpath(
        'table[1]/tbody[1]/tr[4]/td[2]/textarea[1]').send_keys(
        new_org_description)
    browser.find_element_by_id('addOrg').click()
    time.sleep(4)
    browser.find_element_by_link_text(new_org).click()
    time.sleep(2)
    # 取列表中字段
    a = browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[2]').text
    b = browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[3]').text
    f = browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[4]').text
    if wheretoAddOrg == '江苏京玉信息技术有限公司':
        parent=''
    else:
        parent=wheretoAddOrg
    # 比较判断是否是新增的机构
    if a == new_org and b == new_org_description and f==parent:
        print('机构新增成功')
    else:
        print('机构新增失败')
wheretoAddOrg = '江苏京玉信息技术有限公司'
new_org = '市场部'
new_org_description = '市场部描述'
edit_org = '编辑市场部的叶子'
edit_org_description = '编辑市场部的叶子描述'
#根节点下新增父节点
addOrg(new_org,new_org_description,wheretoAddOrg)
wheretoAddOrg =new_org
#items = browser.find_element_by_id('orgTree').find_element_by_xpath('li')
child_new_org='市场部的叶子'
child_new_org_description='市场部的叶子描述'
#父节点下新增子节点
print('子机构：')
addOrg(child_new_org,child_new_org_description,wheretoAddOrg)

# 修改机构名称和描述，判断是否修改成功
def editOrg(org_to_edit):
    browser.find_element_by_link_text(org_to_edit).click()
    time.sleep(1)
    browser.find_element_by_id('editOrgBtn').click()
    # 修改传参
    time.sleep(1)
    browser.find_element_by_id('auOrgForm').find_element_by_xpath('table[1]/tbody[1]/tr[3]/td[2]/input[1]').clear()
    browser.find_element_by_id('auOrgForm').find_element_by_xpath('table[1]/tbody[1]/tr[3]/td[2]/input[1]').send_keys(edit_org)
    browser.find_element_by_id('auOrgForm').find_element_by_xpath('table[1]/tbody[1]/tr[4]/td[2]/textarea[1]').clear()
    browser.find_element_by_id('auOrgForm').find_element_by_xpath('table[1]/tbody[1]/tr[4]/td[2]/textarea[1]').send_keys(edit_org_description)
    # 点击【保存】
    browser.find_element_by_id('addOrg').click()
    time.sleep(4)
    browser.find_element_by_link_text(edit_org).click()
    time.sleep(2)
    c = browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[2]').text
    d = browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[3]').text
    # 比较判断是否是修改的机构
    if c == edit_org and d == edit_org_description:
        print('机构修改成功')
    else:
        print('机构修改失败')
editOrg(child_new_org)
#添加、删除机构的部门经理
def departmentManager(manager):
    # 选择修改的机构
    browser.find_element_by_link_text(edit_org).click()
    time.sleep(1)
    # 点击部门经理的【新增】
    browser.find_element_by_id('addDepManager').click()
    # 模糊查询
    depManager = manager
    browser.find_element_by_id('depUsersForm').find_element_by_xpath('div[1]/input[1]').send_keys(depManager)
    time.sleep(1)
    browser.find_element_by_id('depUsersForm').find_element_by_xpath('div[1]/button[1]').click()
    time.sleep(2)
    # 点击【添加】
    browser.find_element_by_link_text('添加').click()
    time.sleep(3)
    browser.find_element_by_class_name('layui-layer-close1').click()
    time.sleep(4)
    e = browser.find_element_by_id('depManagerTb').find_element_by_xpath('tbody[1]/tr[1]/td[2]').text
    if e == depManager:
        print('部门经理添加成功')
    else:
        print('部门经理添加成功')
    browser.find_element_by_id('depManagerTb').find_element_by_link_text('删除').click()
    try:
        browser.find_element_by_id('depManagerTb').find_element_by_link_text(depManager)
    except selenium.common.exceptions.NoSuchElementException:
        print('部门经理删除成功')
manager='经理'
departmentManager(manager)


#删除机构并判断是否删除成功
def deleteOrg(wheretoDelOrg):
    items3 = browser.find_element_by_id('orgTree').find_element_by_xpath('li')
    item = traversal(items3,wheretoDelOrg).find_element_by_xpath('a[1]').click()
    time.sleep(1)
    browser.find_element_by_id('delOrgBtn').click()
    warningText=browser.find_element_by_class_name('layui-layer-padding').text
    if child_new_org in warningText:
        print('删除定位正确')
    else:
        print('删除定位错误')
    browser.find_element_by_class_name('layui-layer-btn-').find_element_by_xpath('a[1]').click()
    time.sleep(2)
    items3 = browser.find_element_by_id('orgTree').find_element_by_xpath('li')
    if traversal(items3,child_new_org) is None:
        print('删除成功')
    else:
        print('删除失败')
deleteOrg(edit_org)
#退出登陆
browser.switch_to.parent_frame()
browser.find_element_by_id('navbar-container').find_element_by_xpath('div[2]/ul[1]/li[3]/a[1]').click()
browser.find_element_by_id('user-menu').find_element_by_xpath('li[5]/a[1]').click()
time.sleep(1)
browser.find_element_by_class_name('ui-dialog-buttons').find_element_by_xpath('div[3]/div[1]/button[1]').click()
#关闭浏览器
browser.close()
    # browser.find_element_by_id('loginBtn').click()
    # browser.find_element_by_class_name('btn  index_btn active_index').click()

    # browser.find_element_by_id("su").click()
    # try:
    #   assert "service" in browser.title
    # except AssertionError:
    #    print(browser.title)
    # elem = browser.find_element_by_name("p") # Find the query box
    # elem.send_keys("seleniumhq" + Keys.RETURN)
    # time.sleep(0.2) # Let the page load, will be added to the API
    # try:
    #   browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
    # except NoSuchElementException:
    #   assert 0, "can't find seleniumhq"
    # browser.close()
    #
