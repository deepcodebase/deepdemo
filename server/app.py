import io
import os
import re
from pathlib import Path

from flask import Flask, request, send_file, Response
from flask_cors import CORS
from flask_compress import Compress
from moviepy.editor import VideoFileClip
from PIL import Image

from .dataset.coin import COIN

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
Compress(app)
app.config.from_object(__name__)

VIDEO_ROOT = Path('/data/home/lanyanyan/hongxin/data/coin/annotations/videos')

# enable CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})


root = Path(__file__).parent
coin = COIN(
    root / 'dataset' / 'coin.json',
    root / 'dataset' / 'missing_videos.json')


@app.route("/api/list", methods=["GET"])
def get_list():
    res = {
        'videos': coin.keys
    }
    return res


@app.route("/api/video", methods=["GET"])
def get_random_video():
    res = {
        'data': coin.random_pick()
    }
    return res


@app.route("/api/video/<name>", methods=["GET"])
def get_video(name):
    res = {
        'data': coin.get(name)
    }
    return res


def get_full_path(name):
    if name in coin.keys:
        if name.endswith('.mp4'):
            name = name[:-4]
        video = coin.get(name)
        label = video['coin']['recipe_type']
        path = VIDEO_ROOT / str(label) / f'{name}.mp4'
        return path
    else:
        return None


@app.after_request
def after_request(response):
    response.headers.add('Accept-Ranges', 'bytes')
    return response


def get_chunk(full_path, byte1=None, byte2=None):
    file_size = os.stat(full_path).st_size
    start = 0

    if byte1 < file_size:
        start = byte1
    if byte2:
        length = byte2 + 1 - byte1
    else:
        length = file_size - start

    with open(full_path, 'rb') as f:
        f.seek(start)
        chunk = f.read(length)
    return chunk, start, length, file_size


@app.route('/api/video_src/<name>', methods=["GET"])
def get_file(name):
    range_header = request.headers.get('Range', None)
    byte1, byte2 = 0, None
    if range_header:
        match = re.search(r'(\d+)-(\d*)', range_header)
        groups = match.groups()

        if groups[0]:
            byte1 = int(groups[0])
        if groups[1]:
            byte2 = int(groups[1])
       
    full_path = get_full_path(name)
    chunk, start, length, file_size = get_chunk(full_path, byte1, byte2)
    resp = Response(chunk, 206, mimetype='video/mp4',
                      content_type='video/mp4', direct_passthrough=True)
    resp.headers.add(
        'Content-Range', 'bytes {0}-{1}/{2}'.format(
            start, start + length - 1, file_size))
    return resp


def numpy2fileobj(array):
    img = Image.fromarray(array)
    file_obj = io.BytesIO()
    img.save(file_obj, format="PNG")
    file_obj.seek(0)
    return file_obj


@app.route('/api/frame/<name>/<t>', methods=["GET"])
def get_frame(name, t):
    full_path = get_full_path(name)
    t = float(t)
    if full_path:
        video = VideoFileClip(str(full_path))
        if 0 <= t <= video.duration:
            frame_array = video.get_frame(t)
            frame = numpy2fileobj(frame_array)
            return send_file(frame, mimetype='image/PNG')
        else:
            return 'time is out of range'
    else:
        return 'video is not found'



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
