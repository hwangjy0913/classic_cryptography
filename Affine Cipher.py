# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 09:13:10 2022

@author: user
"""

ABC='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
abc='abcdefghijklmnopqrstuvwxyz'

def encryption(P,K_1,K_2):#K_1은 Z_26에서 곱셈에 대한 역원이 필요하기 때문에 Z_26에서 26과 서로소인 수들의 집합의 원소만 가능하다!!!
    C=[]#C를 문자로 했으면, 18번째 줄 필요x!!!
    for x in P:
        p=abc.index(x)#P의 각 문자(x)들을 숫자로 바꿔주는 것!
        c=(K_1*p+K_2)%26#P의 각 문자(x) 암호화(숫자 형태)
        c=ABC[c]#암호화된 숫자를 문자로!!!(ABC에서의 위치)
        C=C+[c]
    C=''.join(C)
    return C

def decryption(C,K_1,K_2):
    P=''
    for x in C:
        c=ABC.index(x)#C의 각 문자들의 숫자(ABC에서의 위치)로 바꿔주는 과정(그래야 사칙연산 할 수 있으니까)
        p=(pow(K_1,-1,26)*c-K_2)%26#C의 각각의 문자 복호화(숫자), pow(K_1,-1,26)은 K_1의 26에서의 곱셈에 대한 역원!!!, mod26=%26 
        p=abc[p]
        P=P+p#문자열 덧셈으로 하면 훨씬 쉬움
    return P