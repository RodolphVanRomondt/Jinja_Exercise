from flask import Flask, request, render_template

app = Flask(__name__)

@add.route("/home")
def home():
    return "WELCOME"