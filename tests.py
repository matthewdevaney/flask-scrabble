from app.models import Word
from app import db


w = Word(id=1, word='a')
w.points = w.calculate_points(w.word)
print(w, w.points)
word_valid = w.valid_word_check(w.word)
print(word_valid)