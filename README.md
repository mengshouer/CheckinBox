# Cloud189Checkin
天翼云盘每日签到一次，抽奖2次  
使用方法  
1.测试环境为python3.7.6,自行安装python3  
2.requirements.txt 是所需第三方模块，执行 `pip install -r requirements.txt` 安装模块  
3.可在脚本内直接填写账号，密码  
4.Python 和需要模块都装好了直接在目录 cmd 运行所要运行的脚本。  

登录看的以下项目：
> [Cloud189](https://github.com/Dawnnnnnn/Cloud189)
> [cloud189](https://github.com/Aruelius/cloud189)

# Github Actions说明
## 一、Fork此仓库
![](http://tu.yaohuo.me/imgs/2020/06/f059fe73afb4ef5f.png)
## 二、设置账号密码
添加名为**USER**、**PWD**的变量  
值分别为**账号**、**密码**  
多账号时账号密码一行一个一一对应
示例：
**USER**
```
123456
24678
```
**PWD**
```
cxkjntm
jntmcxk
```
![](http://tu.yaohuo.me/imgs/2020/06/748bf9c0ca6143cd.png)
![](http://tu.yaohuo.me/imgs/2020/06/af2013b1ef5d8430.png)
![](http://tu.yaohuo.me/imgs/2020/06/09c22adcec7b5d81.png)


## 三、启用Action
1 点击**Action**，再点击**I understand my workflows, go ahead and enable them**  
2 修改任意文件后提交一次  
![](http://tu.yaohuo.me/imgs/2020/06/34ca160c972b9927.png)

## 四、查看运行结果
Actions > Cloud189Checkin > build  
能看到如下图所示，表示成功  
![](http://tu.yaohuo.me/imgs/2020/06/b9e596c99f3835e0.png)

此后，将会在每天10:00-10:45之间和22:00-22:45之间各签到一次  
若有需求，可以在[.github/workflows/run.yml]中自行修改

## 可能遇到的问题
- 1. 验证码错误  
首先考虑是不是密码错误  
其次查看是否已经关闭设备锁  
- 2. 暂无

## 关于泄露密码的说明
起初有人提醒我会把账号密码打印出来，我就抽空把这个问题解决了。但是我没有意识到事情的严重性，认为无伤大雅。  
我原以为Actions的Biuld记录只有自己可以看到，所以并未在意，直到malaohu大佬发说明我才意识到不对。万万没想到是任何人只要点开都能看到。  
对此我很惭愧，也很无奈，我似乎没有什么直接有效的挽救的办法。  
这个问题出现在【6月~~21~~24号】前Fork的仓库(单账号版本无影响)，在新增多账号的功能时，我憨憨地把每个账号密码打印出来了，这是我的憨憨习惯。  
这个问题存在的时间不算长，糟糕的是就在这不长的时间当中Fork的数量不小，问题很严重。  
所以，请各位第一时间修改天翼云盘密码，删除Fork的仓库。重新Fork。  
这次密码泄露，我算是始作俑者，同时也是这个问题的受害者(我的密码也一样有泄露的风险)。  
### 再次表示歉意！
### 请务必尽快修改天翼云盘密码！删除Fork的仓库！
