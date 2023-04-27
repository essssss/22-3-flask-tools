from flask import Flask, request, render_template, redirect, flash, jsonify
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# the toolbar is only enabled in debug mode:
app.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = '<replace with a secret key>'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


MOVIES = {'Amadeus', 'Chicken Run', 'Dances With Wolves'}

@app.route("/")
def home_page():
    """Home page! Nothing good!!"""
    return render_template("hello.html")

@app.route("/old-home-page")
def redirect_to_home():
    """redirects to home page"""
    flash('That page has moved! This is our new page!')
    return redirect("/")

@app.route('/movies')
def show_all_movies():
    """Show list of all movies in DB"""
    return render_template('movies.html', movies=MOVIES)

@app.route("/movies/json")
def get_movies_json():
    json_obj = jsonify(list(MOVIES))
    raise
    return json_obj

@app.route('/movies/new', methods =["POST"])
def add_movie():
    title = request.form['title']
    # Add to Pretend DB
    if title in MOVIES:
        flash("Your movie is already in our database!", "error")
    else:
        MOVIES.add(title)
        flash("Movie Added!", "success")
    # import pdb
    # pdb.set_trace()
    return redirect("/movies")