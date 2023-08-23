from youtube_transcript_api import YouTubeTranscriptApi
import sys

videoId = sys.argv[1]
transcript = YouTubeTranscriptApi.get_transcript(videoId)
# join transcript text
transcript = ' '.join([i['text'] for i in transcript])
print(transcript)