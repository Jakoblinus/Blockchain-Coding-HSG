import hashlib as hasher
import datetime as date
import random
import json

a = str(input("Your name please: "))
usernames = ["Jordi", "Phillip"]
userdata = ["ID: 1, money available: 200", "id: 2, money: 100"]
if a == "Jordi" in usernames:
  print("Hello", a)
  print(userdata[0])
elif a == "Phillip" in usernames:
  print("Hello", a)
  print(userdata[1])
else:
    print("You are not a registered user.")
