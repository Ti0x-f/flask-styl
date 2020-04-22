#Import environment variables (SPOTIPY KEYS)
from dotenv import load_dotenv
load_dotenv()

from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello"
