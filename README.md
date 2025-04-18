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

- dlib [cmake]

- imutils

- pygame or playsound for audio alert

- streamlit (optional for UI)
<p>&nbsp;</p>

## 📸 Screenshot

Here's how the app looks:
<p>&nbsp;</p>
Home-Page:<p>&nbsp;</p>
![Home Page](https://github.com/user-attachments/assets/3151576c-815b-4ff7-881f-3aa1a8493064)
<p>&nbsp;</p>
Cam-Window:<p>&nbsp;</p>
![Cam Window](https://github.com/user-attachments/assets/1ae2fc30-99c6-49d7-b67c-0681ae0d141f)
<p>&nbsp;</p>
Detection-System:<p>&nbsp;</p>
![Detection System](https://github.com/user-attachments/assets/09832e17-fc85-4f25-a99f-30b6aa3499f7)
<p>&nbsp;</p>
Alarm-Alert Window:<p>&nbsp;</p>
![Alarm Alert](https://github.com/user-attachments/assets/7ec138c9-bf96-432a-86db-0ac70f69823f)
<p>&nbsp;</p>

This how the final project look.



