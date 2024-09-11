"""
Description : This file is intended as an entry to Computer Vision to demo
using Python to track faces in a live video feed & drawing a 'mesh' of all
key points to detect face expressions, gestures, moods, etc. It uses the 
two most common python libraries - opencv & mediapipe. It is expected that 
users have at least python 3.8 installed and the libraries described above.

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

# using the drawing style to customize how the
# detected face mesh is displayed
mp_drawing_styles = mp.solutions.drawing_styles
# Here is where the custom style is implemented
drawSpec = mpDraw.DrawingSpec(color=mp_drawing_styles._GREEN,thickness=1, circle_radius=2)

# MediaPipe face mesh solution
mpFaceMesh = mp.solutions.face_mesh

# MediaPipe face mesh object
faceMesh = mpFaceMesh.FaceMesh(refine_landmarks=True)

# a while loop to constantly capture
# images from the camera
while True:
    # captures each frame from the video feed
    success, img = cap.read()
    
    # converts the camera images cv2 default BGR 
    # format (Blue, Green, Red) to RGB format
    # (Red, Green, Blue
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Run mediapipe algo to gather analyze the image/video for 
    # possible faces and their mesh points
    results = faceMesh.process(imgRGB)
    
    # Check to see if a face has been detected
    if results.multi_face_landmarks:
        # loop through all found faces, collect all all 
        # of their landmarks (the mesh points)
        for faceLmks in results.multi_face_landmarks:
            # draw the mesh with the custom styling
            mpDraw.draw_landmarks(img, faceLmks, mpFaceMesh.FACEMESH_CONTOURS,drawSpec)
            # mpDraw.draw_landmarks(img, faceLmks, mpFaceMesh.FACEMESH_TESSELATION)

        # print 'Face Detected' to the video stream when a face is seen
        cv2.putText(img, f'Face Detected!', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                    3, (0,255, 0), 3)
    
    # show the annotated video stream
    cv2.imshow("Image", img)

    # Typing in the 'q' key in the keyboard will
    # kill the live camera feed window
    if cv2.waitKey(1) == ord('q'):
        break