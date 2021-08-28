# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제1 
# 상속기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든속성, 메소드 사용가능

# 라면 -> 속성(종류, 회사, 맛, 면 종류, 이름) : 부모

class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class "Show Method!"'
# 부모 클래스 생성

class BmwCar(Car):    #   21 번 안에있는 Car 은 11번에 있는 부모클래스안에있는 내용을 상속
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)  # 부모에게 넘겨줘야 하기때문에 super = 부모 클래스
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name


class BenzCar(Car):   
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)  
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

    def show(self):
        print(super().show())
        return 'Car Info : %s %s %s ' % (self.car_name, self.type, self.color)

# 일반 사용

model1 = BmwCar('520d', 'sedan', 'White')
print(model1.color)  # super 상속
print(model1.type)   # super 상속
print(model1.car_name) 
print(model1.show())  # 부모 class 에 저장된 show 를 불러옴 
print(model1.show_model()) # 자식 class 에 저장된 show_model 을 불러옴 
print(model1.__dict__)

# Method Overriding(오버라이딩)   자식 class 가 부모 class 에 올라타서 재구성 시킨다   Java = OverLoading 
model2 = BenzCar('GLC', 'SUV', 'Black')
print(model2.color)
print(model2.show())

# Parent Method Direct Call
model3 = BenzCar('xc60', 'SUV', 'GrapiteBlue')
print(model3.show())

# Inheritance Info    왼쪽부터 어떻게 상속받았는지 보여줌   (상속정보를 리스트 타입으로 보여줌 )
print(BmwCar.mro())
print(BenzCar.mro())


# 예제 2 
# 다중상속

class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

print(M.mro())

# 너무 많은 다중상속은 길을 잃게 만든다 