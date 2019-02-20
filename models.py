from app import db
from sqlalchemy.sql import func


class Song(db.Model):
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    asset_url = db.Column(db.String(), nullable=False)
    title = db.Column(db.String())
    artist = db.Column(db.String())
    video_url = db.Column(db.String(), nullable=False)
    date_added = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"Song {self.id}"
