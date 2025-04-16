print('========== 2025.04.16 ==========\n')

"""
# 예외처리

myStr = "파이썬은 재미있어요. 예외처리 공부"

strPosList = []
index = 0

while(True):
    try:
        index = myStr.index('공부',index)
        strPosList.append(index)
        index += 1
    except: # <-- except 뒤에 예외종류를 적지 않으면 모든 종류의 예외를 처리
        break

print('파이썬 글자 위치 -->', strPosList)

# 실습
res = 0
while(True):
    num1 = input("숫자1 --> ")
    num2 = input("숫자2 --> ")
    try:
        num1 = int(num1)
        num2 = int(num2)
        # if 버전
        # if(num2 == 0):
        #     print('다시 입력하세요')
        #     continue
        # else:
        #     res = num1/num2
        #     break
        res = num1/num2
        break

    except ZeroDivisionError :
        print("0으로 나눌 수 없습니다 다시 입력하세요")
    except ValueError :
        print("문자열은 숫자로 변환할 수 없습니다 다시 입력하세요")
    except KeyboardInterrupt :
        print("Ctrl + C를 눌렀군요 종료합니다")
        break
    except Exception as e:
        print(type(e).__name__,"에러났음" ) # __변수명__ : 해당 클래스 내부 변수
print(res)


# try_except_else_finally

# 형식
# try :
#     실행할 문장들
# except :
#     오류일 때 실행할 문장들
# else :
#     오류가 발생하지 않으면 실행할 문장들
# finally :
#     오류가 발생하던지, 아니던지 상관없이 무조건 실행하는 문장

try:
    inF = None
    inF = open("./Python2/temp/data3.tt", "r",encoding = "utf-8")
except FileNotFoundError:
    print("파일이 없습니다")
else :
    inList = inF.read()
    print(inList)
finally :
    if(inF is not None):
        inF.close()


# 객체지향 프로그래밍(OOP : Objected Oriented Programming)

# 1단계  클래스 선언
# 2단계  인스턴스 생성
# 3단계  필드나 메소드 사용

class Car :
    # 필드(멤버 필드) : 클래스 안에 선언한 변수
    color = ""
    speed = 0

    # 매서드 : 클래스 안에 선언한 함수
    def upSpeed(self, value):
        self.speed += value
        return
    def downSpeed(self, value):
        self.speed -= value
        return
    # 생성자 __init__(self)
    # 생성자 __init__(self,value1,value2)
    def __init__(self,color,speed = 0):
        self.color = color
        self.speed = speed
        return

myCar1 = Car("Red",0)

myCar2 = Car("Blue",0)

myCar3 = Car("Yellow")

myCar1.upSpeed(30)
print("자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다." %(myCar1.color,myCar1.speed))

myCar2.upSpeed(60)
print("자동차2의 색상은 %s이며, 현재 속도는 %dkm입니다." %(myCar2.color,myCar2.speed))

myCar3.upSpeed(0)
print("자동차3의 색상은 %s이며, 현재 속도는 %dkm입니다." %(myCar3.color,myCar3.speed))

print()


# 클래스에서 생성자의 가매개변수의 갯수를 유동적으로 하려면
# '*변수명' <-- 튜플 형식으로 저장됨
# '**변수명' <-- 딕셔너리 형식으로 저장됨

class Car :
    color = ""
    price = 0
    speed = 0
    def __init__(self,*args,**kwargs):
        if(len(args) == 0):
            self.color = "BLACK"
        elif(len(args) == 1):
            self.color = args[0]
        elif(len(args) == 2):
            self.color = args[0]
            self.price = args[1]
        elif(len(args) == 3):
            self.color = args[0]
            self.price = args[1]
            self.speed = args[2]
        else:
            print('too many argument')
        return

myCar1 = Car("RED", 1000, 30)
print(myCar1.color, myCar1.price, myCar1.speed)

myCar2 = Car("BLUE", 2000)
print(myCar2.color, myCar2.price, myCar2.speed)

myCar3 = Car("YELLOW")
print(myCar3.color, myCar3.price, myCar3.speed)

myCar4 = Car()
print(myCar4.color, myCar4.price, myCar4.speed)


# *args, **kwargs 예제

class Person :
    name = ""
    age = 0
    address = ""
    def __init__(self, *args, **kwargs):
        if(args):
            self.name = args[0]
            self.age = args[1]
            self.address = args[2]
        if(kwargs):
            self.name = kwargs["name"]
            self.age = kwargs["age"]
            self.address = kwargs["address"]
        return

p1 = Person("홍길동", 20, "성남시")
print( p1.name, p1.age, p1.address)

p2 = Person(name = "이순신", age = 30, address = "서울시")
print(p2.name, p2.age, p2.address)

p3 = Person()
print(p3.name, p3.age, p3.address)


# 상속
# 실습1)

class Dog:
    c_var = "클래스 변수"
    c_i_var = 100

    def __init__(self):
        self.in_var = "인스턴스 변수"
        self.in_i = 200

myDog = Dog()
print(myDog.c_var, myDog.in_var, myDog.c_i_var, myDog.in_i)
print(Dog.c_var, Dog.c_i_var)
print(myDog.in_var, myDog.in_i)
# 인스턴스 변수는 사용하려면 반드시 객체생성해야한다. 객체가 소멸할 때 소멸
# 클래스 변수는 컴파일 단계에서 스택 메모리에 올라간다. 프로그램 종료할 때 소멸



class Car:
    speed = 0
    def upSpeed(self,value):
        self.speed += value
        print("현재 속도(슈퍼 클래스) : %d" % self.speed)

class Sedan(Car):
    def upSpeed(self,value):
        self.speed += value
        if(self.speed > 150):
            self.speed = 150
        print("현재 속도(서브 클래스) : %d" % self.speed)
    
class Truck(Car):
    pass

sedan1, truck1 = None, None

truck1 = Truck()
sedan1 = Sedan()

print("트럭 --> ", end = " ")
truck1.upSpeed(200)

print("승용차 --> ", end = " ")
sedan1.upSpeed(200)



# 실습2)

import turtle
import random

## 클래스 선언 부분 ##
class Shape:  # 부모 클래스
    myTurtle = None
    cx, cy = 0, 0  # 사각형 및 원의 중심점.

    def __init__(self):
        self.myTurtle = turtle.Turtle('turtle') # 거북이 생성.
   
    def setPen(self) : # 펜 색상과 두께를 랜덤하게 뽑기
        r = random.random()
        g = random.random()
        b = random.random()
        self.myTurtle.pencolor((r, g, b))
        pSize = random.randrange(1,10)
        self.myTurtle.pensize(pSize)                

    def drawShape(self):  # 하위 클래스에서 상속받아서 오버라이딩
        pass

class Rectangle(Shape): # 자식 클래스
    width, height = [0] * 2
    def __init__(self, x, y):
        Shape.__init__(self)  
        self.cx = x
        self.cy = y
        self.width = random.randrange(20, 100)
        self.height = random.randrange(20, 100)
        
    def drawShape(self) :
        # 네모 그리기
        sx1, sy1, sx2, sy2 = [0] * 4  # 왼쪽 위 X, Y와 오른쪽 아래 X,Y
        
        sx1 = self.cx - self.width/2
        sy1 = self.cy - self.height /2
        sx2 = self.cx + self.width/2
        sy2 = self.cy + self.height /2

        self.setPen() # 부모 클래스 메소드
        self.myTurtle.penup()
        self.myTurtle.goto(sx1, sy1)
        self.myTurtle.pendown()
        self.myTurtle.goto(sx1, sy2)
        self.myTurtle.goto(sx2, sy2)
        self.myTurtle.goto(sx2, sy1)
        self.myTurtle.goto(sx1, sy1)
        
## 함수 선언 부분 ##
def  screenLeftClick(x,y):
    rect = Rectangle(x, y)
    rect.drawShape()
    
## 메인 코드 부분 ##
turtle.title('거북이로 객체지향 사각형  그리기')
turtle.onscreenclick(screenLeftClick,1)
turtle.done()

"""

# 특별한 메소드
# del 클래스명 <-- 객체 소멸
# 1) __del__()
# 소멸자
# 인스턴스를 삭제할 때 자동으로 호출된다.

# 2) __repr__()
# 인스턴스를 print()문으로 출력할 때 실행되는 메소드이다. print(인스턴스)를 실행하면 호출된다.

# 3) __add__()
# 인스턴스 사이에 덧셈 작업이 일어날 때 실행되는 메소드이다.

# 4) 비교메소드
# __lt__(), __le__(), __gt__(), __ge__(), __eq__(), __ne__()

# 12. 추상 메소드
# 13. 멀티스레드
# 14. 멀티프로세싱