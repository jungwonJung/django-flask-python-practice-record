# Section05-2
# 파이썬 흐름제어 (반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결중요

# 기본반복문 : for, while

v1 = 1
while v1 < 11:
    print(v1)
    v1 += 1

for v2 in range(10):
    print(v2)

for v3 in range(1, 15):  # 첫번째 시작 마지막 15이전까지
    print(v3)

# 1 ~ 100합

sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1
print(sum1)

# 다른방법
print(sum(range(1,101)))


# 시퀀스(순서가 있는)자료형 반복
# 문자열, 리스트, 튜플, 집합 ,사전
# iterable : range, reversed, enumerate, filter, map, zip

names = ["Jung", "Park", "Choi", "Cho", "Yoo", "Park"]

for name in names:
    print(name)

my_info = {
    "name" : "Ganzi",
    "age" : 28,
    "City" : "Incheon"
}

for key in my_info:  # 기본값은 키
    print(key)

for key in my_info.values(): # 밸류값만
    print(key)

for key in my_info.keys(): # 키값만
    print(key)

for key in my_info.items(): # 키 and 밸류
    print(key)

name = "JungJW"

# 네임 안에 n 값이 만약 대문자로들어왔으면 대문자를 소문자로 나타내고 아니면(소문자는) 대문자로 나타내라
for n in name:
    if n.isupper():     
        print(n.lower())
    else:
        print(n.upper())

# break
numbers = [1, 3, 7, 8 ,9 ,14 ,16 ,24, 26, 47, 86]

for number in numbers:
    if number == 24:
        print("found : 24!")   # 찾으면 break 반복하지않음 
        break
    else:
        print("Not found")

# for -else 구문

for number in numbers:
    if number == 24:
        print("found : 24!")   # 찾으면 break 반복하지않음 
        break
    else:
        print("Not found")
else:
    print("Not found ..........")  # 반복문의 else  반복문이 정상적으로 수행 된경우에 else 블럭 실행

# continue

lt = ["1", 4, 5, True, 4.3, complex(5)]

for v in lt:
    if type(v) is float:
        continue
    print(type(v))

