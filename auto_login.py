from selenium import webdriver
#browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
browser = webdriver.Chrome(executable_path='D:\TheSurgicalStrike\chromedriver_win32/chromedriver.exe')

browser.maximize_window()
username = "useid"
password = "pass"
browser.get("https://www.facebook.com")
browser.implicitly_wait(3)
browser.find_element_by_xpath('//*[@id="email"]').send_keys(username)
browser.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
#How webpage looks before login screenshot
browser.get_screenshot_as_file("Facebook.png")
browser.find_element_by_id("loginbutton").click()
#How webpage looks after login screenshot
browser.get_screenshot_as_file("Facebook1.png")
