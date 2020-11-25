"""
API: /api/score?t1=<text1>&t2=<text2>
Example: http://10.61.2.216:9000/api/score?t1=hello%20world&t2=ni%20hao
"""
from flask import Flask, request, send_file
from flask_cors import CORS
from flask_compress import Compress
import numpy as np

# import custom module here, example:
# import module
# print(module.x)


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
Compress(app)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route("/api/score", methods=["GET"])
def get_score():
    text1 = request.args.get("t1")
    text2 = request.args.get("t2")

    res = {
        "score": "",
        "error": "",
        "attention": [[], []],
        "text1": text1,
        "text2": text2,
    }

    # code to generate score
    # ...
    res["score"] = 0.0

    return res


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
