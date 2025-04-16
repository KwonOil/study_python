print('========== 2025.04.09 ==========')
"""
# 복습
# list
menu_list = ['아메리카노','카푸치노']
m = list('김')
print(menu_list, m)
# tuple
menu_tuple = ('아메리카노','카푸치노')
a_tuple = (1,)
ma = tuple(range(10))
print(ma)
# set - 집합 합집합 | 교집합 & 차집합 -
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
# dictionary - 사전,map
d1 = {'김':30, '이':20}
print(d1['김'])
d1 = {'a':[100, 150], 'b':(10,20), 'a':'홍길동'}
print(d1['a'])
# d1에 'c':{1,2,3,1,2}
d1['c'] = {1,2,3,1,2}
print(d1)
# d1에서 'a':홍길동 삭제
del d1['a']
print(d1)
# update
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

# 방법1
a = [10,20,30,40,50]
b = ('a','b','c','d','e')
# d = dict()
# for i in range(len(a)):
#     d[b[i]] = a[i]
# print(d)

# 방법2
keys = ('apple','pear','peach')
vals = (300,250,400)
r = dict(zip(keys,vals))
print(r)

d = dict(zip(b,a))
print(d)

# 실습 2
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date,close_price))
print(close_table)
# 알고싶은 날짜는? 09/06
# 종가는 10300원입니다
while(True):
    date_in = input('알고싶은 날짜는? ')
    if(date_in == '99/99'):
       print('종료합니다')
       break 
    elif(date_in in close_table.keys()):
        print('종가는', str(close_table[date_in]) + '원 입니다')
    else:
        print('데이터가 없습니다')

# ========== 혼자 공부하는 파이썬 04-2 ========== 
# 예제
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고","설탕","메타중아황산나트륨","치자황색소"],
    "orgin" : "필리핀"
}

for key in dictionary:
    print(key)

# 확인문제
# 2번
pets = [
    {"name": "구름", "age": 5},
    {"name": "초코", "age": 3},
    {"name": "아지", "age": 1},
    {"name": "호랑이", "age": 1}
]
# print("우리동네 애완 동물들")
# for pet in pets:
#     print(pet["name"], str(pet["age"]) + '살')
for pet in pets:
    print(pet)


# 3번
numbers = [1,2,3,4,5,6,7,8,9,1,4,1,5,2,4,7,5,4,7,8,9,6,3,2,1,4,5,6,8,7,4]
counter = {}
for number in numbers:
    counter[number] = numbers.count(number)
print(counter)


# 4번
character = {
    "name":"기사",
    "level":12,
    "items":{
        "sword":"불꽃의 검",
        "armor":"풀플레이트"
    },
    "skill":["베기","세게 베기","아주 세게 베기"]
}

for key in character:
    if(type(character[key]) is dict):
        for value in character[key]:
            print(value,":",character[key][value])
    elif(type(character[key]) is list):
        for value in character[key]:
            print(key,":",value)
    else:
        print(key,":",character[key])

# 문제5
inventory = {
    '메로나':[300,20],
    '비비빅':[400,3],
    '죠스바':[250,100]
    }
print(inventory)


# 문제6
trans = {
    '달러' : 1167,
    '엔' : 1096,
    '유로' : 1268,
    '위안' : 171
}

while(True):
    while(True):
        money,currency = input('입력 : ').split()
        if(money.isdigit()):
            money = float(money)
            break
        else:
            print('숫자를 입력하세요')
    
    if(currency == 'exit'):
        print('종료합니다')
        break
    elif(currency in trans.keys()):
        for key in trans.keys():
            if(key == currency):
                print((money * trans[key]),'원')
    else:
        print('달러, 엔, 유로, 위안 중에 고르세요')

# 문제7
ohlc = [
    ["open", "high", "low", "close"],
    [100, 110, 70, 100],
    [200, 210, 180, 190],
    [300, 310, 300, 310]
]
for i in ohlc[1:]:
    print(i[3],end = " ")


l1 = list(range(1,20,3))
l2 = list(range(30,1,-7))
l3 = list(range(0,91,8))
l4 = list(range(0,11,1))
print(l1)
print(l2)
print(l3)
print(l4)


# 문제1) 1번째 알파벳부터 5번째 알파벳까지 알파벳 순으로 구성된 문자열
# 'abcde'를 사용하여 다음과 같이 출력 결과를 나타내는 프로그램을 작성해 보자
# [출력 결과]
# 1번째 알파벳은 a
# 2번째 알파벳은 b
# 3번째 알파벳은 c
# 4번째 알파벳은 d
# 5번째 알파벳은 e

al = 'abcde'
for i in range(len(al)):
    print(str(i+1) + '번째 알파벳',al[i])
    print(f'{i+1}번째 알파벳은 {al[i]}')
    print('{}번째 알파벳은 > {}'.format(i+1,al[i]))

# 문제2) 사용자가 입력한 정수의 팩토리얼 값을 출력하는 프로그램을 만들고자 한다.
# 입력값을 n으로 가정했을 때 n! = 1 x 2 x 3 x ... n-1 x n의 연산을 하여라

num = int(input('입력값은? '))
result = 1
str_num = '1'
for i in range(1,num+1):
    if(i > 1):
        str_num += 'x'+ str(i)
    result *= i
print(f'{str(num)}! = {str_num} = {result}')

# 문제1) mix_list = ['apple', 5, 'banana', 'grape', 3, 8, 6,'melon']
# mix_list의 각 element의 형이 string형인지, int형인지 판별해 출력하기

mix_list = ['apple', 5, 'banana', 'grape', 3, 8, 6,'melon']
for i in mix_list:
    print(f"'{i}'의 타입은 {type(i)}입니다")


# 문제2)  1이상의 정수를 입력하면 그 수의 약수를 출력해주는 프로그램이다.  for문을 이용해 작성해보자.

num = int(input('1 이상의 정수 입력 : '))
print(f'{num}의 약수')
for i in range(1,num+1):
    if(num % i == 0):
        print(i,end = " ")
        
"""

# 문제3) 리스트를 원소로 갖는 리스트의 각 원소들의 합을 구하는 프로그램을 while문을 이용하여 작성해보자.

a = [(1, 3), (5, 7), (9, 11), (13, 15)]

# r = 0
# for i in a:
#     for j in i:
#         r += j
#     print(r)
#     r = 0

for(n1, n2) in a: # unpack
    print(n1+n2)

# 문제1-2) mix_list = ['apple', 5, 'banana', 'grape', 3, 8, 6,'melon']
# mix_list의 각 element의 형이 string형인지, int형인지 구분해 각 리스트에 넣기

mix_list = ['apple', 5, 'banana', 'grape', 3, 8, 6,'melon']
str_list =[]
int_list = []
for i in mix_list:
    print(f"'{i}'의 타입은 {type(i)}입니다")
    if( type(i) is str):
        str_list.append(i)
    elif( type(i) is int):
        int_list.append(i)
print(str_list, int_list)

