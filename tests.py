from app.models import Word
from app.models.word import valid_word_check
from app import db

print(valid_word_check('liker'))


w = Word(id=1, word='a')
w.points = w.calculate_points(w.word)
print(w, w.points)
word_valid = w.valid_word_check(w.word)
print(word_valid)