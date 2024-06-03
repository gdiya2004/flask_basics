from flask import Flask,render_template,Response
import cv2
app=Flask(__name__)
camera=cv2.VideoCapture(0)

def gen_Frames():
    while TRUE:
        success,frame=camera.read()
        if not success:
            break
        else: 
            # here 2 pre-trained cascadeclassifiers are loaded:one for detecting faces and other for detecting eyes
            #CascadeClassifier: ML based algorithm used for object detection
            #cascade means series of stages in algorithm, each of which progressively refines detection
            detector=cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
            eye_cascade = cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')
            #detectMultiScale: used to detect objects  of different sizes in input image
            #'frame':This is input image/frame in which algorithm will search for faces
            #1.1:scale factor . lower value will increse the chance of detecting small faces but will increase computational time
            #7: minimum no. of neighbour rectangles to be detected
            faces=detector.detectMultiScale(frame, 1.1,7)
            #cv2.Color:is used to concert fram eto grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       #Draw the rectangle around each face
            for (x, y, w, h) in faces:
             cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
             #roi_gray extracts region of interest from grayscale image gray
             roi_gray = gray[y:y+h, x:x+w]
             #This line extracts region of interest from color image 'frame'
             roi_color = frame[y:y+h, x:x+w]
             
             eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
             for (ex, ey, ew, eh) in eyes:
              cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        ret,buffer=cv2.imencode('.jpg',frame)
        frame=buffer.tobytes()
        yield(b'--frame\r\n'+b'Content-Type:image/jpeg\r\n\r\n'+frame+b'\r\n')

@app.route('/')
def index():
    return render_template('face_rec.html')

@app.route('/video_feed')
def video_feed():
    return Response(geb_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)
        