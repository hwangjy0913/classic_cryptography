# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 09:34:19 2022

@author: jaey0
"""

#리스트 응용
abc='abcdefghijklmnopqrstuvwxyz'#from string import ascii_lowercase(대문자는 uppercase)로 불러올 수도 있음
ABC=abc.upper()
# P는 평문, C는 암호문, K는 암호키이다.
def encryption(P,K):
    C=[]
    for x in P:             #문자열 P문자들을 왼쪽에서부터 한개씩 뽑아내는 for문
        p=abc.index(x)      #P에서 뽑아낸 문자가 알파벳에서 몇 번째에 해당하는지 알아내기
        p=(p+K)%26          #암호키K를 이용하여 P의 각 문자를 일정한 간격으로 알파벳 위치 이동
        c=ABC[p]            #P의 각각의 문자를 알파벳에서 K만큼 이동시킨 위치로 알파벳 바꾸기
        C=C+[c]             #문자를 한 개씩 바꿀 때마다 리스트형으로 나열
    C=''.join(C)            #리스트를 문자형으로
    return C
# 16부터 18까지가 암호화과정이라 보면 된다.

def decryption(C,K):
    P=[]
    for x in C:
        c=ABC.index(x)
        c=(c-K)%26
        p=abc[c]
        P=P+[p]
    P=''.join(P)
    return P

