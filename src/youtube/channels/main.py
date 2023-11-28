from youtube_statistics import YTstats

import json 

def get_api():
    with open('src/youtube/comments/api_key.json', 'r') as openfile:
        api_key = json.load(openfile)
        return api_key.get('API_KEY')
    
api_key = get_api()  
# channel_id ='UCbXgNpp0jedKWcQiULLbDTA' #patrick_loeber
channel_id ='UCwBew3PWseCYjLUwrnXqFrw' #huyen tam mon
yt = YTstats(api_key, channel_id)
yt.get_channel_statistics()
yt.get_channel_video_data()
# url = "https://www.googleapis.com/youtube/v3/search?key=AIzaSyBZnBVHK5L57k4cwbEVPN7GXMKHOlmnW3U&channelId=UCbXgNpp0jedKWcQiULLbDTA&part=snippet,id&order=date"

# yt._get_channel_content_per_page(url)
yt.dump()

