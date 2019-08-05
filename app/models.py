from app import db

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(64), index=True, unique=True)
    definition = db.Column(db.String(256))
    points = db.Column(db.Integer)
    length = db.Column(db.Integer)

    def __repr__(self):
        return f'<Word: {self.word}>'
    
    def calculate_points(self, word):
        """returns the points scored by playing a word"""

        letter_points = {
            'a': 1,
            'b': 3,
            'c': 3,
            'd': 2,
            'e': 1,
            'f': 4,
            'g': 2,
            'h': 4,
            'i': 1,
            'j': 8,
            'k': 5,
            'l': 1,
            'm': 3,
            'n': 1,
            'o': 1,
            'p': 3,
            'q': 10,
            'r': 1,
            's': 1,
            't': 1,
            'u': 1,
            'v': 4,
            'w': 4,
            'x': 8,
            'y': 4,
            'z': 10
        }

        word_points = 0

        for letter in word:
            word_points += letter_points[letter.lower()]

        return word_points