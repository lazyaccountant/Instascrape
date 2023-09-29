from instagrapi import Client
from ensta import Guest
from instagrapi.exceptions import ChallengeRequired
from ensta.lib.Exceptions import APIError

guest = Guest()
cl = Client()
cl.delay_range = [1, 3]
cl.load_settings("session.json")
cl.login()

try:
	cl.get_timeline_feed() # check session
except ChallengeRequired:
	print(ChallengeRequired.message)

class User:
	def __init__(self, username):
		self.username = username
		self.profile = guest.profile(self.username)
		self.id = self.profile.user_id
		self.followers = self.profile.follower_count
		self.bio = self.profile.biography
		self.name = self.profile.full_name
		self.post_count = self.profile.total_post_count
		self.professional = self.profile.is_professional_account
		#self.info = cl.user_info(self.id)
		#self.cat = self.info.category_name


	def get_user_posts(self):
		posts = cl.user_medias(self.id, 20)
		return posts

	def get_user_following(self):
		following_list = []
		self.following = cl.user_following(
					user_id=self.id,
					amount=0
					)

		followings = self.following.values()

		for user in followings:
			following_list.append(user.username)

		return following_list

	def get_user_followers(self):
		followers_list = []
		self.followers = cl.user_followers(
					user_id=self.id,
					amount=20
					)

		followers = self.followers.values()

		for user in followers:
			followers_list.append(user.username)

		return followers_list



class Post:
	def __init__(self, post):
		self.pk = post.pk
		self.likes = post.like_count
		self.comments = post.comment_count
		self.media_type = post.media_type
		if self.media_type == 2:
			self.views = post.view_count



if __name__ == "__main__":
	user = User("diana_eneje")
	followings = user.get_user_following()

	for username in followings:
		try:
			following = User(username)
			if 10000 < following.followers < 100000:
				print(username, following.followers, following.professional)
		except APIError:
			pass
