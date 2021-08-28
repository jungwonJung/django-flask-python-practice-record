# Section05-1
# 파이썬 흐름제어(제어문)
# 조건물 실습

print(type(True))
print(type(False))

# ex .1
if True:
    print("yes")

# ex.2 
if False:
    print("No") 
else:
    print("yes2")

# 관계 연산자
# >, >= , <, <=, ==, != (같지않다)

a = 10
b = 0 

print(a == b)
print(a != b)
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)

# 참 거짓 종류(True, False)
# 참 : "내용",[내용],(내용),{내용},1, True
# 거짓 : "", [],(), {}, 0 ,False

city = ""
if city:
    print("True")
else:
    print(">>>>>>>>>>False")

# 논리 연산자

# and,  or, not
a = 100
b = 60
c = 15 

print("and : ", a > b and b > c)
print("or : ", a > b or c > b)
print("not : ", not a > b)
print(not True)
print(not False)

# 산술, 관계,  논리 연산자
# 산술 > 관계 > 논리 순서로 적용

print('ex : ', 5 + 10 > 0 and not 7 + 3 == 10 )

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print("합격입니다")
else:
    print("죄송합니다. 불합격입니다") 

# 다중조건문

num = 90

if num >= 90:
    print("num 등급 A",num)
elif num >= 80: 
    print("num 등급 B",num)
elif num >= 70:
    print("num 등급 C",num)
else : 
    print("꽝")


# 중첩 조건문

age = 28
height = 175

if age >= 20:
    if height >= 170:           # 중첩조건문 
        print("1지망 지원 가능")  #
    elif height >= 160:           #  heigt 조건에 대한 조건문
        print("2지망 지원 가능")    #
    else :                        #
        print("지원 불가")        #
else :
    print("20세 이상 지원 가능")     # 86번 라인 조건에대한 else 문 출력

