from youtube_transcript_api import YouTubeTranscriptApi

json = YouTubeTranscriptApi.get_transcript("iclLPntjocg")

for line in json:
    print(line['start'], ":", line['text'])