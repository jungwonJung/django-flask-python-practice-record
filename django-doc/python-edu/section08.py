# Section 08
# 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# .  : 현재 디렉토리


from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex1 : ", Fibonacci.fib2(400))
print("ex1 : ", Fibonacci().title)


# 예제2 (클래스)

from pkg.fibonacci import Fibonacci as fb 

fb.fib(500)

print("ex2 : ", fb.fib2(600))
print("ex2 : ", fb().title)

# 예제 3 (함수)
import pkg.calculations as c  # 함수는 import 만해도 다 들어옴 너무 기니깐 as 사용

print("ex3 : ",c.add(10, 100))
print("ex3 : ",c.div(200, 10))
print("ex3 : ",c.mul(10, 10))


# 예제 4 (함수)
from pkg.calculations import div as d
print("ex5 : ", int(d(10, 10)))

# 예제 5
import pkg.prints as p
import builtins   # 여태 패키지 안에서 사용한 함수들을 가져오는 값
p.prt1()
p.prt2()
print(dir(builtins)) 