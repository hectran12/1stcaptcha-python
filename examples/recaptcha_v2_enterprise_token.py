from onest_captcha import OneStCaptchaClient

if __name__ == '__main__':
    client = OneStCaptchaClient(apikey="YOUR_API_KEY")
    token = client.recaptcha_v2_task_proxyless(site_key="YOUR_SITE_KEY",
                                               site_url="YOUR_SITE_URL")
    print(token)
    # process your task with token here
