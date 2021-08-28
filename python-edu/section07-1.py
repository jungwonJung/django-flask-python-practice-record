# Section07-1
# 파이썬 클래스 상세 이해
# Self,  클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용가능, 객체 보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용한다

# 선언
# class 클래스명:
#     함수
#     함수
#     함수


# 예제 1
class UserInfo: # 클래스를 선언해줄땐 첫글자를 대문자로 단어와 단어 연결시에도 첫글자 대문자
    # 속성, 메소드
    def __init__(self,name):
        self.name = name
    def user_info_p(self):   
        print("name : ", self.name)


user1 = UserInfo("Ganzi")  # user1 과 user2 는 다름 
user1.user_info_p()
user2 = UserInfo("Park")
user2.user_info_p()

print(id(user1))  # class 선언 id 값 다름
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)

# 예제2
# self 의 이해
class SelfTest:
    def function1():
        print('function1 called!')
    def function2(self):
        print('function1 called!')

# 인스턴스를 생성하는 문자들은 self 인자가 자동으로 넘어간다
# self 가 없는것들은 class 에서 직접호출한다
self_test = SelfTest()
# self_test.function1
SelfTest.function1()


# 클래스 변수 와 인스턴스 변수
#    self 없음     self 있음
# 예제 3

class WareHouse:
    stock_num = 0
    def __init__(self,name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('Jung')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__) # 클래스 네임스페이스, 클래스 변수 (공유함)


print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num)  # user1 의 네임스페이스가 없으면 class 네임스페이스로 가서 찾고 그래도 없으면 에러발생
print(user2.stock_num)
print(user3.stock_num)

del user1
