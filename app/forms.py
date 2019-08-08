from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp

class SearchForm(FlaskForm):
    letters = StringField('Your Letters', 
                            validators=[Length(min=2, max=15, message='must be between 2-15 letters')], #Regexp('[a-zA-Z]+', message='must only contain letters')
                            render_kw={
                            'id': 'nav-search-bar',
                            'class': 'form-control',
                            'placeholder': 'Your Letters',
                            'size': '125'
                            })

    submit = SubmitField('Search',
                            render_kw={
                            'id': 'nav-search-btn',
                            'class': 'btn btn-outline-secondary'
                            })