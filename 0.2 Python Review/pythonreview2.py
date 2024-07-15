def create_youtube_video(title,descreption):
	video={"title":title,"descreption":descreption,"likes":0,"dislikes":0,"comments":{}}
	return video

def like(create_youtube_video):
	if "likes" in create_youtube_video:
		create_youtube_video["likes"]+=1
	return create_youtube_video

def dislike(create_youtube_video):
	if dislikes in create_youtube_video:
		create_youtube_video["dislikes"]+=1
	return create_youtube_video


def add_comments(create_youtube_video,username,comment_txt):
	create_youtube_video["comments"][username]=comment_txt
	return create_youtube_video

saved_dictionary=create_youtube_video("Atef","Wooooo")
for i in range(495):
	new_dictionary=like(saved_dictionary)

print(new_dictionary)

