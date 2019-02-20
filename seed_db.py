import csv
from app import db, Song


with open('kpop_songs.csv') as csvfile:
    reader = csv.reader(csvfile)
    counter = 0
    for song_url, title, artist, video_url in reader:
        exists = db.session.query(db.exists().where(Song.title == title)).scalar()
        if exists:
            print(f"{title} already exists in db")
            continue
        else:
            one_song = Song(
                asset_url=song_url,
                title=title,
                artist=artist,
                video_url=video_url,
            )
            db.session.add(one_song)
            counter += 1
db.session.commit()
print(f"Added {counter} rows to the db")
