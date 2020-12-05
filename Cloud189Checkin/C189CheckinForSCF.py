# -*- coding: utf8 -*-

import requests, time, re, rsa, json, base64, os
from urllib import parse

username = os.environ.get('username')
password = os.environ.get('password')
SCKEY = os.environ.get('SCKEY')
#推送url
scurl = f"https://sc.ftqq.com/{SCKEY}.send"

def C189Checkin(*args):
    try:
        msg = ""
        s = login(username, password)
        if(s == "error"):
            return "天翼云盘登录出错"
        else:
            pass
        rand = str(round(time.time()*1000))
        surl = f'https://api.cloud.189.cn/mkt/userSign.action?rand={rand}&clientType=TELEANDROID&version=8.6.3&model=SM-G930K'
        url = f'https://m.cloud.189.cn/v2/drawPrizeMarketDetails.action?taskId=TASK_SIGNIN&activityId=ACT_SIGNIN'
        url2 = f'https://m.cloud.189.cn/v2/drawPrizeMarketDetails.action?taskId=TASK_SIGNIN_PHOTOS&activityId=ACT_SIGNIN'
        headers = {
            'User-Agent':'Mozilla/5.0 (Linux; Android 5.1.1; SM-G930K Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 Ecloud/8.6.3 Android/22 clientId/355325117317828 clientModel/SM-G930K imsi/460071114317824 clientChannelId/qq proVersion/1.0.6',
            "Referer" : "https://m.cloud.189.cn/zhuanti/2016/sign/index.jsp?albumBackupOpened=1",
            "Host" : "m.cloud.189.cn",
            "Accept-Encoding" : "gzip, deflate",
        }
        #签到
        response = s.get(surl,headers=headers,timeout=20)
        netdiskBonus = response.json()['netdiskBonus']
        if(response.json()['isSign'] == "false"):
            print(f"未签到，签到获得  {netdiskBonus}  M空间")
            msg += f"未签到，签到获得  {netdiskBonus}  M空间\n"
        else:
            print(f"已经签到过了，签到获得  {netdiskBonus}  M空间")
            msg += f"已经签到过了，签到获得  {netdiskBonus}  M空间,"

        #第一次抽奖
        response = s.get(url,headers=headers,timeout=20)
        if ("errorCode" in response.text):
            if("User_Not_Chance" in response.text):
                print("抽奖次数不足")
                msg += "抽奖次数不足,"
            elif("InternalError" in response.text):
                print("内部错误，可能是活动下线")
                msg += "内部错误，可能是活动下线,"
            else:
                print(response.text)
                msg += "第一次抽奖出错,"
                if(SCKEY != ""):
                    data = {
                        "text" : "第一次抽奖出错",
                        "desp" : response.text
                        }
                    sc = requests.post(scurl, data=data)
        else:
            description = response.json()['description']
            print(f"抽奖获得  {description}  ")
            msg += f"抽奖获得  {description}  ,"

        #第二次抽奖
        response = s.get(url2,headers=headers,timeout=20)
        if ("errorCode" in response.text):
            if("User_Not_Chance" in response.text):
                print("抽奖次数不足")
                msg += "抽奖次数不足,"
            elif("InternalError" in response.text):
                print("内部错误，可能是活动下线")
                msg += "内部错误，可能是活动下线,"
            else:
                print(response.text)
                msg += "第二次抽奖出错,"
                if(SCKEY != ""):
                    data = {
                        "text" : "第二次抽奖出错",
                        "desp" : response.text
                        }
                    sc = requests.post(scurl, data=data)
        else:
            description = response.json()['description']
            print(f"抽奖获得  {description}  ")
            msg += f"抽奖获得  {description}  ,"
    except Exception as e:
        print("天翼云签到出错：", repr(e))
        if(SCKEY != ""):
            data = {
                "text" : "天翼云签到出错",
                "desp" : repr(e)
                }
            sc = requests.post(scurl, data=data)
        msg += "天翼云签到出错："+repr(e)
    return msg

BI_RM = list("0123456789abcdefghijklmnopqrstuvwxyz")
def int2char(a):
    return BI_RM[a]

b64map = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
def b64tohex(a):
    d = ""
    e = 0
    c = 0
    for i in range(len(a)):
        if list(a)[i] != "=":
            v = b64map.index(list(a)[i])
            if 0 == e:
                e = 1
                d += int2char(v >> 2)
                c = 3 & v
            elif 1 == e:
                e = 2
                d += int2char(c << 2 | v >> 4)
                c = 15 & v
            elif 2 == e:
                e = 3
                d += int2char(c)
                d += int2char(v >> 2)
                c = 3 & v
            else:
                e = 0
                d += int2char(c << 2 | v >> 4)
                d += int2char(15 & v)
    if e == 1:
        d += int2char(c << 2)
    return d


def rsa_encode(j_rsakey, string):
    rsa_key = f"-----BEGIN PUBLIC KEY-----\n{j_rsakey}\n-----END PUBLIC KEY-----"
    pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(rsa_key.encode())
    result = b64tohex((base64.b64encode(rsa.encrypt(f'{string}'.encode(), pubkey))).decode())
    return result

def calculate_md5_sign(params):
    return hashlib.md5('&'.join(sorted(params.split('&'))).encode('utf-8')).hexdigest()

def login(username, password):
    s = requests.Session()
    url = "https://cloud.189.cn/udb/udb_login.jsp?pageId=1&redirectURL=/main.action"
    r = s.get(url)
    captchaToken = re.findall(r"captchaToken' value='(.+?)'", r.text)[0]
    lt = re.findall(r'lt = "(.+?)"', r.text)[0]
    returnUrl = re.findall(r"returnUrl = '(.+?)'", r.text)[0]
    paramId = re.findall(r'paramId = "(.+?)"', r.text)[0]
    j_rsakey = re.findall(r'j_rsaKey" value="(\S+)"', r.text, re.M)[0]
    s.headers.update({"lt": lt})

    username = rsa_encode(j_rsakey, username)
    password = rsa_encode(j_rsakey, password)
    url = "https://open.e.189.cn/api/logbox/oauth2/loginSubmit.do"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/76.0',
        'Referer': 'https://open.e.189.cn/',
        }
    data = {
        "appKey": "cloud",
        "accountType": '01',
        "userName": f"{{RSA}}{username}",
        "password": f"{{RSA}}{password}",
        "validateCode": "",
        "captchaToken": captchaToken,
        "returnUrl": returnUrl,
        "mailSuffix": "@189.cn",
        "paramId": paramId
        }
    r = s.post(url, data=data, headers=headers, timeout=5)
    if(r.json()['result'] == 0):
        print(r.json()['msg'])
    else:
        if(SCKEY == ""):
            print(r.json()['msg'])
        else:
            msg = r.json()['msg']
            print(msg)
            data = {
                "text" : "登录出错",
                "desp" : f"错误提示：{msg}"
                }
            sc = requests.post(scurl, data=data)
        return "error"
    redirect_url = r.json()['toUrl']
    r = s.get(redirect_url)
    return s

if __name__ == "__main__":
    if username and password:
        print("----------天翼云盘开始尝试签到----------")
        C189Checkin()
        print("----------天翼云盘签到执行完毕----------")
