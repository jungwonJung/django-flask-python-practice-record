import requests



def start():
  print("Welcome to IsItDown.py!")
  print("Please write a URL or URLs you want to check. (separated by comma)")
  sites = input().lower().split(",")
  for site in sites:
    site = site.strip()
    if "." not in site:
      print("site","is not a valid URL")
    else:
      if "http://" not in site:
        site = f"http://{site}"
      try:
        request = requests.get(site)
        if request.status_code == 200:
          print(site, "is up")
        else:
          print(site, "is down")
      except:
        print(site, "is down")
  again()


start()

def again():
  message = input("do you want to start over? y/n ").lower()
  if message == "y" or message == "n":
    if message == "y":
      return start()
    elif message == "n":
      print("k.bye!")
      return
    else:
      print("That's not a valid answer")
      again()

### 코드는 만들었는데 동작이안되요....최선을다했습니다 ㅠㅠㅠ###
### I made the code, but it doesn't work... sry ㅠㅠㅠㅠ ####
