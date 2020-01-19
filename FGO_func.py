# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:51:36 2019

@author: McLaren
"""
import time
import sys
from tqdm import tqdm
sys.path.append(r'F:\FGO_Project')
from playsound import playsound 
import Serial 
import Base_func
import Config
from Notice import sent_message

def enter_battle():    
    Flag,Position = Base_func.match_template('Menu_button')
    while bool(1-Flag):
        time.sleep(1)       
        Flag,Position = Base_func.match_template('Menu_button')
        #确认已经返回菜单界面
    Flag,Position = Base_func.match_template('LastOrder_sign') 
    if Flag:
        Serial.touch(Position[0]+230,Position[1]+50)       
        print(' ')
        print(' enter battle success')
        return Flag
    else:
        print(' enter battle fail')
        return Flag
    
def apple_feed(): 
    time.sleep(1.5)
    Flag,Position = Base_func.match_template('AP_recover')
    if Flag:
        Flag,Position = Base_func.match_template('Silver_apple')
        if Flag:
            Serial.touch(709,Position[1])
            time.sleep(1.5)            
            Flag,Position = Base_func.match_template('Feedapple_decide')
            Serial.touch(Position[0],Position[1])           
            print(' feed silver apple success')
            return Flag
        else:
            Flag,Position = Base_func.match_template('Gold_apple')
            if Flag:
                Serial.touch(709,Position[1])
                time.sleep(1.5)                
                Flag,Position = Base_func.match_template('Feedapple_decide')
                Serial.touch(Position[0],Position[1])                
                print(' feed gold apple success')
                return Flag
            else:
                print(' no apple remain')
                Serial.touch(0,0)                
                exit(0)
                return Flag
    else:
        print(' no need to feed apple')
        
def find_friend():       
    Flag,Position = Base_func.match_template('friend_sign')
    while bool(1-Flag):
        time.sleep(1)       
        Flag,Position = Base_func.match_template('friend_sign')
        if Flag:
            break
        Flag,Position = Base_func.match_template('no_friend')
        if Flag:
            break
    Flag,Position = Base_func.match_template('CBA_skill_level')
    time_limit_flag = 1
    #找310CBA直到找到为止
    while bool(1-Flag):
        print(' didn\'t find CBA, retry. attempt{}'.format(time_limit_flag))
        if time_limit_flag>1:
            time.sleep(15)          
        #Flag,Position = Base_func.match_template('Refresh_friend')
        Serial.touch(710,110)       
        time.sleep(1.5)
        Flag,Position = Base_func.match_template('Refresh_decide')
        Serial.touch(Position[0],Position[1])
        time.sleep(1.5)
        
        Flag,Position = Base_func.match_template('friend_sign')
        while bool(1-Flag):
            time.sleep(1)       
            Flag,Position = Base_func.match_template('friend_sign')
            if Flag:
                break
            Flag,Position = Base_func.match_template('no_friend')
            if Flag:
                break
            
        if time_limit_flag>10:
            k=input(' 10次刷新未找到CBA，需人工操作，按0退出执行:')
            if k==0:
                Serial.touch(0,0)                
                exit(0)        
        Flag,Position = Base_func.match_template('CBA_skill_level')
        time_limit_flag+=1
        
    if Flag:
        print(' success find CBA')
        Serial.touch(Position[0],Position[1]-60)
        time.sleep(1)               
        Serial.touch(1005,570)       
        print(' Start battle button pressed')
        
def quit_battle():
    time.sleep(15)
    while True:
        time.sleep(1)
        Flag,Position = Base_func.match_template('Battlefinish_sign')
        if Flag:
            break
        Flag,Position = Base_func.match_template('Master_face')
        if Flag:
            break
    Flag,Position = Base_func.match_template('Master_face')
    if Flag:
        for i in range(3):
            playsound('F:/FGO_Project/11750.mp3')
        print(' 翻车，需要人工处理')          #翻车检测，系统三声报警
        Serial.mouse_set_zero()
        sent_message(text='【FGO】: Encounter a battle error.')        
        exit(0) 
    print(' battle finished')
    time.sleep(1)
    Flag,Position = Base_func.match_template('Rainbow_box')  #检测是否掉礼装，若掉落则短信提醒
    if Flag:
        sent_message()
    Serial.touch(986,565,6)    
    Serial.touch(285,525,2)                #拒绝好友申请
    print(' quit success')
    time.sleep(7)
        
def Master_skill(skill_no,para1=3,para2=2):
    Serial.touch(1010,266)               #御主技能按键    
    if skill_no==1:
        Serial.touch(760,266)        
    elif skill_no==2:
        Serial.touch(835,266)        
    elif skill_no==3:                   #换人
        Serial.touch(920,266)                           
        Serial.touch(630+(para2-1)*170,300)            #默认换最后一人与替换区第二人        
        Serial.touch(120+(para1-1)*170,300)        
        Serial.touch(530,530)
    Flag,Position = Base_func.match_template('Master_face')
    while bool(1-Flag):
        time.sleep(1)        
        Flag,Position = Base_func.match_template('Master_face')
    print(' master skill{} has pressed'.format(skill_no))
        
def character_skill(character_no,skill_no,para=None):   #角色编号，技能编号，选人（可选）
    Position = (65+(character_no-1)*270+(skill_no-1)*80,488)
    Serial.touch(Position[0],Position[1])    
    if para != None:
        Position = (280+(para-1)*250,350)  #技能选人
        Serial.touch(Position[0],Position[1])        
    time.sleep(3)         #等待技能动画时间
    Flag,Position = Base_func.match_template('Master_face')
    while bool(1-Flag):
        time.sleep(1)        
        Flag,Position = Base_func.match_template('Master_face')
    print(' character{}\'s skill{} has pressed'.format(character_no,skill_no))
    
def card(Baoju_no=1):    
    Serial.touch(950,510)   #点击attack按钮 
    time.sleep(2)       
    Serial.touch(350+(Baoju_no-1)*200,200)   #打手宝具,参数可选1-3号宝具位        
    Serial.touch(350+(Baoju_no-1)*200,430)  #随便两张牌        
    Serial.touch(540,430)    
    print(' Card has pressed')
    
def battle(): 
    #判断是否进入战斗界面
    time.sleep(10)                          #等待战斗开始
    Flag,Position = Base_func.match_template('Master_face')
    while bool(1-Flag):
        time.sleep(1)        
        Flag,Position = Base_func.match_template('Master_face')
    #Turn1
    Serial.mouse_set_zero()         #鼠标复位,防止误差累积
    time.sleep(6)                   #等待6秒，因为礼装效果掉落暴击星会耗时
    character_skill(3,1,1)
    character_skill(2,1,1)
    character_skill(1,1)
    character_skill(1,3)  
    card()
    
    Serial.mouse_set_zero()         #鼠标复位,防止误差累积
    time.sleep(10)                          #等待战斗动画播放完成
    Flag,Position = Base_func.match_template('Master_face')
    while bool(1-Flag):
        time.sleep(1)        
        Flag,Position = Base_func.match_template('Master_face')
    #Turn2
    character_skill(3,3,1)
    Master_skill(3)
    time.sleep(1)
    character_skill(3,3)
    card()    
    
    Serial.mouse_set_zero()         #鼠标复位,防止误差累积
    time.sleep(10)                          #等待战斗动画播放完成
    Flag,Position = Base_func.match_template('Master_face')
    while bool(1-Flag):
        time.sleep(1)        
        Flag,Position = Base_func.match_template('Master_face')
    #Tun3
    character_skill(3,1,1)
    character_skill(2,3,1)
    character_skill(2,2)    
    card()

def config2battle():
    Flag,Position = Base_func.match_template('Master_face')
    while bool(1-Flag):
        time.sleep(2)        
        Flag,Position = Base_func.match_template('Master_face')
    #Turn1    
    Config.Config2Command(Config.df1)
    
    time.sleep(5)                          #等待战斗动画播放完成
    Flag,Position = Base_func.match_template('Master_face')
    while bool(1-Flag):
        time.sleep(2)        
        Flag,Position = Base_func.match_template('Master_face')
    #Turn2
    Config.Config2Command(Config.df2)
    
    time.sleep(5)                          #等待战斗动画播放完成
    Flag,Position = Base_func.match_template('Master_face')
    while bool(1-Flag):
        time.sleep(2)        
        Flag,Position = Base_func.match_template('Master_face')
    #Tun3
    Config.Config2Command(Config.df3)
    
    
def FGO_process(times=1,command_switch=False):
    for i in tqdm(range(times)):
        times-=1
        enter_battle()
        apple_feed()
        find_friend()
        if command_switch:
           config2battle()
        else:
           battle()        
        quit_battle()
        Serial.mouse_set_zero()         #鼠标复位,防止误差累积        
        print(' ')
        print(' {}times of battles remain'.format(times))
        time.sleep(1)
      
def main(port_no,times=1,use_commmand=False):
    Serial.port_open(port_no)   #写入通讯的串口号
    Serial.mouse_set_zero()
    FGO_process(times,use_commmand)
    Serial.port_close()
    print(' All done!') 
    
    
if __name__=='__main__':
	main('com5',40)

