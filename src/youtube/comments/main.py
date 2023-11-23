import json

from yt_comments import YTComments

def get_api():
    with open('src/youtube/comments/api_key.json', 'r') as openfile:
        api_key = json.load(openfile)
        return api_key.get('API_KEY')
    
api_key = get_api()
video_id ='Q2c13OEz9Ls' 

yt = YTComments(api_key, video_id)
yt.fetch_comments()
yt.dump()

