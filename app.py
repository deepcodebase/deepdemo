from pathlib import Path

from flask import Flask, request, send_file
from flask_cors import CORS
from flask_compress import Compress

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
Compress(app)
app.config.from_object(__name__)

IMAGE_ROOT = 'image'

# enable CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route("/api/text", methods=["GET"])
def get_text():
    text = request.args.get("text")

    res = {
        "text": "I hear you, you say " + str(text)
    }
    return res


@app.route("/api/image", methods=["GET"])
def get_score():
    name = request.args.get("name")
    path = Path(IMAGE_ROOT) / name.split('/')[-1]
    if path.is_file():
        return send_file(path)
    else:
        return 'File not found.'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
