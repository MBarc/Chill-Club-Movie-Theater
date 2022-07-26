"""

Description: This script will be ran via cron job every Friday, Saturday, and Sunday at 9:55pm.

Crontab time -> 55 17 * * 5,6,7
"""
import subprocess
from datetime import datetime

def stream_movie(streamFile):
    """
    Runs the ffmpeg command to stream the movie.
    streamFile (str): absolute path to the file to stream.
    """

    # FFmpeg command to stream the movie via RTMP
    subprocess.call([f"/usr/bin/ffmpeg -re -i {streamFile} -c:v copy -c:a aac -ar 44100 -ac 1 -f flv rtmp://localhost/live/stream"])

# Getting the current day
currentDay = datetime.utcnow().isoweekday()

# Directory where the movies to stream are stored
movieDir = "/scripts/movieCompiler/temp"

# If today is Friday
if currentDay == 5:

    streamFile = f"{movieDir}/friday.mp4"

# If today is Saturday
if currentDay == 6:

    streamFile = f"{movieDir}/satruday.mp4"

# If today is Sunday
if currentDay == 7:

    streamFile = f"{movieDir}/sunday.mp4"

# Actually streaming the movie
stream_movie(streamFile)
