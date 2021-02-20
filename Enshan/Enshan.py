import requests, json, time, os
from lxml import etree
requests.packages.urllib3.disable_warnings()

cookie = os.environ.get("cookie_enshan")

def run(*arg):
    msg = ""
    SCKEY = os.environ.get('SCKEY')
    s = requests.Session()
    s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'})

    # 签到
    url = "https://www.right.com.cn/forum/home.php?mod=spacecp&ac=credit&op=log&suboperation=creditrulelog"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
        'Connection' : 'keep-alive',
        'Host' : 'www.right.com.cn',
        'Upgrade-Insecure-Requests' : '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language' : 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Cookie': cookie
    }
    try:
        r = s.get(url, headers=headers, timeout=120)
        # print(r.text)
        if '每天登录' in r.text:
            h = etree.HTML(r.text)
            data = h.xpath('//tr/td[6]/text()')
            msg += f'签到成功或今日已签到，最后签到时间：{data[0]}'
        else:
            msg += '签到失败，可能是cookie失效了！'
            scurl = f"https://sc.ftqq.com/{SCKEY}.send"
            data = {
                "text" : "恩山论坛  签到失败，可能是cookie失效了！！！",
                "desp" : r.text
                }
            requests.post(scurl, data=data)
    except:
        msg = '无法正常连接到网站，请尝试改变网络环境，试下本地能不能跑脚本，或者换几个时间点执行脚本'
        print(msg)
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
        print("----------恩山论坛开始尝试签到----------")
        main()
        print("----------恩山论坛签到执行完毕----------")
