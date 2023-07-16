1stCaptcha package for Python
=
[1stcaptcha.com](https://1stcaptcha.com) package for Python3

Solver recaptchaV2, recaptchaV3, hcaptcha, funcaptcha, imageToText, Zalo Captcha,.... Super fast and cheapest.

# Install

```bash
pip install 1stcaptcha
```

# Usage

## init client

```python
from onest_captcha import OneStCaptchaClient

APIKEY = "0aa92cd8393a49698c408ea0ee56c2a5"
client = OneStCaptchaClient(apikey=APIKEY)
```

## solver recaptcha v2:

```python
result = client.recaptcha_v2_task_proxyless(site_url="YOUR_SITE_URL", site_key="YOUR_SITE_KEY", invisible=False)
if result["code"] == 0:  # success:
    print(result["token"])
else:  # wrong
    print(result["messeage"])
```

## solver recaptcha v2 enterprise:

```python

result = client.recaptcha_v2_enterprise_task_proxyless(site_url="YOUR_SITE_URL", site_key="YOUR_SITE_KEY")
if result["code"] == 0:  # success:
    print(result["token"])
else:  # wrong
    print(result["messeage"])
```

## solver recaptcha v3:

```python
result = client.recaptcha_v3_task_proxyless(site_url="YOUR_SITE_URL", site_key="YOUR_SITE_KEY",
                                            page_action="YOUR_PAGE_ACTION")
if result["code"] == 0:  # success:
    print(result["token"])
else:  # wrong
    print(result["messeage"])
```

## solver recaptcha v3 enterprise:

```python
result = client.recaptcha_v3_enterprise_task_proxyless(site_key="YOUR_SITE_KEY",
                                                       site_url="YOUR_SITE_URL",
                                                       page_action="YOUR_PAGE_ACTION")
if result["code"] == 0:  # success:
    print(result.get('token'))
    print(result.get('user_agent'))
else:  # wrong
    print(result["messeage"])
```

## solve image2text

```python

result = client.image_to_text(file="1.jpg")
if result["code"] == 0:  # success:
    print(result["token"])
else:  # wrong
    print(result["messeage"])
```

## solve recaptchaClick

```python
url_list = ['']
caption = 'cars'
result = client.recaptcha_click(url_list=url_list, caption=caption)
if result["code"] == 0:  # success:
    print(result["token"])
else:  # wrong
    print(result["messeage"])
```

## funcaptcha

```python
site_key = "2CB16598-CB82-4CF7-B332-5990DB66F3AB"
site_url = "https://outlook.com/"
result = client.fun_captcha_task_proxyless(site_url, site_key)
if result["code"] == 0:  # success:
    print(result["token"])
else:  # wrong
    print(result["messeage"])
```