from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

# the toolbar is only enabled in debug mode:
app.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'secret'

toolbar = DebugToolbarExtension(app)

@app.route("/")
def show_questions():
    """Show the prompts"""

    prompts = story.prompts

    return render_template("questions.html", prompts=prompts)

@app.route("/story")
def show_story():
    """Show story result"""

    text = story.generate(request.args)

    return render_template("story.html", text=text)
