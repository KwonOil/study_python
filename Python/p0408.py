"""
# 1~30 출력하기
for i in range(30):
    print(i+1, end=" ")

# 문방구 상품리스트 '펜', '지우개', '샤프', '자'
# 사고싶은 상품은? 마우스
# 마우스는 없어요

list = ['펜', '지우개', '샤프', '자']

while(1):
    s = input("사고싶은 상품은? ")

    if(s in list):
        print(s + " 여기있습니다")
    elif(s == 'no'):
        break
    else:
        print(s + "는 없어요")

# 학생이름(종료 exit)? 홍길동
# 홍길동은 학생명단에 없습니다
# 학생이름(종료 exit)? 함선아
# 함선아씨는 우리반 학생입니다
# 오늘도 수고 많이 하셨습니다. 우리반은 4명입니다

student_list = ['구윤서', '함선아', '박민수', '선상님']

while(True):
    s = input("학생이름은(종료 exit)? ")

    if(s in student_list):
        print(s + "씨는 우리반 학생입니다")
    elif(s == 'exit'):
        print("오늘도 수고 많이 하셨습니다. 우리반은 " + str(len(student_list)) + "명입니다")
        break
    else:
        print(s + "은 학생명단에 없습니다")

a = ['사과', '배', '복숭아']
a.remove('복숭아') # 값으로 삭제하기
del a[0] # 인덱스로 삭제하기
print(a)

# 반찬가게 관리자 프로그램

food_list = ['김치', '멸치볶음']
while(True):
    for i in range(len(food_list)):
        print(type(food_list[i]),end = " ")
    print()
    print('1.추가 2.삭제 3.전체목록 9.종료')
    menu = int(input('메뉴를 선택하세요(1/2/3/9): '))
    if(menu == 1):
        add_menu = input('추가하고 싶은 메뉴는? ')
        if(add_menu not in food_list):
             food_list.append(add_menu)
        else:
             print(add_menu + '은(는) 이미 있습니다')
        print()
    elif(menu == 2):
        print('===== [',end = " ")
        for i in range(len(food_list)):
                print(food_list[i], end = " ")
        print('] =====')
        remove_menu = input('삭제하고 싶은 메뉴는? ')
        if(remove_menu in food_list):
            food_list.remove(remove_menu)
        else:
             print(remove_menu + '은(는) 목록에 없습니다')
        print()
    elif(menu == 3):
        print('===== [',end = " ")
        # for i in range(len(food_list)):
        #         print(food_list[i], end = " ")
        for food in food_list:
             print(food, end=" ")
        print('] =====')
    elif(menu == 9):
        print('프로그램을 종료합니다')
        break
    else:
        print('잘못 입력하셨습니다 다시 입력해주세요')
        print()

# 튜플 생성 1. ()
months = ('Jan','Feb','Dec')
days = ('Mon','Tue','Sun')
print('days :', type(days))
# 2. tuple(변수 또는 상수)
string_march = 'March'
tuple_march = tuple(string_march)
print('tuple_march :', type(tuple_march))
# print('months[1] :',months[1])
# print('days[2] :',days[2])
# print('Jan' in months)

# 튜플은 수정,삭제,추가 안됨
# 튜플을 리스트로 변환해 수정
days_list = list(days)
print('days_list :',type(days_list))
days_list.insert(2,'Wed')
days_list.remove('Mon')
days_list[0] = 'Thu'
days = tuple(days_list)

print(days)

# 1~50 리스트
n_list = list(range(1,51,1))
print(n_list)

# 10~100 튜플(5단위)
n_tuple = tuple(range(10,101,5))
print(n_tuple)

t = ()
t_1 = (1,)
print('t_1 : ',type(t_1))

numbers = tuple(range(10))
print(numbers)

tuple_t = tuple( range(10,71,10))
print(tuple_t[0] + tuple_t[2] + tuple_t[4])

a = tuple(range(1,11))
b = tuple(range(1,11))
c = tuple(range(1,11))

d = a + b + c
print(d)
a = a*3
print(a)
print(a[0:3])
print(a[:5])
print(a[10:])


a = ('영어', '수학', '과학', '사회')
b = list(a)
b[1] = '과제'
print('대체과목(list) : ',b)
print('원래과목(tuple) : ',a)

str_red = 'RED'
list_color = ['Red','Yellow','Orange']

tuple_red = tuple(str_red)
tuple_Yellow = tuple(list_color[1])
tuple_color = tuple(list_color)
print(tuple_red, tuple_color, tuple_Yellow)


set1 = {2,3,1,1,1}
print(len(set1))
print(set1)


color_list = ['red','blue','red','green','pink','blue','black']
print(color_list)
color_list = set(color_list)
print(color_list)

color_tuple = ('red','blue','red','green','pink','blue','black')
print(color_tuple)
color_tuple = set(color_tuple)
color_tuple = tuple(color_tuple)
print(color_tuple)


s1 = {0,1,2,3,4}
s2 = {3,4,5,6,7}

print(s1 & s2) # 교집합
print(s1 | s2) # 합집합
print(s1 - s2) # 차집합


s1 = {'red','yellow','green','blue'}
print('red' in s1)
print('white' in s1)


fruit = {'딸기', '바나나', '오렌지', '사과'}
print(fruit)
existence = '바나나' in fruit
fruit.remove('바나나')
fruit.add('멜론')
number_fruit = len(fruit)
print(existence, number_fruit, fruit)


staff = {'홍길동','이수지','박상민','강민우','하누리'}
staff_late = {'홍길동','이수지','박상민'}
staff_no = {'박상민','하누리'}

staff_bonus = staff - (staff_late | staff_no)
staff_overtime = staff_late & staff_no

print(staff)
print('보너스 받을 사원은 ', staff_bonus,'이고, 야근할 사원은 ', staff_overtime,'입니다')


price = {'오뎅':'2000원', '떡볶이':'3000원'}
print(price['오뎅'],price['떡볶이'])
price['오뎅'] = '1000원'
print(price)

L = [20, 40, 60, 80, 100]
T = (2, 4, 6, 8, 10)
lt = {}
for i in range(len(T)):
    lt[T[i]] = L[i]
print(lt)
print(lt[T[2]])


eng = ['apple','banana','orange']
kor = ('사과','바나나','오렌지')
dic3 = {}
for i in range(len(eng)):
    dic3[kor[i]] = eng[i]
print(dic3)


a = 2
number = {1:'one',  a:'two',  3:'three',  4:'four',  5:'five' }
print(number)
print(number.keys())


food = {'분식':['떡볶이','호떡'], '중식':['짜장면','탕수육']}
print(food)
del food['중식']
print(food)


d1 = {'k1' : 100, 'k2': 200}
d1['k3'] = 'kbs'
del d1['k2']
print(d1)


value_list = [1,2,3,4]
key_tuple = ('a','b','c','d')
dictionary = {}
for i in range(len(key_tuple)):
    dictionary[key_tuple[i]] = value_list[i]
print(dictionary)

# 문제1
menu_cafe = {'Americano':'2000원', 'Cafe latte':'2500원', 'Green Tea latte':'3000원', 'Mocha latte':'3500원'}
print('Americano' in menu_cafe.keys())
print('Vanila latte' in menu_cafe.keys())

# 문제2
menu_mun = {'연필':'200원','펜':'800원','지우개':'500원','자':'300원'}
print(list(menu_mun.values()))

# 문제3
animal_list = ['dog', 'pig', 'tiger', 'eagle','cat', 'dog', 'pig', 'lion']
animal_set = set(animal_list)
new_animal_list = list(animal_set)

"""

# 문제4
inven = {'배':[2000,3], '사과':[1500,4], '딸기':[1800,1], '참외':[2300,5]}
inven['수박'] = [2200,2]
inven['당근'] = [3300,1]
cost_total = 0
num = 5

for i in list(inven.keys()):
    if(inven[i][1] < num):
        num_buy = (num-inven[i][1])
        cost = inven[i][0] * num_buy
        cost_total += cost
        print(i, str(num_buy) + '개의 구매가격은',str(cost) +'원 입니다')
    else:
        print(i + '는 구매할 필요가 없습니다')
print('총 구매가격은',str(cost_total) +'원 입니다')

