from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

drive = webdriver.Remote(
    # 固定格式只有地址可以改变
    command_executor="http://192.168.100.2:4444/wd/hub",
    desired_capabilities=DesiredCapabilities.CHROME
)

drive.get("http://www.baidu.com")
print(drive.title)
with open("/data/baidu.html", "w") as f:
    f.write(drive.page_source)
print(drive.page_source)
drive.close()
