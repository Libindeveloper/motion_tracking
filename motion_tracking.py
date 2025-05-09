import cv2
import numpy as np
import streamlit as st

# Streamlit UI
st.title("Motion Tracking in Drone Video using FAST and ORB")
video_file = st.file_uploader("Upload a drone video", type=['mp4', 'avi'])

if video_file:
    tfile = open("temp_video.mp4", 'wb')
    tfile.write(video_file.read())
    cap = cv2.VideoCapture("temp_video.mp4")

    stframe = st.empty()

    orb = cv2.ORB_create()
    fast = cv2.FastFeatureDetector_create()

    ret, prev_frame = cap.read()
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    kp1 = fast.detect(prev_gray, None)
    kp1, des1 = orb.compute(prev_gray, kp1)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        kp2 = fast.detect(gray, None)
        kp2, des2 = orb.compute(gray, kp2)

        if des1 is not None and des2 is not None:
            bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
            matches = bf.match(des1, des2)
            matches = sorted(matches, key=lambda x: x.distance)
            match_img = cv2.drawMatches(prev_gray, kp1, gray, kp2, matches[:50], None, flags=2)
        else:
            match_img = frame

        stframe.image(match_img, channels='BGR', use_column_width=True)

        prev_gray = gray.copy()
        kp1, des1 = kp2, des2

    cap.release()
