import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://127.0.0.1:8080/itsm")  # 打开网页
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
# 点击【节假日管理】
browser.find_element_by_id('menu_li_id').find_element_by_xpath('li[2]/ul[1]/li[4]/a[1]').click()
time.sleep(2)
# iframe切换
iframe = browser.find_element_by_id('maincontent').find_element_by_xpath('div[1]/div[1]').find_element_by_class_name(
    'main').find_elements_by_tag_name('iframe')[oldFrameCut]
browser.switch_to_frame(iframe)
time.sleep(1)
#新增节假日
def addHolidayTime(holiday_time_name):
    browser.find_element_by_class_name('iconsh-plus').click()
    time.sleep(1)
    browser.find_element_by_id('holiday_div').find_element_by_xpath('table[1]/tbody[1]/tr[1]/td[2]/div[1]/input[2]').send_keys(holiday_time_name)#通过第一个节点找平级的第二个节点
    browser.find_element_by_id('holiday_div').find_element_by_xpath('table[1]/tbody[1]/tr[2]/td[1]/div[1]/button[1]').click()
    time.sleep(2)
    results=browser.find_element_by_id('baseTable').find_elements_by_xpath('tbody[1]/tr/td[3]')
    result=[]
    for i in results:
        result.append(i.text)
    if holiday_time_name in result:
        print('节假日添加成功')
    else:
        print('节假日添加失败')
holidayTimeName='测试节假日'
addHolidayTime(holidayTimeName)
#模糊查询节假日
def selectHolidayTime(holiday_time_name):
    time.sleep(1)
    browser.find_element_by_id('keyWord').clear()
    browser.find_element_by_id('keyWord').send_keys(holiday_time_name)
    browser.find_element_by_class_name('iconsh-search1').click()
    time.sleep(2)
#修改节假日
def editHolidayTime(edit_holiday_time_name):
    selectHolidayTime(holidayTimeName)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]/label[1]/input[1]').click()
    browser.find_element_by_class_name('iconsh-edit').click()
    time.sleep(1)
    browser.find_element_by_id('holiday_div').find_element_by_xpath(
        'table[1]/tbody[1]/tr[1]/td[2]/div[1]/input[2]').clear()
    browser.find_element_by_id('holiday_div').find_element_by_xpath(
        'table[1]/tbody[1]/tr[1]/td[2]/div[1]/input[2]').send_keys(edit_holiday_time_name)  # 通过第一个节点找平级的第二个节点
    browser.find_element_by_id('holiday_div').find_element_by_xpath(
        'table[1]/tbody[1]/tr[2]/td[1]/div[1]/button[1]').click()
    time.sleep(1)
    browser.find_element_by_id('keyWord').clear()
    browser.find_element_by_class_name('iconsh-search1').click()
    time.sleep(1)
    results = browser.find_element_by_id('baseTable').find_elements_by_xpath('tbody[1]/tr/td[3]')
    result = []
    for i in results:
        result.append(i.text)
    if edit_holiday_time_name in result:
        print('节假日修改成功')
    else:
        print('节假日修改失败')
editHolidayTimeName = '编辑测试节假日'
editHolidayTime(editHolidayTimeName)
#节假日配置：节假日和特定工作日
def holidayTimeSetting(name_setting,name_setting_other,time_format):
    selectHolidayTime(holidayTimeName)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]/label[1]/input[1]').click()
    browser.find_element_by_class_name('iconsh-setting').click()
    time.sleep(1)
    iframe = browser.find_element_by_class_name('layui-layer-content').find_element_by_xpath('iframe[1]')
    browser.switch_to.frame(iframe)
    time.sleep(1)
    browser.find_element_by_id('calendar').find_element_by_xpath('div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[7]/div[1]').click()
    time.sleep(1)
    browser.find_element_by_id('holiday_detail_div').find_element_by_xpath('table[1]/tbody[1]/tr[1]/td[2]/div[1]/input[4]').send_keys(name_setting)
    browser.find_element_by_id('btn_submit').click()
    time.sleep(1)
    holidaySettingResult = browser.find_element_by_class_name('layui-layer-hui').find_element_by_xpath('div[1]').text

    time.sleep(4)
    browser.find_element_by_id('calendar').find_element_by_xpath('div[2]/div[2]/table[1]/tbody[1]/tr[1]/td[3]/div[1]').click()
    time.sleep(1)
    browser.find_element_by_id('holiday_detail_div').find_element_by_xpath('table[1]/tbody[1]/tr[1]/td[2]/div[1]/input[4]').send_keys(name_setting_other)
    browser.find_element_by_id('holiday_detail_div').find_element_by_xpath('table[1]/tbody[1]/tr[2]/td[2]/div[1]/label[2]').click()
    time.sleep(1)
    browser.find_element_by_id('holiday_detail_div').find_element_by_xpath('table[1]/tbody[1]/tr[4]/td[2]/div[1]/input[1]').send_keys(time_format)
    browser.find_element_by_id('btn_submit').click()
    time.sleep(3)
    specificworkingSettingResult = browser.find_element_by_class_name('layui-layer-hui').find_element_by_xpath('div[1]').text
    time.sleep(4)
    browser.switch_to.parent_frame()
    time.sleep(1)
    browser.find_element_by_class_name('layui-layer-close').click()
    time.sleep(1)
    holidayDetail=browser.find_element_by_id('detailTable').find_elements_by_xpath('tbody[1]/tr/td[2]')
    holidayDetails=[]
    for i in holidayDetail:
        holidayDetails.append(i.text)
    if holidaySettingResult == '数据保存成功!' and name_setting in holidayDetails:
        print('节假日配置成功')
    else:
        print('节假日配置失败')
    if specificworkingSettingResult == '数据保存成功!' and name_setting_other in holidayDetails:
        print('特定工作日配置成功')
    else:
        print('特定工作日配置失败')
settingName='元旦'
settingNameOther='春节'
timeFormat='09:00:00-18:00:00'
holidayTimeSetting(settingName,settingNameOther,timeFormat)
#删除节假日
def deleteHolidayTime():
    selectHolidayTime(holidayTimeName)
    browser.find_element_by_id('baseTable').find_element_by_xpath('tbody[1]/tr[1]/td[1]/label[1]/input[1]').click()
    browser.find_element_by_class_name('iconsh-delete').click()
    time.sleep(2)
    holidayDeleteResult = browser.find_element_by_class_name('layui-layer-hui').find_element_by_xpath('div[1]').text
    if holidayDeleteResult == '数据删除成功！':
        print('节假日删除成功')
    else:
        print('节假日删除失败')
deleteHolidayTime()