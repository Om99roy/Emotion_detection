from email.mime import image
from passlib.hash import sha256_crypt
import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash 
from flask import Response
import pickle
import cv2
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import time
# from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)


@app.route('/')
def index():
     return render_template('index.html')
    

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
    return render_template('register.html')

@app.route('/home', methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/about', methods=['GET','POST'])
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    return render_template('contact.html')

@app.route('/features', methods=['GET','POST'])
def features():
    return render_template('features.html')

@app.route('/privacy-policy', methods=['GET','POST'])
def privacypolicy():
    return render_template('privacy-policy.html')

@app.route('/terms-of-service', methods=['GET','POST'])
def termsofservice():
    return render_template('terms-of-service.html')

# @app.route('/video-feed')
# def videofeed():
#     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')



detected_emotion = "Neutral"

@app.route('/get_started', methods=['GET', 'POST'])
def get_started():
    global detected_emotion  # Reference the global variable
    classifier = load_model('./emotion_detection_model.h5')
    face_classifier = cv2.CascadeClassifier('./haarcascade/haarcascade_frontalface.xml')

    emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

    def generate_frames():
        global detected_emotion
        cap = cv2.VideoCapture(0)

        while True:
            success, frame = cap.read()
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
                        detected_emotion = label  # Update the global detected emotion
                        # print(detected_emotion,label)

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


@app.route('/camera_feed')
def camera_feed():
    return render_template('get_started.html')

# SSE Endpoint to send emotion label updates
# @app.route('/emotion_feed')
# def emotion_feed():
#     def generate_emotions():
#         global detected_emotion
#         print(detected_emotion)
#         while True:
#             time.sleep(1)  # Send the emotion every second
#             yield f"data: {detected_emotion}\n\n"  # SSE format
#     return Response(generate_emotions(), mimetype='text/event-stream')

@app.route('/detected_emotion', methods=['GET'])
def get_detected_emotion():
    global detected_emotion
    # print(detected_emotion)
    return jsonify({'emotion': detected_emotion})


   
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)