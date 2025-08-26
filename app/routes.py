from flask import render_template, flash, redirect, url_for
from app import app, socketio
from app.forms import BibleSearchForm
from app.models import Bible

@app.route("/")
@app.route("/index")
def index():
    return render_template("base.html")


@app.route("/bible_search", methods=["GET", "POST"])
def bible_search():
    form = BibleSearchForm()
    if form.validate_on_submit():
        # Pull values from the form
        book_code = form.book_name.data
        chapter = form.chapter.data
        start_verse = form.start_verse.data
        end_verse = form.end_verse.data
        translations = form.translations.data
        # Build up SQL query
        query = (
            Bible.query
            .filter(Bible.book_code == book_code)
            .filter(Bible.chapter == chapter)
            .filter(Bible.verse >= start_verse, Bible.verse <= end_verse)
            .filter(Bible.translation.in_(translations))
            .order_by(Bible.translation, Bible.verse)
        )

        results = query.all()

        # Convert to list of dicts
        results_json = [result.to_dict() for result in results]
        print(f"results_json: \n{results_json}")
        socketio.emit("bible_search_results", {"bible_search_results": results_json})
        return render_template("bible_search_form.html", form=form) # redirect(url_for("index"))
    return render_template("bible_search_form.html", form=form)

@app.route("/display")
def display():
    return render_template("display.html")


@socketio.on("nav_clicked")
def handle_nav_link_clicked(data):
    print(f'The server has detected that the client has clicked one of the nav links: {data}')
    socketio.emit("layout_changed", {"layout": data['id']})