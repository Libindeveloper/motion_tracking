

Project Title:

Motion Tracking in Drone Video Using FAST and ORB

Overview:

This project uses computer vision techniques—**FAST (Features from Accelerated Segment Test)** and **ORB (Oriented FAST and Rotated BRIEF)**—to detect and track motion in drone-captured videos. A user interface built using **Streamlit** allows users to upload videos and visualize tracked motion in real time.


Technologies Used:

* Python
* OpenCV
* Streamlit
* Computer Vision (FAST + ORB)


 Applications:

* Security Surveillance
* Wildlife Monitoring
* Sports Analytics
* Traffic and Crowd Monitoring


 Project Structure:


motion_tracking/
│
├── motion_tracking.py        # Main Streamlit application
├── requirements.txt          # Required Python libraries
└── sample_video.mp4          # (Optional) Test video file

How to Run the Project:


streamlit run motion_tracking.py


### 3. Upload Video

* In the Streamlit browser interface, click "Browse files"
* Upload a `.mp4` or `.avi` drone video
* Watch the motion tracking in real-time

---

## Key Concepts:

* **FAST**: Quickly detects corner features in frames
* **ORB**: Combines FAST keypoints with BRIEF descriptors and tracks them across frames
* **BFMatcher**: Finds the best match between keypoints in consecutive frames

---

## Skills Gained:

* Python scripting
* Real-time video processing
* Computer vision using OpenCV
* Web app interface using Streamlit
* Application in real-world domains

