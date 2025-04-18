import streamlit as st
import subprocess
# from streamlit_option_menu import option_menu
import requests 
from streamlit_lottie import st_lottie
import pandas as pd
import os 



st.set_page_config(page_title="Drowsiness Detection",page_icon="Assests/logo-blue.png",layout="wide")



#-----Navbar-----------------------------------------------




#lottie animation--------------------------------------------

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#---Load Assets-------
lottie_coding = load_lottieurl("https://lottie.host/3fb77eb9-97a8-44ba-9777-82719b51e2f8/ojtQ1Sw3tJ.json")


#-----Header------
  
logo_image = ("Assests/logo-no-background 1.png")
st.image(logo_image, width=500)





  
    

#-------WHat I DO-------------------------------------

with st.container():
    st.write("---")
    left_column,right_column = st.columns(2)
    with left_column:
        st.header("Introduction")
        # st.write("##") 
        st.write("⭕ Key Features ")
        st.write(" - Real-Time Detection :")
        st.write(" Our system utilizes advanced algorithms to continuously monitor facial expressions, eye movements, and head postures, providing real-time alerts when signs of drowsiness are detected")
        eye_image = ("Assests/detection.png")
        st.image(eye_image,width=100)

       

        st.write("- Integration Capabilities : ")
        st.write(" Our system can be seamlessly integrated with existing devices and platforms, such as wearable devices, in-vehicle systems, and industrial machinery.")
with right_column:
    st.write("##")
    
    st.write("##")
    st.write("- Customizable Alert Levels : ")
    st.write(" Users can tailor the system's sensitivity to their specific needs, ensuring that alerts are triggered at appropriate levels of drowsiness.")
    eye_image = ("Assests/alarm.png")
    st.image(eye_image,width=100)
    



with st.container():
    st.write("-------")
    st.title("⭕ Working ")
    st.write("---------")
    start_column,left_column,center_column,right_column = st.columns(4)
    with start_column:
        
        st.write("- Image/Video Processing: ")
        st.write(" Eyelid Analysis")
        st.write(" Facial Feature Detection")
        st.write("#")
        eye_image = ("Assests/eye-scan.png")
        st.image(eye_image,width=100)
        
    with left_column:
    
        st.write("- Feature Extraction: ")
        st.write("Perceptual Features")
        st.write(" Facial Feature Detection")
        st.write("#")
        eye_image = ("Assests/face-scanner1.gif")
        st.image(eye_image,width=100)


    with center_column:
       
        st.write("- Machine Learning:")
        st.write(" Model Training")
        st.write(" Feature Classification")
        st.write("#")
        eye_image = ("Assests/efficiency.png")
        st.image(eye_image,width=100)
    
    with right_column:
        
        st.write("- Alert Generation:")
        st.write(" Alert Triggering")
        st.write("Buzzer")
        st.write("#")
        eye_image = ("Assests/alarm.png")
        st.image(eye_image,width=100)
        
# with right_column:
#     # st_lottie()


#-----Project--------------------------------------------------

    st.write("---------")
    st.header("Click Here To Start ")
    st.write("#")

#--------start button--------------------------------------------


def run_python_file(file_path):
    try:
        # Use subprocess.Popen to execute the Python file
        subprocess.run(["python", file_path],check=True)
        st.success("Run successfully!")
    except subprocess.CalledProcessError as e:
        st.error(f"Error executing file: {e}")


file_path = "Drowsiness_Detection.py"
st.button("Start",on_click=run_python_file, args=(file_path,),use_container_width=10)

st.write("#")
#----Footer----------------------------------------------------------------
with st.container():
    st.write("-------")
    st.header("About")
    st.write("---------")
    start_column,left_column,center_column,right_column = st.columns(4)
    with start_column:
        eye_image = ("Assests/index.png")
        st.write("Index")
        
        
        st.image(eye_image,width=20)
        
    with left_column:
        eye_image = ("Assests/contact.png")
        st.write("Contact ")
        
        
        st.image(eye_image,width=20)

    with center_column:
        eye_image = ("Assests/mail.png")
        st.write("Mail ")
        
        st.image(eye_image,width=20)

    with right_column:
        eye_image = ("Assests/review.png")
        st.write("Feedback ")
        
        st.image(eye_image,width=20)

