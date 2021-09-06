import ffmpeg

import time
import logging
from pprint import pprint
import os

logging.basicConfig(filename='./converter.log',
                    level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

MEDIA_CONTAINER = "mp4"
MEDIA_AUDIO_CODEC = "aac"
MEDIA_VIDEO_CODEC = "h264"
MEDIA_VIDEO_WIDTH = 720

MEDIA_PATH = os.environ.get("MEDIA_PATH") or "./media"
CONVERTER_PATH = os.path.join(MEDIA_PATH, "converter") or "./media/converter"
media_files = os.listdir(MEDIA_PATH)

folders = [file for file in os.listdir(MEDIA_PATH)
         if os.path.isdir(os.path.join(MEDIA_PATH, file))]

if not "converter" in folders:
    logging.info("Creating 'converter' folder...")
    os.mkdir(os.path.join(MEDIA_PATH, "converter"))

logging.info(f"""Starting converter with:
        Params: media: {MEDIA_CONTAINER}, acodec: {MEDIA_AUDIO_CODEC}, vcodec: {MEDIA_VIDEO_CODEC}, vwidth: {MEDIA_VIDEO_WIDTH}.
        Paths: converter: {CONVERTER_PATH}, media: {MEDIA_PATH}.""")
while True:
    files = [file for file in os.listdir(MEDIA_PATH)
             if os.path.isfile(os.path.join(MEDIA_PATH, file))]
    if not files:
        logging.info(f"No files to convert, trying search for new ones in {MEDIA_PATH}")
        time.sleep(300)
    for filename_tc in files:
        #filename_tc = files[0]
        logging.info(f"Converting file {filename_tc}...")
        filepath_tc = os.path.join(MEDIA_PATH, filename_tc)
        new_filepath_tc = os.path.join(CONVERTER_PATH, filename_tc)
        os.rename(filepath_tc, new_filepath_tc)
        logging.info(f"moving file location from {filepath_tc} to {new_filepath_tc}.")
        stream = ffmpeg.input(new_filepath_tc)
        stream = ffmpeg.filter(stream, "format", "yuv420p")
        stream = ffmpeg.filter(stream, "scale", "-1", str(MEDIA_VIDEO_WIDTH))
        stream = ffmpeg.output(stream,
                               f"{new_filepath_tc}.mp4",
                               vcodec="libx264",
                               acodec="aac")
        logging.info(f"args passing to ffmpeg cli: {stream.get_args()}")
        ffmpeg.run(stream)
        logging.info("file successfully converted.")
        logging.info(f"removing old file already converted {new_filepath_tc}.")
        os.remove(new_filepath_tc)
