# 반복문: 정해진 명령어를 반복적으로 수행하고 싶은 경우

# (1) for - range 반복문
for i in range(10) : #(0~10미만), 0부터 9까지 순차적으로 i에 대입이 된다.
    print(i, end=',')
# 0,1,2,3,4,5,6,7,8,9,

for i in range(1, 10) : #1부터 10미만, 1씩 증가(1~9)
    print(i, end=',')  #for문에 속해진 문장을 Tab으로 띄우기, 안띄우면 오류가 뜬다. 파이썬은 줄 각격으로 해당문장이 어디에 속해져있는지 판단하기 때문에 꼭 띄워주어야 한다.
# 1,2,3,4,5,6,7,8,9,

# range(시작값, 마지막값, 증감값)
for i in range(1, 10, 2) : #1부터 10미만, 2씩 증가(1~9)
    print(i, end=',')
# 1,3,5,7,9,

#연습문제
# (1) 1~100까지의 총합
# num = 1+2+3+4+5+.....+100 << 너무 비효율적!
total = 0
for i in range(1, 101) :
    total += i
print(total) #5050

# (2) 1~100까지의 짝수들의 합
#range 증감값 주기

total = 0
for i in range(2, 101, 2) :
    total += i
print(total) #2550

# (3) 00:00:00 ~ 23:59:59 초까지 출력
# 시계출력 (초만 출력)
for sec in range(60) :
    print(sec)


# 반복문 안에 반복문 넣을 수 있다.
# 분과 초 같이 출력
for min in range(60) :
    for sec in range(60) :
        print(f'{min:0>2}:{sec:0>2}') #뒤에 :0>2 붙여줘야 1 이렇게 안나오고 01 이렇게 나온다

# 시, 분, 초 같이 출력
for hour in range(24) :
    for min in range(60) :
        for sec in range(60) :
            print(f'{hour:0>2}:{min:0>2}:{sec:0>2}')

#과제 : 다음처럼 숫자가 출력될 수 있도록 반복문을 활용하기
# 01 02 03 04 05
# 06 07 08 09 10
# 11 12 13 14 15
# 16 17 18 19 20