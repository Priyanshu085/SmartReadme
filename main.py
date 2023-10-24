import openai
import streamlit as st
from utils import generate, api

st.set_page_config(
    page_title="Smart Readme",
    # page_icon="",
)

# Create an empty slot for the radio button
element_slot = st.empty()

openai.api_key = element_slot.text_input("Enter the Open AI API KEY")


if(openai.api_key):
  element_slot.empty()

  api(key=openai.api_key)

  # Input the Required Values
  name = st.text_input("Enter The Project Name")
  tech = st.multiselect("Enter the Tech Stack used in the Project", ['ReactJS','NextJS','MongoDB','NodeJS','JavaScript','TypeScript'])
  desc = st.text_input("Write a breif about your project")

  if st.button('Generate README file'):
    if ( name and tech and desc ):
      res = generate(name=name, tech=tech, desc=desc)
      st.markdown(res)  