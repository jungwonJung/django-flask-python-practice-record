# 파이썬 자료구조(List, Tuple)

# 리스트 특징

# 튜플 특징

# 인덱싱

# 슬라이싱

# 삽입, 삭제 ,함수 사용

# Section04-2 
# 파이썬 데이터 타입 (자료형)
# 리스트 , 튜플

# 리스트 (순서o, 중복o, 수정o, 삭제o)
# 선언

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange'] # 내부적으로 인덱스를 가지고있음 0,1,2 등등
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱 
print(d[-2])
print(e[2][2])
print(e[-1][1])

# 슬라이싱
print(d[0 : 3])
print(e[2][1 : 3])

# 연산
print(c + d)
print(c * 3)
print(str(c[0]) + 'hi')

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1 : 2] = [10, 100, 1000]
print(c)

c[1] = ['a', 'b', 'c']
print(c)

del c[1] # 삭제하려는 리스트에서 인덱스번호 부여
print(c)
del c[-1]
print(c)
print()
print()
print()

# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)

y.append(6) # 리스트 끝에 추가시킨다
print(y)

y.sort()  # 리스트 순서대로 정렬
print(y)

y.reverse()
print(y)

y.insert(2, 7) # 2번인덱스에 7이 들어간다
print(y)

y.remove(2)  # 2번인덱스를 지우는게 아니라 리무브는 2라는 값을 지움 
print(y)

y.pop()  # 맨마지막 데이터를 꺼내고 날려버립니다  LIFO
print(y)

ex = [88, 87]
y.append(ex)  # 끝에 리스트째로 들어감

y.extend(ex)
print(y)

# 삭제 : del, remove , pop 

# 튜플 (순서o, 중복o,수정x, 삭제x)

a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(d[2][1])

print(d[2:])

# 튜플 함수

z = (5, 4, 3, 2, 1)
print(z)

y.append(ex)
print(2 in z)
print(z.index(3))  # 3의 위치가 있는 인덱스의위치를 반환함
print(z.count(1))