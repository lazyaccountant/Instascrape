from models import *
from utils import *
import csv
from ensta.lib.Exceptions import APIError



def stalk():
	prompt = input("stalk: ")
	user = User(prompt)
	followings = user.get_user_following()

	with open("data.csv", "a") as f:
		fieldnames = ["username", "category", "email", "followers", "avg_likes", "avg_comments", "avg_views", "engagement_rate(%)", "post_count"]
		writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
		#writer.writeheader()

		for username in followings:
			try:
				following = User(username)
				if 10000 < following.followers < 100000 and following.professional:
					data = user_stat(following)
					writer.writerow(data)
					print(data)
			except APIError:
				pass

def save_stat(usernames: list):

	with open("stat.csv", "w", newline="") as f:
		fieldnames = ["username", "category", "email", "followers", "avg_likes", "avg_comments", "avg_views", "engagement_rate(%)", "post_count"]
		writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
		writer.writeheader()

		for username in usernames:
			try:
				user = User(username)
				if 10000 < user.followers < 100000 and user.professional:
					data = user_stat(user)
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


#users = search()
#save_stat(users)
stalk()
