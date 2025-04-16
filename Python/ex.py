"""
1. 자료형(int,float,string,boolean)
2. 변수(개념, 선언, 초기화, 사용)
3. 연산자
4. 조건문
5. 반복문
6. 조건문과 반복문 혼합 및 중복
7. 리스트, 튜플, 셋, 딕셔너리
8. 함수

"""
# 1. 자료형(int,float,string,boolean)
"""

수(int,float)
문자열(string)
불린(boolean)

리스트(list)
튜플(tuple)
딕셔너리(dictionary)

"""
# 2. 변수(개념, 선언, 초기화, 사용)
"""

변수의 개념

int a; 선언
a = 0; 초기화
print("%d",a); 사용

string s;
s = "This is string";
print("%s",s);

a = 0
print(a)

s = "This is string"
print(s)

"""
# 3. 연산자
"""

3-1. 산술연산자(=,+,-,*,**,/,//,%)

a = 1 + 2
a = 1 - 2
a = 1 * 2
a = 1 ** 2
a = 1 / 2
a = 1 // 2
a = 1 % 2

3-2. 비교연산자(==,!=,>,<,>=,<=)

결과를 True or Flase 로 반환
a == b
같음

!=
a != b
같지 않음

>
a > b
큼 (초과)

<
a < b
작음 (미만)

>=
a >= b
크거나 같음 (이상)

<=
a <= b
작거나 같음 (이하)

"""
# 4. 조건문
"""

수직선으로 조건문 개념
if(x >= 3):
    ...
if(-1 < x <= 1):
    ...
if(x < -3):
    ...
else:

조건문의 흐름 알기
if...if...if와 if...elif...else의 차이 알기
생명주기 알기

"""
# 5. 반복문
"""

5-1 for 반복문
for i in range[10]:
    print(i)

횟수, 범위같은 개념으로 반복할 때 주로 for 반복문 사용

5-2 while 반복문
while(True):
    ...

while(a < 10):
    ...
    a += 1

+=,-=,*=,**=,/=,//=,%=

무한루프, 조건으로 반복할 때 주로 while 반복문 사용
조건 설정을 잘 확인할 것
어떤 반복문이든 흐름 잘 찾기

"""
# 6. 조건문과 반복문 혼합 및 중복
"""

가장 가까운 반복문을 빠져나오는 break
현재 실행중인 반복을 멈추고 다음 반복을 계속하는 countinue
다음 코드에 break, countinue를 넣어서 과정과 결과 예상

a = 0
while(True):
    if(a == 0):
        print(a)
    if(a == 1):
        print(a)
    if(a == 2):
        print(a)
    if(a == 3):
        print(a)
    if(a == 4):
        print(a)
    if(a == 5):
        print(a)
    if(a == 6):
        print(a)
    if(a == 7):
        print(a)
    if(a == 8):
        print(a)
    if(a == 9):
        print(a)
    if(a == 10):
        print(a)
    a += 1

x = input('x = ')
if(x >= 3):
    for i in range[10]:
        print(x, i)
if(-1 < x <= 1):
    ...
if(x < -3):
    for i in range[10]:
        print(x, i)
else:

a = 0
while(True):
    while(a < 10):
        print(a)
        a += 1


if(x >= 3):
    if(x > 5):
        ...
if(-1 < x <= 1):
    ...
if(x < -3):
    if(x < -10):
        ...
else:

"""
# 7. 리스트, 튜플, 셋, 딕셔너리
"""
리스트의 개념-그림으로

가장 일반적인 list
list = [1, 2, 3, 4]

변경이 불가능한 tuple
tuple = (1, 2, 3, 4)

중복제거와 정렬을 시켜주는 set
set = {1, 2, 3, 4}

{key:value} 구조를 가진 dictionnary
dictionary = {
                'a' : 1,
                'b' : 2,
                'c' : 3,
                'd' : 4
            }

"""
# 8. 함수
"""

함수의 개념
선언 정의 호출
흐름 알기
"""


