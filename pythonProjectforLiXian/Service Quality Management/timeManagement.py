import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://118.178.253.144:8080/itsm")  # 打开网页
# #填写用户名
browser.find_element_by_id('accountNameId').send_keys('admin#jingyu')
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
# 点击【工作时间管理】
browser.find_element_by_id('menu_li_id').find_element_by_xpath('li[2]/ul[1]/li[3]/a[1]').click()
time.sleep(2)
# iframe切换
iframe = browser.find_element_by_id('maincontent').find_element_by_xpath('div[1]/div[1]').find_element_by_class_name(
    'main').find_elements_by_tag_name('iframe')[oldFrameCut]
browser.switch_to_frame(iframe)
time.sleep(1)



#循环选择时间
def loopSelecting(startandend,timepicker):
    for data in range(1, len(startandend)-3):
        # 1
        startdata = startandend[data].find_element_by_xpath('td[2]/div[1]/input[1]')
        startdata.click()
        b=timepicker[data*2-1]
        b.find_element_by_xpath('div[2]/table[1]/tbody[1]/tr[1]/td[1]/span[10]').click()
        b.find_element_by_xpath('div[1]/table[1]/tbody[1]/tr[1]/td[1]/span[1]').click()
        # 2
        #time.sleep(1)
        enddata = startandend[data].find_element_by_xpath('td[2]/div[1]/input[2]')
        enddata.click()
        b = timepicker[data * 2 ]
        b.find_element_by_xpath('div[2]/table[1]/tbody[1]/tr[1]/td[1]/span[19]').click()
        b.find_element_by_xpath('div[1]/table[1]/tbody[1]/tr[1]/td[1]/span[1]').click()
    """for i in range(1,len(start)):
        for j in range(2*i-1,14):
            a = start[i]
            a.click()
            b=timepicker[j]
            b.find_element_by_xpath('div[2]/table[1]/tbody[1]/tr[1]/td[1]/span[10]').click()
            b.find_element_by_xpath('div[1]/table[1]/tbody[1]/tr[1]/td[1]/span[1]').click()
            break
        for j in range(2 * i, 14):
            a = end[i]
            a.click()
            b = timepicker[j]
            b.find_element_by_xpath('div[2]/table[1]/tbody[1]/tr[1]/td[1]/span[19]').click()
            b.find_element_by_xpath('div[1]/table[1]/tbody[1]/tr[1]/td[1]/span[1]').click()
            break"""
    """for i in range(1,len(start)):
        for j in range(2*i,14):
            if j%2==0:
                #z=j+1
                a = end[i]
                a.click()
                b=timepicker[j]
                b.find_element_by_xpath('div[2]/table[1]/tbody[1]/tr[1]/td[1]/span[19]').click()
                b.find_element_by_xpath('div[1]/table[1]/tbody[1]/tr[1]/td[1]/span[1]').click()
                break"""

#新增工作时间
def addWorkingTime(work_time_name):
    browser.find_element_by_class_name('iconsh-plus').click()
    time.sleep(1)
    iframe = browser.find_element_by_class_name('layui-layer-content').find_element_by_xpath('iframe[1]')
    browser.switch_to.frame(iframe)
    time.sleep(1)
    browser.find_element_by_id('hours_name').send_keys(work_time_name)
    #Start = browser.find_element_by_id('hoursForm').find_elements_by_xpath('table[1]/tbody[1]/tr/td[2]/div[1]/input[1]')
    # browser.find_element_by_id('hoursDiv').find_element_by_xpath('//following【流程操作】中选择【申请审核】，点击【流程下一步】-sibling::div[i]')
    #End = browser.find_element_by_id('hoursForm').find_elements_by_xpath('table[1]/tbody[1]/tr/td[2]/div[1]/input[2]')
    startAndEndDatas = browser.find_element_by_id('hoursForm').find_elements_by_xpath('table[1]/tbody[1]/tr')
    Timepicker = browser.find_elements_by_xpath("//div[@id='hoursDiv']/../div")
    time.sleep(1)
    loopSelecting(startAndEndDatas,Timepicker)
    #father=browser.find_element_by_id('hoursDiv').find_element_by_xpath('//parent::body')#通过子节点寻找父节点，要指明父节点标记
    #mother = browser.find_element_by_xpath("//div[@id='hoursDiv']/../div[2]")#另一个方法，像linux的层级
    #youngerBrother=father.find_element_by_xpath("//div[@id='hoursDiv']/following-sibling::div[1]")#通过第一个节点找平级的第二个节点
    #elderBrother = youngerBrother.find_element_by_xpath("//preceding-sibling::div[1]")#通过第二个节点找平级的第一个节点
    time.sleep(1)
    browser.find_element_by_id('btn_submit').click()
    time.sleep(1)
    result=browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[2]').text
    if result=='数据新增成功！':
        browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
        print('工作时间添加成功')
    else:
        print('工作时间添加失败')
#模糊查询工作时间
def selectWorkingTime(work_time_name):

    browser.find_element_by_id('keyWord').clear()
    browser.find_element_by_id('keyWord').send_keys(work_time_name)
    browser.find_element_by_class_name('iconsh-search1').click()
    time.sleep(1)
workingTime='测试工作时间'
addWorkingTime(workingTime)
#修改工作时间
def editWorkingTime(edit_work_time_name):
    browser.switch_to.parent_frame()
    selectWorkingTime(workingTime)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]/label[1]/input[1]').click()
    browser.find_element_by_class_name('iconsh-edit').click()
    time.sleep(1)
    iframe = browser.find_element_by_class_name('layui-layer-content').find_element_by_xpath('iframe[1]')
    browser.switch_to.frame(iframe)
    time.sleep(1)
    browser.find_element_by_id('hours_name').clear()
    browser.find_element_by_id('hours_name').send_keys(edit_work_time_name)
    browser.find_element_by_id('btn_submit').click()
    time.sleep(1)
    result = browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[2]').text
    if result == '数据修改成功！':
        browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
        print('工作时间修改成功')
    else:
        print('工作时间修改失败')
editworkingTime='编辑测试工作时间'
editWorkingTime(editworkingTime)
#删除工作时间
def  deleteWorkingTime():
    browser.switch_to.parent_frame()
    selectWorkingTime(workingTime)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]/label[1]/input[1]').click()
    browser.find_element_by_class_name('iconsh-delete').click()
    time.sleep(1)
    warnning = browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[2]').text
    if warnning == '确定要删除选择的数据?':
        browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
    else:
        print('操作有误')
    time.sleep(1)
    result=browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[2]').text
    if result == '数据删除成功！':
        browser.find_element_by_class_name('layui-layer-dialog').find_element_by_xpath('div[3]/a[1]').click()
        print('工作时间删除成功')
    else:
        print('工作时间删除失败')
    time.sleep(2)
deleteWorkingTime()
browser.close()

