# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 23:22:12 2022

@author: user
"""

def LFA_caesar(C):
    from CaesarCipher import decryption, ABC
    C_count=[]#A부터 Z까지 C에서의 갯수가 차례로 이 리스트에 들어갈 것
    C_list=list(C)
    for x in ABC:#C_count의 자릿수는 A에서 Z까지의 순서대로의 자리수와 같다.(A갯수부터 차례대로 집어넣으니까)
        C_count+=[C_list.count(x)] #A~Z까지 각각의 문자 개수를 list로 묶어서 나타낸 것
        c=C_count.index(max(C_count))#C에서 가장 많이 나오는 알파벳의 ABC에서의 위치 반환
    for p in "ETAOINSHRDLCUMWFGYPBVKJQXZ":#평문에서 알파벳 빈도수 순
        K=(c-ABC.find(p))%26#find 대신 index써도 상관 없음!!!
        print(decryption(C,K))
        print("복호화 완료되었으면 y, 아니면 n을 누르시오 : ")
        command=input()#python 프로그램 자체 오류->다시 깔자
        if command=='y':
            break

    
        
