# Enshan
### 恩山论坛每日签到<br>
### 使用方法<br>
Github Actions版本<br>
1.点击项目右上角的Fork，Fork此项目<br>
2.到自己Fork的项目点击Setting→Secrets→New secrets<br>
3.Name填写cookie_enshan，Value填写 获取到的cookie<br>
4.在"Actions"中的"run"下点击"Run workflow"即可手动执行签到，后续运行按照schedule，默认在每天凌晨0:30自动签到，可自行修改<br>
5.(可选)New secrets，Name填写SCKEY，Value填写 Server酱推送SCKEY  报错提醒用
<br>
<br>
[腾讯云函数SCF](https://console.cloud.tencent.com/scf/index)的版本<br>
1.下载requirements.zip所需库，到[层](https://console.cloud.tencent.com/scf/layer)里面新建一个层<br>
2.到[函数服务](https://console.cloud.tencent.com/scf/list)里面新建一个函数，输入名字，运行环境选择python3.6，选择空白模板，下一步<br>
3.修改执行方法为index.main，修改index.py文件，把SCF版py文件内容覆盖掉里面的函数，删除config.json<br>
4.高级设置，添加多个环境变量key内输入：1.cookie_enshan 2.SCKEY(选填)<br>
value内输入：1.获取到的cookie 2.Server酱推送SCKEY,报错提醒<br>
5.层配置，添加层，选择刚才新建的层。最后点完成<br>
6.进入函数→触发管理→新建触发器，按自己需求定时启动<br>

### Cookie获取方法<br>
浏览器打开需要签到的网站并登录，F12打开检查<br>
在 Chrome 浏览器下方的开发工具中单击 Network 标签页(其他浏览器大同小异)<br>
F5刷新当前网站，随便选一个Name里面的网页，在右侧Headers内找到Cookie: xxxxxx，复制xxxx的东西，一般很长一大串<br>
Headers如果没有Cookie就换另一个Name里面的网页，实在看不懂就自行baidu吧.jpg<br>
Cookie过期就必须手动更换，再重复一次获取流程，然后Github到secrets里更新，腾讯云函数就到函数配置中修改环境变量的值
