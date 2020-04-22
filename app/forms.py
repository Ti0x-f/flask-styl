from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    search = StringField("The Song That You Love", validators = [DataRequired()])
    submit = SubmitField("Get recommendations")
