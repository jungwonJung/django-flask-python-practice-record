# 데이터 타입

v_str1 = "Niceman" # 문자열
v_bool = True # 불리언 True, False  대문자 주의
v_str2 = "Good boy"
v_float = 10.3  # 소수점
v_int = 7   # 정수
v_dict = {
    "name" : "Jung",
    "age" : 28
}
v_tuple = 3, 5, 7
v_set = {7, 8, 9}
v_list = [3, 5, 7]

# type 현재 변수의 타입이 뭔지 알려줌
print(type(v_tuple))
print(type(v_set))
print(type(v_float))

# 파이썬 숫자형 및 연산자
#  + 더하기
#  - 빼기
#  * 곱하기
#  / 나누기
#  // 나누기 (몫)
#  % 나누기 나머지만 보여줌
#  ** 지수 (제곱)
#   단항 연산자

i1 = 39
i2 = 939
big_int1 = 999999999999999999999999999999999999
big_int2 = 77777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

print(i1 * i2)

result = i1 * i2
print(result,type(result))


# 형변환
# int, float, complex(복소수)

a = 5. 
b = 5
c = 10
result2 = a + b 
print(result2)

print(int(result2))
print(float(c))
print(complex(3))
print(int(True))
print(int(False))
print(int('3'))


# 단항 연산자 
y = 100
y += 100
y *= 100
print(y)


print(abs(-7)) # abs 절대값을 나타내주는 함수
n, m = divmod(100, 8)   #몫은 n 나머지는 m 으로 들어감 100을 8로나누면 
print(n, m)


