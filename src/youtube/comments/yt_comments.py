import json

from googleapiclient.discovery import build

class YTComments:
    def __init__(self, api_key, video_id):
        self.api_key = api_key
        self.video_id = video_id
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.ytcomments =  None

    def fetch_comments(self):
        comments = []
        nextPageToken = None
        processed_comments = set()

        while True:
            comment_threads = self._build_params(nextPageToken)

            for comment in comment_threads['items']:
                comment_id = comment['id']
                if comment_id in processed_comments:
                    continue

                comment_info = self._extract_comment_info(comment)
                comments.append(comment_info)
                processed_comments.add(comment_id)

                self._process_replies(comment, comments, processed_comments)

            nextPageToken = comment_threads.get('nextPageToken')
            if not nextPageToken:
                break
        self.ytcomments = comments 

        return comments

    def _build_params(self, page_token=None):
        return self.youtube.commentThreads().list(
            part='snippet',
            videoId=self.video_id,
            textFormat='plainText',
            pageToken=page_token
        ).execute()

    def _extract_comment_info(self, comment):
        snippet = comment['snippet']['topLevelComment']['snippet']
        author = snippet['authorDisplayName']
        author_channel_url = snippet['authorChannelUrl']
        content = snippet['textDisplay']
        published_at = snippet['publishedAt']
        updated_at = snippet['updatedAt']

        return {
            'author': author,
            'authorChannelUrl': author_channel_url,
            'content': content,
            'published_at': published_at,
            'updated_at': updated_at
        }

    def _process_replies(self, comment, comments, processed_comments):
        comment_id = comment['id']
        reply_comment_id = comment_id
        replies = self.youtube.comments().list(
            part='snippet',
            parentId=reply_comment_id,
            maxResults=100
        ).execute()

        for reply in replies['items']:
            reply_id = reply['id']
            if reply_id in processed_comments:
                continue

            reply_info = self._extract_reply_info(reply)
            comments.append(reply_info)
            processed_comments.add(reply_id)

    def _extract_reply_info(self, reply):
        reply_snippet = reply['snippet']
        reply_author = reply_snippet['authorDisplayName']
        reply_author_channel_url = reply_snippet['authorChannelUrl']
        reply_content = reply_snippet['textDisplay']
        reply_published_at = reply_snippet['publishedAt']
        reply_updated_at = reply_snippet['updatedAt']

        return {
            'author': reply_author,
            'authorChannelUrl': reply_author_channel_url,
            'content': reply_content,
            'published_at': reply_published_at,
            'updated_at': reply_updated_at
            
        }

    def dump(self):
        base_file = 'src/youtube/comments/'
        base_file += self.video_id + '.json'
        with open(base_file,'w',encoding='utf-8') as f:
            json.dump(self.ytcomments,f,indent=4)
        
        print('file dumped to', self.video_id,'have ', len(self.ytcomments), 'comments')

# if __name__ == "__main__":
#     # Replace with your own API key and video ID
#     api_key = 'AIzaSyBZnBVHK5L57k4cwbEVPN7GXMKHOlmnW3U'
#     video_id = '-FITFOdvQLw'

#     yt_comments = YTComments(api_key, video_id)
#     video_comments = yt_comments.fetch_comments()

    
    