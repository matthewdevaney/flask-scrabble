from app import db

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(64), index=True, unique=True)
    definition = db.Column(db.String(256))
    points = db.Column(db.Integer)
    length = db.Column(db.Integer)

    def __repr__(self):
        return f'<Word: {self.word}>'

    def __len__(self):
        return len(self.word)
    
    scrabble_tiles = {
        'a': {'points':  1, 'tiles':  9},
        'b': {'points':  3, 'tiles':  2},
        'c': {'points':  3, 'tiles':  2},
        'd': {'points':  2, 'tiles':  4},
        'e': {'points':  1, 'tiles': 12},
        'f': {'points':  4, 'tiles':  2},
        'g': {'points':  2, 'tiles':  3},
        'h': {'points':  4, 'tiles':  2},
        'i': {'points':  1, 'tiles':  9},
        'j': {'points':  8, 'tiles':  1},
        'k': {'points':  5, 'tiles':  1},
        'l': {'points':  1, 'tiles':  4},
        'm': {'points':  3, 'tiles':  2},
        'n': {'points':  1, 'tiles':  6},
        'o': {'points':  1, 'tiles':  8},
        'p': {'points':  3, 'tiles':  2},
        'q': {"points": 10, 'tiles':  1},
        'r': {'points':  1, 'tiles':  6},
        's': {'points':  1, 'tiles':  4},
        't': {'points':  1, 'tiles':  6},
        'u': {'points':  1, 'tiles':  4},
        'v': {'points':  4, 'tiles':  2},
        'w': {'points':  4, 'tiles':  2},
        'x': {'points':  8, 'tiles':  1},
        'y': {'points':  4, 'tiles':  2},
        'z': {"points": 10, 'tiles':  1},
        'blank': {'points': 0, 'tiles': 2}
}
    
    def calculate_points(self, word):
        """returns the points scored by playing a word"""

        word_points = 0

        for letter in word:
            word_points += self.scrabble_tiles[letter.lower()]['points']

        return word_points

    def valid_word_check(self, word):
        """returns true when word length is 2-15 characters and individual letters do not exceed quantity of scrabble tiles"""

        if len(word) < 2 or len(word) > 15:
            return False

        scrabble_tiles_remaining = {k:v['tiles'] for (k,v) in self.scrabble_tiles.items()}

        for letter in word:
            if scrabble_tiles_remaining[letter] == 0:
                return False
            scrabble_tiles_remaining[letter] -= 1

        return True