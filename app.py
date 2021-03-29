from datetime import datetime
from pathlib import Path

from flask import Flask, jsonify, request, render_template


BASE_DIR = Path(__file__).parent
TRAINING_DIR = BASE_DIR / "training"
DATA_DIR = BASE_DIR / "data"
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = str(DATA_DIR)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/api/new-sentence/", methods=["GET"])
def new_sentence():
    # TODO Need to make some nice sentences... with plenty of
    #  swear words but not too overboard, with additional request.GET
    #  to check if the user wants swear words in the first place.
    if "no_swearing" in request.args:
        return jsonify({"sentence": ""})
    return jsonify({"sentence": ""})


@app.route("/api/upload/", methods=["POST"])
def upload_new_audio_file():
    """
    This is an API view so that we can handle requests
    asynchronously, allowing the user to continue if the
    server may be a little slow.

    You might be wondering 'why not use the computer directly?'
    My only answer is: button. I don't necessarily want to use
    a VAD, but I also need a UI to be able to see the sentences
    I need to read. If anything, these WAV files are small so
    a bit of data transferring is nothing on your localhost.

    Also just learning Flask, so that's another excuse :P
    """
    file = request.files.get("file")
    if file:  # I wish I could have the walrus... :(
        file.save(DATA_DIR / datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f.wav"))
        # TODO Figure out format for saving files with their sentence...
    return jsonify(success=True)


# TODO Add browsing the files method that allows you to delete some media
#  which additionally deletes its record in our CSV file.


if __name__ == "__main__":
    app.run()
    TRAINING_DIR.mkdir(parents=True, exist_ok=True)
    # Where we'll store the prepared data for train/dev/test sets
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    (TRAINING_DIR / "sets").mkdir(parents=True, exist_ok=True)
