from flask import render_template, flash, redirect, url_for
from app import app

@app.route("/")
@app.route("/index")
def index():
    return render_template("base.html")


@app.route("/bible_search")
def bible_search():
    return render_template("bible_search_form.html")