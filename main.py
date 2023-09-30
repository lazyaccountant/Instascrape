import os
import time
from models import User, Post
from utils import *
import csv
from instagrapi import Client
from ensta import Guest
from instagrapi.exceptions import ChallengeRequired
from ensta.lib.Exceptions import APIError
from dotenv import load_dotenv

load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")


guest = Guest()
cl = Client()

cl.delay_range = [1, 3]
cl.load_settings("session.json")
cl.login(username, password)

try:
        cl.get_timeline_feed() # check session
except ChallengeRequired:
        print(ChallengeRequired.message)


def stalk():
	prompt = input("stalk: ")
	user = User(prompt)
	followings = user.get_user_following()

	with open("data.csv", "w", newline="") as f:
		fieldnames = ["username", "category", "bio_links", "followers", "avg_likes", "avg_comments", "avg_views", "engagement_rate(%)", "post_count"]
		writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
		writer.writeheader()

		for username in followings:
			try:
				following = User(username)
				if 10000 < following.followers < 100000 and following.professional:
					data = user_stat(following)
					writer.writerow(data)
					print(data)
			except APIError:
				pass

# edit instagrapi/mixins/fbsearch.py count to 50
def search():
	query = input("Search: ")
	response = cl.search_users(query)

	results = []
	for user in response:
		results.append(user.username)

	return results


users = search()
print(users)
