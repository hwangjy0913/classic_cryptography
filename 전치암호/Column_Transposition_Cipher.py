# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 16:03:26 2022

@author: user
"""
#암호키K는 0부터 len(K)-1로 입력할 것(python의 index는 0부터 시작이니까)
def E(P,K):#bogus letter=z로 약속
    #1 평문 P와 암호키K 입력 후 평문 list화
    P=list(P)
    length_P=len(P)

    #2 P를 가로부터 나열할 행렬의 크기 계산(len(K)는 열의 갯수가 된다.)
    if length_P%len(K) != 0: # 이 경우  row_num을 else의 경우처럼 하면, P의 문자들이 행렬에 모두 들어갈 수 없으므로 행을 1개 더 추가해줘야 한다.
        row_num=length_P//len(K)+1 #행의 갯수를 1개 더 추가하면 빈 공간이 생기게 되는데,
        #len(K)-length_P%len(K)만큼의 entry가 비어버린다.
        P=P+['z']*(len(K)-length_P%len(K))#그러므로, 리스트가 된 P에 z를 len(K)-length_P%len(K)만큼 더해주기
    else:
        row_num=len(P)//len(K)

    #3 P를 reshape하기(K의 원소 개수만큼의 열을 가지고 있는 행렬로...-> 그 이유는 열끼리 자리를 바꿀 때, 열들의 인덱스를 암호키 K로 하기로 했기에!!!)
    import numpy as np
    P=np.array(P)
    P_matrix=P.reshape(row_num,len(K))

    #4 K에 따라 P_matrix섞기(for문과 append함수로)
    C_matrix=P_matrix
    for i in range(len(K)):#C_matrix를 열 한개씩 지워서 마지막엔 열 index만 남아있는 빈 행렬만드는 방법
        C_matrix=np.delete(C_matrix,0,axis=1)#바로 이 다음에 P_matrix열을 암호키에 맞게 각각 배치하기 위해 P_matrix의 행의 수와 일치하는 비어있는 행렬을 만드는 과정
    for i in K:
        C_matrix=np.append(C_matrix,P_matrix[:,i].reshape(np.size(P_matrix[:,i]),1),axis=1)
        #30에서 reshape(4,1)로 해버리면 P='enemyattackstonight'처럼 길이가 16~20사이 것만 가능(나눗셈 후(#2)엔 4이니까)하므로 제한적 -> 더해질 P_matrix 열 길이로 해야 맞음!
    #5 C_matrix 열 순으로 읽기(C_matrix를 transpose해서 가로로 읽어도 같은 결과값 C가 나온다!)
    C=''
    for i in range(len(K)):# C_matrix의 열 수
        for j in range(C_matrix.shape[0]):# C_matrix의 행 수
            C=C+C_matrix[j,i]#C_matrix 1행1열부터 세로로 읽어 C에 순서대로 입력시키기
    C=C.upper()
    return C
##############################################################
def D(C,K):
    import numpy as np
    #1. 암호키의 역함수 구하기
    inv_K=['']*len(K)
    for i in range(len(K)):
        inv_K[K[i]]=i

    #2. 암호문 (len(C)/len(K))*len(K) matrix로 만들기!-> 애초에 암호문 만들 때, 암호키로 나눠 떨어지게끔 만들었으니, 암호문 만들 때처럼 나머지 걱정 x
    C=list(C)
    C_matrix=np.array(C)
    C_matrix=C_matrix.reshape(len(inv_K),len(C)//len(inv_K))#len(C)/len(inv_K)로 하면 나눠떨어져도 float취급이라 오류가 난다.
    C_matrix=C_matrix.transpose()
    #3. 암호문 matrix열 inv_K에 따라 다시 재배열->원래순서로 되돌림(암호화의 #4응용)
    P_matrix=C_matrix
    for i in range(len(inv_K)):
        P_matrix=np.delete(P_matrix,0,axis=1)
    for i in inv_K:
        P_matrix=np.append(P_matrix,C_matrix[:,i].reshape(np.size(C_matrix[:,i]),1),axis=1)
        
    #4 재배열해서 만든 P_matrix 가로로 읽기
    P_matrix=P_matrix.reshape(1,np.size(P_matrix))#P_matrix원소를 1행으로 나열
    P=''
    for i in range(np.size(P_matrix)):
        P=P+P_matrix[0,i]
    P=P.lower()
    return P
    