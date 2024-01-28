from flask import Flask, request, render_template
import cv2
import numpy as np
import io
import base64
import os
import requests

app = Flask(__name__)

def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return image, len(faces)

def encode_image(image):
    _, buffer = cv2.imencode('.jpg', image)
    encoded_image = base64.b64encode(buffer).decode('utf-8')
    return encoded_image

@app.route('/', methods=['GET'])
def index():
    # Ładowanie i przetwarzanie przykładowego obrazu
    example_image_path = 'images/test.png'
    if os.path.exists(example_image_path):
        example_image = cv2.imread(example_image_path)
        processed_example_image, example_face_count = detect_faces(example_image.copy())
        original_encoded_example = encode_image(example_image)
        processed_encoded_example = encode_image(processed_example_image)
    else:
        original_encoded_example = processed_encoded_example = example_face_count = None

    return render_template('index.html',
                           original_example_image=original_encoded_example,
                           processed_example_image=processed_encoded_example,
                           example_face_count=example_face_count)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('index.html', error="Nie znaleziono pliku")

    file = request.files['file']
    in_memory_file = io.BytesIO()
    file.save(in_memory_file)
    data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
    image = cv2.imdecode(data, cv2.IMREAD_COLOR)

    processed_image, face_count = detect_faces(image.copy())
    original_encoded = encode_image(image)
    processed_encoded = encode_image(processed_image)

    return render_template('index.html',
                           original_image=original_encoded,
                           processed_image=processed_encoded,
                           face_count=face_count)


@app.route('/upload_url', methods=['POST'])
def upload_from_url():
    image_url = request.form['image_url']
    if not image_url:
        return render_template('index.html', error="Nie podano adresu URL")

    response = requests.get(image_url)
    if response.status_code == 200:
        in_memory_file = io.BytesIO(response.content)
        data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
        image = cv2.imdecode(data, cv2.IMREAD_COLOR)
        processed_image, face_count = detect_faces(image.copy())
        original_encoded = encode_image(image)
        processed_encoded = encode_image(processed_image)
    else:
        return render_template('index.html', error="Nie można pobrać obrazu z podanego URL")

    return render_template('index.html',
                           original_image=original_encoded,
                           processed_image=processed_encoded,
                           face_count=face_count)


if __name__ == '__main__':
    app.run(debug=True)
