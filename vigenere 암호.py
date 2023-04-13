# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 12:54:24 2022

@author: user
"""

def vigenere_encryption(P,Keyword):#Keyword도 문자열 형태(대문자)임
    ABC="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    abc="abcdefghijklmnopqrstuvwxyz"
    C=''
    for i in range(len(P)):#평문 첫번째 문자부터 차례대로 len(Keyword) 구간씩 Keyword의 각 문자들과 차례대로 Caesarcipher적용됨.
        c=(abc.index(P[i])+ABC.index(Keyword[i%len(Keyword)]))%26#평문에서 len(Keyword)구간 하나만 살펴보자면,
#각각의 문자들은 Keyword의 각 문자들과 순서대로 Caesarcipher가 적용되기에 ABC.index(Keyword[i%len(Keyword)])에서 Keyword[i%len(Keyword)]를 쓴 것        
        C+=ABC[c]
    return C
        
        
def vigenere_decryption(C,Keyword):
    ABC="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    abc="abcdefghijklmnopqrstuvwxyz"
    P=''
    for i in range(len(C)):
        p=(ABC.index(C[i])-ABC.index(Keyword[i%len(Keyword)]))%26
        P+=abc[p]
    return P