import cv2
import numpy as np
#load the xml files for face, eye and mouth detection into the program
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
#read the image for furthur editing
image = cv2.imread('333.jpg')
#show the original image
cv2.imshow('Original image', image)
cv2.waitKey(100)
#convert the RBG image to gray scale image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#identify the face using haar-based classifiers
faces = face_cascade.detectMultiScale(image, 1.4, 4)
#iteration through the faces array and draw a rectangle
for(x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
    roi_gray = gray_image[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    #identify the eyes and mouth using haar-based classifiers
eyes = eye_cascade.detectMultiScale(gray_image, 1.3, 5)
mouth = mouth_cascade.detectMultiScale(gray_image, 1.5, 11)

#iteration through the eyes and mouth array and draw a rectangl
for(ex, ey, ew, eh) in eyes:
    cv2.rectangle(image,(ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
for(mx, my, mw, mh) in mouth:
    cv2.rectangle(image, (mx, my), (mx+mw, my+mh), (255, 0, 0), 2)
#show the final image after detection
cv2.imshow('face, eyes and mouth detected image', image)
cv2.waitKey()
#show a successful message to the user
print("Face, eye and mouth detection is successful")
