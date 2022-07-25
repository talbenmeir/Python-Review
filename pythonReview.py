def create_youtube_video (title,description):
	youtube_video = {"title":title, "description":description, "likes":0, "dislikes":0, "comments":{}}
	return youtube_video

def like (youtube_video):
	if "likes" in youtube_video:
		youtube_video["likes"]+=1

def dislike (youtube_video):
	if "dislikes" in youtube_video:
		youtube_video["dislikes"]+=1\

def add_comment (youtubevideo, username, comment_text):
	youtubevideo["username"]=comment_text
	return youtubevideo

new_video = create_youtube_video("turtle", "new turtle")
like(new_video)
dislike(new_video)
add_comment(new_video,"Niv","Have fun!!!!")
print(new_video)







