import os
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
import streamlit as st

def api(key):
  os.environ['OPENAI_API_KEY'] = key

def generate(name, desc, tech):
  llm = OpenAI()
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

  return(chain.predict(name=name, desc=desc, tech=tech))