import openai
import streamlit as st
from utils import generate, api


st.set_page_config(
  page_title="SmartReadme",
  page_icon="logo.jpg",
  layout="wide",

)
st.title("Welcome to SmartReadme App")

st.text("SmartReadme is a README File generator app")

# Create an empty slot for the radio button
element_slot = st.empty()
openai.api_key = element_slot.text_input(label="OPENAI API Key", placeholder="Please enter your OpenAI_API_KEY to proceed")



if(openai.api_key):
  element_slot.empty()

  api(key=openai.api_key)

  # Input the Required Values
  name = st.text_input(
    label="Project Title",
    placeholder="Enter the title of your project"
  )

  tech = st.multiselect(
    "Select Tech Stack", 
    placeholder='Select the Tech Stack used in the Project', 
    options=['ReactJS','NextJS','MongoDB','NodeJS','JavaScript','TypeScript','Pyhton','Git']
  )
  
  desc = st.text_input(
    label='Description',
    placeholder="Write a breif description about your project",
  )

  if st.button('Generate README file'):
    if ( name and tech and desc ):
      res = generate(name=name, tech=tech, desc=desc)
      st.markdown(res)  
    else:
      st.warning("Please fill the required fields")
    