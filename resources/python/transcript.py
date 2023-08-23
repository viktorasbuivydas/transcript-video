from youtube_transcript_api import YouTubeTranscriptApi

transcript = YouTubeTranscriptApi.get_transcript('5cOwh-8scu8')
# join transcript text
transcript = ' '.join([i['text'] for i in transcript])
print(transcript)