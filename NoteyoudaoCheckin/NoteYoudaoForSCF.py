import requests, sys, json, time, hashlib, os

requests.packages.urllib3.disable_warnings()

s = requests.Session()

note_username = os.environ.get('note_username')
note_password = os.environ.get('note_password')
SCKEY = os.environ.get('SCKEY')

def checkin(YNOTE_SESS): 
    checkin_url = 'http://note.youdao.com/yws/mapi/user?method=checkin'
    cookies = {
        'YNOTE_LOGIN': 'true',
        'YNOTE_SESS': YNOTE_SESS
    }
    r = s.post(url=checkin_url, cookies=cookies, verify=False)
    if r.status_code == 200:
        info = json.loads(r.text)
        total = info['total'] / 1048576
        space = info['space'] / 1048576
        t = time.strftime('%Y-%m-%d %H:%M:%S',
                          time.localtime(info['time'] / 1000))
        msg = ' 签到成功，本次获取 '+str(space) + ' M, 总共获取 '+str(total)+' M, 签到时间 '+str(t)
        print(msg)
        return msg
    # cookie 登录失效或获取失败，改用用户名密码登录
    else:
        YNOTE_SESS = login(note_username, note_password)
        if YNOTE_SESS:
            checkin(YNOTE_SESS)

def login(username, password):
    t = str(round(time.time()*1000))
    login_url = 'https://note.youdao.com/login/acc/urs/verify/check?app=web&product=YNOTE&tp=ursto' \
                'ken&cf=6&fr=1&systemName=&deviceType=&ru=https%3A%2F%2Fnote.youdao.com%2FsignIn%2F%2Flo' \
                'ginCallback.html&er=https%3A%2F%2Fnote.youdao.com%2FsignIn%2F%2FloginCallback.html&vc' \
                f'ode=&systemName=Windows&deviceType=WindowsPC&timestamp={t}'
    password = hashlib.md5(password.encode()).hexdigest()
    data = {
        'username': username,
        'password': password
    }
    r = s.post(url=login_url, data=data, verify=False)
    x = [i.value for i in s.cookies if i.name == 'YNOTE_SESS']
    if x.__len__() == 0:
        YNOTE_SESS = "-1"
        msg = "有道云登录失败"
        print(msg)
        if SCKEY:
            scurl = f"https://sc.ftqq.com/{SCKEY}.send"
            data = {
                    "text" : msg,
                    "desp" : r.text
                    }
            requests.post(scurl, data=data)
        return
    else:
        print(username+'登陆成功，更新YNOTE_SESS,重新签到')
        YNOTE_SESS = x[0]
        # 尝试更新cookie到config.json
        try:
            data = {"YNOTE_SESS" : YNOTE_SESS}
            with open('./config.json', 'w', encoding="utf8") as f:
                json.dump(data, f, ensure_ascii=False)
        except:
            print("无法写入config.json ,pass")
        return YNOTE_SESS


def main(*args):
    try:
        with open('./config.json', 'r', encoding="utf8") as f:
            data = json.load(f)
        YNOTE_SESS = data["YNOTE_SESS"]
    except:
        YNOTE_SESS = ""
    if YNOTE_SESS:
        msg = checkin(YNOTE_SESS)
        return msg
    else:
        if note_username and note_password:
            YNOTE_SESS = login(note_username, note_password)
            if YNOTE_SESS:
                msg = checkin(YNOTE_SESS)
                return msg
        else:
            print("未设置账号密码")

if __name__ == '__main__':
    main()
