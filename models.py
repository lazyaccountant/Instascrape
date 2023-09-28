from instagrapi import Client
from ensta import Guest


guest = Guest()
cl = Client()

class User:
	def __init__(self, username):
		self.username = username
		self.profile = guest.profile(self.username)
		self.id = self.profile.user_id
		self.followers = self.profile.follower_count
		self.bio = self.profile.biography
		self.name = self.profile.full_name
		self.post_count = self.profile.total_post_count
		self.info = cl.user_info(self.id)
		self.cat = self.info.category_name


	def get_user_posts(self):
		posts = cl.user_medias(self.id, 20)
		return posts

class Post:
	def __init__(self, post):
		self.pk = post.pk
		self.likes = post.like_count
		self.comments = post.comment_count
		self.media_type = post.media_type
		if self.media_type == 2:
			self.views = post.view_count



if __name__ == "__main__":
	user = User("_.zah0k._")
	id = user.id
	medias = user.get_user_posts()
	print(medias)
	#for media in medias:
		#print(media.pk)
