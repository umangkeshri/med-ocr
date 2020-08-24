import os
import tempfile

from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)


ALLOWED_EXTENSIONS = set(["pdf"])


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/test")
def test():
    return "Your Flask app is running."


@app.route("/extract_tables", methods=["POST"])
def extract_tables():
    if "file" not in request.files:
        return jsonify({"message": "No file part in the request"}), 400
    doc = request.files["file"]
    if doc.filename == "":
        return jsonify({"message": "No file selected for uploading"}), 400
    if doc and allowed_file(doc.filename):
        filename = secure_filename(doc.filename)
        with tempfile.TemporaryDirectory() as tmpdirname:
            doc_path = os.path.join(tmpdirname, filename)
            image.save(doc_path)
            # tagged_img, label_cnt = count_trees(img_path)
            return jsonify({"tree_count": "done"}), 200
    else:
        return (
            jsonify({"message": "Allowed file types are png, jpg, jpeg"}),
            400,
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8360, debug=True)
