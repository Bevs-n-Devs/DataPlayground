"""
Description : This file is intended as an entry to Computer Vision to demo
using Python to track faces in a live video feed. It uses the two most common 
python libraries - opencv. It is expected that users have at least python 3.8 
installed and the libraries described above.

This file uses the HAAR-Cascades approach for face detection, specifically using
an already trained model for detecting the front of a face. There are much more 
models available in the following repository:
https://github.com/opencv/opencv/tree/master/data/haarcascades

Author : Nerdboy_Q
Last Update : Sep 11, 2024
"""

import cv2  # open-cv python library

# Using the Cascade Classifier with the trainined model file name
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# starts your sytem camera
cap = cv2.VideoCapture(0)

# a while loop to constantly capture
# images from the camera
while True:
    # captures each frame from the video feed
    success, img = cap.read()

    # HAAR-Cascades algorithm processes gray scale images only
    # so we convert the image format from BGR to Gray
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Using cascades we attempt to detect the faces
    # NOTE: we're running detection on the GRAY image
    faces = face_cascade.detectMultiScale(gray_img, 1.1, 4)

    # if faces are found, we can draw a rectangle around them
    # for good visual representation
    # NOTE: We get the face position from the gray scale image
    # but we're now drawing on the default BGR image as that
    # is what is seen in the live feed; converting the format
    # does not change the coordinates of the faces found.
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,255), 2)

    # we show the image with the rectangles in the live feed
    cv2.imshow("Image", img)

    # Typing in the 'q' key in the keyboard will
    # kill the live camera feed window
    if cv2.waitKey(1) == ord('q'):
        break
