from app import app
from app.forms import SearchForm
from flask import redirect, render_template, url_for

@app.route('/', methods=['GET','POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
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