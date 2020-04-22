#Import environment variables (SPOTIPY KEYS)
from dotenv import load_dotenv
load_dotenv()

from flask import render_template, json, url_for

from app.recommendations import get_recommendations, get_covers, display
from app.forms import SearchForm
from app import app


@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():

    form = SearchForm()

    if form.validate_on_submit():

        recommendations = get_recommendations(form.search.data)
        covers = get_covers(recommendations)
        html_code = display(recommendations, covers)


        return render_template('index.html', title = 'STYL - Recommendations based on that one song you love', \
            form = form, html_code = html_code)

    return render_template('index.html', title = 'STYL - Recommendations based on that one song you love', form = form)
