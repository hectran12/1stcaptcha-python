from onest_captcha import OneStCaptchaClient

if __name__ == '__main__':
    client = OneStCaptchaClient(apikey="YOUR_API_KEY")
    token = client.recaptcha_v2_task_proxyless(site_key="6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-",
                                               site_url="https://www.google.com/recaptcha/api2/demo")
    print(token)
    # process your task with token here
