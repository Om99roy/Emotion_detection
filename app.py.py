from flask import Flask, render_template, Response
import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array

app = Flask(__name__)

# Load the pre-trained models
classifier = load_model(r'C:\Users\ANKAN ROY\Desktop\Smart Perfume Dispenser\Flask\model\emotion_detection_model.h5')
face_classifier = cv2.CascadeClassifier(r'C:\Users\ANKAN ROY\Desktop\Smart Perfume Dispenser\Flask\haarcascade\haarcascade_frontalface.xml')

# Emotion labels
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

@app.route('/')
def index():
    # Render the main page (get_started2.html) at the default route
    return render_template('get_started2.html')

def generate_frames():
    camera = cv2.VideoCapture(0)  # Open webcam
    
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()
        if not success:
            break
        else:
            # Convert to grayscale for face detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)
            
            for (x, y, w, h) in faces:
                # Draw rectangle around the face
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
                
                # Extract region of interest (ROI)
                roi_gray = gray[y:y + h, x:x + w]
                roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
                
                if np.sum([roi_gray]) != 0:
                    # Preprocess the face for emotion prediction
                    roi = roi_gray.astype('float32') / 255.0
                    roi = img_to_array(roi)
                    roi = np.expand_dims(roi, axis=0)
                    
                    # Make prediction on the ROI
                    prediction = classifier.predict(roi)[0]
                    label = emotion_labels[prediction.argmax()]
                    
                    # Display the label on the frame
                    label_position = (x, y - 10)
                    cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                else:
                    cv2.putText(frame, 'No Face Detected', (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            # Encode frame to JPEG format
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Yield the frame for live streaming
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    camera.release()

@app.route('/video-feed')
def video_feed():
    # Return the live video feed
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
