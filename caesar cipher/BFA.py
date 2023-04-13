# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 12:36:40 2022

@author: user
"""
import CaesarCipher as cc
def BFA(C):#전수 조사 공격
    for K in range(0,26):
        print('키: %d일 때, 평문: %s'%(K, cc.decryption(C,K)))
    
