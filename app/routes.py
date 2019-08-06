from app import app
from app.forms import SearchForm
from app.models import Word
from flask import redirect, render_template, url_for

@app.route('/', methods=['GET','POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        scrabble_dictionary_words = Word.query.all()
        words_found = []

        for scrabble_word in scrabble_dictionary_words:
            check_letters = list(form.letters.data)
            
            for letter in scrabble_word.word:
                if letter in check_letters:
                    check_letters.remove(letter)
                else:
                    break
                
                if len(scrabble_word.word) == len(list(form.letters.data)) - len(check_letters): 
                    words_found.append(scrabble_word.word)
                    break

        print(words_found)        

        return redirect(url_for('search_results'))
    return render_template('search.html', form=form)


@app.route('/search_results')
def search_results():
    return render_template('search_results.html')


@app.errorhandler(404)
def error_page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_internal_sever(error):
    return render_template('500.html'), 500