# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 20:17:33 2020

@author: McLaren
"""

import sys
sys.path.append(r'F:\FGO_Project') 
import Serial

#无限池抽取函数
def Infinate_pool():
    Serial.mouse_set_zero()
    Serial.mouse_move((320,360))
    for i in range(100):
        Serial.mouse_click()
