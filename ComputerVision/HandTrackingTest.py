"""
Description : This file is intended as an entry to Computer Vision to demo
using Python to track hands in a live video feed. It uses the two most common 
python libraries - opencv & mediapipe. It is expected that users have at least 
python 3.8 installed and the libraries described above.

Author : Nerdboy_Q
Last Update : Sep 4, 2024
"""

import cv2  # open-cv python library
import mediapipe as mp # Google Module for hand tracking
import time

# starts your sytem camera
cap = cv2.VideoCapture(0)

# w
mpHands = mp.solutions.hands
hands = mpHands.Hands()
# utilities to help draw hand data points
mpDraw = mp.solutions.drawing_utils

# a while loop to constantly capture
# images from the camera
while True:
    # captures each frame from the video feed
    success, img = cap.read()
    
    # converts the camera images cv2 default BGR 
    # format (Blue, Green, Red) to RGB format
    # (Red, Green, Blue
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Using the hands object to process the RGB format
    # of the camera's captured images
    results = hands.process(imgRGB)
    # test # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # draws the points on each given hand
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Image", img)

    # Typing in the 'q' key in the keyboard will
    # kill the live camera feed window
    if cv2.waitKey(1) == ord('q'):
        break
