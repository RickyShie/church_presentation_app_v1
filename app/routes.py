from flask import render_template, flash, redirect, url_for
from app import app, socketio
from app.forms import BibleSearchForm

@app.route("/")
@app.route("/index")
def index():
    return render_template("base.html")


@app.route("/bible_search", methods=["GET", "POST"])
def bible_search():
    form = BibleSearchForm()
    if form.validate_on_submit():
        return render_template("bible_search_form.html", form=form) # redirect(url_for("index"))
    return render_template("bible_search_form.html", form=form)

@app.route("/display")
def display():
    return render_template("display.html")


@socketio.on("nav_clicked")
def handle_nav_link_clicked(data):
    print(f'The server has detected that the client has clicked one of the nav links: {data}')
    socketio.emit("layout_changed", {"layout": data['id']})