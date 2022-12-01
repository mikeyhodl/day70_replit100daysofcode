# import os

# password = os.environ['password'] # Uses the os library to talk to the environment and get the secret password stored there.

# userPass = input("Password > ")

# if userPass == password:
#   print("Well done")
# else:
#   print("Better luck next time")


# import os

# password = os.environ['password'] 

# userPass = input("Password > ")

# if userPass == password:
#   print("Well done")
# else:
#   print("Better luck next time")


import os
import time

while True:
  username = input("Username: ")
  password = input("Password: ")
  if username == os.environ['adminUsername'] and password == os.environ['adminPassword']:
    print("Welcome Admin")
    break
  elif username ==  os.environ['username'] and password == os.environ['password']:
    print("Welcome Normie")
    break
  else:
    print("Try again after 3 seconds")
    time.sleep(3)