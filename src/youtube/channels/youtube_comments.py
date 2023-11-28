import requests
import json

class YouTubeCommentsFetcher:
    def __init__(self, api_key, video_id):
        self.api_key = api_key
        self.video_id = video_id
        self.base_url = "https://www.googleapis.com/youtube/v3/"

    def get_params(self, page_token=None):
        return {
            'part': 'snippet',
            'videoId': self.video_id,
            'key': self.api_key,
            'pageToken': page_token,
            'maxResults': 100
        }

    def get_fetch_comments(self):
        comments = []
        next_page_token = None

        while True:
            params = self.get_params(next_page_token)

            response = requests.get(f"{self.base_url}commentThreads", params=params)
            data = json.loads(response.text)
            item_data = data['items']

            for item in item_data:
                topLevelComment = item['snippet']['topLevelComment']
                
                etag  = topLevelComment['etag']
                author = topLevelComment['snippet']['authorDisplayName']
                author_channel_url = topLevelComment['snippet']['authorChannelUrl']
                content = topLevelComment['snippet']['textDisplay']
                published_at = topLevelComment['snippet']['publishedAt']
                updated_at = topLevelComment['snippet']['updatedAt']

                
                comments.append({'etag': etag,
                                'author': author,
                                'authorChannelUrl': author_channel_url,
                                'content': content,
                                'published_at': published_at,
                                'updated_at': updated_at
                                })

                reply_count = item['snippet']['totalReplyCount']

                if reply_count > 0:
                    parent_id = item['id']
                    replies = self.get_comment_replies(parent_id)
                    comments.append(replies)

            next_page_token = data.get('nextPageToken')

            if not next_page_token:
                break

        return comments
    

    def get_comment_replies(self, parent_id):
        replies = []
        next_page_token = None

        while True:
            params = self.get_params(next_page_token)
            response = requests.get(f"{self.base_url}comments?parentId={parent_id}", params=params)
            data = json.loads(response.text)

            item_data = data.get('items')
            for item in item_data:
                try:
                    etag = item['etag']
                    author = item['snippet']['authorDisplayName']
                    author_channel_url = item['snippet']['authorChannelUrl']
                    content = item['snippet']['textDisplay']
                    published_at = item['snippet']['publishedAt']
                    updated_at = item['snippet']['updatedAt']

                    replies.append({'author': author,
                                    'authorChannelUrl': author_channel_url,
                                    'content': content,
                                    'published_at': published_at,
                                    'updated_at': updated_at
                                 })
                    

                except KeyError as e:
                    print('Error! Could not extract data from item:\n', item)

            next_page_token = data.get('nextPageToken')
            if not next_page_token:
                break  
        
        return replies

    def dump(self, data):
        base_file = 'src/youtube/data/'
        base_file += self.video_id + '.json'
        with open(base_file,'w',encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        print('file dumped')

api_key = 'AIzaSyB6Qhlr3A0YReR5f_imkwgv7L-xDlVPDQw'
video_id = '39TQUbn3e_Q'

youtube_fetcher = YouTubeCommentsFetcher(api_key, video_id)
all_comments = youtube_fetcher.get_fetch_comments()
youtube_fetcher.dump(all_comments)