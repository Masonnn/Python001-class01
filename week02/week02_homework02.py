from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()

    # browser.get('https://shimo.im/desktop')

    browser.get('https://shimo.im/login?from=home')
    time.sleep(1)

    browser.find_elements_by_tag_name('input')[0].clear()
    time.sleep(1)
    browser.find_elements_by_tag_name('input')[0].send_keys("username")  # fake username & password
    time.sleep(2)

    browser.find_elements_by_tag_name('input')[1].clear()
    time.sleep(1)
    browser.find_elements_by_tag_name('input')[1].send_keys("password")
    time.sleep(2)

    loginBtn = browser.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div/div/div[2]/div/div/div[1]/button")
    loginBtn.click()
    time.sleep(5)

    mydesk = browser.find_element_by_xpath("//*[@id='desktop-list']/a[3]")
    # print(mydesk.text)
    assert mydesk.text, u'我的桌面'

except Exception as e:
    print(e)
finally:
    browser.close()
