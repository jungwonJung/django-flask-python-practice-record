# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
# 나의 풀이
if "가을" in q1:    # 가을이 q1 안에있으면   
    b = q1["가을"]    # "가을" 이라는 값을 b 에 포함시켜준다 그런다음 출력시켜보면
    print(b)    # b 의 키값이 딕셔너리안에 있기때문에 value 값을 출력시킨다

# 정답풀이
for k in q1.keys():
    if k == '가을':
        print(q1[k])

for k,v in q1.items():
    if k == '가을':
        print(q1[k])

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

# 나의 풀이

if "사과" in q2.values():    # 만약 사과가 q2.values() 값에 포함되어있으면 
    print("포함되어있습니다")

# 정답풀이

for k,v in q2.items():
    if v == '사과':
        print(k, v)
        break
    else:
        print("사과 없음")
 


    
# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

num = 93

if num >= 81 and num <= 100:
    print("A학점")
elif num >= 61 and num <= 80:
    print("B학점")
elif num >= 41 and num <= 60:
    print("C학점")
elif num >= 21 and num <= 40:
    print("D학점")
else : 
    print("E학점")



# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
a = 12
b = 6
c = 18
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)
else:
    print("큰 수가 없습니다")


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
s = '891022-2473837'

if int(s[7]) % 2 == 1:
    print("남자")
else:
    print("여자")

# 6 ~ 10 반복문 사용(while 또는 for)



# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.

q3 = ["갑", "을", "병", "정"]

#나의풀이
while '정' in q3:  # 큰따옴표가 들어가서 큰따옴표로 "정" 을적었지만 작은따옴표로 진행하니 됨
    q3.remove('정')   
    print(q3)

# 강의 풀이
for v in q3:
    if v == "정":
        continue
    else:
        print(v)

# 리스트 컴프리헨션 사용

com = [x for x in q3 if x != '정']
print(com)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.


# 나의풀이
n= 1
while n <= 100:
    print(n,end=" ") # end 를 안하면 자동 줄바꿈으로 되서 한라인으로 출력되지않음 
    n += 2
print()

# 강의풀이

for n in range(1,101):
    if n % 2 != 0:
        print(n)

# 리스트 컴프리헨션

com2 = [x for x in range(1,101) if x % 2 != 0]
print(com2)



# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.

# 나의 풀이

q4 = ["nice", "study", "python", "anaconda", "!"]
n = 5
for q4_s in q4:
    if q4_s and len(q4_s) >= n:
        print(q4_s)

# 정답풀이
for q4_s in q4:
    if len(q4_s) >= 5:
        print(q4_s)


# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.

q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]


# 나의 풀이
for v in q5:
    if v.islower():   #isupper(), islower() 을 이용하면. 이 문자가 모두 대문자인지 모두 소문자인지 확인하여 Boolean형태로 뱉어내준다. True False로 .
        print("9, ",v)

# 강의 풀이
for v in q5:
    if v.isupper():
        continue
    else:
        print(v)


# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.

q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

# 나의 풀이
for v in q6:
    if v.isupper():
        print("10, ",v.lower())
    elif v.islower():
        print("10, ",v.upper())

# 강의풀이
for v in q6:
    if v.isupper():
        print("10, ",v.lower())
    else:
        print(v.upper())


# 리스트 컴프리헨션

# 일반적인 방법

numbers = []
for n in range(1, 101):
    numbers.append(n)
print(numbers)

#  컴프리헨션

numbers2 = [x for x in range(1, 101)]
print(numbers2)