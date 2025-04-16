print('========== 2025.04.10 ==========')

"""
# 문제4) 다음의 요구사항에 따라 프로그램을 작성하시오.
I 요구사항 I
시험을 치른 후, 맞은 개수를 알려주는 프로그램이다. 사용자의 이름과 문제의 개수를
입력하고, 문제를 맞혔는지 아닌지를 입력하면 맞은 개수를 출력해준다.
for문을 이용해서 프로그램을 작성해보자.
I 테스트 I
>>>
이름: 수진
문제 개수: 6
**********************************
1 번 문제를 해결했나요?(y/n):
y
2 번 문제를 해결했나요?(y/n):
y
3 번 문제를 해결했나요?(y/n):
n
4 번 문제를 해결했나요?(y/n):
y
5 번 문제를 해결했나요?(y/n):
y
6 번 문제를 해결했나요?(y/n):
n
**********************************
수진 학생, 총 4 문제를 해결했습니다.

name = input('이름 : ')
test_num = int(input('문제 개수 : '))
count = 1
result = 0
print('**********************************')
while(count <= test_num):
    print(count,'번 문제를 해결했나요?(y/n) : ')
    y_or_n = input()
    if(y_or_n == 'y'):
        result += 1
        count += 1
    elif(y_or_n == 'n'):
        count += 1
    else:
        print('잘못 입력했습니다 다시 입력하세요')
print('**********************************')
print(f'{name} 학생, 총 {result} 문제를 해결했습니다')

# 문제5) 하나의 열을 하나의 리스트로, 총 2개의 리스트를 갖는 이차원 리스트 stock을 정의 하세요.
# 문제6) stock 이름의 딕셔너리로 표현하라.시가를 key로 저장하고, 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다.
# 종가 역시 key로 저장하고 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다.
stock = {"시가" : [100, 200, 300], "종가" : [80, 210, 330]}

# 문제7) apart = [ [101, 102], [201, 202], [301, 302] ] 의 이중 리스트를
# 101 호102 호201 호202 호301 호302 호
# 이렇게 출력하는 프로그램을 작성하세요. 힌트 이중 for문


apart = [ [101, 102], [201, 202], [301, 302] ] # 아파트 리스트

for i in apart:
    for j in i:
        print(str(j)+'호',end = " ")
print()

# 문제8) 문제7의 자료를 가지고
# 301 호302 호201 호202 호101 호102 호
# 출력하세요.

# apart 리스트를 거꾸로
# reverse()는 반환값 없이 뒤집는 함수
# apart.reverse()

for i in reversed(apart): # for i in apart:
    for j in i:
        print(str(j)+'호',end = " ")
print()

# 문제9) 문제7의 자료를 가지고
# 302 호301 호202 호201 호102 호101 호
# 나오게 출력하세요

for i in apart: # for i in apart:
    for j in reversed(i): # apart 리스트의 각 인자(i)들을 거꾸로
        print(str(j)+'호',end = " ")
print()


# ================ 함수 ================

# 실습1)

def calc(v1,v2,op):
    result = 0
    if(op == '+'):
        result = v1 + v2
    elif(op == '-'):
        result = v1 - v2
    elif(op == '*'):
        result = v1 * v2
    elif(op == '/'):
        result = v1 / v2
    return result

res = 0
var1, var2, poer = 0, 0, ""

oper = input("계산을 입력하세요(+,-,*,/) : ")
var1 = int(input("첫 번째 수를 입력하세요 : "))
var2 = int(input("두 번째 수를 입력하세요 : "))

res = calc(var1,var2,oper)

print("## 계산기 : %d %s %d = %d ##" %(var1, oper, var2, res))

# 문제1) 실습1 코드를 아래와 같이 수정하여 추가해 보세요.
# - 숫자, 연산자, 숫자2 순서로 입력받는다.
# - 제곱연산자를 추가한다.
# - 0으로 나누려면 메시지를 출력하고 계산하지 않는다.

# < 출력결과 >
# 첫번째 수를 입력하세요  2
# 계산 연산자를 입력하세요 (+,-,*,/,**) : **
# 두번째 수를 입력하세요 : 4
# 계산 결과는 2 ** 4 = 16

def calc(v1,v2,op):
    result = 0
    if(op == '+'):
        result = v1 + v2
    elif(op == '-'):
        result = v1 - v2
    elif(op == '*'):
        result = v1 * v2
    elif(op == '/'):
        if(v2 == 0):
            print("0으로 나눌 수는 없습니다")
            return result
        result = v1 / v2
    elif(op == '**'):
        result = pow(v1,v2)
    return result

res = 0
var1, var2, poer = 0, 0, ""

var1 = int(input("첫 번째 수를 입력하세요 : "))
oper = input("계산을 입력하세요(+,-,*,/) : ")
var2 = int(input("두 번째 수를 입력하세요 : "))

res = calc(var1,var2,oper)

print("## 계산기 : %d %s %d = %d ##" %(var1, oper, var2, res))



# 실습2)

## 전역 변수 선언 부분 ##
coffee = 0

## 함수 선언 부분 ##
def coffee_machine(button) :
     print()
     print("#1. (자동으로) 뜨거운 물을 준비한다.")
     print("#2. (자동으로) 종이컵을 준비한다.")

     if button == 1 :
          print("#3. (자동으로) 보통커피를 탄다.")
     elif button == 2 :
          print("#3. (자동으로) 설탕커피를 탄다.")
     elif button == 3 :
          print("#3. (자동으로) 블랙커피를 탄다.")
     else :
          print("#3. (자동으로) 아무거나 탄다.\n")

     print("#4. (자동으로) 물을 붓는다.")
     print("#5. (자동으로) 스푼으로 젓는다.")
     print()

## 메인 코드 부분 ##
coffee = int(input("어떤 커피 드릴까요?(1:보통, 2:설탕, 3:블랙)"))
coffee_machine(coffee)
print("손님~ 커피 여기 있습니다.")


def para_func(para) :
     print(para)
     result = max(para)

     return result

## 전역 변수 선언 부분 ##
hap = 0
a_data = (10,-20,50,80,200,-30)
## 메인 코드 부분 ##
hap = para_func( a_data )
print("가장 큰 숫자를 찾는 함수를 호출한 결과 ==> %d" % hap)


# 문제2) 위의 실습2) 문제에 추가해서 코드를 작성해 보세요
# 커피의 종류를 아메리카노, 카페라떼, 카프치노, 에스프레소 중 하나를 선택할 수 있도록 하자
## 전역 변수 선언 부분 ##
coffee = 0

## 함수 선언 부분 ##
def coffee_machine(button) :
     print()
     print("#1. (자동으로) 뜨거운 물을 준비한다.")
     print("#2. (자동으로) 종이컵을 준비한다.")

     if button == 1 :
          print("#3. (자동으로) 아메리카노를 탄다.")
     elif button == 2 :
          print("#3. (자동으로) 카페라떼를 탄다.")
     elif button == 3 :
          print("#3. (자동으로) 카푸치노를 탄다.")
     elif button == 4 :
          print("#3. (자동으로) 에스프레소를 탄다.")
     else :
          print("#3. (자동으로) 아무거나 탄다.\n")

     print("#4. (자동으로) 물을 붓는다.")
     print("#5. (자동으로) 스푼으로 젓는다.")
     print()

## 메인 코드 부분 ##
coffee = int(input("어떤 커피 드릴까요?(1:아메리카노, 2:카페라떼, 3:카푸치노, 4:에스프레소)"))
coffee_machine(coffee)
print("손님~ 커피 여기 있습니다.")


## 함수 선언 부분 ##
def func1() :
     global a     # 이 함수 안에서 a는 전역 변수
     a = 10
     print("func1()에서 a값 %d" % a)

def func2() :
     print("func2()에서 a값 %d" % a)

## 함수 변수 선언 부분 ##
a = 20           # 전역 변수

## 메인 코드 부분 ##
func1()
func2()


## 함수 선언 부분 ##
def para_func(*para) :
     result = 0
     for num in para :
          result = result + num

     return result

## 전역 변수 선언 부분 ##
hap = 0

## 메인 코드 부분 ##
hap = para_func(10, 20)
print("매개변수가 2개인 함수를 호출한 결과 ==> %d" % hap)
hap = para_func(10, 20, 30)
print("매개변수가 3개인 함수를 호출한 결과 ==> %d" % hap)


def mixed_params(age, name="아이유", *args, **kwargs):
    print("age =", age)
    print("name =", name)
    print("args =", args)
    print("kwargs =", kwargs)

mixed_params( 20, "정우성", 'male', address="seoul", mobile="01012341234")


# 문제1) 다음은 삼각형의 너비와 높이를 입력받아 함수를 이용하여 삼각형의 면적을 구하는 프로그램이다.

# 실행결과
# 너비를 입력하세요? 10
# 높이를 입력하세요? 15
# 삼각형의 너비 : 10
# 삼각형의 높이 : 15
# 삼각형의 면적 : 75.0

def cal_tri(width, height):
    print('삼각형의 너비 : %d'%width)
    print('삼각형의 높이 : %d'%height)
    print('삼각형의 면적 : %f'%(width*height/2))
    return

w = int(input('너비를 입력하세요 : '))
h = int(input('높이를 입력하세요 : '))
cal_tri(w,h)

# 문제2) 다음은 함수를 이용하여 1~100까지의 양의 정수 중 배수의 합를 구하는 프로그램입니다

# 실행결과
# 구하고자 하는 배수를 입력하세요? 3
# 1~100사이의 3의 배수의 합계는 1683


def sum_bae(input):
    i = 0
    result = 0
    while(input * i <= 100):
        result += input * i
        i += 1

    return result

num = int(input('입력: '))
print('결과는 : ', sum_bae(num) )


def max_return(v1,v2,v3):
    max_value = max(v1,v2,v3)
    return max_value

max_x = max_return(11,22,33)
print(max_x)



# 문제3) 다음은 함수를 이용하여 영어 문장에 포함된 공백을 카운트하는 프로그램이다.
# 영어문장 eng_sent = 'Python is easy and powerful'

# 실행결과
# Python is easy and powerful
# 공백의 갯수 : 4

def count_blank(sent):
    count = 0
    for i in sent:
        if(i == ' '):
            count += 1
    return count

eng_sent = 'Python is easy and powerful'
print(eng_sent)
print('공백의 갯수 : ',count_blank(eng_sent))



# 문제5) 함수로 딕셔너리에서 게임 아이템을 가져오기
# 다음은 사용자 아이디에 따라 딕셔너리에 저장되어 있는 게임 아이템을 가져오는 프로그램이다.

# 힌트
# game_items={'kim':'총', 'lee':'대포','choi':'전투기','hwang':'병사' }

# 결과화면
# 이름은? kim
# kim의 게임 아이템은 총입니다

def get_item(nickname):
    if(nickname == 'null'):
        print('종료합니다')
    elif(nickname in game_items):
        print(f'{nickname}의 게임 아이템은 {game_items[nickname]}입니다')
    else:
        print('잘못 입력하셨습니다')
    return

game_items={'kim':'총', 'lee':'대포','choi':'전투기','hwang':'병사' }

while(True):
    nickname = input('이름은? ')
    
    get_item(nickname)

    if(nickname == 'null'):
        break



# 문제6) 다음과 같이 프로그램을 하면 오류가 난다 원인이 무엇인지 말하시고 고치세요
def func():
   global x
   x = 200

func()
print(x)


# 문제7) 다음 프로그램의 실행결과는?

def func() :
   x=200
   print(x)

x=100
func()
print(x)

# 문제8) 다음 프로그램의 실행결과는?

def func() :
   global x
   x=200
   print(x)

x=100
func()
print(x)


# 문제9) 사용자 함수를 정의하여 킬러미터를 마일로 환산하는 프로그램을 작성하시오

# 힌트 환산 수식
# 마일 = 킬로미터 X 0.621371

# 실행결과
# 킬로미터를 입력하세요 30
# 30킬로미터는 18.64마일입니다

def to_mile(km):
    mile = 0.621371 * km
    return mile

km = int(input('킬로미터를 입력하세요 : '))
mile = to_mile(km)
print(f'{km}km는 {mile}마일입니다')



# 문제10 사용자 함수를 이용하여 영어문장에 있는 알파벳의 개수를 카운트하는 프로그램을 작성하시오

# 실행결과
# 영어문장을 입력하세요 I am a student
# 알파벳 하나를 입력하세요 a
# I am a student에 포함된 a의 개수는 2개입니다


def count_en(sentence, alphabet):
    count = 0
    for i in sentence:
        if(i == alphabet):
            count += 1
    return count

sentence_input = input('영어문장을 입력하세요 : ')
a = input('알파벳 하나를 입력하세요 : ')
result = count_en(sentence_input,a)
print(f'{sentence_input}에 포함된 {a}의 개수는 {result}개 입니다')


# 배수의 합
def sum_bae(input):
    result = 0
    for i in range(1,101,1):
        if(i % input == 0):
            result += i

    return result

num = int(input('입력: '))
print('결과는 : ', sum_bae(num) )



# 문제11) 딕셔너리 eng_dict를 이용하여 영어 단어 퀴즈 맞추기 프로그램을 작성하세요. 사용자 정의함수를 이용하세요

# eng_dict = {"house":"집",  "piano":"피아노",  "christmas":"크리스마스",  "friend":"친구", "bread":"빵" }

# 실행결과
# 집의 영어단어는? house
# 맞았습니다.
# 피아노의 영어단어는? piano
# 맞았습니다
# 크리스마스의 영어단어는?chir
# 틀렸습니다.
# 정답은 chrustmas입니다

def quiz(answer, input):
    if(answer == input):
        print('정답입니다')
    else:
        print('틀렸습니다')
        print(f'정답은 {input}입니다')

    return

eng_dict = {"house":"집",  "piano":"피아노",  "christmas":"크리스마스",  "friend":"친구", "bread":"빵" }

for key in eng_dict.keys():
    answer = input(eng_dict[key]+'의 영어단어는? : ')
    quiz(answer, key)

"""