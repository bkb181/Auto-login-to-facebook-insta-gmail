from selenium import webdriver
browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")

browser.maximize_window()
username = "useid" # write your used id
password = "pass"   # write your password
browser.get("https://www.facebook.com")  # change the url for different website
browser.implicitly_wait(3)
browser.find_element_by_xpath('//*[@id="email"]').send_keys(username)
browser.find_element_by_xpath('//*[@id="pass"]').send_keys(password)

