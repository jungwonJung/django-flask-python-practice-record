# Separator 옵션 사용
# sep 값으로 문자를 연결해주는 것


print('T','E','S','T',sep='')

print('2020','10','18',sep='')

print('wjdwjd1501','gmail.com',sep='@')

# End 옵션 사용
# 끝을 내지 않겟다 저 두라인이 연결되서 나옴

print('Welcome To',end=' ')
print('the black parade', end=' ')
print(' piano note')

# 줄바꿈이 되서 나옴 이어서 할거면 end 사용 end=' ' 처럼 안에 띄어쓰기 가능

print('testtest')


# format 사용 [] 대괄호 , {} 중괄호, () 소괄호


print('{} and {}' .format('you', 'me'))

print('{0} and {1} and {0}'.format('you','me')) # 작은따옴표대신 큰따옴표를 써도 상관무

print('{a} are {b}'.format(a = 'you', b = 'Me'))

# %s : 문자   %d : 정수   %f : 실수 
print("%s 's favorite number is %d" % ('Ganzi', 7))

