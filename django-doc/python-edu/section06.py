# Section06
# 파이썬 함수식 및 람다(lamda)

# 함수 정의 방법
# def 함수명 (parameter):
#         code

# 함수 호풀
# 함수명 (parameter)

# 함수선언위치 중요

# 예제 1

def hello(world):
    print("hello", world)

hello("Python")
hello(77777)     # def 밑에 사용해야함 위에서 부터 밑으로 실행

# 예제2

def hello_return(world):
    val = "hello" + str(world)
    return val

str = hello_return("Python!!!!!!!!!!")
print(str)

# 예제3 (다중리턴)

def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(100)
print(val1, val2, val3)

# 예제 4 (데이터 타입 변환)


def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]   # 리스트, 튜플로 감싸면 됨 현재 리스트

lt = func_mul2(100)
print(lt)

# 예제 5
# *args, *kwargs

def args_func(*args):  # 가변형   투플형태
    # print(args)  이걸지우고나서 튜플일때

    # for t in args:
    #     print(t)   #  튜플인자를 받아서 나타냄
    
    for i, v in enumerate(args):   # enumerate(range(10))
        print(i, v)   # 인덱스번호와 벨류값이 같이나옴

args_func('jung')
args_func('jung', 'kim')

# kwargs (keyword)  딕셔너리 형태

def kwargs_func(**kwargs):
    print(kwargs)   # k,v 는 items 필수  for ~~ in 

kwargs_func(name1='jung')

# 전체 혼합

def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10, 20)
example_mul(10, 20, 'jung', 'park', age4=28, age5=29)

# 중첩함수(closer)
# 함수 안에 함수 func_in_func

def nested_func(num):  # 2.
    def func_in_func(num): # 3.
        print('>>>>>>', num)   # 6.
    print("in func")  # 5.
    func_in_func(num + 10000)  # 4. 입력해주면

nested_func(10000)  #  입력해주면 1.


# 힌트 함수

def func_mul3(x : int) -> list:  # int  값을 넣으면 list 값으로 반환 해준다 
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

print(func_mul3(5.0))


# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당

def mul_10(num : int) -> int:
    return num * 10  # 설정해주지않고 리턴에서 바로 값 정하기

var_func = mul_10   # var_func 함수라는 타입을 생성 메모리에 저장
print(var_func)
print(var_func(10))

# 게시판 데이터를 가져와서 대량으로 수정할때 사용 
lambda_mul_10 = lambda num : num * 10

print(lambda_mul_10(20))

def func_final(x, y, func):
    print( x * y * func(10))

func_final(10, 10,lambda_mul_10)

print(func_final(10, 10, lambda x : x * 1000))

# 람다 이해불가 함수를 매개변수로 넘길때