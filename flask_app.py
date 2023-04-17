import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/dog")
def dog():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()
    image_url = data["message"]
    return render_template("index.html", img=image_url)


if __name__ == "__main__":
    app.run()
