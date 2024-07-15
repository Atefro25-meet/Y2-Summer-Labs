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


while create_youtube_video["likes"]<495:
	create_youtube_video["likes"]+=1



