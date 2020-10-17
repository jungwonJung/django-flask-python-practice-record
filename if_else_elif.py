def age_check(age): # def 끝에 : 을 항상 해줘야함
  print(f"you are {age}")
  if age < 18:
    print("you cant drink")
  elif age >20 and age < 25:  # elif 조건형성 마지막에도 : 동일
    print("you are still kind young")
  elif age == 18 or age == 19:
    print("you are newstart!")
  else:  # else 는 조건이 없다 if 의 거짓일때만 발동하기때문 
    print("enjoy your drink")
    
age_check(22)
