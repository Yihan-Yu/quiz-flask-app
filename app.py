from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# Define submit_page() here
# Reminder: Don't forget the decorator before the "def" line



if __name__ == '__main__':
    app.run()