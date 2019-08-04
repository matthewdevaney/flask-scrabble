from app import db

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(64), index=True, unique=True)
    definition = db.Column(db.String(256))
    points = db.Column(db.Integer)
    length = db.Column(db.Integer)

    def __repr__(self):
        return f'<Word: {self.word}>'