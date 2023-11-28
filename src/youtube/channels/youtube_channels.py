import json
import requests

from youtube_comments import YouTubeCommentsFetcher

class YTchannels:

    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.base_url = "https://www.googleapis.com/youtube/v3/"
        self.video_count = None
    
    def get_channel_statistics(self):

        url = f"{self.base_url}channels?part=statistics&id={self.channel_id}&key={self.api_key}"

        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            data = data['items'][0]['statistics']
        except KeyError:
            print('Could not get channel statistics')
            data = {}
        self.video_count = data['videoCount']
        print(data)
    
    def get_video_ids(self, num_results):
        playlist_id = self._get_playlist_id()

        video_ids = []
        next_page_token = None

        while len(video_ids) < num_results:
            playlist_url = f"{self.base_url}playlistItems?part=snippet&playlistId={playlist_id}&maxResults=50&key={self.api_key}"

            if next_page_token:
                playlist_url += f"&pageToken={next_page_token}"

            playlist_response = requests.get(playlist_url)
            playlist_data = json.loads(playlist_response.text)

            for item in playlist_data.get('items'):
                video_id = item['snippet']['resourceId']['videoId']
                video_ids.append(video_id)

            next_page_token = playlist_data.get('nextPageToken')

            if not next_page_token:
                break

        return video_ids[:num_results]

    def _get_playlist_id(self):
        channel_url = f"{self.base_url}channels?part=contentDetails&id={self.channel_id}&key={self.api_key}"
        channel_response = requests.get(channel_url)
        channel_data = json.loads(channel_response.text)

        return channel_data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    
    
    
    
    
api_key = "AIzaSyBZnBVHK5L57k4cwbEVPN7GXMKHOlmnW3U"
# channel_id ='UCwBew3PWseCYjLUwrnXqFrw' #huyentammon have 19 video
channel_id ='UCwBew3PWseCYjLUwrnXqFrw' #blv_AQ_D 814 video 

num_results = 3

yt = YTchannels(api_key, channel_id)

yt.get_channel_statistics()
print(yt.video_count)
video_ids = yt.get_video_ids(num_results)


# api_key = 'AIzaSyB6Qhlr3A0YReR5f_imkwgv7L-xDlVPDQw'
# video_id = 'WDG4X3jDSlA'
for video_id in video_ids:
    youtube_fetcher = YouTubeCommentsFetcher(api_key, video_id)
    all_comments = youtube_fetcher.get_fetch_comments()
    youtube_fetcher.dump(all_comments)


    