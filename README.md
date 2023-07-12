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
site_key = "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-"
site_url = "https://www.google.com/recaptcha/api2/demo"
invisible = False
result = client.recaptcha_v2_task_proxyless(site_url, site_key, invisible=invisible)
if result["code"] == 0:  # success:
    print(result["token"])
else:  # wrong
    print(result["messeage"])
```

## solver recaptcha v3:

```python
token = client.recaptcha_v3_task_proxyless(site_key="YOUR_SITE_KEY",
                                           site_url="YOUR_SITE_URL",
                                           page_action="YOUR_PAGE_ACTION")
if result["code"] == 0:  # success:
    print(result["token"])
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