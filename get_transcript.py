from youtube_transcript_api import YouTubeTranscriptApi
import sys

try:
    transcript = YouTubeTranscriptApi.get_transcript('37aUuoRyMhM', languages=['en'])
    with open('EP10_OVEREASY_FR/TRANSCRIPCION.txt', 'w') as f:
        for item in transcript:
            start = int(item['start'])
            mins = start // 60
            secs = start % 60
            text = item['text'].replace('\n', ' ')
            f.write(f"[{mins:02d}:{secs:02d}] {text}\n")
    print("Transcript saved.")
except Exception as e:
    print(f"Error: {e}")
