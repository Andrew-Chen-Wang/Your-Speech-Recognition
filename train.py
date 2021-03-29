"""
This is the main file for training. To quickly execute this training, though,
use the shell file train.sh
"""
import argparse
import json
from io import BytesIO
from pathlib import Path
from shutil import unpack_archive
from zipfile import ZipFile

import requests


BASE_DIR = Path(__file__).parent
DEFAULT_DEEPSPEECH_VERSION = "0.9.3"


def setup_deepspeech(version):
    deepspeech_path = BASE_DIR / "DeepSpeech"
    if not deepspeech_path.is_dir():
        r = requests.get(
            f"https://github.com/mozilla/DeepSpeech/archive/refs/tags/v{version}.zip",
        )
        with ZipFile(BytesIO(r.content)) as z:
            z.extractall(BASE_DIR)
        Path(f"{deepspeech_path}-{version}").rename(deepspeech_path)

    # Download checkpoints
    checkpoints_dir = deepspeech_path / f"fine_tuning_checkpoints"
    if not checkpoints_dir.is_dir():
        _checkpoint_file = deepspeech_path / f"deepspeech-{version}-checkpoint.tar.gz"
        if not _checkpoint_file.is_file():
            # First we have to get the release data to get the asset URL
            r = requests.get(
                "https://api.github.com/repos/mozilla/DeepSpeech/"
                f"releases/tags/v{version}"
            )
            data = json.loads(r.text)
            asset_url = None
            for _f in data["assets"]:
                if _f.get("name") == str(_checkpoint_file):
                    asset_url = _f.get("url")
                    break
            if asset_url is None:
                raise LookupError(
                    "We couldn't find the checkpoint file for this version. "
                    f"Try another version like {DEFAULT_DEEPSPEECH_VERSION}."
                )
            r = requests.get(
                asset_url, stream=True, headers={"Accept": "application/octet-stream"}
            )
            with open(str(_checkpoint_file), "wb") as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)
        unpack_archive(str(_checkpoint_file), deepspeech_path)
        Path(str(_checkpoint_file).replace(".tar.gz", "")).rename(checkpoints_dir)

    (BASE_DIR / "output_models").mkdir(parents=True, exist_ok=True)


def check_training_is_done():
    assert (BASE_DIR / "training").is_dir(), (
        "You should first train your speech using `python app.py` and follow "
        "the website's directions. The website url is http://localhost:5000."
    )


def main():
    parser = argparse.ArgumentParser(description="Setup Training and Trains your data")
    parser.add_argument(
        "-v",
        "--deepspeech_version",
        type=str,
        default=DEFAULT_DEEPSPEECH_VERSION,
        help="Sets the version of DeepSpeech you'd like to use."
        f"Default: {DEFAULT_DEEPSPEECH_VERSION}",
    )
    parser.add_argument(
        "--ignore-training-check",
        action="store_true",
        default=False,
        help="Ignores validation check that the training directory is "
        "filled out using the website.",
    )
    args = vars(parser.parse_args())

    if not args.get("ignore-training-check"):
        try:
            check_training_is_done()
        except AssertionError as e:
            print(e)
            quit(1)
    setup_deepspeech(args["deepspeech_version"])


if __name__ == "__main__":
    main()
