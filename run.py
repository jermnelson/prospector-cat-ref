__author__ = "Jeremy Nelson"

from flask import Flask, render_template
from flask_flatpages import FlatPages

app = Flask(__name__)
app.config["FLATPAGES_EXTENSION"] = ".md"
pages = FlatPages(app)

@app.route("/")
def home():
    return render_template("prospector-cat-ref/index.html", pages=pages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8224, debug=True)
