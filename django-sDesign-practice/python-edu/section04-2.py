#  문자형 관련 연산자

#  문자열 생성, 길이

#  이스케이프 문자

#  문자열 연산

#  문자열 형 변환

#  문자열 함수

#  문자열 슬라이싱 

# Section04-2 
# 문자열, 문자열연산, 슬라이싱

str1 = "I am boy."
str2 = 'Nice man'
str3 = ' '
str4 = str('ace')
print(len(str1), len(str2), len(str3), len(str4))

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab \t Tab \t Tab"
print(escape_str2)

# Raw string
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)


# 멀티라인   \ 가 들어가있으면 끝나지않고 밑에를 연결시켜준다는 의미
multi = \
"""

String

Multiline

Test

"""
print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = "abc"
str_o3 = "def"
str_04 = "Nice man"

print(str_o1 * 100)
print(str_o2 + str_o3)
print('a' in str_04)
print('a' not in str_04)

# 문자열 형 변환

print(str(77) + 'a')
print(str(10.4))

# 문자열 함수

# a = 'nice man'
# b = 'orange'

# print(a.islower())  # 소문자로 구성되어있는지
# print(b.endswith('e'))  # e로 끝나는지 현재 물어본거임
# print(a.capitalize()) # 첫글자만 대문자로 변경해줌
# print(a.replace('nice', 'good'))  # 나이스를 굿으로변경해주겟다 재설정
# print(list(reversed(b)))


a = 'nice man'
b = 'orange'

print(a[0 : 3]) # 마지막 3 이전까지만 나옴
print(a[0 : 8])
print(a[0 : len(a)])
print(a[:4])
print(a[:])
print(a[0 : 4 : 2]) # 0부터 4 거기서 2까지 
print(a[1 : -2]) # 1부터 -2 사이에있는거
print(a[:: -1]) 