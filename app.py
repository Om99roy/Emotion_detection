from email.mime import image
from passlib.hash import sha256_crypt
import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash 
from flask import Response
import pickle
import cv2
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login.html', methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/register.html', methods=['GET','POST'])
def register():
    return render_template('register.html')

@app.route('/home.html', methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/about.html', methods=['GET','POST'])
def about():
    return render_template('about.html')

@app.route('/contact.html', methods=['GET','POST'])
def contact():
    return render_template('contact.html')

@app.route('/features.html', methods=['GET','POST'])
def features():
    return render_template('features.html')

@app.route('/video-feed')
def videofeed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')




@app.route('/get_started.html', methods=['GET', 'POST'])
def get_started():
    classifier = load_model(r'C:\Users\ANKAN ROY\Desktop\Smart Perfume Dispenser\Flask\model\emotion_detection_model.h5')
    face_classifier = cv2.CascadeClassifier(r'C:\Users\ANKAN ROY\Desktop\Smart Perfume Dispenser\Flask\haarcascade\haarcascade_frontalface.xml')

    # Define emotion labels
    emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

    def generate_frames():
        cap = cv2.VideoCapture(0)

        while True:
            success, frame = cap.read()  # Capture frame-by-frame
            if not success:
                break
            else:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray)

                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
                    roi_gray = gray[y:y+h, x:x+w]
                    roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

                    if np.sum([roi_gray]) != 0:
                        roi = roi_gray.astype('float32') / 255.0
                        roi = img_to_array(roi)
                        roi = np.expand_dims(roi, axis=0)

                        prediction = classifier.predict(roi)[0]
                        label = emotion_labels[prediction.argmax()]
                        label_position = (x, y-10)

                        cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    else:
                        cv2.putText(frame, 'No Faces Detected', (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()

                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        cap.release()

    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


   
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)