import face_recognition
import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)
#load sample image and learn how to recognize
diya_image=face_recognition.load_image_file(".jpg")
diya_face_encoding=face_recognition.face_encodings(diya_image)[0]

#load sample image and learn how to recognize
namu_image=face_recognition.load_image_file(".jpg")
namu_face_encoding=face_recognition.face_encodings(namu_image)[0]

#creating arrays of known face encodings and their names
known_face_encodings={
    diya_face_encoding,
    namu_face_encoding
}
known_face_names={
    "Diya",
    "Namish"
}

face_locations={}
face_encodings={}
face_names={}
process_this_frame=True