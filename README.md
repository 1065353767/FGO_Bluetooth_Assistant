# FGO_Bluetooth_Assistant
This is the V2.0 ver game assitant for Fate Grand Order (IOS &amp; Android both suitable)

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

6.更多功能开发中。。。。。

## 二.使用方法
1.安装python3.7运行环境

2.安装Airplayer，分辨率调成iPhone6/6s Plus(由于本人测试环境为iPhone6s Plus，不排除其他手机模板不匹配的可能，如需使用请自行裁剪模板)

3.打开FGO_func文件，在battl函数中写入战斗脚本，在main函数中配置串口以及战斗次数

4.配置手机短信提醒服务，如果不需要请删除FGO_func文件中的sent_message函数

5.配置蓝牙鼠标模块，模块使用AT指令关闭自动休眠，设置一个名字即可连接(操作说明在bluebooth文件夹下)

6.运行FGO_func，等待完成即可
