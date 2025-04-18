# Drowsiness-Detection

The Driver Drowsiness Detection System is a real-time safety application designed to monitor and detect signs of driver fatigue using computer vision. The system uses a webcam to track eye and facial movements, alerting the driver with an alarm when signs of drowsiness (like closed eyes or frequent blinking) are detected.
<p>&nbsp;</p>

💡 Key Features:

- Eye Aspect Ratio (EAR)-based detection to recognize eye closure

- Real-time facial landmark tracking using dlib or mediapipe

- Audio alarm to wake the driver when drowsiness is detected

- Compatible with standard USB webcams or laptop cameras

<p>&nbsp;</p>

🐍 Built with
- OpenCV
- Python
- Streamlit for UI
- 
<p>&nbsp;</p>

⚙️ How It Works

- Captures live video feed from the camera

- Detects the face and tracks eye landmarks

- Calculates the Eye Aspect Ratio (EAR)

- If EAR drops below a threshold for a certain time → triggers an alert
<p>&nbsp;</p>

📦 Libraries Used
- opencv-python

- dlib / mediapipe

- imutils

- pygame or playsound for audio alert

- streamlit (optional for UI)
<p>&nbsp;</p>

## 📸 Screenshot

Here's how the app looks:

![App Screenshot](screenshot.png)

