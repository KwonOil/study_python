print('========== 2025.04.15 ==========\n')

"""
# read_ex1
# data1.txt 파일을 읽어서 화면에 출력하기

inF = open("./Python2/temp/data1.txt", "r", encoding = "utf-8")
while( True ):
    inStr = inF.readline() # <-- readline()
    if(inStr == ""): ## 참이면 EOF(End Of File)
        break
    else:
        print(inStr)
inF.close()

# readlines_ex1
inF = None
inList = []
inF = open("./Python2/temp/data2.txt", "r", encoding = "utf-8")
inList = inF.readlines() # <-- readlines()
print(inList)
inF.close()

### with ~ as 문 ###

inF = None
inList = []
with open("./Python2/temp/data1.txt","r",encoding = "utf-8")as inF:
    inList = inF.readlines()
    print(inList)


# 문제1) data.txt 파일 내용은 apple 엔터 banana 엔터 cherry 이다
# 위에 파일을 읽어서 출력해 보세요.

inF = None
inList = []
with open("./Python2/temp/data_ex1.txt","r",encoding = "utf-8")as inF:
    inList = inF.read()
    print(inList)

# 문제2) data_utf8.txt 파일은 UTF-8 인코딩으로 저장되어 있고, 내용은 다음과 같습니다.
# 파일 내용 data_utf8.txt
# 안녕하세요.
# 파이썬 파일 읽기 문제입니다.
# 행운을 빕니다!

inF = None
inList = []
with open("./Python2/temp/data_utf8.txt","r",encoding = "utf-8")as inF:
    inList = inF.read()
    print(inList)


# 문제3) 텍스트 파일명을 입력 받아서 내용을 출력하기
# [출력결과]
# 파일명을 입력하세요? c:/windows/win.ini

inF = None
inList = []
inputStr = input('파일명을 입력하세요 : ')
with open(inputStr,"r")as inF: # 영어만 있으면 유니코드로 인코딩하지 않아도 된다
    inList = inF.read()
    print(inList)


# 파일 열 때 오류 처리하기

import os # os관련 모듈

inF = None
inList = []

while(True):
    inputStr = input('파일명을 입력하세요 : ')

    if(os.path.exists(inputStr)):
        with open(inputStr,"r")as inF:
            inList = inF.read()
            print(inList)
        break
    else:
        print("%s 파일이 없습니다" %inputStr)


# 실습1)  키보드 입력 -- input() --> 파이썬 프로그램 -- write(), writelines() --> 출력 파일 생성

import os # os관련 모듈

def readFile(inputStr):
    outF = open(inputStr,"a") # "w"는 덮어쓰기, "a"는 이어쓰기
    while(True):
        outStr = input('내용입력 : ')
        if(outStr != ""):
            outF.writelines(outStr+"\n")
        else:
            break
    print('--- 파일이 정상적으로 써졌음 ---')
    outF.close()
    return

inF = None
inList = []

while(True):
    inputStr = input('파일명을 입력하세요 : ')

    if(os.path.exists(inputStr)):
        with open(inputStr,"r")as inF:
            inList = inF.read()
            print(inList)
        break
    else:
        print("%s 파일이 없습니다" %inputStr)

readFile(inputStr)



# 문제1) 출력할 파일명을 입력받고 키보드로 문장을 입력하여 출력파일을 만들어 보자

import os # os관련 모듈

def readFile():
    fName = input('저장할 이름 입력 : ')

    outF = open(fName,"w", encoding = "utf-8")
    while(True):
        outStr = input('내용입력 : ')
        if(outStr != ""):
            outF.writelines(outStr+"\n")
        else:
            break
    print('--- 파일이 정상적으로 써졌음 ---')
    outF.close()
    return

readFile()


# 입력파일 - read() readline(), readlines() --> 파이썬 프로그램 -- write(), writelines() --> 출력파일

inF, outF = None, None
inStr = ""

inF = open("./Python2/temp/data_ex1.txt", "r",encoding = "utf-8")
outF = open("./Python2/temp/data_ex2.txt", "w",encoding = "utf-8")

inList = inF.readlines()
for inStr in inList:
    outF.write(inStr)
# ouF.writelines(inList)
inF.close()
outF.close()


inF, outF = None, None

inF = open("./Python2/temp/gitHub.png", "rb")
outF = open("./Python2/temp/gitHub_copy.png", "wb")

for i in inF.readlines():
    outF.write(i)
    
# while(True):
#     i = inF.read()
#     if( i == ""):
#         print("EOF")
#         break
#     else:
#         outF.write(i)


inF.close()
outF.close()
print("end")



# 동영상(이미지) 복사
inF, outF = None, None

inF = open("./Python2/temp/CherryBlossom.mp4", "rb")
outF = open("./Python2/temp/CherryBlossom_copy.mp4", "wb")

for i in inF.readlines():
    outF.write(i)

inF.close()
outF.close()


# 문제2) 두 파일 모두 파일명을 입력받아서 복사해 보자
# [출력결과]
# 소스파일명을 입력하세요 : c:/windows/win.ini
# 타깃 파일명을 입력하세요 : c:/temp/data4.txt
# --- c:/windows/win.ini 파일이 c:/temp/data4.txt 파일로 복사되었음 ---

inF, outF = None, None
inStr = input("소스파일명을 입력하세요 : ")
outStr = input("타깃 파일명을 입력하세요 : ")

inF = open(inStr, "rb")
outF = open(outStr, "wb")

for i in inF.readlines():
    outF.write(i)
print(f'{inStr}파일이 {outStr}파일로 복사되었음')

inF.close()
outF.close()


# 암호화

## 변수 선언 부분 ##
inF, outF = None, None
inStr, outStr = "", ""
i = 0
security = 0
num = 1

## 메인 코드 부분 ##
# 입력부
Choice = input(" 1. 암호화  2. 암호 해석 중 선택 : ")
inF_name = input("입력 파일명을 입력하세요 : ")
outF_name = input("출력 파일명을 입력하세요 : ")

# 암호화/복호화 키 지정
if Choice == "1" :
    security = num
elif Choice == "2" :
    security = -num

# 파일 열기(읽기위해)
inF = open(inF_name, 'r', encoding = 'utf-8')
# 파일 열기(쓰기위해)
outF = open(outF_name, 'w', encoding = 'utf-8')

inStr = inF.readline()
print(inStr)
while True :
    inStr = inF.readline() # 입력받은 파일의 한 줄을 inStr에 대입
    if not inStr :          # inStr이 없으면(EOF)
        break               # 반복종료

    outStr = ""                     # outStr 초기화
    for i in range(0, len(inStr)) : # inStr의 문자 하나하나 반복
        ch = inStr[i]               # inStr의 i번째 인자를 ch에 대입
        chNum = ord(ch)             # ch를 유니코드의 숫자로 변환해 chNum에 대입
        chNum = chNum + security    # 변환한 chNum에 security를 더함(암호화)
        ch2 = chr(chNum)            # chNum을 문자로 변환한 값을 ch2에 대입
        outStr = outStr + ch2       # outStr에 변환된 문자를 추가

    outF.write(outStr)     # 변환된 문자열 outStr을 outF에 쓰기

outF.close()    # 파일 닫기
inF.close()     # 파일 닫기

print(' %s --> %s 변환 완료' % (inF_name, outF_name))


"""

# 파일과 디렉터리

import shutil
import os

"""

# shutil
dir(shutil) # shutil 모듈에 있는 함수들 목록 보기

# shutil.copy("./Python2/temp/data_ex1.txt","./Python2/temp/data_ex2.txt")
# shutil.move("./Python2/temp/data_ex1.txt","./Python2/temp/data_ex3.txt")

# os
os.mkdir("./Python2/temp/ss") # 디렉터리 생성
# shutil.rmtree("./Python2/temp/mm") # 디렉터리 삭제

for dirName, subDirList, fnames in os.walk("./Python2/temp"): # 디렉토리의 목록 모두 보기
    for fname in fnames:
        print(os.path.join(dirName, fname))
    for s in subDirList:
        print(s)

# 파일 또는 폴더가 존재하면 삭제

if(os.path.exists("./Python2/temp/ss")):
    shutil.rmtree("./Python2/temp/ss")


# 파일 크기 확인

if(os.path.exists("./Python2/temp")):
    file_size = os.path.getsize("./Python2/temp/cherryBlossom.mp4")
    print(file_size,'byte')
    print(file_size//1024, 'KB')
    print(round(file_size/1024/1024,2), 'MB')

"""

# 파일 압축하기
import zipfile
newZip = zipfile.ZipFile("./Python2/temp/new.zip","w")
newZip.write("./Python2/temp/CherryBlossom.mp4", compress_type = zipfile.ZIP_DEFLATED)
newZip.close()

# 압축된 파일을 풀기
extZip = zipfile.ZipFile("./Python2/temp/new.zip","r")
extZip.extractall("./Python2/temp")
extZip.close()