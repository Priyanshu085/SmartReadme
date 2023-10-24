import os
import openai
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv, find_dotenv
import streamlit as st

load_dotenv(find_dotenv())


st.set_page_config(
    page_title="Smart Readme",
    # page_icon="",
)

# Create an empty slot for the radio button
element_slot = st.empty()

openai.api_key = element_slot.text_input("Enter the Open AI API KEY")

if(openai.api_key):

  llm = OpenAI()
  chat_model = ChatOpenAI()

  element_slot.empty()

  # Input the Required Values
  name = st.text_input("Enter The Project Name")
  tech = st.multiselect("Enter the Tech Stack used in the Project", ['ReactJS','NextJS','MongoDB','NodeJS','JavaScript','TypeScript'])
  desc = st.text_input("Write a breif about your project")

  if st.button('Generate README file'):
    if ( name and tech and desc ):
      my_template = '''
      Project name {name}.
      Tech Stack is/are {tech}.
      A Breif desription about my project is {desc}.

      \'\'\'Include the columns in following order in the README File.\'\'\'
      - Table of Content
      - Screenshot of project
      - Description (in 50 words)
      - Features (in 5 Bullet Points)
      - Technology Used
      - Usage
      - Deployment
      - License 

      \* Make the Deployment and License part as optional for the user

      Create a README file in markdown. Also fill the details appropriately.

      '''

      prompt_template = ChatPromptTemplate.from_template(template=my_template)

      chain = LLMChain(llm=llm, prompt=prompt_template)

      st.markdown(chain.predict(name=name, desc=desc, tech=tech))
