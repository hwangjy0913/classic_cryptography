# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 09:54:31 2022

@author: user
"""


#f='NOATRFBECFUXDQGYLKHVIJMPZSW'
#P='thismessageiseasytoencrypbuthardtofindthekey'

abc='abcdefghijklmnopqrstuvwxyz'

def E(P,f):#f는 각 알파벳을 일대일 대응시키는 함수(A~Z까지 자기 원하는 순서대로 나열하기)
    C=''
    for i in P:
        C+=f[abc.index(i)]
    return C

def D(C,f):
    P=''
    for i in C:
        P+=abc[f.index(i)]
    return P
