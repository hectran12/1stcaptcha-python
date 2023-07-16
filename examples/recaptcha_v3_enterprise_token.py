from onest_captcha import OneStCaptchaClient

if __name__ == '__main__':
    client = OneStCaptchaClient(apikey="YOUR_API_KEY")
    result = client.recaptcha_v3_enterprise_task_proxyless(site_key="YOUR_SITE_KEY",
                                                           site_url="YOUR_SITE_URL",
                                                           page_action="YOUR_PAGE_ACTION")
    token = result.get('token')
    user_agent = result.get("user_agent")
    print(token)
    # process your task with token here
