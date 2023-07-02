import time

from selenium import webdriver

from onest_captcha import OneStCaptchaClient


def demo_funcaptcha():
    APIKEY = "0aa92cd8393a49698c408ea0ee56c2a5"
    client = OneStCaptchaClient(apikey=APIKEY)
    sitekey = "2CB16598-CB82-4CF7-B332-5990DB66F3AB"
    siteurl = "https://twitter.com"
    while (True):
        result = client.funCaptcha_task_proxyless(siteurl, sitekey)
        # result= client.image_to_text(base64img="base64img") # if you send base64img
        if result["code"] == 0:  # success:
            return result["token"]
        else:  # wrong
            continue


driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://outlook.com")
# send username, password, birthday,......
input()
driver.switch_to.frame(driver.find_element_by_id('enforcementFrame'))
time.sleep(0.5)
token = demo_funcaptcha()
print(token)
driver.execute_script(
    'parent.postMessage(JSON.stringify({eventId:"challenge-complete",payload:{sessionToken:"' + token + '"}}),"*")')
input()
