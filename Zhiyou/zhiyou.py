import requests, json, time, os, re

requests.packages.urllib3.disable_warnings()

cookie = os.environ.get("cookie_zhiyou")

def run(*arg):
    msg = ""
    SCKEY = os.environ.get('SCKEY')
    s = requests.Session()
    s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'})

    # 签到
    url = "http://bbs.zhiyoo.net/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&inajax=1"
    payload='formhash=f09af3af&qdxq=yl'
    headers = {
        'Connection' : 'keep-alive',
        'Content-Type' : 'application/x-www-form-urlencoded',
        'Origin' : 'http://bbs.zhiyoo.net',
        'Upgrade-Insecure-Requests' : '1',
        'Host' : 'bbs.zhiyoo.net',
        'Referer' : 'http://bbs.zhiyoo.net/plugin.php?id=dsu_paulsign:sign',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language' : 'zh-cn',
        'Accept-Encoding' : 'gzip, deflate',
        'Cookie': cookie
    }
    r = s.post(url, headers=headers, data=payload, verify=False, timeout=120)
    # print(r.text)
    if '成功' in r.text:
        msg += re.compile(r'恭喜你签到成功!获得随机奖励 金币 \d+ 元.').search(r.text)[0]
    elif '' in r.text:
        msg += '您今日已经签到，请明天再来！'
    else:
        msg += '签到失败，可能是cookie失效了！'
        scurl = f"https://sc.ftqq.com/{SCKEY}.send"
        data = {
            "text" : "智友邦  签到失败，可能是cookie失效了！！！",
            "desp" : r.text
            }
        requests.post(scurl, data=data)
    return msg + '\n'

def main(*arg):
    msg = ""
    global cookie
    clist = cookie.split("\n")
    i = 0
    while i < len(clist):
        msg += f"第 {i+1} 个账号开始执行任务\n"
        cookie = clist[i]
        msg += run(cookie)
        i += 1
    print(msg[:-1])
    return msg[:-1]


if __name__ == "__main__":
    if cookie:
        print("----------智友邦开始尝试签到----------")
        main()
        print("----------智友邦签到执行完毕----------")
