from flask import Flask, render_template, request
import os
import sqlite3
import cv2

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

# =========================
# APP CONFIG
# =========================

app = Flask(__name__)

UPLOAD_FOLDER = "static/photos"
DB_FILE = "photo_ai.db"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# =========================
# AZURE CONFIG
# =========================

AZURE_KEY = "YOUR_AZURE_KEY"
AZURE_ENDPOINT = "YOUR_AZURE_ENDPOINT"

vision_client = ComputerVisionClient(
    AZURE_ENDPOINT,
    CognitiveServicesCredentials(AZURE_KEY)
)

# =========================
# DATABASE
# =========================

conn = sqlite3.connect(DB_FILE, check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS photos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    caption TEXT,
    objects TEXT,
    faces INTEGER
)
""")

conn.commit()

# =========================
# FACE DETECTOR
# =========================

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# =========================
# FUNCTIONS
# =========================

def detect_faces(path):

    img = cv2.imread(path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    return len(faces)


def analyze_image(path):

    with open(path, "rb") as image:

        analysis = vision_client.analyze_image_in_stream(
            image,
            visual_features=["Description", "Objects"]
        )

    caption = "No caption found"
    objects = []

    if analysis.description.captions:
        caption = analysis.description.captions[0].text

    if analysis.objects:
        for obj in analysis.objects:
            objects.append(obj.object_property)

    return caption, ", ".join(objects)


# =========================
# ROUTES
# =========================

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        file = request.files["photo"]

        if file:

            filename = file.filename

            save_path = os.path.join(UPLOAD_FOLDER, filename)

            file.save(save_path)

            caption, objects = analyze_image(save_path)

            faces = detect_faces(save_path)

            cur.execute(
                """
                INSERT INTO photos(filename, caption, objects, faces)
                VALUES(?,?,?,?)
                """,
                (filename, caption, objects, faces)
            )

            conn.commit()

    cur.execute("SELECT * FROM photos ORDER BY id DESC")

    photos = cur.fetchall()

    return render_template("index.html", photos=photos)


# =========================
# START APP
# =========================

if __name__ == "__main__":
    app.run(debug=True)