from pydub import (
    AudioSegment,
    playback,
)
from pytube import YouTube


def convert_mp4_to_mp3(stream, file_handle):
    "Callback for converting downloaded mp4 to mp3"

    filename = str(file_handle.name)
    print(filename)
    song = AudioSegment.from_file(filename, "mp4")
    song.export(f"./assets/sotd.mp3", format="mp3")
    # TODO remove mp4
    # How about here? Does something need to get returned?


def upload_to_assets(filename):
    pass


def convert_link_to_mp4(yt_link=None):
    "Given a YT link, downloads mp4 file in ./assets"

    if not yt_link:
        return "You need to specify a YouTube link."
    yt = YouTube(yt_link)
    yt.register_on_complete_callback(convert_mp4_to_mp3)
    stream = yt.streams.first()
    stream.download('./assets', 'sotd')
    # Do I return here? I continue to be confused by callbacks.
