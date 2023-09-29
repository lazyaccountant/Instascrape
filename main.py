import time
from models import *
from utils import *
import csv

username = input("Enter Username: ")
user = User(username)



start = time.time()
followers = user.followers_list
#data = user_stat(user)
stop = time.time()

print(stop-start)
print(followers)
print(user.info)
