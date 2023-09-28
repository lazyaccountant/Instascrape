from models import *

def engagement_rate(user: User, post: Post):
        rate = (post.likes + post.comments)/user.followers
        rate = round(rate*100, 2)

def user_stat(user: User):
	post_count = user.post_count
	posts = user.get_user_posts()
	followers = user.followers

	data = {
		"likes": [],
		"comments": [],
		"views": []
		}


	stat = {}
	rates = []
	for i, post in enumerate(posts, start=1):
		media  = Post(post)

		data["post_count"] = i
		data["likes"].append(media.likes)
		data["comments"].append(media.comments)
		rates.append(round((media.likes + media.comments)/followers, 2))
		if media.media_type == 2:
			data["views"].append(media.views)

	stat["avg_likes"] = average(data["likes"])
	stat["avg_comments"] = average(data["comments"])
	stat["avg_views"] = average(data["views"])
	stat["engagement_rate"] = average(rates, True)
	stat["post_count"] =  post_count


	return stat


def average(x: list, percent=False) -> int:
	length = len(x)
	total = sum(x)
	if percent:
		avg = round((total / length)*100, 2)
	else:
		avg = round(total / length)

	return avg
