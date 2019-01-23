import csv
from app import db, Song


with open('kpop_songs.csv') as csvfile:
    reader = csv.reader(csvfile)
    counter = 0
    for song_url, title, artist, korean_artist, video_url in reader:
        one_song = Song(
            asset_url=song_url,
            title=title,
            artist=artist,
            korean_artist=korean_artist,
            video_url=video_url,
        )
        db.session.add(one_song)
        counter += 1
db.session.commit()
print(f"Added {counter} rows to the db")
