from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def main():
    return render_template("main.html")


app.run(port=8880, host='127.0.0.1')
