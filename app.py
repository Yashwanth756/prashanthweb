from datetime import datetime
import os

from flask import Flask, render_template


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-key")


@app.route("/")
def home() -> str:
    return render_template("index.html", year=datetime.now().year)


@app.route("/about")
def about() -> str:
    return render_template("about.html", year=datetime.now().year)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8000")), debug=True)
