from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def main():
    return render_template("main.html")


app.run("0.0.0.0", 5000)
