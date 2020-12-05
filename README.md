# CheckinBox
### 自己用的一些脚本，不填数值默认不启用<br>
- [天翼云盘每日签到一次，抽奖2次](https://github.com/mengshouer/CheckinBox/tree/master/Cloud189Checkin)

- [最终幻想14积分商城签到](https://github.com/mengshouer/CheckinBox/tree/master/FF14Checkin)

- [什么值得买网页每日签到](https://github.com/mengshouer/CheckinBox/tree/master/smzdmCheckin)

- [52pojie每日签到](https://github.com/mengshouer/CheckinBox/tree/master/Checkin52pj)

- [网易云音乐每日签到与刷歌单](https://github.com/mengshouer/CheckinBox/tree/master/NetEase_Music_daily)

- [有道云笔记签到](https://github.com/mengshouer/CheckinBox/tree/master/NoteyoudaoCheckin)


### Github Actions版本<br>
1.点击项目右上角的Fork，Fork此项目<br>
2.到自己Fork的项目点击Setting→Secrets→New secrets<br>
3.填写Name，和Value，具体到各脚本中看<br>
4.在"Actions"中的"run"下点击"Run workflow"即可手动执行签到，后续运行按照schedule，默认在每天凌晨0:30自动签到，可自行修改<br>
<br>
### [腾讯云函数SCF](https://console.cloud.tencent.com/scf/index)的版本<br>
### SCF计费问题：如果不是大量跑脚本的话，达不到收费标准的，如果不放心的话可以查询[账单详细](https://console.cloud.tencent.com/expense/bill/summary?businessCode=p_scf)<br>
### 实际从账户扣费时按2位小数进行扣费（即扣到分）,账单详细可以看到8位小数<br>
1.下载requirements.zip所需库，到[层](https://console.cloud.tencent.com/scf/layer)里面新建一个层<br>
2.到[函数服务](https://console.cloud.tencent.com/scf/list)里面新建一个函数，输入名字，运行环境选择python3.6，选择空白模板，下一步<br>
3.修改执行方法为index.函数入口(具体到各脚本中看)，修改index.py文件，把SCF版py文件内容覆盖掉里面的函数，删除config.json<br>
4.高级设置，添加多个环境变量key内输入：1.username 2.password 3.SCKEY(选填)<br>
value内输入：1.登录手机号 2.登录密码 3.Server酱推送SCKEY,报错提醒<br>
5.层配置，添加层，选择刚才新建的层。最后点完成<br>
6.进入函数→触发管理→新建触发器，按自己需求定时启动<br>
7.自己酌情修改函数的内存与执行超时时间以及其他参数<br>

### 一切提醒都是报错提醒，没问题不提醒
