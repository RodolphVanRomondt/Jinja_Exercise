from stories import Story, story_list
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "YaLa123"

debug = DebugToolbarExtension(app)

@app.route("/")
def home_route():
    """ Return homepage (to pick a story). """
    return render_template("home.html")


@app.route("/form")
def form_route():
    select = request.args["num"]
    words = story_list[select][0]
    global story
    story = Story(story_list[select][0], story_list[select][1])

    return render_template("form.html", words=words)


@app.route("/story")
def story_route():

    msg_dict = {}

    for k, v in request.args.items():
        msg_dict[k] = v
    
    msg = story.generate(msg_dict)

    return render_template("story.html", msg=msg)