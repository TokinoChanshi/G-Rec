import speech_recognition as sr
import os
import argparse
from pydub import AudioSegment
import json
from pathlib import Path

def run_google_asr(audio_path, lang="zh-CN"):
    r = sr.Recognizer()
    
    # Check if we need to convert format
    audio_file = Path(audio_path)
    wav_path = str(audio_file.with_suffix(".wav"))
    
    if audio_file.suffix.lower() != ".wav":
        print(f"🔄 Converting {audio_file.name} to WAV...")
        try:
            sound = AudioSegment.from_file(str(audio_file))
            sound.export(wav_path, format="wav")
        except Exception as e:
            return {"status": "error", "message": f"FFmpeg/Pydub conversion failed: {e}"}
    else:
        wav_path = str(audio_file)

    try:
        with sr.AudioFile(wav_path) as source:
            print(f"🎤 uploading to Google Speech Recognition ({lang})...")
            audio_data = r.record(source)
            text = r.recognize_google(audio_data, language=lang)
            return {"status": "success", "text": text}
    except sr.UnknownValueError:
        return {"status": "error", "message": "Google Speech Recognition could not understand audio"}
    except sr.RequestError as e:
        return {"status": "error", "message": f"Could not request results from Google Service; {e}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        # Cleanup WAV if we made it
        if wav_path != str(audio_file) and os.path.exists(wav_path):
            os.remove(wav_path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--audio", required=True)
    parser.add_argument("--lang", default="zh-CN")
    args = parser.parse_args()
    
    res = run_google_asr(args.audio, args.lang)
    print(json.dumps(res, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()