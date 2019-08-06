from app import db
from app.models import Word
import json

input_file = 'words.json'

with open(input_file, 'r') as f:
    scrabble_words = json.load(f)

for k, v in scrabble_words.items():
    w = Word(word=k, definition=v)
    w.points = w.calculate_points(w.word)
    w.length = len(w)
    db.session.add(w)
    db.session.commit()