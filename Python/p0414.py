import module_test2
from module_test import *
import sys # 표준모듈
print('========== 2025.04.14 ==========')

"""

module_test2.m3()
func3()

print(sys.builtin_module_names)

# =========== math ============
import math

print(math.log(10))

list_1 = [10,20,30,40]
print(math.fsum(list_1))

a = 5
print(math.pow(a,3))

print(math.pi)

# =========== time ===========
import time

print(time.time()) # UTC 표준시를 기준으로 한 현재 시간(타임스탬프 시간)
utc = time.time()

gm = time.gmtime(utc) # GMT 기준시간
print(gm)

tm = time.localtime(utc) # 각 지역(한국)의 시간
print(tm)
print(tm.tm_year,'년')
print(tm.tm_mon,'월')
print(tm.tm_mday,'일')
print(tm.tm_hour,'시')
print(tm.tm_min,'분')
print(tm.tm_sec,'초')

string = time.ctime(time.time()) # 미국식 시간 표기법
# print(string)

tm = time.localtime(time.time())
string = time.strftime("%Y-%m-%d %p %I:%M:%S", tm) # strftime()을 통해 str생성
print(string)

# ============= datetime ==================
import datetime
today = datetime.date.today()
print('today :',today)

# from datetime import datetime

now = datetime.datetime.now()
print('now :',now)

from datetime import datetime as dt # as 사용
now = dt.now()
print('now :',now)


# 문제1)  math 모듈 사용하기
# 반지름이 5인 원의 넓이를 구하세요.
# 힌트: math 모듈의 pi와 pow 함수를 사용하세요.

import math

radio = 5
print(math.pi * pow(radio,2))


# 문제2) random 모듈로 숫자 뽑기
# 1부터 100 사이의 숫자 중 랜덤으로 1개를 출력하는 코드를 작성하세요.
# 힌트: random.randint() 함수를 사용해 보세요.

import random

print(random.randint(1,100))


# 문제3) datetime 모듈로 현재 날짜 구하기
# 오늘 날짜를 YYYY-MM-DD 형식으로 출력하세요.
# 힌트: datetime 모듈과 strftime()을 활용해 보세요.

# time 사용하기
import time
tm = time.localtime(time.time())
print(time.strftime("%Y-%m-%d", tm)) # strftime()을 통해 str생성

# datetime 사용하기
import datetime
today = datetime.datetime.today()
stm = today.strftime("%Y-%m-%d")
print(stm)


# 내부함수
def outFunc(v1,v2):
    def inFunc(num1,num2):
        return num1+num2
    return inFunc(v1,v2)
print(outFunc(10,20))

# 재귀함수 - 반복문을 대신할 때
def count(num):
    if(num >= 1):
        print(num,end=" ")
        count(num-1)
    else:
        return

count(10)
count(20)

"""

# 제너레이터 함수
def genFunc(num):
    for i in range(num):
        yield i
        ('제너레이터 진행중..')


for data in genFunc(5):
    print(data)