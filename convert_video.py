from argparse import ArgumentParser
import os
import re

from pydub import (
    AudioSegment,
    playback,
)
from pytube import YouTube


def _convert_mp4_to_mp3(stream, file_handle):
    "Callback for converting downloaded mp4 to mp3"

    mp4_filepath = str(file_handle.name)
    song = AudioSegment.from_file(mp4_filepath, "mp4")
    filename = re.split("[/\/.]", mp4_filepath)[3]
    song.export(f"./assets/{filename}.mp3", format="mp3")
    # Clean up mp4 file
    os.remove(mp4_filepath)
    # How about here? Does something need to get returned?


def upload_to_assets(filename):
    pass


def convert_link(yt_link=None, asset_name='sotd'):
    "Given a YT link, downloads mp4 file in ./assets"

    if not yt_link:
        return "You need to specify a YouTube link."
    yt = YouTube(yt_link)
    yt.register_on_complete_callback(_convert_mp4_to_mp3)
    stream = yt.streams.first()
    stream.download('./assets', asset_name)
    # Do I return here? I continue to be confused by callbacks.

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        '--link',
        type=str,
        dest='link',
        default='',
        action='store',
        required=True,
        help="Address of YouTube video from which to extract audio",
    )

    parser.add_argument(
        '--asset',
        type=str,
        dest='asset_name',
        default='',
        action='store',
        required=False,
        help="Name of asset file [artist_song_title]",
    )

    args = parser.parse_args()

    convert_link(yt_link=args.link, asset_name=args.asset_name)
