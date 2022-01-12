# 1. 리스트 : 연관된 데이터의 나열
# 리스트 기호: []

# 리스트의 필요성
# 학생 10명의 점수의 평균값
# num1, num2, num3, num4, ...., num10 = 70, 80
# total = num1+num2+num3,...+num10 >> 근데 이걸 일일이 하기가 힘드니까!
scores = [50, 30, 20, 50, 60, 70, 80, 77, 99,100]
# 리스트의 합계
print(sum(scores)) #636
# 리스트의 평균
print(len(scores)) #10, 리스트의 데이터 개수
print(sum(scores)/len(scores)) #63.6
# ---------------------------
# 인덱스를 통한 요소 접근
colors = ['빨강', '파랑', '노랑']
print(colors) #위에 있는 코드 복사하기 > Alt Shift 방향키아래
print(colors[0]) #빨강 #리스트 내의 요소는 0부터 센다
print(colors[1]) #파랑
print(colors[2]) #노랑

# 값을 마지막부터 접근
print(colors[-1]) #마지막 요소
print(colors[-2]) #마지막 전 요소
print(colors[-3]) #마지막 전전 요소

print(colors[3]) #IndexError: list index out of range #인덱스 값을 벗어나서 오류가 났다
# 주의할점: 인덱스를 통해 값 접근시 인덱스 범위내의 값을 넣어야 한다.

# (2) 리스트의 크기
print(len(colors)) #3

# (3) 리스트의 덧셈 : 리스트들끼리 이어서 리턴
colors2 = ['오렌지', '하늘']
colors3 = colors + colors2
print(colors3) #['빨강', '파랑', '노랑', '오렌지', '하늘']

# (4) 리스트의 곱셉: 곱한 수 만큼 리스트를 반복해서 리턴
nums = [1, 2, 3]
nums2 = nums*2
print(nums2) #[1, 2, 3, 1, 2, 3]

#리스트의 요소수가 100이고 모든 값이 0인 리스트
zero100 = [0]*100
print(zero100)

# (5) 리스트 내의 요소 검색 : 값이 있는지 여부 True/False
nums = [1, 2, 3]
print(1 in nums) #True
print(99 in nums) #False
print('빨강' in colors) #True
print('검정' in colors) #False

# (6) 인덱스 슬라이싱 (다른언어에는 없는 파이썬의 특징)
numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numlist[0:5]) #인덱스 0 이상 ~ 5 미만(0, 1, 2, 3, 4)
# [1, 2, 3, 4, 5]
print(numlist[2:8]) #인덱스 2 이상 ~ 8 미만 (2, 3, 4, 5, 6, 7)
# [3, 4, 5, 6, 7, 8]
print(numlist[:5]) #인덱스 처음부터 5 미만 (0, 1, 2, 3, 4)
# [1, 2, 3, 4, 5]
print(numlist[5:]) #인덱스 5부터 끝까지 (5, 6, 7, 8, 9)
# [6, 7, 8, 9, 10]
print(numlist[:]) #처음부터 끝까지
print(numlist)


# 인덱스 슬라이싱 증감값 주기
print(numlist[0:10:2]) #인덱스 0 이상, 10 미만에서 인덱스를 2 씩 증가해서 가져옴
# [1, 3, 5, 7, 9]
print(numlist[::2]) #인덱스 처음부터 끝까지 2씩 증가해서 가져오기

print(numlist[1:7:3]) #인덱스 1부터 7미만 3씩 증가해서 가져오기
#(1, 4) => [2, 5]

print(numlist[::-1]) #리스트 역순 출력
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(numlist[9::-1])
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(numlist[-1:-10:-1]) #-1부터 -10초과 (-1~-9) 까지 -1씩 감소해서 가져옴
# [10, 9, 8, 7, 6, 5, 4, 3, 2]

# (6) 리스트 요소의 값 수정
numlist[0] = 100
print(numlist) #[100, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# (7) 리스트 요소의 언패킹(Unpacking)
# 리스트 내의 요소를 변수에 각각 값 할당
c1, c2, c3 = colors
print(c1, c2, c3) #빨강 파랑 노랑

# 주의할점: 언패킹되는 변수의 개수와, 리스트의 요소수가 일치
c1, c2, c3, c4 = colors #오류 ValueError: not enough values to unpack

# (8) 리스트 내의 다양한 데이터 자료형 허용
templist = ['빨강', 1, 3.14, [1, 2, 3]]
print(templist) #['빨강', 1, 3.14, [1, 2, 3]
print(len(templist)) #4
print(templist[-1]) #[1, 2, 3]
print(templist[-1][0]) #1 #1,2,3 에서 0번째 숫자 출력
print(templist[-1][1]) #2 

# -----------------------------------------------------
# 리스트의 메서드(리스트를 조작하는 함수들)
#(1) append() : 새로운 값 리스트 맨 끝에 추가
colors = []
colors.append('노랑')
colors.append('빨강')
colors #Shif+Enter로 실행시 print() 안하더라도 출력됨
# ['노랑', '빨강']

# (2) insert() : 리스트 특정 인덱스 위치에 값 삽입
colors.insert(0, '검정')
colors #['검정', '노랑', '빨강']

# (3) remove() : 리스트 내의 특정값 삭제
colors.remove('검정')
colors #['노랑', '빨강']

# (4) del 키워드 : 인덱스를 통한 리스트 요소 삭제
del colors[0] #인덱스 0인 요소 삭제
colors #['빨강']

# (5) pop() :리스트의 마지막 요소를 돌려주고 해당 요소 삭제
c1 = colors.pop()
c1 #'빨강'
colors #[]

colors = ['빨강', '파랑', '노랑']
c2 = colors.pop(1) #인덱스 1을 리턴해주고 해당 요소 제거
c2 #파랑
colors #'빨강', '노랑']

# (6) sort() : 리스트의 정렬
nums = [9, 4, 1, 5, 7]
nums.sort() #nums 리스트 오름차순 정렬
nums #[1, 4, 5, 7, 9]
nums.sort(reverse=True) #내림차순 정렬
nums #9, 7, 5, 4, 1]

# (7) sorted() 함수 : 기존 리스트를 변경하지 않고 정렬된 리스트 반환
nums = [9, 4, 1, 5, 7]
sortNums = sorted(nums)
nums, sortNums #([9, 4, 1, 5, 7], [1, 4, 5, 7, 9])
sortNums = sorted(nums, reverse=True)
nums, sortNums #([9, 4, 1, 5, 7], [9, 7, 5, 4, 1])

# (8) count() : 리스트 내의 특정 요소의 개수를 반환
nums = [1, 1, 2, 2, 2, 3] #nums에 2가 몇개 있는지 확인하기
nums.count(2) #3
nums.count(1) #2

