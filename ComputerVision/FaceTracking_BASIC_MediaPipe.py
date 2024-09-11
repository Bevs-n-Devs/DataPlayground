"""
Description : This file is intended as an entry to Computer Vision to demo
using Python to track faces in a live video feed. It uses the two most common 
python libraries - opencv & mediapipe. It is expected that users have at least python 3.8 
installed and the libraries described above.

This file uses Google's MediaPipe approach for face detection, specifically using
an already trained models+algorithms for detecting all faces any an image/video. 
For more info about mediapipe, checkout the following:

Author : Nerdboy_Q
Last Update : Sep 11, 2024
"""

import cv2
import mediapipe as mp
import time

# starts your sytem camera
cap = cv2.VideoCapture(0)

# using an initial time for calculating frame rate
pTime = 0

# utilities to help draw face data points
mpDraw = mp.solutions.drawing_utils

# mediapipe  face_detection solution
mpFaceDetection = mp.solutions.face_detection

# mediapipe face detection object
faceDetection = mpFaceDetection.FaceDetection()

# a while loop to constantly capture
# images from the camera
while True:
    # captures each frame from the video feed
    success, img = cap.read()
    
    # converts the camera images cv2 default BGR 
    # format (Blue, Green, Red) to RGB format
    # (Red, Green, Blue)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Run mediapipe algo to gather analyze the image/video for 
    # possible faces
    results = faceDetection.process(imgRGB)
    
    # check if any face have been detected
    if results.detections:
        # for each detected face, draw a bounding box around it
        for id, detection in enumerate(results.detections):
            # get the bounding box coordinates of the detected face 
            bboxC = detection.location_data.relative_bounding_box
            
            # get the shape of the image/video
            ih, iw, ic = img.shape

            # create a bounding box based the bounding box coordinates
            # in relation to the sive of the image/video frame
            bbox  = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                    int(bboxC.width * iw), int(bboxC.height * ih)
            
            # draw the bounding box around the detected face
            cv2.rectangle(img, bbox, (128,0,128), 2)

        # Display Text on video feed when face detected
        cv2.putText(img, f'Face Detected', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (128,0, 128), 3)
        
    # display the image with the annotations
    cv2.imshow("Image", img)

    # Typing in the 'q' key in the keyboard will
    # kill the live camera feed window
    if cv2.waitKey(1) == ord('q'):
        break