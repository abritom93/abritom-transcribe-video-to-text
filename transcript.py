import logging
import pytube
import whisper
import sys
import argparse

parser = argparse.ArgumentParser(description='Transcript a YouTube video using Whisper')

parser.add_argument("--video", help = "Pass the YouTube url to transcribe")
parser.add_argument("--model", help = "Indicate the Whisper model to download", default="small")
args = parser.parse_args()

logging.basicConfig(
  level=logging.INFO,
  format="%(asctime)s [%(levelname)s] %(message)s",
  handlers=[
    logging.StreamHandler(sys.stdout)
  ]
)

if not args.video:
  logging.error("Please pass a YouTube url to transcribe")
  exit()

logging.info("Downloading Whisper model")
model = whisper.load_model(args.model)

logging.info("Downloading the video from YouTube...")
youtubeVideo = pytube.YouTube(args.video)

logging.info("Get only the audio from the video")
audio = youtubeVideo.streams.get_audio_only()
audio.download(filename='tmp.mp4')

logging.info("Transcribe the audio")
result = model.transcribe('tmp.mp4',fp16=False,language='Spanish')

print(result["text"])