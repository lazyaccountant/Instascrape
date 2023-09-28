import time
from models import *
from utils import *

username = input("Enter Username: ")
user = User(username)
id = user.id
cat = user.cat


start = time.time()
data = user_stat(user)
stop = time.time()

print(stop-start)
print(cat)
print(data)
