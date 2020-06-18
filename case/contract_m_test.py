from selenium.webdriver.common.keys import Keys
from handle.get_utils import ActionUtil
from selenium import webdriver

mobileEmulation = {'deviceName': 'iPhone X'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
driver.get('http://wxadmin.wegui.cn/admin/#/')

ActionUtil.input(driver, "//input[@placeholder='用户名']", 'xiaod90')
ActionUtil.input(driver, "//input[@placeholder='密码']", '123456')
ActionUtil.click(driver, "//button[@class='mint-button primary-btn mint-button--default mint-button--large']")
ActionUtil.click(driver, "//div[contains(text(),'合同审批(新)')]/parent::*/parent::*")
ActionUtil.click(driver, "//span[contains(text(),'添加申请')]")
if ActionUtil.get_attribute(driver, "//div[@class='edit-cabinet']/div[@class='title']", "请仔细填写合同审批"):
    print("开始填写合同审批")
    ActionUtil.input(driver, "//input[@placeholder='请输入网点名称']", "2020061601")
    # Click(driver, "//label[text()='需扣除运费']")
    # driver.find_element_by_css_selector("[for='needFreight']").send_keys(Keys.ENTER)

    # WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//label[text()='需扣除运费']/preceding-sibling::*"))).click()
    # 滚动到最底部
    # js = "var q=document.documentElement.scrollTop=100000"
    # driver.execute_script(js)
    # time.sleep(3)
    # Action_util.add_photo(driver, "//input[@type='file']", "E:/xt/xtselenium/util/v.png")
    # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys("E:/xt/xtselenium/util/v.png")
    # file = driver.find_element_by_xpath("//input[@type='file']")
    # file.send_keys("E:/xt/xtselenium/util/v.png")
else:
    print("合同审批文案对比失败")
