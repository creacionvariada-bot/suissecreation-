import webvtt
import re
import sys
import html

def clean_text(text):
    text = re.sub(r'<[^>]+>', '', text)
    text = html.unescape(text)
    return text.strip()

def process_vtt(file_path):
    vtt = webvtt.read(file_path)
    lines = []
    last_text = ""
    for caption in vtt:
        text = clean_text(caption.text)
        # Deduplicate rolling captions (simplified logic)
        # Often a caption contains the previous line and a new line.
        # We can just look at unique lines
        for line in text.split('\n'):
            line = line.strip()
            if line and line != last_text:
                lines.append(f"[{caption.start}] {line}")
                last_text = line

    with open('transcript_cleaned.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

if __name__ == "__main__":
    process_vtt(sys.argv[1])
