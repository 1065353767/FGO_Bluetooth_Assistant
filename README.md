# FGO_Bluetooth_Assistant
This is the V2.0 ver game assitant for Fate Grand Order (IOS &amp; Android both suitable). For details, see the following photos.

### Important：
Android phones can be directly controlled by a windows PC or Mac PC, but iPhone can only be controlled by a Mac PC. If you are Android player or ios player with Mac PC, I highly recommend you to use Airtest or other scripts on Github, because they are totally free and have more functions. This programm let those who play FGO on ios devices but only have windows PC realise automatic play, just like using Adb to control Android devices. 

![image1](https://github.com/McLaren12345/FGO_Bluetooth_Assistant/blob/master/images_for_Readme/1.jpg)

![image2](https://github.com/McLaren12345/FGO_Bluetooth_Assistant/blob/master/images_for_Readme/2.jpg)

![image3](https://github.com/McLaren12345/FGO_Bluetooth_Assistant/blob/master/images_for_Readme/3.jpg)

To lunch this program, all you need to do is to buy a bluebooth mouse module(about 40RMB / 6USD / 800JPY) and inatall Airplayer on your PC. You don't need to install any third party software on your phone. Also no need to jailbreak or root your phone.(Make sure that your system is ios13 or later, Android user need Android3.0 or later)

If you don't know how to connect a bluebooth mouse with your phone, just Google it!

I know that in Japan, it's not allowed to use a PC simulator to play FGO, but this programm use the phone's own function to realize automatic play. It's time to liberate your hands and time!

Since I'm a FGO player of Chinese server, all the image templates are Chinese ver. For player in other countries, you need to make templates by yourself.

The following is the instruction of this programme, you can use translate webpage to read them.

## 更新日志
### 2020-2-23:
1.修复了鼠标长时间来回移动会向左上方漂移的问题

2.fgo_optional_func中新增友情池抽取功能，日后将添加搓丸子的功能

### 2020-2-1：
1.在截图和图像识别部分加入了熔断功能，防止因小概率事件(如电话，低电量提醒等事件)导致程序死在死循环里，这里使用手机短信提醒功能来提醒人工处理。该功能参考了[hgjazhgj的脚本文件](https://github.com/hgjazhgj/FGO-py)

2.FGO主函数代码轻量化重构，使用面向对象方法增强了可读性，增加了以下子功能或优化：

&ensp;&ensp;2.1.在feed_apple函数前增加了延时防止因投屏延迟导致的识别错误

&ensp;&ensp;2.2.find_friend函数支持自定义好友(目前自带CBA及孔明的模板)，在调用main函数时修改好友名即可(默认选CBA)

&ensp;&ensp;2.3.card函数增加了随机发牌的功能(防脚本检测)

3.新增了无限池抽取功能(仅仅是简单的点击功能，未使用机器视觉)
## 一.概述
### 文件概述：
0.ReadMe.docx中有模块的淘宝地址以及使用概述

1.Base_func.py中定义了游戏图像截取以及模板匹配函数

2.Serial.py中定义了蓝牙鼠标通讯函数(感谢B站玩家@lsq5i5j_提供的相关代码)

3.FGO_func定义了FGO的相关函数，包括主程序(可在程序中的battle函数里直接修改战斗脚本)

4.Notice.py定义了手机短信通知的函数(需注册相关服务才能使用)

5.Config.py定义了csv脚本读取函数

6.Bluebooth文件夹包含蓝牙鼠标模块的使用方法

7.Template文件夹包含识别用的图片模板

8.Config文件夹包含可以使用Excel编辑的战斗脚本
### 功能：
1.支持AP不够自动喂苹果(优先银苹果后金苹果，铜苹果功能暂未开发)

2.支持自动找310CBA，如需找其他助战需自行制作图片模板

3.自定义战斗脚本和战斗次数(3T脚本基本170~190秒一关)

4.礼装掉落手机短信提醒

5.翻车提醒(实测目前没翻过车hhh)

6.新增无限池抽取功能(不是智能化抽取)

7.更多功能开发中。。。。。

## 二.使用方法
1.安装python3.7运行环境(建议直接安装Anaconda)

&ensp;&ensp;1.1.安装opencv、numpy、twilio库(否则程序无法运行)

2.安装Airplayer，分辨率调成iPhone6/6s Plus(由于本人测试环境为iPhone6s Plus，不排除其他手机模板不匹配的可能，如需使用请自行裁剪模板)

3.打开FGO_func文件，在battle函数中写入战斗脚本，在main函数中配置串口以及战斗次数

4.配置手机短信提醒服务，如果不需要请删除FGO_func文件中的sent_message函数

5.配置蓝牙鼠标模块，模块使用AT指令关闭自动休眠，设置一个名字即可连接(操作说明在bluebooth文件夹下)

6.手机连接电脑的Airplayer

7.运行FGO_func，等待完成即可
