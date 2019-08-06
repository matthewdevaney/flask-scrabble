from app import app
from app.forms import SearchForm
from app.models import Word
from flask import redirect, render_template, request, url_for

@app.route('/', methods=['GET','POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('search_results', letters=form.letters.data))
    return render_template('search.html', form=form)


@app.route('/search_results')
def search_results():

    # retrieve all words from the database 
    scrabble_dictionary_words = Word.query.all()

    words_found = []

    # check if each word can be constructed from users tiles
    for scrabble_word in scrabble_dictionary_words:
        check_letters = list(request.args['letters'])
        
        for letter in scrabble_word.word:

            if letter.lower() in check_letters:
                check_letters.remove(letter.lower())
            else:
                break
            
            # add the word to results set if length of word is equal to tiles used 
            count_tiles_used = len(list(request.args['letters'])) - len(check_letters)

            if len(scrabble_word.word) == count_tiles_used: 
                words_found.append(scrabble_word)
                break      
    
    # sort the results by points from greatest to least
    words_found.sort(key=lambda w: w.points, reverse=True)

    return render_template('search_results.html', results=words_found)


@app.errorhandler(404)
def error_page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_internal_sever(error):
    return render_template('500.html'), 500