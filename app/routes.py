from app import app
from app.forms import SearchForm
from app.models import Word
from flask import redirect, render_template, request, url_for

@app.route('/', methods=['GET','POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('search_results', letters=form.letters.data))
    return render_template('index.html', form=form)

@app.route('/search_results', methods=['GET','POST'])
def search_results():
    form = SearchForm()

    search_letters = request.args.get('letters', default=[])
    words_found = []

    # if form.validate_on_submit():
    if search_letters:
    
        # retrieve all words from the database 
        scrabble_dictionary_words = Word.query.all()

        # check if each word can be constructed from users tiles
        for scrabble_word in scrabble_dictionary_words:
            check_letters = list(search_letters)
            
            for letter in scrabble_word.word:

                if letter.lower() in check_letters:
                    check_letters.remove(letter.lower())
                else:
                    break
                
                # add the word to results set if length of word is equal to tiles used 
                count_tiles_used = len(list(search_letters)) - len(check_letters)

                if len(scrabble_word.word) == count_tiles_used: 
                    words_found.append(scrabble_word)
                    break      
        
        # sort the results by points from greatest to least
        words_found.sort(key=lambda w: w.points, reverse=True)

    return render_template('search_results.html', results=words_found, form=form)

@app.errorhandler(404)
def error_page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_internal_sever(error):
    return render_template('500.html'), 500