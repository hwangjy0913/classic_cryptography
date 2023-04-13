# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 16:34:05 2022

@author: user
"""
#P='helloworld'일 때 뿐만 아니라, P="hidethegoldinthetreestump"(wiki백과 playfair 예시) 때도 알맞게 암호화 된다.
#bogus letter는 x를 넣기로 했고, i=j 약속했음.
def E(P,Keyword):
#암호화 준비
#Keytable만들기 전 배열의 중복문자 모두 제거하면서 keyword+ABC순서 유지하기('파이썬 중복된 문자 제거'구글링하면 내가 한 것보다 쉬운 방법 많이 나옴)
    ABC='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    KeyABCstring=Keyword+ABC
    KeyABCdict={}
    for x in KeyABCstring:#string의 첫 문자부터 마지막 문자까지 차례대로 위치값을 value, 그 문자를 key값으로 대응시키면,
        KeyABCdict[x]=KeyABCstring.index(x)#index함수 메커니즘 자체가 처음으로 문자가 나온 위치만 말해주기 때문에, for문에서 뒤에 같은 문자가 반복되어도. 처음 나온 위치가 반환되기에, 결국 dictionary에서는 중복된 문자들은 모두 제거되면서, KeyABClist가 순서대로 나열된다.
    KeyABClist=list(KeyABCdict.keys())
    del KeyABClist[KeyABClist.index('J')]#I=J라 가정하고, 이 KeyABClist를 5x5matrix(keytable)로 만들기 위해서는 'J'를 제거해야 한다.
#Keytable만들기
    import numpy as np
    KeyABCvector=np.array(KeyABClist)#KeyABClist를 1x25vector로 만들기
    Keytable=KeyABCvector.reshape(5,5)#Keytable 만들기

#P(평문)에서 j가 있으면 모든 j는 i로 바꿔주기(내가 i=j로 하기로 약속하고, Keytable에서 j를 없앴으니)
    if P.count('j')!=0:
        for i in range(len(P)):
            if P[i]=="j":
                P=P.replace(P[i],"i")

#P(평문)에서 문자 2개씩 묶고, 같은 문자끼리 묶기는 경우, 그 사이에 X 넣기(빈도수 낮은 문자 아무거나 넣으면 되는데, 내가 X넣기로 약속한 것)
    while True:
        j=0
        for i in range(len(P)//2):
            j+=1
            b=P[2*i:2*i+2]#2*i, 2*(i+1)번째 문자만 뽑아냄.
            if b[0]==b[1]:
                P=list(P)
                P.insert(2*i+1,'x')#본래의 2*i+1번째 문자는 2*(i+1)번째 위치로 미뤄자 다음 루프 때 또 사용됨!
                P=''.join(P)
                break#도중에 x가 삽입되면, P의 길이가 변하기에, 처음으로 돌아가 다시시작해야 해서 x추가할 때마다 break로 다시 첨부터 하기!
        if j==len(P)//2:
            break 
#이후 P의 길이가 짝수가 되어야 암호화가 가능하기에, 홀수이면 마지막에 X 더하기!!!
    if len(P)%2==1:
        P=P+'x'
    P=P.upper()#암호화를 하기 위해서는 암호화 준비된 평문을 대문자로 바꿔야 한다.(Keytable이 대문자라)
#암호화 시작
#P에서 각각 2개씩 문자를 묶어서 keytable에 나타날 수 있는 형태 3가지-> if 3번 써서 각 쌍이 3가지 중 하나의 법칙에 의해 암호화되게 하기
    P=list(P)#P를 list로 바꿔야 P의 원소들을 다른 것으로 바꿀 수 있다!!!(문자열은 한번에는 불가능!!1)
    for i in range(len(P)//2):
        b=P[2*i:2*i+2]#P의 문자 2개씩 쌍으로 순서대로 뽑아 암호화하겠다는 의미
    #1.각 문자가 서로 다른 행, 열에 있는 경우(직사각형 만듦)
    #b[0], b[1]의 keytable에서의 index를 행별로, 열별로 비교해 둘다 다르면 if문 실행되게 하기(index가 행, 열별로 다르다는 것은, 직사각형을 이룬다는 뜻)
        if (np.where(Keytable==b[0])[0]!=np.where(Keytable==b[1])[0]) and (np.where(Keytable==b[0])[1]!=np.where(Keytable==b[1])[1]):#1행 1열짜리 array 안에 boolean값이 들어가 있으나, 일반적인 if문처럼 그냥 바로 조건문의 참, 거짓에 따라 다음 문장을 수행한다!!!
            b=[Keytable[np.where(Keytable==b[0])[0][0],np.where(Keytable==b[1])[1][0]],Keytable[np.where(Keytable==b[1])[0][0],np.where(Keytable==b[0])[1][0]]]
            #54번째 줄은 b[0]와 b[1] 각각의 행값은 유지하면서 열값만 서로의 것을 맞바꾸는 문장
            #np.where(Keytable==b[0])은 Keytable에서의 b[0]의 위치(몇 행 몇 열인지)를
            #array 2개짜리 튜플로 나타내고 첫번째 array의 첫번째 원소가 행 그리고 두번째 array의 첫번째 원소가 열을 의미한다.
            #그러므로 np.where(Keytable==b[0])[0][0]까지 해야, b[0]의 행의 위치를 숫자로 받을 수 있다!
            #질문 : 그런데 왜 np.where(Keytable==b[0])[0][1]하면 index error?->datatype이 튜플의 두번째 원소에 들어있는데?
            #54번째 줄은 b[0]와 b[1]의 행은 각자 자기 행, 열은 서로의 열을 바꾼 형태
            #원래 b[0]와 b[1]을 따로따로 54, 55번째 줄에 썼는데, 그럼 b[0]의 값에
            #b[0]의 열이 b[0]가 위치한 행의 b[1]이 위치한 열의 값이 저장된 후 55번째 문장에서 
            #b[1]의 열 값에 이미 바뀐 b[0] 값 즉, 현재 b[1]의 열 값이 다시 저장 되는 것이므로, 위치가 바뀌지 않게 된다.
            #그러므로 지금 54번째 줄처럼 한번에 써야한다.
            #50번째 줄에서 b=P[2*i:2*i+2]라고 하면 54번째 줄에서 typerror:'str' object does not support item assignment라 뜨던데 왜?(b로 하든 list(b)로 한 다음 b[0]를 했을 때, 둘 다 string으로 뜨는데?)->애초에 b가 문자열로 인식되면 수정이 불가능한 자료구조이기 때문에!!! -> P자체를 리스트로 바꾸고 하기!!!(47번째 문장이 필요한 이유)
            #1번과 달리 유형2, 3번은 b[0], b[1]은 서로의 값을 변환하는데 있어 독립적(각자의 좌표만 씀)이기에 따로따로 계산 가능
    #2. 각 문자가 같은 행에 있는 경우(b[0], b[1]이 같은 행에 있는 경우)
        elif np.where(Keytable==b[0])[0]==np.where(Keytable==b[1])[0]:
            if np.where(Keytable==b[0])[1][0]==4:#b[0]가  가장 끝 열에 위치한 경우(b[1]은 자연스럽게 절대로 가장 끝 열에 위치하진 x, 이미 암호화 준비할 때, 각 쌍의 문자들이 서로 무조건 다르도록 했으므로 그리고 이 문장이 실행되는 것 자체가 둘은 같은 행에 있다는 것이기에)
                b[0]=Keytable[np.where(Keytable==b[0])[0][0],0]#b[0]의 같은행 1열에 위치시킨 것
                b[1]=Keytable[np.where(Keytable==b[1])[0][0],np.where(Keytable==b[1])[1][0]+1]#옆으로 한칸만 이동
            elif np.where(Keytable==b[1])[1][0]==4:
                b[1]=Keytable[np.where(Keytable==b[1])[0][0],0]
                b[0]=Keytable[np.where(Keytable==b[0])[0][0],np.where(Keytable==b[0])[1][0]+1]
            else:#둘 다 끝 열에 아닐 때 -> 각자의 위치에서 오른쪽으로 한 칸씩만
                b[0]=Keytable[np.where(Keytable==b[0])[0][0],np.where(Keytable==b[0])[1][0]+1]
                b[1]=Keytable[np.where(Keytable==b[1])[0][0],np.where(Keytable==b[1])[1][0]+1]
    #3. 위의 두 if문이 안 되면 남은 것은 각 문자가 같은 열에 있는 경우 뿐
        else:
            if np.where(Keytable==b[0])[0][0]==4:#b[0]의 행 위치가 4인 경우
                b[0]=Keytable[0,np.where(Keytable==b[0])[1][0]]
                b[1]=Keytable[np.where(Keytable==b[1])[0][0]+1,np.where(Keytable==b[1])[1][0]]
            elif np.where(Keytable==b[1])[0][0]==4:#b[1]의 행 위치가 4인 경우
                b[1]=Keytable[0,np.where(Keytable==b[1])[1][0]]
                b[0]=Keytable[np.where(Keytable==b[0])[0][0]+1,np.where(Keytable==b[1])[1][0]]
            else:#둘 다 행의 위치가 4보다 작은 경우
                b[0]=Keytable[np.where(Keytable==b[0])[0][0]+1,np.where(Keytable==b[0])[1][0]]
                b[1]=Keytable[np.where(Keytable==b[1])[0][0]+1,np.where(Keytable==b[1])[1][0]]
        P[2*i:2*i+2]=b
    C="".join(P)
    return C