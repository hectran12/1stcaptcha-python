website : 1stcaptcha.com

solver recaptchaV2, recaptchaV3, hcaptcha, funcaptcha, imageToTexxt ,Zalo Captcha, .... Super fast and cheapest.
Install library :

cd anycaptcha-python
pip install -e .

read demo.py to know how to use the library

# init client 

    from onestCaptcha import onestCaptchaClient
    APIKEY ="0aa92cd8393a49698c408ea0ee56c2a5"
    client= onestCaptchaClient(apikey=APIKEY)


#  solver recaptcha v2:

    sitekey="6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-"
    siteurl="https://www.google.com/recaptcha/api2/demo"
    invisible= False
    result= client.recaptchaV2_task_proxyless(siteurl,sitekey,invisible=invisible)
    if result["code"]==0 : # success:
        print(result["token"])
    else: # wrong
        print(result["messeage"])

# solve image2text


    result= client.image_to_text(file="1.jpg")
    #if file # result= client.image_to_text(base64img="base64img") # if you send base64img
    if result["code"]==0 : # success:
        print(result["token"])
    else: # wrong
        print(result["messeage"])

# solve recaptchaClick

    url_list=['']
    caption='cars'
    result= client.recaptcha_click(url_list=url_list,caption=caption )
    # result= client.image_to_text(base64img="base64img") # if you send base64img
    if result["code"]==0 : # success:
        print(result["token"])
    else: # wrong
        print(result["messeage"])

# funcaptcha
    sitekey="2CB16598-CB82-4CF7-B332-5990DB66F3AB"
    siteurl="https://outlook.com/"
    result= client.funCaptcha_task_proxyless(siteurl,sitekey )
    # result= client.image_to_text(base64img="base64img") # if you send base64img
    if result["code"]==0 : # success:
        print(result["token"])
    else: # wrong
        print(result["messeage"])


