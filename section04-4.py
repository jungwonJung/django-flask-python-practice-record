#  파이썬 자료구조 (Dictionary, Set)

#  딕셔너리 특징 

#  딕셔너리 추가

#  집합 특징

#  집합 자료형 함수

#  자료형 변환

# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary): 순서x, 중복 x,수정o , 삭제o

# Key, Value (json) -> MongoDB
# 선언
a = {'name' : 'Jung', 'Phone' : '010-9918-9176', 'Birth' : 930315}
b = {0 : 'Hello python', 1 : 'Hello Coding'}
c = {'arr' : [1, 2, 3, 4, 5]}

# print(type(a))

# 출력
print(a['name'])
print(a.get('name'))
print(a.get('address'))
print(c['arr'][1 : 3])

# 딕셔너리 추가
a['address'] = 'Incheon'
print(a)
a['rank'] = [1,3,4]
a['rank2'] = (1,2,3,) 
print(a)

# items, Keys , Value
print(a.keys())
print(list(a.keys()))  # key 를 가져올때 list 로 형변환 하지않으면 가져올수없음

temp = list(a.keys())
print(temp[1 : 3])  # 템플릿 처리가능 형변환한 키값을 함수 지정가능

print(a.values())  
print(list(a.values()))

print(list(a.items()))  # value item 도 형변환 가능 함
print(2 in b)
print('name2' not in a)

# 집합 (Sets)  순서x 중복x

a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c)  # 중복을 허용하지않기때문에 1,4, 5, 6 만표기

t = tuple(b)
print(t)
l = list(b)
print(l)   # 형변환 쌉가능

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2))  # intersetion == 교집합 
print(s1 & s2)

print(s1 | s2)   # 합집합 union
print(s1.union(s2))

print(s1 - s2)  # 차집합 differnce
print(s1.difference(s2))

# 추가 & 제거

s3 = set([7, 8, 10, 15])
s3.add(18)
print(s3)

s3.remove(15)
print(s3)
