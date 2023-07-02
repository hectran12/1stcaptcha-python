import threading
import time
import json
import requests
import base64
def convert_img_to_base64(img_path):
    with open(img_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read())
        return b64_string.decode("utf8")

class onestCaptchaClient():
    def __init__(self,apikey):
        self.apikey= apikey
    def get_balance(self):
        r= requests.get("https://api.1stcaptcha.com/user/balance?apikey="+self.sitekey)
        if r.status_code ==200:
            data= r.json()
            if data['Code']==0:
                return data['Balance']
            else:
                raise RuntimeError("Error "+ str(data))
        else:
            raise RuntimeError("Error " + r.text)

    def get_result(self,taskId,timeout,time_sleep,type_captcha= ""):
        t_start = time.time()
        while((time.time()-t_start) < timeout ):
            r= requests.get("https://api.1stcaptcha.com/getresult?apikey="+self.apikey+"&taskid="+str(taskId))
            if r.status_code == 200:
                data = r.json()
                print(data)
                if data['Code'] == 0:
                    if data['Status']=="SUCCESS" :
                        if type_captcha=="image2text" or type_captcha=="recaptcha_click":
                            return data["Data"]
                        return data["Data"]["Token"]
                    elif data['Status']=="ERROR":
                        raise Exception(data["Message"])
                    time.sleep(time_sleep)
                else:
                    raise RuntimeError("Error " + data["Message"])
            else:
                raise RuntimeError("Error " + r.text)
        raise RuntimeError("TIMEOUT")

    def recaptchaV2_task_proxyless(self,siteurl,sitekey,invisible= False, timeout = 180, time_sleep=1):
        try :
            r= requests.get("https://api.1stcaptcha.com/recaptchav2?apikey="+self.apikey+"&sitekey="+sitekey+"&siteurl="+siteurl+"&version=v2&invisible="+str(invisible).lower())
            if r.status_code ==200:
                data= r.json()
                if data['Code']==0:
                    taskId= data['TaskId']
                else:
                    raise RuntimeError("Error "+ str(data))
            else:
                raise RuntimeError("Error " + r.text)
            return {"code":0,"token":self.get_result(taskId,timeout,time_sleep)}
        except Exception as e:
            return {"code":1,"messeage": str(e)}

    def funCaptcha_task_proxyless(self,siteurl,sitekey, timeout = 180, time_sleep=3):
        try:
            r = requests.get("https://api.1stcaptcha.com/funcaptchatokentask?apikey="+self.apikey+"&sitekey="+sitekey+"&siteurl="+siteurl)
            if r.status_code ==200:
                data= r.json()
                if data['Code']==0:
                    taskId= data['TaskId']
                else:
                    raise RuntimeError("Error "+ str(data))
            else:
                raise RuntimeError("Error " + r.text)
            return {"code": 0, "token": self.get_result(taskId,timeout,time_sleep)}
        except Exception as e:
            return {"code": 1, "messeage": str(e)}

    def recaptcha_click(self,url_list,caption,timeout=60,time_sleep=3):
        try:
            req = {'Image_urls': url_list, 'Caption': caption,"Apikey": self.apikey,"Type": "recaptcha",}
            data = json.dumps(req)
            headers = {
                'Content-Type': 'application/json',
            }
            r = requests.post(
                "https://api.1stcaptcha.com/recognition",headers=headers, data=data)
            if r.status_code ==200:
                data= r.json()
                if data['Code']==0:
                    taskId= data['TaskId']
                else:
                    raise RuntimeError("Error "+ str(data))
            else:
                raise RuntimeError("Error " + r.text)
            return {"code": 0, "token": self.get_result(taskId, timeout, time_sleep,type_captcha="recaptcha_click")}
        except Exception as e:
            return {"code": 1, "messeage": str(e)}


    def image_to_text(self,base64img= None,file=None,timeout=60,time_sleep=1):
        try :
            if base64img is None:
                if file is None:
                    raise RuntimeError("base64img and file is None ")
                else :
                    base64img= convert_img_to_base64(file)
            req = {'Image': base64img,"Apikey": self.apikey,"Type": "imagetotext"}
            data = json.dumps(req)
            headers = {
                'Content-Type': 'application/json',
            }
            r = requests.post(
                "https://api.1stcaptcha.com/recognition",headers=headers, data=data)
            if r.status_code ==200:
                data= r.json()
                if data['Code']==0:
                    taskId= data['TaskId']
                else:
                    raise RuntimeError("Error "+ str(data))
            else:
                raise RuntimeError("Error " + r.text)
            return {"code": 0, "token": self.get_result(taskId, timeout, time_sleep,type_captcha="image2text")}
        except Exception as e:
            return {"code": 1, "messeage": str(e)}


