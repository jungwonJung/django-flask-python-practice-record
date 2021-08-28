# 파이썬 구성요소 기초학습 

# 인코딩 (입력, 출력)

# 변수 

# 조건문 

# 함수, 클래스, 인스턴스(객체)

# 정보 출력

# import this
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print('My name is Ganzi')

# 변수 선언  내용을 담는 그릇
myName = 'good boy'

# 조건문
if myName == "good boy":
    print('ok')

# 반복문  구구단 출력
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d= ' % (i,j), i * j )

# 함수 선언
def SayHi():
    print('Hello everyone')

SayHi()

# 클래스
class Cookie():
    pass

# 객체 선언
cookie = Cookie
print(id(cookie))
print(dir(cookie))