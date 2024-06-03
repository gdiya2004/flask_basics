#response is for creating HTTP responses
from flask import Flask,render_template,Response
import cv2

app=Flask(__name__)
camera=cv2.VideoCapture(0) # 0 means it will capture video from default camera

def generate_frames():#cont capture frames from webcam using camera.read()
    while True:
     #success is boolean parameter. if it is true we are able to read it from camera
     success,frame=camera.read() ##returns 2 parameter:any type of framework
     if not success:
        break
     else: 
        #encode each frame into jpeg format and yield it as bytes 
        ret,buffer=cv2.imencode('.jpg',frame)##ret:boolean, buffer:encoded image data
        frame=buffer.tobytes()##buffer is converted to bytes now frame is containing jpeg image data as bytes
     #byte string: 
     # b'--frame\r\n':boundary marker indicating start of frame
     #b'Content-Type..':indicates content type of file i.e. jpeg
     #frame:frame in form byte string
     #b'\r\n':new line character indicating end of frame
     yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('webcam.html')

@app.route('/video')
def video():
    #mimetype:std way of indicating  nauture and format of document
    #multipart: content consists of multiple parts where each part can be of different type
    #x-mixed-replace: content is being replaced over time,with each part replacing the previous one.abs
    #used in streaming scenarios  where new content replaces old content dynamically without reloading the entire document
    #boundary =frame : specifies boundary marker that separates each part within multipart content
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
  app.run(debug=True)