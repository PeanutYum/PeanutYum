# 주석: 코드에 영향을 주지 않고 설명문을 쓰는 것
# 단축키: Ctrl + /
# --------------------
# 1.기본 자료형
# 1) 정수형
num1 = 1
num2 = 2
print(num1)
# 2) 실수형
floatNum1 = 3.14
floatNum2 = 1.25
print(floatNum1, floatNum2)

# 3) 문자형
str1 = "Hello"
str2 = 'World'
# str3 = "Error'
print(str1, str2)

# 4) 논리형
bool1 = True
bool2 = False
print(bool1, bool2)
#--------------------------------

# 2. 숫자 자료형의 기본연산
num1 = 10
num2 = 20
# 1) 덧셈
result = num1 + num2
print(result) #30
# 2) 뺄셈
result = num1 - num2
print(result) # -10
# 3) 곱셈
result = num1 * num2
print(result) #200
# 4) 나눗셈
result = num1 / num2
print(result) #0.5 (정수형끼리의 나눗셈 실수형으로 반환)
# 5) 몫 연산자
result = num1 // num2
print(result) #0
# 6) 나머지 연산자
result = num1 % num2
print(result) #10
# 7) 증감연산자 : 기존 변수의 값에 변화를 줄 때 사용
num1, num2 = 10, 20
num1 += 1 #num1 = num1 +1
num2 -= 5 #num2 = num2 -5
print(num1, num2) #11 15

# 8) 제곱연산자
result = 3**2
print(result) #9
result = 2**3
print(result) #8
#----------------------------------------
# 3. 자료형 변환
# 1) 정수와 실수간의 형변환
num1, num2 = 10, 3
print(num1/num2) #3.3333 #실수로 자동형변환
#int() : 어떤 값을 정수형으로 바꾸고 싶을 때 사용
print(int(num1/num2)) #3
floatNum = 3.141592
print(int(floatNum)) #3

#float() : 어떤 값을 실수형으로 바꾸고 싶을 때 사용
num = 5
print(float(num)) #5.0

# 2) 숫자형과 문자형 간의 변환
# 2-1) 문자형 -> 숫자형
str1 = '3.14'
str2 = '5'
#실수형으로 변환
print(float(str1)) #3.14
print(float(str2)) #5.0
#정수형으로 변환
print(int(str1)) #오류
print(int(float(str1))) #3  #3.14라는 실수로 바꾸고 정수로 바꿔야함
print(int(str2)) #5
#2-2) 숫자형 -> 문자형
#str() 함수 사용
floatNum = 3.14
intNum = 5
print(str(floatNum), str(intNum)) #3.14 5
#---------------------
# 4. 자료형 확인
num1 = 19
floatNum = 3.141952
numStr = '58.11'
print(type(num1)) #<class 'int'>
print(type(floatNum)) #<class 'float'>
print(type(numStr)) #<class 'str'> #Str은 String의 약자이다.

