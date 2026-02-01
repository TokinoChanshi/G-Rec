import json
import requests
import sys

# Force UTF-8 for output
sys.stdout.reconfigure(encoding='utf-8')

def google_translate(text, target="en"):
    url = "https://translate.googleapis.com/translate_a/single"
    params = {"client": "gtx", "sl": "auto", "tl": target, "dt": "t", "q": text}
    try:
        r = requests.get(url, params=params, timeout=5)
        if r.status_code == 200: return r.json()[0][0][0]
    except Exception as e:
        pass
    return text

import re

try:
    # Read clean JSON
    with open('segments.json', 'r', encoding='utf-8') as f:
        segments = json.load(f)

    print(f"Translating {len(segments)} segments...")
    
    for i, seg in enumerate(segments):
        trans = google_translate(seg['text'])
        # print(f"[{i}] {trans}")
        seg['text'] = trans

    with open('segments_en.json', 'w', encoding='utf-8') as f:
        json.dump(segments, f, indent=2, ensure_ascii=False)
    print("Translation done.")

except Exception as e:
    print(f"Error: {e}")
